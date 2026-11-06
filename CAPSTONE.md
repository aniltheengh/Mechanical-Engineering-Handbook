# Integrated capstone: a hypothetical water-transfer skid

This project connects several handbook subjects through one calculation package. It is an educational model with declared assumptions, not an approved equipment selection or fabrication design. All numerical inputs below are hypothetical unless a physical definition is stated.

## 1. Need, boundary, and assumptions

Transfer clean water between two large atmospheric tanks at **3 L/s**, with receiving free surface **12 m above** the source free surface. Analyse a 40 m equivalent straight pipeline with **50 mm internal diameter**, plus fittings represented separately by total minor-loss coefficient **6**. Use water density 998 kg/m³, gravity 9.81 m/s², Darcy friction factor 0.025, pump efficiency 0.70, and motor efficiency 0.90. Assume steady incompressible flow, equal atmospheric pressure at both free surfaces, negligible tank surface velocities, and no other equipment pressure drop.

The word “equivalent” here refers to the stated straight-pipe route length, not an equivalent length already incorporating the fittings; fittings are represented only by the supplied minor-loss coefficient. To avoid ambiguity in a real calculation, identify actual pipe segments and each fitting separately.

The friction factor is supplied for the exercise. In a real design it must be obtained from Reynolds number, roughness, and the relevant flow model. Pump efficiency is also an assumed value, not a measured constant over all flows.

## 2. Flow and head

The pipe flow area is $A=\pi D^2/4=0.00196350\ \mathrm{m^2}$. Average velocity is

$$
v=Q/A=0.003/0.00196350=1.52789\ \mathrm{m/s}.
$$

Using the Darcy–Weisbach and minor-loss relations,

$$
h_L=\left(f_D\frac LD+\sum K\right)\frac{v^2}{2g}
=\left(0.025\frac{40}{0.05}+6\right)\frac{1.52789^2}{2(9.81)}
=3.09355\ \mathrm m.
$$

Required total head at this flow is $H=12+3.09355=15.09355$ m. The two tank pressures cancel because both are assumed atmospheric; the pump still has to supply elevation and friction losses. This calculation determines a duty point, not an actual operating point. The latter requires an actual pump curve intersecting the system curve.

## 3. Power and annual energy

Hydraulic output is $P_h=\rho gQH\approx443.31$ W. With the assumed efficiencies,

$$
P_e=\frac{\rho gQH}{\eta_p\eta_m}=703.67\ \mathrm W.
$$

At an assumed 4000 operating hours per year, steady-duty electrical use is approximately $0.703674(4000)=2814.70$ kWh/year. At an illustrative tariff of 25 currency units/kWh, energy cost is 70,367.4 currency units/year. This is not a current utility quotation. Starting, variable duty, maintenance, and other loads are excluded.

If total dynamic head rises through fouling or a valve change, both operating flow and efficiency may change. Multiplying the original power by a guessed percentage can miss the new pump/system interaction. Use the full characteristic curves when available.

## 4. Suction conditions and transients

A discharge-head calculation does not establish freedom from cavitation. NPSH available depends on source absolute pressure, vapor pressure at actual water temperature, elevation relative to the pump, and suction losses. Compare it with manufacturer NPSH information and the project's margin criteria over the operating range. Do not reuse the total 40 m route as suction length without locating the pump.

Rapid valve closure or pump trip can generate transient pressure. The steady Darcy calculation contains no wave speed, pipe elasticity, closure time, check-valve dynamics, or surge protection model. Those inputs are missing from this educational model and should be explicitly requested before a transient assessment.

## 5. Structure, temperature, and layout

The contained water mass in a 2 m unsupported interval is approximately $\rho AL=998(0.00196350)(2)=3.919$ kg. This excludes pipe, insulation, valves, equipment loads, and dynamic effects. A support calculation needs all those loads, actual support conditions, section stiffness, and allowable criteria. A bracket should not be selected from water weight alone.

If a 10 m steel run has an assumed thermal expansion coefficient $12\times10^{-6}\ \mathrm{K^{-1}}$ and temperature rise 40 K, free expansion is $\Delta L=\alpha L\Delta T=4.8$ mm. Fully restraining it would create stress and reactions; actual flexibility and support arrangement determine the response. The free-expansion result is not a piping stress assessment.

Draw both a schematic and a layout. Identify flow direction, pump, isolation, drainage, instrumentation, maintenance removal space, and each support. Record which dimensions are functional interfaces and which are approximate routing dimensions.

## 6. Sensing and control

For an illustrative pressure transmitter covering 0–300 kPa with 4–20 mA output, the linear mapping is $p=300(I-4)/16$ kPa when $I$ is expressed numerically in mA. At 12 mA, pressure is 150 kPa. This scaling requires the correct configured range and reference (gauge or absolute). A signal outside the valid range may represent a fault and should not be interpreted as ordinary pressure without checking the device specification.

Define permitted start and stop conditions, loss-of-suction behaviour, sensor-fault behaviour, and power-loss state before tuning a controller. A PID equation by itself does not define an operable control system.

## 7. Verification plan

| Requirement or prediction | Evidence to collect | Model limitation |
|---|---|---|
| Target flow at stated tank levels | Calibrated flow measurement and level record | Pump characteristic and instrument uncertainty needed |
| Head balance | Pressure/elevation/velocity terms at clearly located taps | Gauge locations affect interpretation |
| Electrical energy | Measured input power at the duty | Efficiency assumptions may be wrong |
| Support adequacy | Load cases, section properties, support analysis, review | Water-only mass is incomplete |
| Thermal movement | Layout, flexibility model, temperature cases | Simple free expansion gives no reactions |
| Control behaviour | Defined sequence and controlled functional tests | No hardware test is performed by this repository |

## 8. Three extensions

1. Replace the fixed friction factor with a Reynolds-number/roughness calculation and compare 40, 50, and 65 mm internal diameters. Include installed cost before declaring an economic optimum.
2. Add a hypothetical pump curve, find its intersection with the system curve, and compare the new flow with 3 L/s. Use the [systems chapter](chapters/35-systems-engineering.md) as a worked pattern.
3. Build a lifecycle-cost comparison including initial cost, yearly electricity, maintenance, salvage, and a declared discount rate. Keep energy prices as dated assumptions or traceable quotations.

The arithmetic of velocity, losses, electrical power, annual energy/cost, contained water mass, free thermal expansion, and transmitter scaling is checked in `scripts/verify_foundations.py`. No pump, control system, or piping assembly is tested here.
