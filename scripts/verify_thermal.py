"""Recompute the 20 thermal-volume worked examples using only the standard library.

Expected numbers are the rounded values printed in the chapters, not a property
database. Each check also requires the printed value to occur in its example.
These checks verify arithmetic and selected balances, not industrial qualification.
"""

from math import exp, isclose, log, pi
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "08": "08-thermodynamics.md",
    "09": "09-power-cycles.md",
    "10": "10-fluid-mechanics.md",
    "11": "11-pipe-flow-and-pumps.md",
    "12": "12-heat-transfer.md",
    "13": "13-heat-exchangers.md",
    "14": "14-turbomachinery.md",
    "15": "15-refrigeration-and-hvac.md",
    "16": "16-combustion-and-engines.md",
    "17": "17-mass-transfer.md",
}
SECTIONS = [
    "Learning map", "Theory", "Formula handbook", "Derivation",
    "Worked examples", "Exercises", "Solutions", "Common mistakes",
    "Applications and limits", "Further reading",
]


def main():
    examples = {}
    words = 0
    for number, filename in FILES.items():
        source = (ROOT / "chapters" / filename).read_text(encoding="utf-8")
        words += len(source.split())
        assert re.findall(r"^## (.+)$", source, flags=re.M) == SECTIONS, filename
        assert len(re.findall(r"^# ", source, flags=re.M)) == 1, filename
        assert source.count("$$") % 2 == 0, filename
        found = re.findall(
            r"^### Example (\d{2}-[AB]):.*?\n(.*?)(?=^### |^## |\Z)",
            source, flags=re.M | re.S,
        )
        assert {key for key, _ in found} == {number + "-A", number + "-B"}, filename
        examples.update(found)
        for section in ("Exercises", "Solutions"):
            body = source.split("## " + section + "\n", 1)[1].split("\n## ", 1)[0]
            assert re.findall(r"^([1-3])\. ", body, flags=re.M) == ["1", "2", "3"], filename

    checks = []
    covered = set()

    def check(case, quantity, calculated, printed, token, rel=5e-5, absolute=1e-10):
        assert token in examples[case], (case, "printed value missing", token)
        assert isclose(calculated, printed, rel_tol=rel, abs_tol=absolute), (
            case, quantity, calculated, printed
        )
        checks.append((case, quantity))
        covered.add(case)

    # 08-A: closed-system storage; 08-B: isentropic reference and actual compressor.
    check("08-A", "tank heat kJ", 2 * 718 * (380 - 300) / 1000, 114.88, "114.88")
    t2s = 300 * 4 ** (0.4 / 1.4)
    t2 = 300 + (t2s - 300) / 0.8
    check("08-B", "isentropic K", t2s, 445.798, "445.798")
    check("08-B", "actual K", t2, 482.248, "482.248")
    check("08-B", "shaft input kW", 0.12 * 1005 * (t2 - 300) / 1000, 21.979, "21.979")
    entropy_rise = 1005 * log(t2 / 300) - (1005 - 1005 / 1.4) * log(4)
    assert entropy_rise > 0, "actual adiabatic compressor must generate entropy"

    # 09-A: ideal Otto; 09-B: separate component work and independent heat balance.
    eta_otto = 1 - 8 ** (-0.4)
    check("09-A", "Otto percent", 100 * eta_otto, 56.47, "56.47", rel=1e-4)
    check("09-A", "Otto kJ/kg", 800 * eta_otto, 451.780, "451.780")
    t2 = 300 * 6 ** (0.4 / 1.4)
    t4 = 1200 / 6 ** (0.4 / 1.4)
    wt = 1005 * (1200 - t4)
    wc = 1005 * (t2 - 300)
    qin = 1005 * (1200 - t2)
    qout = 1005 * (t4 - 300)
    check("09-B", "compressor exit K", t2, 500.553, "500.553")
    check("09-B", "turbine exit K", t4, 719.204, "719.204")
    check("09-B", "turbine kJ/kg", wt / 1000, 483.200, "483.200")
    check("09-B", "compressor kJ/kg", wc / 1000, 201.556, "201.556")
    check("09-B", "net kJ/kg", (wt - wc) / 1000, 281.644, "281.644")
    check("09-B", "input kJ/kg", qin / 1000, 702.944, "702.944")
    check("09-B", "efficiency percent", 100 * (qin - qout) / qin, 40.066, "40.066")
    assert isclose(wt - wc, qin - qout, rel_tol=1e-12)

    # 10-A: integrate hydrostatic pressure; 10-B: continuity and mechanical energy.
    force = 1000 * 9.81 * 2 * (4**2 - 1**2) / 2
    moment = 1000 * 9.81 * 2 * (4**3 - 1**3) / 3
    check("10-A", "force N", force, 147150, "147,150")
    check("10-A", "pressure-center m", moment / force, 2.8, "2.80")
    v1 = 0.01 / (pi * 0.1**2 / 4)
    v2 = 0.01 / (pi * 0.05**2 / 4)
    check("10-B", "inlet m/s", v1, 1.27324, "1.27324")
    check("10-B", "outlet m/s", v2, 5.09296, "5.09296")
    check("10-B", "pressure drop kPa", 1000 * (v2*v2 - v1*v1) / 2000, 12.159, "12.159")

    # 11-A: straight and fitting losses; 11-B: absolute suction-energy balance.
    loss = (0.025 * 80 / 0.1 + 4) * v1*v1 / (2 * 9.81)
    head = 12 + loss
    check("11-A", "loss m", loss, 1.98304, "1.98304")
    check("11-A", "duty head m", head, 13.9830, "13.9830")
    check("11-A", "shaft kW", 1000 * 9.81 * 0.01 * head / 0.7 / 1000, 1.95962, "1.95962")
    check("11-B", "NPSH m", (101325 - 2340) / (998 * 9.81) + 2 - 1.5, 10.6104, "10.6104")

    # 12-A: series resistances; 12-B: transient capacitance and validity check.
    resistance = 1 / (8 * 10) + 0.15 / (0.8 * 10) + 1 / (20 * 10)
    check("12-A", "resistance K/W", resistance, 0.03625, "0.03625")
    check("12-A", "heat W", 30 / resistance, 827.586, "827.586")
    tau = 0.020 * 500 / (20 * 0.010)
    bi = 20 * (0.020 / 7800 / 0.010) / 15
    check("12-B", "time constant s", tau, 50, "50.0")
    check("12-B", "final Celsius", 20 + 50 * exp(-300 / tau), 20.12394, "20.12394")
    assert bi < 0.001, "lumped-temperature approximation must have small Bi"

    # 13-A: LMTD rating; 13-B: counterflow effectiveness and both outlet balances.
    lmtd = (80 - 50) / log(80 / 50)
    check("13-A", "LMTD K", lmtd, 63.8293, "63.8293")
    check("13-A", "area m2", 100000 / (500 * lmtd), 3.13336, "3.13336")
    eps = (1 - exp(-2 * (1 - 0.5))) / (1 - 0.5 * exp(-2 * (1 - 0.5)))
    duty = eps * 1000 * (100 - 20)
    th = 100 - duty / 1000
    tc = 20 + duty / 2000
    check("13-B", "effectiveness", eps, 0.774600, "0.774600")
    check("13-B", "duty kW", duty / 1000, 61.9680, "61.9680")
    check("13-B", "hot outlet Celsius", th, 38.0320, "38.0320")
    check("13-B", "cold outlet Celsius", tc, 50.9840, "50.9840")
    assert isclose(1000 * (100-th), 2000 * (tc-20), rel_tol=1e-12)
    assert 100 > tc and th > 20, "both counterflow terminal differences must be positive"

    # 14-A: angular momentum; 14-B: fixed-impeller speed scaling.
    we = 30 * 18 - 10 * 2
    check("14-A", "Euler J/kg", we, 520, "520")
    check("14-A", "Euler head m", we / 9.81, 53.0071, "53.0071")
    check("14-A", "actual head m", 0.8 * we / 9.81, 42.4057, "42.4057")
    check("14-A", "rotor kW", 0.05 * 1000 * we / 1000, 26, "26.0")
    check("14-A", "hydraulic kW", 0.8 * 0.05 * 1000 * we / 1000, 20.8, "20.8")
    check("14-B", "flow m3/s", 0.030 * 0.8, 0.0240, "0.0240")
    check("14-B", "head m", 25 * 0.8**2, 16, "16.0")
    check("14-B", "power kW", 4 * 0.8**3, 2.048, "2.048")

    # 15-A: vapor-compression bookkeeping; 15-B: ideal moist-air convention.
    ql = 0.050 * (400-250)
    pc = 0.050 * (440-400)
    qh = 0.050 * (440-250)
    check("15-A", "cooling kW", ql, 7.5, "7.50")
    check("15-A", "compression kW", pc, 2, "2.00")
    check("15-A", "COP", ql/pc, 3.75, "3.75")
    check("15-A", "condenser kW", qh, 9.5, "9.50")
    assert isclose(qh, ql+pc, rel_tol=1e-12)
    w = 0.62198 * 1500 / (101325-1500)
    check("15-B", "humidity ratio", w, 0.00934606, "0.00934606")
    check("15-B", "enthalpy kJ/kg dry air", 1.006*25 + w*(2501+1.86*25), 48.9591, "48.9591")

    # 16-A: atomic oxygen demand converted to air mass; 16-B: dyno performance.
    afr = (2 * 32 / 16) / 0.232
    check("16-A", "stoichiometric AFR", afr, 17.2414, "17.2414")
    check("16-A", "actual AFR", 1.2*afr, 20.6897, "20.6897")
    power_kw = 120 * 2 * pi * 3000 / 60 / 1000
    check("16-B", "brake power kW", power_kw, 37.6991, "37.6991")
    check("16-B", "brake efficiency percent", 100*power_kw/(0.003*43000), 29.2241, "29.2241")
    check("16-B", "BSFC kg/kWh", 3600*0.003/power_kw, 0.286479, "0.286479")
    check("16-B", "BMEP kPa", 4*pi*120/0.002/1000, 754, "754", rel=5e-4)

    # 17-A: Fickian flux; 17-B: exponential mass balance with concentration conversion.
    flux = 2e-9*(5-1)/0.002
    check("17-A", "flux mol/(m2 s)", flux, 4e-6, "4.0\\times10^{-6}")
    check("17-A", "molar rate mol/s", flux*0.1, 4e-7, "4.0\\times10^{-7}")
    check("17-A", "molar rate mol/h", flux*0.1*3600, 0.00144, "0.00144")
    concentration = 8*(1-exp(-0.03*100))
    check("17-B", "concentration mg/L", concentration, 7.60170, "7.60170")
    check("17-B", "inventory kg", concentration*0.001*2, 0.0152034, "0.0152034")

    assert covered == set(examples), "every published worked example must be checked"
    print(f"PASS: {len(FILES)} thermal chapters; {len(covered)} worked examples; "
          f"{len(checks)} printed numerical results; 30 exercises/solutions; {words} source words.")
    print("Scope: supplied-property arithmetic, balance and structural checks; no real-fluid database or equipment certification.")


if __name__ == "__main__":
    main()
