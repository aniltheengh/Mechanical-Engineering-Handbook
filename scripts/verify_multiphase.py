"""Check chapter 43 arithmetic, source results, conservation and limiting cases.

Only the Python standard library is required. These checks assess the declared
reduced models; they do not identify a real flow regime or qualify equipment.
"""
from math import isclose, pi
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "chapters" / "43-multiphase-flow.md"
HEADINGS = ["Learning map", "Theory", "Formula handbook", "Derivation", "Worked examples",
            "Exercises", "Solutions", "Common mistakes", "Applications and limits", "Further reading"]


def void_fraction(quality, gas_density, liquid_density, slip=1.0):
    assert 0 <= quality <= 1
    assert gas_density > 0 and liquid_density > 0 and slip > 0
    return quality*liquid_density / (quality*liquid_density + (1-quality)*gas_density*slip)


def main():
    text = CHAPTER.read_text(encoding="utf-8")
    assert re.findall(r"^## (.+)$", text, re.M) == HEADINGS
    assert text.count("$$") % 2 == 0
    worked = re.findall(r"^### Example ([12]):[^\n]*\n(.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    assert [key for key, _ in worked] == ["1", "2"]
    passages = {"W"+key: value for key, value in worked}
    exercises = text.split("## Exercises\n", 1)[1].split("\n## ", 1)[0]
    assert re.findall(r"^([123])\. ", exercises, re.M) == ["1", "2", "3"]
    solutions = text.split("## Solutions\n", 1)[1].split("\n## ", 1)[0]
    solved = re.findall(r"^([123])\. (.*?)(?=^[123]\. |\Z)", solutions, re.M | re.S)
    assert [key for key, _ in solved] == ["1", "2", "3"]
    passages.update({"E"+key: value for key, value in solved})
    checked = []

    def check(case, quantity, computed, published, token):
        assert token in passages[case], (case, "published source value missing", token)
        assert isclose(computed, published, rel_tol=1e-5, abs_tol=1e-15), (
            case, quantity, computed, published
        )
        checked.append((case, quantity))

    # W1: derive occupied fractions from independently calculated volume flows.
    mass, x, rg, rl, area = 1., .001, 1.2, 1000., .01
    mg, ml = mass*x, mass*(1-x)
    qg, ql = mg/rg, ml/rl
    jg, jl = qg/area, ql/area
    alpha = qg/(qg+ql)
    velocity = (qg+ql)/area
    density = (mg+ml)/(qg+ql)
    check("W1", "gas mass flow", mg, .001, ".001000")
    check("W1", "liquid mass flow", ml, .999, ".999000")
    check("W1", "gas superficial speed", jg, .0833333, ".0833333")
    check("W1", "liquid superficial speed", jl, .0999, ".0999000")
    check("W1", "common actual speed", velocity, .183233, ".183233")
    check("W1", "gas void fraction", alpha, .454794, ".454794")
    check("W1", "homogeneous density", density, 545.752, "545.752")
    assert isclose(alpha, void_fraction(x, rg, rl), rel_tol=1e-12)
    assert isclose(density, alpha*rg+(1-alpha)*rl, rel_tol=1e-12)
    assert isclose(1/density, x/rg+(1-x)/rl, rel_tol=1e-12)
    assert isclose(rg*alpha*area*velocity, mg, rel_tol=1e-12)
    assert isclose(rl*(1-alpha)*area*velocity, ml, rel_tol=1e-12)
    assert isclose(density*velocity*area, mass, rel_tol=1e-12)
    flux = mass/area
    momentum_separate = alpha*rg*velocity**2+(1-alpha)*rl*velocity**2
    assert isclose(momentum_separate, flux**2/density, rel_tol=1e-12)

    # W2: obtain terminal velocity by balancing submerged weight and linear drag.
    diameter, rp, rf, viscosity, gravity = 20e-6, 2650., 1000., .001, 9.81
    displaced_volume = pi*diameter**3/6
    net_weight = (rp-rf)*gravity*displaced_volume
    drag_per_speed = 3*pi*viscosity*diameter
    terminal = net_weight/drag_per_speed
    reynolds = rf*terminal*diameter/viscosity
    time = 1/terminal
    check("W2", "settling speed", terminal, .0003597, ".000359700")
    check("W2", "particle Reynolds", reynolds, .007194, ".00719400")
    check("W2", "submerged weight N", net_weight, 6.78019e-11, "6.78019")
    check("W2", "travel seconds", time, 2780.09, "2780.09")
    check("W2", "travel minutes", time/60, 46.3349, "46.3349")
    assert reynolds < .1, "selected example must remain comfortably in creeping flow"
    cd = 24/reynolds
    drag_quadratic_form = .5*cd*rf*terminal**2*(pi*diameter**2/4)
    assert isclose(drag_quadratic_form, net_weight, rel_tol=1e-12, abs_tol=1e-25)

    # Exercises: distinguish mass fraction, phase slip and diameter scaling.
    a_ex = .1
    rho_ex = a_ex*rg+(1-a_ex)*rl
    quality_ex = a_ex*rg/rho_ex
    check("E1", "mixture density", rho_ex, 900.12, "900.120")
    check("E1", "quality", quality_ex, .000133316, ".000133316")
    check("E1", "quality percent", 100*quality_ex, .0133316, ".0133316")
    slip = 2.
    # Obtain alpha from jg/alpha = S*jl/(1-alpha), independently of quality formula.
    a_slip = jg/(jg+slip*jl)
    ug, ul = jg/a_slip, jl/(1-a_slip)
    rho_slip = a_slip*rg+(1-a_slip)*rl
    static_quality = a_slip*rg/rho_slip
    check("E2", "slip-model void fraction", a_slip, .294325, ".294325")
    check("E2", "gas actual velocity", ug, .283133, ".283133")
    check("E2", "liquid actual velocity", ul, .141567, ".141567")
    check("E2", "static quality", static_quality, .000500250, ".000500250")
    assert isclose(ug/ul, slip, rel_tol=1e-12)
    assert isclose(a_slip, void_fraction(x, rg, rl, slip), rel_tol=1e-12)
    assert isclose(rg*a_slip*ug*area, mg, rel_tol=1e-12)
    assert isclose(rl*(1-a_slip)*ul*area, ml, rel_tol=1e-12)
    assert static_quality < x and a_slip < alpha
    # Slip changes inventory density, not prescribed mass/volume-flow ratios.
    assert not isclose(rho_slip, mass/(qg+ql), rel_tol=1e-3)
    larger_d = 2*diameter
    larger_v = (rp-rf)*gravity*larger_d**2/(18*viscosity)
    larger_re = rf*larger_v*larger_d/viscosity
    check("E3", "larger sphere speed", larger_v, .0014388, ".00143880")
    check("E3", "larger sphere Reynolds", larger_re, .057552, ".0575520")
    check("E3", "larger sphere travel seconds", 1/larger_v, 695.024, "695.024")
    assert isclose(larger_v/terminal, 4., rel_tol=1e-12)
    assert isclose(larger_re/reynolds, 8., rel_tol=1e-12) and larger_re < .1

    # Pure-phase, equal-density and slip monotonicity limits.
    for slip_test in (.5, 1., 2., 5.):
        assert void_fraction(0., rg, rl, slip_test) == 0.
        assert void_fraction(1., rg, rl, slip_test) == 1.
    for quality in (.00001, .001, .1, .5, .99):
        assert isclose(void_fraction(quality, 1000., 1000.), quality, rel_tol=1e-12)
        assert 0 < void_fraction(quality, rg, rl, 5) < void_fraction(quality, rg, rl, 2) < void_fraction(quality, rg, rl, 1) < 1
    assert 1/(0/rg+1/rl) == rl and 1/(1/rg+0/rl) == rg
    # A neutrally buoyant rigid sphere has zero gravitational terminal slip.
    assert (rf-rf)*gravity*diameter**2/(18*viscosity) == 0
    # Interphase transfer changes individual phase flow while preserving total mass.
    transfer = .0002
    assert isclose((mg+transfer)+(ml-transfer), mass, rel_tol=1e-12)
    assert {case for case, _ in checked} == set(passages)
    print(f"PASS: chapter 43; 2 worked examples; 3 solved exercises; {len(checked)} printed numerical results; {len(text.split())} source words.")
    print("Additional checks: phase and mixture continuity, homogeneous momentum, Stokes force balance/Reynolds applicability, slip behavior and single-phase/equal-density/neutral-buoyancy limits.")


if __name__ == "__main__":
    main()
