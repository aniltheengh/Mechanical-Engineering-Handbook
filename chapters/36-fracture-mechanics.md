# 36 · Fracture mechanics and fatigue crack growth

## Learning map

Prerequisites are stress, strain, elasticity, energy, fatigue, and elementary integration. This chapter introduces crack-driving force, fracture resistance, and a limited crack-growth model. It connects material testing with geometry and loading. The objective is to explain why a component with modest nominal stress can fail from a crack, and why a crack calculation needs more information than tensile strength. Continue from chapters 06, 07, and 18; use chapter 24 when considering numerical crack analysis.

## Theory

A smooth tensile specimen and a cracked component do not have the same local stress field. Linear elasticity predicts a singular stress near a sharp crack tip. An actual material blunts, yields, fractures, or otherwise changes its behaviour before a literal infinite stress exists. Fracture mechanics characterizes the surrounding field and the energy available for further crack extension rather than interpreting the singular elastic maximum as a directly measurable stress.

Mode I opens the crack faces, mode II slides them in the crack plane, and mode III shears them out of plane. A real defect can experience mixed modes. This introductory chapter concentrates on mode I in isotropic linear elasticity. The stress-intensity factor describes the amplitude of the near-tip elastic field; it is not a stress-concentration factor and is not dimensionless. Its value depends on the load, crack definition, geometry, and boundary conditions.

Linear-elastic fracture mechanics, or LEFM, is useful when a small nonlinear process zone is surrounded by a sufficiently large elastic field. Small-scale yielding must be assessed relative to crack size, remaining ligament, thickness, and other relevant geometry. A low nominal stress alone does not establish validity. Large-scale plasticity needs an appropriate elastic-plastic framework, such as a properly evaluated J integral or crack-tip opening displacement, together with applicable resistance data.

Plane stress approximates a thin region with small through-thickness stress. Plane strain approximates a strongly constrained region with small through-thickness strain. Constraint affects plastic deformation and fracture resistance. A valid plane-strain toughness value is established by a specified test procedure and its validity requirements. A number labelled toughness without specimen, temperature, rate, environment, orientation, and validity information is insufficient for transferring it to another application.

Energy release rate measures how much mechanical potential energy becomes available per increment of projected crack area. Fracture resistance describes the energy required for extension under the model and material conditions. Initiation and unstable propagation are distinct: a growing resistance curve or changing geometry can permit stable extension before instability. Comparing one value of driving force with one resistance value cannot by itself characterize an entire crack path.

Under cyclic loading, a crack may grow at stress levels below those causing immediate fracture. A Paris-type relation approximates an intermediate portion of a measured crack-growth curve. It does not generally describe a near-threshold regime, rapid final growth, overload retardation, short cracks, corrosion-assisted cracking, or load-sequence effects. The stress ratio and environment are part of the test conditions behind the fitted constants. A calculated cycle count inherits every one of those modelling assumptions.

## Formula handbook

1. The leading mode-I near-tip elastic field has the form $\sigma_{ij}=K_I f_{ij}(\theta)/\sqrt{2\pi r}$ plus less singular terms. Here $r$ is tip distance in m and $f_{ij}$ is a dimensionless angular function. The field is used outside the nonlinear process zone and inside the region dominated by the leading term.
2. A common geometry representation is $K_I=Y\sigma\sqrt{\pi a}$, with nominal stress $\sigma$ in Pa, defined crack-size parameter $a$ in m, and dimensionless geometry factor $Y$. The result is Pa $\sqrt{\mathrm m}$. For an infinite plate with a central through crack, $a$ is half the total crack length and $Y=1$.
3. A constant-$Y$ critical-stress estimate is $\sigma_c=K_c/(Y\sqrt{\pi a})$. A compatible resistance $K_c$ and valid LEFM model are required; the equation is not a general acceptance rule.
4. With the same restrictions, $a_c=(K_c/(Y\sigma))^2/\pi$. If $Y$ depends appreciably on $a$, solve the full geometry-dependent equation instead.
5. For mechanical potential energy $\Pi$, $G=-\partial\Pi/\partial A_c$, where $A_c$ is projected crack-plane area under a declared loading convention. Units are J/m², equivalent to N/m. This convention is distinct from counting the combined area of both newly created faces.
6. For isotropic mode-I linear elasticity,

$$
G=\frac{K_I^2}{E'},\qquad E'=E\quad\text{(plane stress)},\qquad E'=\frac{E}{1-\nu^2}\quad\text{(plane strain)}.
$$

Here $E$ is Young's modulus in Pa and $\nu$ is Poisson's ratio. A compatible critical value satisfies $G_c=K_c^2/E'$.
7. Approximate forward plastic-zone estimates are $r_p\approx(K_I/\sigma_Y)^2/(2\pi)$ for plane stress and $r_p\approx(K_I/\sigma_Y)^2/(6\pi)$ for plane strain. They are first-order estimates, not general crack-tip plasticity solutions; $\sigma_Y$ is yield stress in matching stress units.
8. For a nonzero maximum intensity, the cycle ratio is $R_K=K_{\min}/K_{\max}$ and the nominal range is $\Delta K=K_{\max}-K_{\min}$. Closure can make an effective opening range differ from this nominal range.
9. With constant geometry and proportional tensile loading, $\Delta K=Y\Delta\sigma\sqrt{\pi a}$.
10. Paris law is $da/dN=C(\Delta K)^m$, where $N$ counts cycles and $C,m$ are fitted for stated conditions. The units of $C$ depend on both $m$ and the stress-intensity unit.
11. If $Y$, $\Delta\sigma$, $C$, and $m$ remain constant, define $B=C(Y\Delta\sigma\sqrt\pi)^m$. For $m\ne2$,

$$
N_f-N_i=\frac{a_f^{1-m/2}-a_i^{1-m/2}}{B(1-m/2)}.
$$

12. For $m=2$, the corresponding integral is $(N_f-N_i)=\ln(a_f/a_i)/B$.

MPa $\sqrt{\mathrm m}$ is convenient in the examples. Convert to Pa $\sqrt{\mathrm m}$ before using a modulus in Pa. A Paris coefficient calibrated with MPa cannot be retained unchanged after replacing the intensity unit by Pa.

## Derivation

For $m=3$, substituting $\Delta K=Y\Delta\sigma\sqrt{\pi a}$ into Paris law gives $da/dN=Ba^{3/2}$. Separate variables and integrate from a measured initial crack to an explicitly selected final crack:

$$
N_f-N_i=\frac1B\int_{a_i}^{a_f}a^{-3/2}\,da
=\frac2B\left(\frac1{\sqrt{a_i}}-\frac1{\sqrt{a_f}}\right).
$$

The result is positive when $a_f>a_i$. Growth accelerates because the driving range increases as the crack grows under constant nominal stress. The endpoint is not automatically failure: it must be justified separately. The integral also shows why uncertainty in small initial crack size can strongly affect a predicted interval. Inspection detectability is therefore a separate input, not something supplied by the growth law.

## Worked examples

### Example 1: an assumed small crack under tension

Take $a=0.005$ m, $Y=1.12$, tensile stress 100 MPa, $E=210$ GPa, $\nu=0.30$, yield stress 300 MPa, and hypothetical compatible toughness $K_c=40$ MPa $\sqrt{\mathrm m}$. The supplied geometry factor is held constant for this exercise. Intensity is **14.03712 MPa $\sqrt{\mathrm m}$**. Plane-strain effective modulus is 230.769 GPa, giving **$G=853.843$ J/m²**. The approximate plastic-zone sizes are **0.348444 mm** in plane stress and **0.116148 mm** in plane strain. The constant-geometry critical-stress estimate is **284.9588 MPa**. These are model outputs: unknown ligament, thickness, residual stress, and toughness validity prevent a service-acceptance conclusion. In particular, validity must be reconsidered near the predicted critical stress.

### Example 2: a declared Paris-law interval

Assume $C=10^{-12}$ m/cycle divided by $(\mathrm{MPa}\sqrt{\mathrm m})^3$, $m=3$, $Y=1.12$, and $\Delta\sigma=80$ MPa. Integrate from $a_i=0.001$ m to $a_f=0.010$ m. Then $B=4.005427\times10^{-6}$ in the resulting consistent units and the predicted interval is **10,796,739 cycles**. Initial and final rates are **$1.266627\times10^{-10}$ m/cycle** and **$4.005427\times10^{-9}$ m/cycle**, respectively. The constants are hypothetical, and both endpoints are assumed to lie within their intermediate-growth regime. This calculation excludes initiation life and does not establish that the final crack is safe or critical.

## Exercises

1. At unchanged stress and geometry factor, a crack-size parameter increases from 2 mm to 8 mm. Find the intensity ratio and the energy-release-rate ratio.
2. For $K_I=20$ MPa $\sqrt{\mathrm m}$, $E=200$ GPa and $\nu=0.30$, calculate $G$ in plane stress and plane strain.
3. Within an unchanged valid Paris model with $m=3$, how does the cycle interval between the same crack endpoints change when stress range is doubled? Explain one reason that scaling may fail physically.

## Solutions

1. $K_2/K_1=\sqrt{8/2}=2$. Since $G\propto K^2$ at unchanged modulus and constraint, $G_2/G_1=4$.
2. Convert intensity to $20\times10^6$ Pa $\sqrt{\mathrm m}$. Plane-stress $G$ is **2000 J/m²**; plane-strain $G=(1-0.3^2)(2000)=\mathbf{1820\ J/m^2}$. Equal intensity does not mean equal energy release under different constraint models.
3. The integrated interval is proportional to $(\Delta\sigma)^{-3}$, so it becomes **one eighth**. Increased loading may invalidate small-scale yielding or move growth outside the calibrated regime, removing the basis for that scaling.

## Common mistakes

Confusing total crack length with half-length creates a systematic error. Using millimetres with a toughness expressed per square root metre creates a much larger one. Yield strength, fracture toughness, and fatigue endurance describe different responses. A low finite-element residual or mesh-dependent crack-tip peak is not proof that a chosen fracture model is valid. Do not use an unqualified Paris fit to assign an inspection interval without load history, detectability, environmental effects, and an appropriate assessment method.

## Applications and limits

Fracture mechanics supports damage-tolerance thinking: identify credible defects, measure or bound their size, characterize loading, choose applicable resistance data, calculate driving force, and evaluate uncertainty and inspection capability. Weld residual stress, crack closure, mixed-mode loading, and material anisotropy may require extensions beyond this chapter. The accompanying verifier checks the hypothetical arithmetic and a separate numerical integration of the growth interval; it does not qualify a cracked component.

## Further reading

- [MIT OCW, Introduction to Fracture Mechanics](https://ocw.mit.edu/courses/3-91-mechanical-behavior-of-plastics-spring-2007/ca3759efc1b8fd66d57dce1147d4a1db_23_frac.pdf) — freely hosted teaching notes on crack-driving force and fracture concepts.
- [MIT Roylance mechanics modules](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/pages/modules/) — separate fracture and fatigue modules for further study.
- [Allan Bower, Applied Mechanics of Solids: energy methods in fracture](https://solidmechanics.org/Text/Chapter9_4/Chapter9_4.htm) — author-hosted textbook treatment of energy methods and their assumptions.
