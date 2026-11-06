# 35 · Systems engineering and integrated design

## Learning map

This chapter combines the preceding subjects into a traceable engineering process. Prerequisites are basic mechanics, fluid and thermal balances, reliability, and economics. The aim is to turn a need into requirements, architecture, analyses, tests, and an operating system whose interfaces and limitations are understood.

## Theory

A system is a set of interacting elements considered within a defined boundary and environment. The same pump may be a component in a water-treatment plant and a system when analysing its motor, impeller, bearings, seals, and controller. Choosing the boundary determines which flows and interactions must be modelled explicitly. System performance is not generally the sum of isolated component ratings.

A stakeholder need expresses the desired outcome. A requirement converts part of that outcome into a testable constraint under stated conditions. “The skid shall be efficient” cannot be verified without a metric and operating condition. “At 0.003 m³/s and 20 m total head, measured electrical input shall not exceed 1.2 kW under the stated water temperature and supply conditions” can be tested, although the value must first be justified.

Architecture assigns functions to elements and defines interfaces. A mechanical interface includes loads, alignment, dimensions, tolerances, support, and access. A fluid interface includes flow, pressure, temperature, composition, cleanliness, and allowable transients. An electrical interface includes voltage, current, grounding, isolation, and protection. A control interface includes signals, timing, units, failure states, and authority. Most integration problems occur at these boundaries rather than inside a single discipline's idealized calculation.

Verification establishes whether a specified requirement has been met through test, analysis, inspection, or demonstration. Validation establishes whether the delivered system meets its intended use in the relevant environment. A correctly built pump skid may still fail to meet the user's operational need if maintenance is impractical or the expected water contains unmodelled solids. Both questions should influence planning before fabrication.

Budgets allocate limited resources such as mass, power, heat rejection, cost, and time. A margin is a quantified allowance under a stated convention, not a vague feeling of safety. Risk combines uncertain outcomes with consequences, but multiplying ordinal labels such as “low, medium, high” does not create a calibrated probability. Fault analysis should distinguish independent failures, shared causes, and failure propagation.

Configuration control records which requirements, drawings, code, models, and parts belong to a particular version. An accurate calculation attached to an obsolete drawing is not usable evidence. Traceability connects each requirement to its source, implementing element, analysis, and verification evidence. This can be maintained with a simple table for a small project; complexity should support decisions rather than conceal them.

## Formula handbook

1. A conserved quantity satisfies accumulation = inflow − outflow + generation − consumption. Mass has no generation term in ordinary non-nuclear equipment balances.
2. A scalar resource budget is $B_{\mathrm{total}}=\sum_iB_i+B_{\mathrm{shared}}$, provided items do not overlap.
3. Under the convention used here, capacity margin is $m=(C-D)/D$, where capacity $C$ and demand $D>0$ have matching units. Another project may divide by capacity; always state the convention.
4. For a multiplicative chain, total efficiency is $\eta_{\mathrm{total}}=\prod_i\eta_i$, if each stage's useful output is the next stage's input.
5. Steady pump electrical demand is $P_e=\rho gQH/(\eta_p\eta_m\eta_d)$, with pump, motor, and drive efficiencies stated separately.
6. An illustrative system curve is $H_s(Q)=H_0+kQ^2$, with $k$ in s²/m⁵ when $Q$ is in m³/s and head in m. It assumes a compatible fixed configuration and approximately quadratic losses.
7. The operating point satisfies $H_p(Q)=H_s(Q)$. A root must lie within physically permissible pump and system ranges.
8. Local sensitivity: $\Delta y\approx\sum_i(\partial f/\partial x_i)\Delta x_i$ for small perturbations to $y=f(\mathbf x)$.
9. Independent series reliability: $R_{\mathrm{sys}}=\prod_iR_i$ for elements all required to succeed over the same mission.
10. Independent parallel success: $R_{\mathrm{sys}}=1-\prod_i(1-R_i)$ only when any one element suffices and switching/supporting functions are properly accounted for.
11. Expected monetary loss is $E[L]=\sum_i p_iL_i$ for mutually exclusive scenarios covering the modelled outcomes, with calibrated probabilities $p_i$ and losses in a common currency/date basis.
12. For a finish-to-start activity network without resource constraints, earliest finish is $EF_i=\max_{j\in\mathrm{pred}(i)}EF_j+d_i$. Start activities use earliest start zero. Duration $d_i$ and finish times use the same time unit.

These equations assist decisions; none replaces the judgement needed to define requirements, identify credible failure modes, or decide whether evidence is sufficient.

## Derivation

Suppose pump head is approximated by $H_p=a-bQ^2$, with positive constants over a limited operating interval, and the system head is $H_s=H_0+kQ^2$. Equal head at a steady operating point gives $a-H_0=(b+k)Q^2$. Therefore

$$
Q=\sqrt{\frac{a-H_0}{b+k}}
$$

for a positive-flow solution when $a>H_0$ and $b+k>0$. If $a\leq H_0$, this approximation gives no positive delivery against the static head. Adding a valve increases $k$ and lowers the flow for an unchanged pump curve. Changing pump speed shifts the pump curve, so the same algebra must be repeated with the new characteristic. This illustrates why a component nameplate cannot determine the integrated operating condition by itself.

## Worked examples

### Example 1: Pump and system interaction

Let $H_p=30-200000Q^2$ m and $H_s=10+300000Q^2$ m, with $Q$ in m³/s. Equating gives $Q^2=20/500000=4\times10^{-5}$, so $Q=0.00632456\ \mathrm{m^3/s}$, or 6.325 L/s. Either curve gives $H=22$ m. With water density 1000 kg/m³, $g=9.81$ m/s², and total efficiency 0.70, electrical power is $P=1000(9.81)(0.00632456)(22)/0.70=1.950\ \mathrm{kW}$. The assumed curves say nothing about NPSH, allowable operating range, solids, or transient pressures; those are separate interface checks.

### Example 2: A schedule dependency

Activity A, requirements, takes 2 days. B, layout, takes 3 days after A. C, procurement definition, takes 4 days after A. D, integration review, takes 2 days after both B and C. Earliest finish times are A = 2, B = 5, C = 6, and D = $\max(5,6)+2=8$ days. Path A–C–D is critical at 8 days; A–B–D is 7 days. Shortening B by one day alone does not shorten project completion. Resource competition or calendar restrictions would require a more detailed schedule.

## Exercises

1. A motor is 90% efficient and a pump is 70% efficient. What electrical input supports 1 kW of hydraulic output, neglecting other losses?
2. Demand is 80 kg and capacity is 100 kg. Compute capacity margin using this chapter's definition.
3. Two independent required components have mission reliabilities 0.98 and 0.99. Compute series reliability and explain one reason the model might fail.

## Solutions

1. Total efficiency is $0.90(0.70)=0.63$. Required input is $1/0.63=1.587$ kW. Adding efficiencies would have no physical meaning.
2. $m=(100-80)/80=0.25$, or 25%. Relative unused capacity would instead be 20%; state the denominator to avoid ambiguity.
3. $R=0.98(0.99)=0.9702$. A shared power supply, common contamination, or common environmental overload could violate independence and change the result.

## Common mistakes

Optimizing one component while ignoring its interfaces can worsen system performance. Adding several margins without tracking their purpose can create an oversized design; removing them without evidence can erase necessary allowances. Do not equate a completed checklist with validation or treat an untested model as an acceptance test. Requirements should specify conditions, thresholds, and verification methods before results are known.

## Applications and limits

For a small water skid, maintain a requirements table, P&ID, layout, calculation sheet, component list, interface list, operating sequence, failure response, and verification record. Review them as one configuration. The integrated capstone in this repository applies this process to a hypothetical pumping system. Its educational values are deliberately stated so they cannot be mistaken for an approved construction design.

## Further reading

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — publisher-hosted handbook and process guidance.
- [MIT OCW, Design of Electromechanical Robotic Systems](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/) — a project course connecting electromechanical architecture, analysis, and implementation, with an open textbook on design for uncertainty.
