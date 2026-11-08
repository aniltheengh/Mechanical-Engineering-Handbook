"""Verify Chapter 44's two examples and three exercises using stdlib only.

Checks cover mass/enthalpy closure, limiting cases, independently stepped tank
inventory, integrated tracer discharge, utility balances, and printed results.
They do not validate an actual plant, mixing system, instrument, or code design.
"""

from pathlib import Path
import math
import re


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "chapters" / "44-process-plant-engineering.md"
HEADINGS = [
    "Learning map", "Theory", "Formula handbook", "Derivation",
    "Worked examples", "Exercises", "Solutions", "Common mistakes",
    "Applications and limits", "Further reading",
]
checks = 0


def check(label, actual, expected, *, rel_tol=1e-6, abs_tol=1e-10):
    global checks
    if not math.isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol):
        raise AssertionError(f"{label}: computed {actual!r}, expected {expected!r}")
    checks += 1


def require(label, condition):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def section(source, heading):
    match = re.search(rf"^{re.escape(heading)}[^\n]*\n(.*?)(?=^#{{1,3}} |\Z)", source, re.M | re.S)
    if not match:
        raise AssertionError(f"Missing source section: {heading}")
    return match.group(1)


def simpson(function, stop, intervals=2000):
    """Numerically integrate a scalar signal for an independent balance check."""
    if intervals <= 0 or intervals % 2:
        raise ValueError("Simpson integration needs a positive even interval count")
    step = stop / intervals
    values = [function(i * step) for i in range(intervals + 1)]
    return step / 3 * (
        values[0] + values[-1]
        + 4 * sum(values[1:-1:2])
        + 2 * sum(values[2:-1:2])
    )


def main():
    source = CHAPTER.read_text(encoding="utf-8")
    headings = [line[3:] for line in source.splitlines() if line.startswith("## ")]
    require("Exact chapter section structure", headings == HEADINGS)
    require("Exactly two numbered worked examples", len(re.findall(r"^### Example [12]:", source, re.M)) == 2)
    require("Balanced display-math delimiters", source.splitlines().count("$$") % 2 == 0)

    # Example 1: solve separately for total mass, tracer mass, and enthalpy.
    mass_rates = (1.50, 0.500)
    temperatures = (20.0, 80.0)
    fractions = (0.00100, 0.00400)
    cp = 4180.0
    total_mass_rate = sum(mass_rates)
    inlet_tracer_rate = sum(mass * fraction for mass, fraction in zip(mass_rates, fractions))
    inlet_enthalpy_rate = sum(mass * cp * temperature for mass, temperature in zip(mass_rates, temperatures))
    outlet_temperature = inlet_enthalpy_rate / (total_mass_rate * cp)
    outlet_fraction = inlet_tracer_rate / total_mass_rate
    heater_duty = total_mass_rate * cp * (60 - outlet_temperature)
    check("44 E1 outlet mass kg/s", total_mass_rate, 2.00)
    check("44 E1 temperature Celsius", outlet_temperature, 35.0)
    check("44 E1 tracer mass kg/s", inlet_tracer_rate, 0.00350)
    check("44 E1 mass fraction kg/kg", outlet_fraction, 0.001750)
    check("44 E1 tracer mg/kg", outlet_fraction * 1e6, 1750)
    check("44 E1 enthalpy kW", inlet_enthalpy_rate / 1000, 292.6)
    check("44 E1 enthalpy residual W", total_mass_rate * cp * outlet_temperature - inlet_enthalpy_rate, 0)
    check("44 E1 heating duty kW", heater_duty / 1000, 209.0)
    check("44 E1 expanded heater boundary W", inlet_enthalpy_rate + heater_duty, total_mass_rate * cp * 60)
    require("44 E1 blend temperature between feed temperatures", min(temperatures) <= outlet_temperature <= max(temperatures))
    require("44 E1 blend fraction between feed fractions", min(fractions) <= outlet_fraction <= max(fractions))
    # Changing a common enthalpy reference must not change the physical result.
    kelvin_inlet_rate = sum(m * cp * (temp + 273.15) for m, temp in zip(mass_rates, temperatures))
    check("44 E1 reference invariance Celsius", kelvin_inlet_rate / (total_mass_rate * cp) - 273.15, outlet_temperature)

    # Example 2: analytical concentration and explicit inventory conservation.
    volume, flow, inlet_concentration = 1.20, 0.00200, 0.100
    tau = volume / flow
    concentration = lambda time: inlet_concentration * (-math.expm1(-time / tau))
    final_time = 600.0
    outlet_at_600 = concentration(final_time)
    time_95 = -tau * math.log(0.05)
    input_mass = flow * inlet_concentration * final_time
    stored_mass = volume * outlet_at_600
    output_mass_integrated = simpson(lambda time: flow * concentration(time), final_time)
    check("44 E2 residence time s", tau, 600)
    check("44 E2 concentration mg/L", outlet_at_600 * 1000, 63.2120558829)
    check("44 E2 95 percent time s", time_95, 1797.43936413)
    check("44 E2 95 percent time min", time_95 / 60, 29.9573227355)
    check("44 E2 concentration at 95 percent", concentration(time_95) / inlet_concentration, 0.95)
    check("44 E2 tracer input kg", input_mass, 0.120000)
    check("44 E2 tracer inventory kg", stored_mass, 0.0758544670594)
    check("44 E2 integrated tracer discharge kg", output_mass_integrated, 0.0441455329406)
    check("44 E2 integral mass residual kg", input_mass - stored_mass - output_mass_integrated, 0)
    check("44 E2 initial condition", concentration(0), 0)
    check("44 E2 long-time limit", concentration(30 * tau), inlet_concentration)
    require("44 E2 nonnegative bounded response", all(0 <= concentration(t) <= inlet_concentration for t in (0, 1, 60, 600, 6000)))

    # Independent finite-volume time stepping: update stored tracer by in minus out.
    steps = 12000
    dt = final_time / steps
    inventory = 0.0
    discharged = 0.0
    for _ in range(steps):
        out_mass = flow * (inventory / volume) * dt
        inventory += flow * inlet_concentration * dt - out_mass
        discharged += out_mass
    check("44 E2 stepped inventory mass balance kg", inventory + discharged, input_mass)
    check("44 E2 stepped vs analytical concentration", inventory / volume, outlet_at_600, rel_tol=0, abs_tol=2e-6)

    # RTD normalization and first moment, truncated only after 25 residence times.
    density = lambda t: math.exp(-t / tau) / tau
    check("44 RTD normalized area", simpson(density, 25 * tau, 10000), 1.0, rel_tol=1e-8)
    check("44 RTD mean s", simpson(lambda t: t * density(t), 25 * tau, 10000), tau, rel_tol=1e-8)

    # Exercise 1: unequal-flow blending and separate downstream heating duty.
    blend_temperature = (0.8 * 15 + 1.2 * 65) / (0.8 + 1.2)
    exercise_heat = (0.8 + 1.2) * 4180 * (55 - blend_temperature)
    check("44 X1 blend Celsius", blend_temperature, 45.0)
    check("44 X1 heater duty kW", exercise_heat / 1000, 83.60)
    check("44 X1 full energy residual W", 0.8 * 4180 * 15 + 1.2 * 4180 * 65 + exercise_heat - 2 * 4180 * 55, 0)

    # Exercise 2: clean-water washout, using inventory instead of a feed step.
    volume, flow, initial_concentration = 2.00, 0.00500, 0.200
    washout_tau = volume / flow
    ten_percent_time = washout_tau * math.log(10)
    initial_inventory = volume * initial_concentration
    remaining_inventory = initial_inventory * math.exp(-ten_percent_time / washout_tau)
    check("44 X2 residence time s", washout_tau, 400)
    check("44 X2 washout time s", ten_percent_time, 921.034037198)
    check("44 X2 washout time min", ten_percent_time / 60, 15.3505672866)
    check("44 X2 remaining tracer kg", remaining_inventory, 0.0400)
    check("44 X2 discharged tracer kg", initial_inventory - remaining_inventory, 0.360)

    # Exercise 3: utility enthalpy, density conversion, pipe flow, and signal scaling.
    heat, utility_cp, rise, density, pipe_diameter = 84000, 4200, 8.0, 1000, 0.050
    utility_mass_flow = heat / (utility_cp * rise)
    utility_volume_flow = utility_mass_flow / density
    section_area = math.pi * pipe_diameter**2 / 4
    velocity = utility_volume_flow / section_area
    current_ma = 4 + 16 * (utility_volume_flow * 1000) / 5
    check("44 X3 utility mass kg/s", utility_mass_flow, 2.50)
    check("44 X3 utility volume m3/s", utility_volume_flow, 0.00250)
    check("44 X3 pipe speed m/s", velocity, 1.27323954474)
    check("44 X3 transmitter mA", current_ma, 12.0)
    check("44 X3 pipe mass-flow closure kg/s", density * section_area * velocity, utility_mass_flow)
    check("44 X3 utility heat closure W", utility_mass_flow * utility_cp * rise, heat)
    check("44 X3 inverse scaling L/s", (current_ma - 4) * 5 / 16, utility_volume_flow * 1000)

    # Printed source conclusions stay attached to the corresponding problem.
    required_values = {
        "### Example 1:": ["2.00 kg/s", "35.0", "0.001750 kg/kg", "1750 mg/kg", "292.6 kW", "209.0"],
        "### Example 2:": ["600", "63.2121 mg/L", "1797.44", "29.9573 min", "0.120000 kg", "0.0758545", "0.0441455 kg"],
        "## Solutions": ["45.0", "83.60", "921.034", "15.3506 min", "0.0400 kg", "2.50", "0.00250 m³/s", "1.27324", "12.0 mA"],
    }
    anchor_count = 0
    for heading, values in required_values.items():
        body = section(source, heading)
        for value in values:
            require(f"Printed value {value!r} in {heading}", value in body)
            anchor_count += 1
    print(
        f"PASS: Chapter 44; 2 worked examples and 3 exercises; {checks} checks "
        f"including {anchor_count} printed-value anchors, balances, limits, and independent tank stepping."
    )


if __name__ == "__main__":
    main()
