# Specialist foundations in mechanical engineering

Mechanical Engineering Handbook · Expanded edition · 2026-11-08

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [36 · Fracture mechanics and fatigue crack growth](../chapters/36-fracture-mechanics.md)
- [37 · Composite materials and laminated plates](../chapters/37-composite-materials.md)
- [38. Compressible flow](../chapters/38-compressible-flow.md)
- [39. Engineering acoustics](../chapters/39-engineering-acoustics.md)
- [40. Corrosion Engineering](../chapters/40-corrosion-engineering.md)
- [41. Welding Engineering](../chapters/41-welding-engineering.md)

---

## 36 · Fracture mechanics and fatigue crack growth

### Learning map

Prerequisites are stress, strain, elasticity, energy, fatigue, and elementary integration. This chapter introduces crack-driving force, fracture resistance, and a limited crack-growth model. It connects material testing with geometry and loading. The objective is to explain why a component with modest nominal stress can fail from a crack, and why a crack calculation needs more information than tensile strength. Continue from chapters 06, 07, and 18; use chapter 24 when considering numerical crack analysis.

### Theory

A smooth tensile specimen and a cracked component do not have the same local stress field. Linear elasticity predicts a singular stress near a sharp crack tip. An actual material blunts, yields, fractures, or otherwise changes its behaviour before a literal infinite stress exists. Fracture mechanics characterizes the surrounding field and the energy available for further crack extension rather than interpreting the singular elastic maximum as a directly measurable stress.

Mode I opens the crack faces, mode II slides them in the crack plane, and mode III shears them out of plane. A real defect can experience mixed modes. This introductory chapter concentrates on mode I in isotropic linear elasticity. The stress-intensity factor describes the amplitude of the near-tip elastic field; it is not a stress-concentration factor and is not dimensionless. Its value depends on the load, crack definition, geometry, and boundary conditions.

Linear-elastic fracture mechanics, or LEFM, is useful when a small nonlinear process zone is surrounded by a sufficiently large elastic field. Small-scale yielding must be assessed relative to crack size, remaining ligament, thickness, and other relevant geometry. A low nominal stress alone does not establish validity. Large-scale plasticity needs an appropriate elastic-plastic framework, such as a properly evaluated J integral or crack-tip opening displacement, together with applicable resistance data.

Plane stress approximates a thin region with small through-thickness stress. Plane strain approximates a strongly constrained region with small through-thickness strain. Constraint affects plastic deformation and fracture resistance. A valid plane-strain toughness value is established by a specified test procedure and its validity requirements. A number labelled toughness without specimen, temperature, rate, environment, orientation, and validity information is insufficient for transferring it to another application.

Energy release rate measures how much mechanical potential energy becomes available per increment of projected crack area. Fracture resistance describes the energy required for extension under the model and material conditions. Initiation and unstable propagation are distinct: a growing resistance curve or changing geometry can permit stable extension before instability. Comparing one value of driving force with one resistance value cannot by itself characterize an entire crack path.

Under cyclic loading, a crack may grow at stress levels below those causing immediate fracture. A Paris-type relation approximates an intermediate portion of a measured crack-growth curve. It does not generally describe a near-threshold regime, rapid final growth, overload retardation, short cracks, corrosion-assisted cracking, or load-sequence effects. The stress ratio and environment are part of the test conditions behind the fitted constants. A calculated cycle count inherits every one of those modelling assumptions.

### Formula handbook

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

### Derivation

For $m=3$, substituting $\Delta K=Y\Delta\sigma\sqrt{\pi a}$ into Paris law gives $da/dN=Ba^{3/2}$. Separate variables and integrate from a measured initial crack to an explicitly selected final crack:

$$
N_f-N_i=\frac1B\int_{a_i}^{a_f}a^{-3/2}\,da
=\frac2B\left(\frac1{\sqrt{a_i}}-\frac1{\sqrt{a_f}}\right).
$$

The result is positive when $a_f>a_i$. Growth accelerates because the driving range increases as the crack grows under constant nominal stress. The endpoint is not automatically failure: it must be justified separately. The integral also shows why uncertainty in small initial crack size can strongly affect a predicted interval. Inspection detectability is therefore a separate input, not something supplied by the growth law.

### Worked examples

#### Example 1: an assumed small crack under tension

Take $a=0.005$ m, $Y=1.12$, tensile stress 100 MPa, $E=210$ GPa, $\nu=0.30$, yield stress 300 MPa, and hypothetical compatible toughness $K_c=40$ MPa $\sqrt{\mathrm m}$. The supplied geometry factor is held constant for this exercise. Intensity is **14.03712 MPa $\sqrt{\mathrm m}$**. Plane-strain effective modulus is 230.769 GPa, giving **$G=853.843$ J/m²**. The approximate plastic-zone sizes are **0.348444 mm** in plane stress and **0.116148 mm** in plane strain. The constant-geometry critical-stress estimate is **284.9588 MPa**. These are model outputs: unknown ligament, thickness, residual stress, and toughness validity prevent a service-acceptance conclusion. In particular, validity must be reconsidered near the predicted critical stress.

#### Example 2: a declared Paris-law interval

Assume $C=10^{-12}$ m/cycle divided by $(\mathrm{MPa}\sqrt{\mathrm m})^3$, $m=3$, $Y=1.12$, and $\Delta\sigma=80$ MPa. Integrate from $a_i=0.001$ m to $a_f=0.010$ m. Then $B=4.005427\times10^{-6}$ in the resulting consistent units and the predicted interval is **10,796,739 cycles**. Initial and final rates are **$1.266627\times10^{-10}$ m/cycle** and **$4.005427\times10^{-9}$ m/cycle**, respectively. The constants are hypothetical, and both endpoints are assumed to lie within their intermediate-growth regime. This calculation excludes initiation life and does not establish that the final crack is safe or critical.

### Exercises

1. At unchanged stress and geometry factor, a crack-size parameter increases from 2 mm to 8 mm. Find the intensity ratio and the energy-release-rate ratio.
2. For $K_I=20$ MPa $\sqrt{\mathrm m}$, $E=200$ GPa and $\nu=0.30$, calculate $G$ in plane stress and plane strain.
3. Within an unchanged valid Paris model with $m=3$, how does the cycle interval between the same crack endpoints change when stress range is doubled? Explain one reason that scaling may fail physically.

### Solutions

1. $K_2/K_1=\sqrt{8/2}=2$. Since $G\propto K^2$ at unchanged modulus and constraint, $G_2/G_1=4$.
2. Convert intensity to $20\times10^6$ Pa $\sqrt{\mathrm m}$. Plane-stress $G$ is **2000 J/m²**; plane-strain $G=(1-0.3^2)(2000)=\mathbf{1820\ J/m^2}$. Equal intensity does not mean equal energy release under different constraint models.
3. The integrated interval is proportional to $(\Delta\sigma)^{-3}$, so it becomes **one eighth**. Increased loading may invalidate small-scale yielding or move growth outside the calibrated regime, removing the basis for that scaling.

### Common mistakes

Confusing total crack length with half-length creates a systematic error. Using millimetres with a toughness expressed per square root metre creates a much larger one. Yield strength, fracture toughness, and fatigue endurance describe different responses. A low finite-element residual or mesh-dependent crack-tip peak is not proof that a chosen fracture model is valid. Do not use an unqualified Paris fit to assign an inspection interval without load history, detectability, environmental effects, and an appropriate assessment method.

### Applications and limits

Fracture mechanics supports damage-tolerance thinking: identify credible defects, measure or bound their size, characterize loading, choose applicable resistance data, calculate driving force, and evaluate uncertainty and inspection capability. Weld residual stress, crack closure, mixed-mode loading, and material anisotropy may require extensions beyond this chapter. The accompanying verifier checks the hypothetical arithmetic and a separate numerical integration of the growth interval; it does not qualify a cracked component.

### Further reading

- [MIT OCW, Introduction to Fracture Mechanics](https://ocw.mit.edu/courses/3-91-mechanical-behavior-of-plastics-spring-2007/ca3759efc1b8fd66d57dce1147d4a1db_23_frac.pdf) — freely hosted teaching notes on crack-driving force and fracture concepts.
- [MIT Roylance mechanics modules](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/pages/modules/) — separate fracture and fatigue modules for further study.
- [Allan Bower, Applied Mechanics of Solids: energy methods in fracture](https://solidmechanics.org/Text/Chapter9_4/Chapter9_4.htm) — author-hosted textbook treatment of energy methods and their assumptions.


---

## 37 · Composite materials and laminated plates

### Learning map

Prerequisites are elasticity, stress and strain, matrix algebra, and material behaviour. Study chapters 06–07 before this chapter and use chapter 24 for later finite-element applications. The objective is to distinguish constituent properties, lamina response, laminate response, and failure. Two elementary calculations connect a material mixture to an orthotropic ply and a symmetric laminate. They are stiffness models, not a complete composite design procedure.

### Theory

A composite combines distinguishable constituents to obtain a useful combination of properties. A fibre-reinforced polymer uses relatively stiff fibres to carry much of the longitudinal load and a matrix to support, separate, and transfer load between them. The interface is crucial: broken adhesion, porosity, fibre waviness, moisture, and processing defects can change performance substantially. Constituent strength values alone cannot establish the manufactured part's strength.

A unidirectional lamina is a thin layer with a preferred fibre direction, labelled 1. Direction 2 lies transverse to the fibres in the layer. The layer is often treated as orthotropic: its material axes have different elastic responses with specified symmetry. A laminate stacks layers at different angles and positions. The laminate's global axes differ from each layer's local material axes, so stresses and strains must be transformed consistently.

The longitudinal rule of mixtures assumes equal axial strain in continuous, well-bonded constituents. Its transverse counterpart under an equal-stress assumption is a series idealization. These models are useful estimates and teaching bounds for the stated scalar arrangements; they are not exact general transverse-property predictions for a real microstructure. Voids, packing, constituent Poisson effects, and interfaces can matter. Measured lamina data are preferable for detailed analysis.

Classical laminate theory assumes thin layers, small deformation, in-plane elastic response, perfect bonding, and a linear variation of in-plane strain through thickness. Normals to the midplane remain straight and normal in the classical thin-plate kinematics. Transverse shear deformation is neglected. This can be inadequate for thick laminates, sandwich structures with compliant cores, local joints, impact, or delamination. Interlaminar stresses near free edges require more than the elementary in-plane model.

Three stiffness matrices organize the laminate response. A maps midplane strain to membrane force resultants; D maps curvature to moment resultants; B couples extension and bending. A laminate symmetric about its midplane has B equal to zero under this constitutive model. Balanced angle pairs can remove some extension–shear coupling, but balanced and symmetric are different properties. Neither automatically makes a laminate isotropic in bending or guarantees every coupling term vanishes.

Composite failure can involve fibre tension, fibre compression, matrix cracking, shear failure, interface damage, and delamination. The maximum-stress criterion is a simple componentwise screening approach, while interactive criteria use combinations of stresses. A first-ply-failure prediction does not automatically equal final collapse; redistribution and progressive damage require an appropriate model and evidence. Allowables must match direction, sign, condition, and statistical/design basis.

### Formula handbook

Use constituent volume fractions $V_f,V_m$, densities $\rho_f,\rho_m$ in kg/m³, and elastic moduli in Pa. The subscript f denotes fibre and m denotes matrix; the symbol $m$ elsewhere may mean mass, so read local definitions.

1. With no void fraction, $V_f+V_m=1$ and $\rho_c=V_f\rho_f+V_m\rho_m$. Void-containing mixtures require another constituent fraction and an appropriate density model.
2. Equal longitudinal strain gives $E_L=V_fE_f+V_mE_m$ for the simple continuous parallel model.
3. The equal-stress transverse series model gives $1/E_T=V_f/E_f+V_m/E_m$.
4. Under equal axial strain $\epsilon$, constituent stresses are $\sigma_f=E_f\epsilon$, $\sigma_m=E_m\epsilon$, and macroscopic stress is $\sigma_c=V_f\sigma_f+V_m\sigma_m$.
5. Orthotropic reciprocity requires $\nu_{12}/E_1=\nu_{21}/E_2$. Here $\nu_{12}=-\epsilon_2/\epsilon_1$ under uniaxial stress in direction 1, and the reverse ratio defines $\nu_{21}$.
6. The lamina plane-stress compliance relation is

$$
\begin{bmatrix}\epsilon_1\\\epsilon_2\\\gamma_{12}\end{bmatrix}
=\begin{bmatrix}1/E_1&-\nu_{21}/E_2&0\\-\nu_{12}/E_1&1/E_2&0\\0&0&1/G_{12}\end{bmatrix}
\begin{bmatrix}\sigma_1\\\sigma_2\\\tau_{12}\end{bmatrix}.
$$

Engineering shear strain $\gamma_{12}$ is twice the tensor shear strain; use that convention consistently in transformations.
7. Let $d=1-\nu_{12}\nu_{21}$. The reduced stiffness terms are $Q_{11}=E_1/d$, $Q_{22}=E_2/d$, $Q_{12}=\nu_{12}E_2/d$, and $Q_{66}=G_{12}$. They have units Pa, with $\boldsymbol\sigma=\mathbf Q\boldsymbol\epsilon$.
8. In global axes, $\boldsymbol\sigma_{xy}=\overline{\mathbf Q}\boldsymbol\epsilon_{xy}$. At 90 degrees, $\overline Q_{11}=Q_{22}$, $\overline Q_{22}=Q_{11}$, $\overline Q_{12}=Q_{12}$, and $\overline Q_{66}=Q_{66}$; the 16 and 26 terms vanish for a specially orthotropic ply at 0 or 90 degrees.
9. With the convention $\boldsymbol\epsilon(z)=\boldsymbol\epsilon^0+z\boldsymbol\kappa$, layer boundaries $z_k$ measured from the midplane give

$$
\mathbf A=\sum_k\overline{\mathbf Q}_k(z_k-z_{k-1}),\quad
\mathbf B=\frac12\sum_k\overline{\mathbf Q}_k(z_k^2-z_{k-1}^2),\quad
\mathbf D=\frac13\sum_k\overline{\mathbf Q}_k(z_k^3-z_{k-1}^3).
$$

The units are N/m, N, and N m respectively.
10. Without thermal or other initial strains,

$$
\begin{bmatrix}\mathbf N\\\mathbf M\end{bmatrix}
=\begin{bmatrix}\mathbf A&\mathbf B\\\mathbf B&\mathbf D\end{bmatrix}
\begin{bmatrix}\boldsymbol\epsilon^0\\\boldsymbol\kappa\end{bmatrix}.
$$

Membrane resultant $\mathbf N$ is force per width in N/m, moment resultant $\mathbf M$ is moment per width in N, and curvature is in m⁻¹. The bending sign follows the chosen $z$ and curvature convention.
11. Layer stress recovery is $\boldsymbol\sigma_k(z)=\overline{\mathbf Q}_k[\boldsymbol\epsilon^0+z\boldsymbol\kappa-\overline{\boldsymbol\alpha}_k\Delta T]$ when a compatible thermal expansion vector is included. Moisture and other initial strains need additional terms.
12. Simple maximum-stress screening compares local $\sigma_1,\sigma_2,\tau_{12}$ with the corresponding tensile/compressive and shear allowables. For example, $-X_c\leq\sigma_1\leq X_t$ and $|\tau_{12}|\leq S$; the transverse pair uses $Y_t,Y_c$. This separate-component model omits interactions and delamination.

### Derivation

Consider a symmetric laminate with no thermal strain and only applied membrane loads. Identical material at equal positive and negative distances from the midplane makes the integral of $z\overline{\mathbf Q}$ cancel, giving $\mathbf B=0$. If no bending moments act and $\mathbf D$ is nonsingular, curvature is zero. All plies then have the same global in-plane strain, but their stresses differ because their transformed stiffness matrices differ. Integrating those stresses gives $\mathbf N=\mathbf A\boldsymbol\epsilon^0$.

For a cross-ply laminate with equal 0- and 90-degree thicknesses, $A_{16}=A_{26}=0$ and $A_{11}=A_{22}$. Under $N_x$ alone, solving the two coupled normal equations gives $\epsilon_x=N_xA_{11}/(A_{11}^2-A_{12}^2)$ and $\epsilon_y=-N_xA_{12}/(A_{11}^2-A_{12}^2)$. Setting transverse strain to zero would impose an extra constraint and would represent a different boundary condition.

### Worked examples

#### Example 1: a constituent stiffness estimate

Use hypothetical continuous fibres with $E_f=230$ GPa, matrix modulus $E_m=3.5$ GPa, and $V_f=0.60$. The parallel estimate is **$E_L=139.400$ GPa**. The series estimate is **$E_T=8.554729$ GPa**. With fibre and matrix densities 1800 and 1200 kg/m³, density is **1560 kg/m³**. Under a common axial strain 0.001, fibre stress is **230 MPa**, matrix stress **3.5 MPa**, and average stress **139.4 MPa**. The fibre share of total axial force is **0.989957**, about 99.0%, under the parallel assumptions. These values illustrate stiffness and load sharing; they do not predict failure strength or exact transverse response.

#### Example 2: a symmetric cross-ply membrane

Four identical 0.125 mm plies form $[0/90/90/0]$, for total thickness 0.500 mm. Use measured-or-supplied lamina inputs $E_1=135$ GPa, $E_2=10$ GPa, $G_{12}=5$ GPa, and $\nu_{12}=0.30$. Here they are hypothetical teaching inputs. Reciprocity gives $\nu_{21}=0.0222222$. The reduced stiffnesses are $Q_{11}=135.9060$, $Q_{22}=10.06711$, $Q_{12}=3.020134$, and $Q_{66}=5.00000$ GPa.

Integration gives **$A_{11}=A_{22}=36.49329$ MN/m**, **$A_{12}=1.510067$ MN/m**, **$A_{66}=2.500000$ MN/m**, and $\mathbf B=0$. Apply $N_x=50,000$ N/m with $N_y=N_{xy}=0$ and no moments. Midplane strains are **$\epsilon_x=0.001372465$**, **$\epsilon_y=-0.00005679165$**, and zero engineering shear. A 0-degree ply has local stresses **186.3548 MPa** and **3.573300 MPa**; a 90-degree ply has local stresses **−3.573300 MPa** and **13.64524 MPa** in its own 1 and 2 directions. Transforming back and integrating recovers the applied 50,000 N/m and zero transverse resultant. No strength conclusion is possible without appropriate allowables and failure models.

### Exercises

1. For $E_1=140$ GPa, $E_2=10$ GPa and $\nu_{12}=0.28$, find $\nu_{21}$. Explain why setting both Poisson ratios equal is inconsistent here.
2. All ply thicknesses in Example 2 are doubled while the stacking sequence and material properties remain unchanged. How do A, B, and D scale? What happens to strain under the same pure membrane load?
3. Under the same 0.001 axial strain as Example 1, reduce fibre fraction to 0.40. Find the parallel modulus, density, and average stress using the same constituent data.

### Solutions

1. Reciprocity gives $\nu_{21}=0.28(10/140)=\mathbf{0.0200}$. Equal ratios would violate the symmetric compliance relation when the moduli differ.
2. A doubles, D increases by a factor **8**, and B remains **zero** because symmetry is preserved. The same membrane load produces **half the strain**. This scaling assumes every through-thickness coordinate doubles about the same midplane; it is not an arbitrary addition of one new ply.
3. $E_L=0.4(230)+0.6(3.5)=\mathbf{94.100\ GPa}$, density is **1440 kg/m³**, and average stress is **94.100 MPa**. Constituent stresses under prescribed equal strain remain unchanged; their area fractions and total load change.

### Common mistakes

Using isotropic relations to infer $G_{12}$ from $E_1$ and $\nu_{12}$ is generally invalid. A laminate-average stress cannot replace local ply stresses in a directional criterion. Mixing tensor shear and engineering shear introduces factors of two. Symmetric, balanced, and quasi-isotropic describe different properties. An apparently stiff laminate may still be weak at a bolt hole, a free edge, an impact site, or an interface.

### Applications and limits

Use laminate analysis to compare load paths, stiffness, deformation, and coupling before detailed joint and damage assessments. Preserve the layup convention, ply order, thicknesses, fibre angles, property condition, and coordinate definitions in the design record. Thermal and moisture conditions can create self-equilibrated ply stresses even when external resultants vanish. Real qualification needs traceable allowables, processing controls, inspection, and representative tests. The verifier checks stiffness assembly and load recovery, not damage tolerance or manufactured quality.

### Further reading

- [MIT Roylance, Laminated Composite Plates](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/f193c908ec10d95c0bc67c904b65397a_MIT3_11F99_laminates.pdf) — freely hosted derivation of lamina and laminate constitutive equations.
- [NASA RP-1351, Basic Mechanics of Laminated Composite Plates](https://ntrs.nasa.gov/citations/19950009349) — official report record and download route for a fuller reference. The PDF route was identifiable; a prior full download attempt timed out.


---

## 38. Compressible flow

### Learning map

Prerequisites: [thermodynamics](../chapters/08-thermodynamics.md), [fluid mechanics](../chapters/10-fluid-mechanics.md), differential calculus and absolute-pressure measurement. Learn to distinguish static from stagnation conditions, connect Mach number with density change, calculate ideal nozzle flow, and treat a shock as an irreversible discontinuity. The central question is how a gas changes its density while accelerating, compressing or receiving energy. This chapter develops one-dimensional ideal-gas models before identifying the additional physics needed in real ducts and aerodynamic flows.

### Theory

Compressible-flow analysis allows density to change along a flow or with time. Mach number compares local fluid speed with local acoustic propagation speed. It measures how rapidly pressure information can travel relative to the gas. In a subsonic stream, small disturbances can propagate upstream as well as downstream. In a supersonic stream, their propagation relative to the ground is directed downstream within a limited region. The sound speed must be evaluated from the local thermodynamic state, rather than assigned one universal air value.

A small Mach number often supports an incompressible approximation when temperature changes are also small. It does not guarantee constant density in a strongly heated or cooled gas. Conversely, an ideal gas is not automatically incompressible: the ideal-gas equation explicitly relates density to pressure and temperature. The constant-specific-heat model below further assumes a calorically perfect gas. At high temperature, changes in heat capacity and composition invalidate some simple powers of Mach number.

Static properties describe the moving fluid locally. Stagnation properties describe a reference state reached by bringing that fluid to rest through an ideal adiabatic, reversible deceleration. Stagnation enthalpy is useful even when the actual flow contains irreversible regions. An adiabatic nozzle with no shaft work preserves stagnation enthalpy while converting static enthalpy into kinetic energy. It also preserves stagnation pressure only if its flow is isentropic. Across an adiabatic shock, stagnation temperature remains constant for a perfect gas, but stagnation pressure falls.

Nozzle geometry controls acceleration differently on the two sides of Mach one. A converging passage accelerates subsonic flow; a diverging passage accelerates supersonic flow under the stated one-dimensional isentropic assumptions. Thus a converging-diverging nozzle can accelerate a gas through a sonic throat and then to a supersonic exit. Geometry alone does not determine the realized branch: reservoir conditions and downstream pressure determine whether the passage stays subsonic, becomes choked, or contains shocks.

Choking is a maximum mass-flow condition for fixed throat area and upstream stagnation state. Reducing downstream pressure beyond the choking threshold does not keep increasing the ideal mass flow through that throat. It can still alter the downstream jet and shock structure. The critical-pressure ratio used for a simple converging nozzle is not a universal back-pressure criterion for every converging-diverging nozzle, valve, or long gas line.

A shock is a thin region of rapid compression. The conserved mass, momentum and total energy connect the states on its two sides, while entropy increases. A normal shock changes a supersonic upstream flow into a subsonic downstream flow. Static pressure, density and temperature rise, and velocity falls. An isentropic formula can relate static and stagnation properties on either side separately, but cannot equate stagnation pressures across the shock.

### Formula handbook

Use absolute pressure $p$ in Pa, temperature $T$ in K, density $\rho$ in kg/m3, gas-specific $R$ in J/(kg K), speed $V$ in m/s, area $A$ in m2 and mass flow $\dot m$ in kg/s. Subscript 0 denotes stagnation conditions; an asterisk denotes a sonic reference state. Unless stated otherwise, the gas is ideal with constant $\gamma=c_p/c_v$ and $c_p=\gamma R/(\gamma-1)$.

1. State, sound speed and Mach number:

$$
p=\rho RT,\qquad a=\sqrt{\gamma RT},\qquad M=V/a.
$$

2. Steady one-dimensional conservation of mass:

$$
\dot m=\rho VA.
$$

3. Adiabatic flow energy without shaft work or elevation change:

$$
h_0=h+\frac{V^2}{2},\qquad T_0=T+\frac{V^2}{2c_p}.
$$

4. Static-to-stagnation relations, with pressure and density referenced by isentropic deceleration:

$$
\frac{T_0}{T}=1+\frac{\gamma-1}{2}M^2,\qquad \frac{p_0}{p}=\left(\frac{T_0}{T}\right)^{\gamma/(\gamma-1)},\qquad \frac{\rho_0}{\rho}=\left(\frac{T_0}{T}\right)^{1/(\gamma-1)}.
$$

5. Area-velocity relation for smooth quasi-one-dimensional isentropic flow:

$$
\frac{dA}{A}=(M^2-1)\frac{dV}{V}.
$$

6. Area-Mach relation within one isentropic region:

$$
\frac{A}{A^*}=\frac1M\left[\frac2{\gamma+1}\left(1+\frac{\gamma-1}{2}M^2\right)\right]^{(\gamma+1)/[2(\gamma-1)]}.
$$

An area ratio greater than one has both a subsonic and a supersonic mathematical solution.

7. Mass-flow function:

$$
\dot m=\frac{Ap_0}{\sqrt{T_0}}\sqrt{\frac\gamma R}\,M\left(1+\frac{\gamma-1}{2}M^2\right)^{-(\gamma+1)/[2(\gamma-1)]}.
$$

8. Sonic temperature and pressure ratios:

$$
\frac{T^*}{T_0}=\frac2{\gamma+1},\qquad \frac{p^*}{p_0}=\left(\frac2{\gamma+1}\right)^{\gamma/(\gamma-1)}.
$$

9. Ideal choked mass flow, with sonic throat area $A^*$:

$$
\dot m^*=\frac{A^*p_0}{\sqrt{T_0}}\sqrt{\frac\gamma R}\left(\frac2{\gamma+1}\right)^{(\gamma+1)/[2(\gamma-1)]}.
$$

A measured discharge coefficient can modify this ideal result for a specified device; it must not be invented or transferred between unrelated geometries.

10. Normal-shock downstream Mach number, upstream $M_1>1$:

$$
M_2^2=\frac{1+\frac{\gamma-1}{2}M_1^2}{\gamma M_1^2-\frac{\gamma-1}{2}}.
$$

11. Normal-shock static-property ratios:

$$
\frac{p_2}{p_1}=1+\frac{2\gamma}{\gamma+1}(M_1^2-1),\qquad \frac{\rho_2}{\rho_1}=\frac{(\gamma+1)M_1^2}{2+(\gamma-1)M_1^2},\qquad \frac{T_2}{T_1}=\frac{p_2/p_1}{\rho_2/\rho_1}.
$$

12. Normal-shock stagnation-pressure ratio:

$$
\frac{p_{02}}{p_{01}}=\frac{p_2}{p_1}\left[\frac{1+\frac{\gamma-1}{2}M_2^2}{1+\frac{\gamma-1}{2}M_1^2}\right]^{\gamma/(\gamma-1)}.
$$

13. Entropy change for a perfect gas, and its shock-specific reduction:

$$
s_2-s_1=c_p\ln(T_2/T_1)-R\ln(p_2/p_1)=-R\ln(p_{02}/p_{01})>0.
$$

The last equality uses equal stagnation temperatures across an adiabatic normal shock.

14. Mach angle for infinitesimal disturbances in a uniform supersonic stream:

$$
\mu=\sin^{-1}(1/M).
$$

This is not the angle of an arbitrary finite-strength oblique shock.

### Derivation

Start with differential continuity: $d\rho/\rho+dV/V+dA/A=0$. For inviscid steady flow along the passage, momentum gives $dp+\rho V\,dV=0$. Along an isentrope, the acoustic definition is $dp=a^2d\rho$. Combining momentum with this relation gives $d\rho/\rho=-M^2dV/V$. Substitution into continuity yields $dA/A=(M^2-1)dV/V$. The sign reversal at Mach one follows from conservation and compressibility, not from a separate nozzle rule.

To locate maximum mass flow, hold $A,p_0,T_0$ fixed in formula 7 and differentiate its logarithm with respect to $M$. Apart from a positive denominator, the derivative is proportional to $1-M^2$. Flow therefore increases up to $M=1$ and decreases on the supersonic branch of the mathematical mass-flow function. The maximum is the choked value. This derivative result does not mean a simple converging nozzle can select the supersonic branch at its exit; the boundary-value problem still determines which state is attainable.

### Worked examples

#### Example 1: a converging air nozzle

An ideal converging nozzle is supplied by a large reservoir at $p_0=300,000$ Pa absolute and $T_0=300$ K. Exit area is $1.00\times10^{-4}$ m2; back pressure is 100,000 Pa absolute. Use $R=287$ J/(kg K) and $\gamma=1.4$. The back-pressure ratio is 0.333333, below the critical ratio **0.528282**, so the exit is sonic in this model. The sonic static pressure is **158,484.5 Pa**, temperature is **250.000 K**, and speed is **316.938 m/s**. Formula 9 gives **0.0700068 kg/s**. Checking independently with $\rho^*=p^*/(RT^*)$ and $\rho^*a^*A^*$ reproduces that flow. The exit pressure exceeds ambient; further expansion occurs outside the nozzle. Setting exit static pressure equal to back pressure would contradict the choked internal solution.

#### Example 2: a normal shock at Mach two

Air reaches a normal shock with $M_1=2.00$, $p_1=100,000$ Pa and $T_1=300$ K, using the same perfect-gas constants. The shock relations give **$M_2=0.577350$**, **$p_2/p_1=4.50000$**, and **$\rho_2/\rho_1=2.66667$**. Thus downstream pressure is **450,000 Pa** and temperature is **506.250 K**. Stagnation temperature is 540 K on both sides. Stagnation-pressure ratio is **0.720874**, and entropy rises by **93.9325 J/(kg K)**. This combination illustrates the distinction between static compression and loss of stagnation pressure. Independent checks of mass flux, momentum flux $p+\rho V^2$, and total enthalpy must agree across the shock.

### Exercises

1. Air has static temperature 300 K, static pressure 100,000 Pa and Mach number 0.50. With $\gamma=1.4$ and $R=287$ J/(kg K), find local speed, stagnation temperature and stagnation pressure.
2. Find the isentropic area ratio $A/A^*$ at Mach 2 for $\gamma=1.4$. Does that area ratio uniquely identify supersonic flow?
3. A simple ideal converging nozzle has reservoir pressure 150,000 Pa, reservoir temperature 300 K and back pressure 100,000 Pa. Determine whether it is choked and calculate exit Mach number and temperature. Use the same air model and an adequately large reservoir.

### Solutions

1. Sound speed is $\sqrt{1.4(287)(300)}=347.189$ m/s, giving **173.594 m/s**. The temperature multiplier is $1+0.2(0.5)^2=1.05$, so **$T_0=315.000$ K** and **$p_0=118,621.3$ Pa**. These pressures are absolute.
2. Substitution gives **$A/A^*=1.68750$**. A second, subsonic root also exists. Geometry and area ratio must be combined with boundary conditions and the presence or absence of shocks to identify the actual branch.
3. The imposed ratio is **0.666667**, above the critical value 0.528282, so the exit remains subsonic and its pressure matches back pressure in this ideal solution. Inverting formula 4 gives **$M_e=0.783659$** and **$T_e=267.183$ K**. Applying the choked mass-flow formula to this case without checking the ratio would be unjustified.

### Common mistakes

Use absolute pressure and Kelvin in every gas-state and stagnation relation. Do not carry the same stagnation pressure through a shock. Keep the local sound speed separate from fluid speed. A sonic reference area can change across an irreversible region, so one global $A^*$ is not automatically valid. “Adiabatic” does not mean “isentropic.” An increasing static pressure is compatible with a decreasing stagnation pressure when losses occur.

### Applications and limits

These models support early nozzle estimates, gas-turbine inlet reasoning and compressible CFD benchmarks. Long pipes with friction lead to Fanno-flow models; constant-area heating leads to Rayleigh-flow models. Both can produce choking without a geometric throat. Oblique shocks, expansion fans, boundary layers and real-gas effects require further development. The nozzle example does not establish valve capacity, pressure-relief sizing or a safe hardware operating envelope; those need the applicable device data and design methods.

### Further reading

- [NASA Glenn: Mass Flow Choking](https://www.grc.nasa.gov/www/k-12/airplane/mflchk.html) — derivation of the ideal mass-flow function and its sonic maximum.
- [NASA Glenn: Normal Shock Wave Equations](https://www.grc.nasa.gov/www/k-12/airplane/normal.html) — static and stagnation changes across a normal shock.
- [MIT OCW: Compressible Fluid Dynamics](https://ocw.mit.edu/courses/2-26-compressible-fluid-dynamics-spring-2004/) — full course materials extending to area change, friction, heat addition, waves and shocks.


---

## 39. Engineering acoustics

### Learning map

Prerequisites: [vibrations](../chapters/20-vibrations.md), elementary waves, logarithms and fluid properties. Learn to distinguish source sound power from receiver sound pressure, convert between pressure and intensity under appropriate assumptions, add independent sound contributions, and analyze basic reflection and duct resonance. The aim is to build a defensible first acoustic model for mechanical equipment before using detailed measurements or numerical acoustics.

### Theory

Sound in a fluid is a traveling disturbance of pressure, density and particle velocity. The fluid particles oscillate about their mean positions while the disturbance propagates through the medium. Particle velocity is therefore different from sound speed. A small particle motion can accompany a wave traveling hundreds of meters per second. Linear acoustics assumes the disturbances are sufficiently small that products of perturbations can be neglected.

Acoustic pressure is the fluctuating part of total pressure, not the atmospheric or static pressure itself. A sinusoidal pressure has zero mean but nonzero mean square, so its root-mean-square value measures amplitude for many energy calculations. Peak, peak-to-peak and rms values are different conventions. For random sound, rms must be associated with a measurement bandwidth and averaging interval; there need not be a single meaningful sinusoidal peak factor.

Sound pressure level describes pressure at a particular position. Sound power describes the rate of acoustic energy emitted by a source across an enclosing surface. The same source can produce different pressure levels at different distances or in different rooms. Reflections, directionality and absorption influence the received field. Comparing an equipment sound-power declaration directly with a microphone sound-pressure reading confuses two physical quantities, even though both are expressed in decibels.

A decibel is a logarithm of a dimensionless ratio. A level is incomplete without its reference and physical quantity. This chapter uses 20 micropascals for airborne sound pressure, $10^{-12}$ W/m2 for intensity and $10^{-12}$ W for power. These references do not make pressure level and intensity level universally identical. A-weighting and other filters modify the spectral contribution before reporting a level; unweighted calculations here must not be relabeled as dBA.

In a traveling plane wave, pressure and particle velocity are in phase and their ratio is the characteristic impedance. In a standing wave, incident and reflected components interfere. High rms pressure can exist where net average energy flow is small or zero. Thus a microphone pressure measurement alone does not generally determine intensity in a reactive near field or strongly reflecting space.

Independent sound sources combine through mean-square pressure when their cross-correlation averages to zero. Their decibel values do not add arithmetically. Coherent tones require phase-sensitive addition instead: two equal in-phase pressures double the pressure, whereas two equal incoherent sources double the mean-square pressure. This distinction matters when comparing rotating-machine tones with broadband background noise.

### Formula handbook

Let $p'$ be acoustic pressure in Pa, $u'$ particle velocity in m/s, $\rho_0$ mean density in kg/m3, $c$ sound speed in m/s and $W_a$ acoustic power in W. These equations assume linear acoustics unless specified otherwise.

1. Small pressure perturbation and sound speed:

$$
p_{total}=p_0+p',\qquad c=\sqrt{K_s/\rho_0}=\sqrt{\gamma RT}\quad\text{for a perfect gas}.
$$

$K_s$ is the isentropic bulk modulus in Pa. The gas formula uses absolute temperature in K.

2. Homogeneous lossless wave equation with no mean flow:

$$
\nabla^2p'-\frac1{c^2}\frac{\partial^2p'}{\partial t^2}=0.
$$

3. Sinusoidal wave, rms amplitude and wavelength:

$$
p'=\hat p\cos(\omega t-kx+\theta),\qquad p_{rms}=\frac{\hat p}{\sqrt2},\qquad \lambda=\frac cf,\qquad k=\frac{2\pi}{\lambda}.
$$

$\omega=2\pi f$ in rad/s; $f$ is frequency in Hz. The rms conversion applies to a sinusoid.

4. Specific acoustic impedance and progressive plane-wave impedance:

$$
Z=\frac{\tilde p}{\tilde u},\qquad Z_0=\rho_0c.
$$

Tildes denote complex amplitudes; impedance has units Pa s/m. General $Z$ can be complex, while $Z_0$ here is real and positive for a wave traveling in the positive direction.

5. Time-averaged intensity and its plane-wave reduction:

$$
I=\langle p'u'\rangle=p_{rms}u_{rms}\cos\phi,\qquad I=\frac{p_{rms}^2}{\rho_0c}\quad\text{for a progressive plane wave}.
$$

$\phi$ is pressure-velocity phase difference for single-frequency harmonic quantities. For a general broadband signal, use the time average or a suitable cross-spectral calculation rather than assigning one phase angle to all frequencies. Intensity is directional and measured in W/m2.

6. Airborne sound-pressure level:

$$
L_p=20\log_{10}\left(\frac{p_{rms}}{p_{ref}}\right),\qquad p_{ref}=20\times10^{-6}\ \mathrm{Pa}.
$$

7. Intensity and sound-power levels, for positive scalar magnitudes:

$$
L_I=10\log_{10}(I/I_{ref}),\quad I_{ref}=10^{-12}\ \mathrm{W/m^2},\qquad L_W=10\log_{10}(W_a/W_{ref}),\quad W_{ref}=10^{-12}\ \mathrm W.
$$

8. Ideal free-field intensity from a compact source:

$$
I(r)=\frac{Q_dW_a}{4\pi r^2}.
$$

$Q_d$ is a dimensionless directivity factor in the observation direction; $Q_d=1$ for an omnidirectional source. The model excludes reflections and atmospheric attenuation.

9. Pressure-level change in the same free-field far-field direction:

$$
L_p(r_2)-L_p(r_1)=-20\log_{10}(r_2/r_1).
$$

10. Addition of mutually incoherent pressure levels with the same reference and bandwidth:

$$
L_{p,total}=10\log_{10}\left(\sum_i10^{L_{p,i}/10}\right).
$$

11. Coherent pressure addition instead uses complex amplitudes:

$$
\tilde p_{total}=\sum_i\tilde p_i.
$$

Two equal in-phase sinusoidal pressures increase level by $20\log_{10}2=6.0206$ dB; two equal incoherent sources increase it by $10\log_{10}2=3.0103$ dB.

12. Normal-incidence pressure reflection at a boundary between two lossless fluid half-spaces:

$$
r_p=\frac{Z_2-Z_1}{Z_2+Z_1},\qquad t_p=\frac{2Z_2}{Z_2+Z_1}.
$$

$r_p$ and $t_p$ relate reflected and transmitted pressure amplitudes to incident pressure. They are not power fractions.

13. Corresponding energy fractions for real positive impedances:

$$
\mathcal R=r_p^2,\qquad \tau=\frac{Z_1}{Z_2}t_p^2=\frac{4Z_1Z_2}{(Z_1+Z_2)^2},\qquad \mathcal R+\tau=1.
$$

14. Transmission loss and absorption bookkeeping:

$$
TL=10\log_{10}(W_{incident}/W_{transmitted})=-10\log_{10}\tau,\qquad \alpha=1-\mathcal R-\tau.
$$

The absorption relation is for a passive boundary with all reflected and transmitted channels accounted for. Absorption and transmission loss measure different outcomes.

15. Ideal longitudinal duct resonances, neglecting end corrections and losses:

$$
f_n=\frac{nc}{2L}\quad\text{open-open},\qquad f_n=\frac{(2n-1)c}{4L}\quad\text{closed-open},\qquad n=1,2,3,\ldots
$$

An ideal open end is a pressure node; an ideal rigid closed end is a particle-velocity node.

### Derivation

Linearized one-dimensional momentum gives $\rho_0\partial u'/\partial t=-\partial p'/\partial x$. Linearized continuity gives $\partial\rho'/\partial t=-\rho_0\partial u'/\partial x$. For a small isentropic disturbance, $p'=c^2\rho'$. Differentiate the pressure relation in time and substitute continuity and momentum to obtain $\partial^2p'/\partial t^2=c^2\partial^2p'/\partial x^2$. This derivation makes the uniform medium, small disturbance and negligible mean-flow assumptions explicit.

The incoherent addition rule follows from $p_{total}=p_1+p_2$. Squaring and averaging gives $\langle p_{total}^2\rangle=\langle p_1^2\rangle+\langle p_2^2\rangle+2\langle p_1p_2\rangle$. Only when the cross term vanishes do mean squares add. Applying the pressure-level definition then gives formula 10. For coherent tones, the cross term depends on relative phase and cannot be discarded merely because two physical machines are present.

### Worked examples

#### Example 1: pressure, motion and energy in a plane wave

A 1000 Hz progressive plane wave in air has rms pressure 0.200 Pa. Take $\rho_0=1.20$ kg/m3 and $c=343$ m/s as supplied properties. Pressure level is $20\log_{10}[0.200/(20\times10^{-6})]=\mathbf{80.0000\ dB}$ re 20 micropascals. Characteristic impedance is **411.600 Pa s/m**. Intensity is **$9.71817\times10^{-5}$ W/m2**, particle-velocity rms is **$4.85909\times10^{-4}$ m/s**, and wavelength is **0.343000 m**. The pressure peak is **0.282843 Pa**. The intensity result assumes a progressive wave; inserting the same rms pressure from an arbitrary standing-wave measurement would not justify it.

#### Example 2: two sources and increased distance

Two compact, mutually incoherent sources each produce 80.0 dB sound pressure at a 1.0 m reference distance in the observation direction. Treat their separation as negligible for the propagation estimate and assume both the reference and receiver positions are in a free-field far field. Combined level at 1 m is $80+10\log_{10}2=\mathbf{83.0103\ dB}$. At 5.0 m the geometric reduction is $20\log_{10}5=\mathbf{13.9794\ dB}$, giving **69.0309 dB**. Independently, each source's mean-square pressure falls by a factor 25, and the combined rms pressure becomes **0.0565685 Pa**. That pressure reproduces the final level. A reflecting plant room or coherent tonal sources would require a different model.

### Exercises

1. A sinusoidal airborne sound has peak pressure 0.200 Pa. Find rms pressure and sound-pressure level using 20 micropascals as reference. Compare with Example 1, where 0.200 Pa was rms.
2. A normally incident plane wave meets a lossless interface with $Z_1=400$ and $Z_2=1600$ Pa s/m. Find pressure reflection coefficient, reflected power fraction, transmitted power fraction and transmission loss.
3. A 0.500 m duct has an ideal rigid closed end and an ideal open end. With $c=343$ m/s, find its first two longitudinal resonances. Find the fundamental if both ends are instead open, neglecting end correction.

### Solutions

1. Rms pressure is $0.200/\sqrt2=\mathbf{0.141421\ Pa}$ and level is **76.9897 dB**. Confusing the specified peak value with rms would overstate this sinusoid's pressure level by 3.0103 dB.
2. $r_p=(1600-400)/(1600+400)=\mathbf{0.600000}$. Thus **$\mathcal R=0.360000$**, **$\tau=0.640000$** and **$TL=1.93820$ dB**. The pressure transmission coefficient is 1.6, but its square is not the transmitted energy fraction; the impedance ratio is also needed. Reflected and transmitted fractions sum to one.
3. Closed-open resonances begin at **171.500 Hz** and **514.500 Hz**, the fundamental and third harmonic. The open-open fundamental is **343.000 Hz**. Real end radiation and geometry shift these ideal frequencies; pressure and displacement nodes must not be interchanged.

### Common mistakes

Do not add decibel numbers directly or use the factor 20 for a power ratio. Declare rms or peak and the pressure reference. A negative level is possible for a positive quantity below its reference; it does not mean negative acoustic energy. Distinguish acoustic pressure from static pressure and source power from receiver level. A highly absorbing finish can reduce reverberation without providing the transmission loss of a sealed barrier. Leaks and structural transmission can dominate an enclosure.

### Applications and limits

Apply these models to fan and pump noise, duct tones, acoustic sensors and preliminary enclosure reasoning. Begin with source, transmission path and receiver, then identify whether direct sound, reflected sound or structural vibration dominates. Measurements need stated location, bandwidth, weighting, calibration and operating condition. This chapter supplies no occupational exposure limits or compliance conclusions. Flow-generated noise, nonlinear shocks, porous absorbers, room modes and structural-acoustic coupling require models beyond the elementary equations here.

### Further reading

- [MIT OCW: The Quantification of Sound and the Wave Equation](https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/c45734e2684a8592c0600120a0b6584c_lec_1_2004.pdf) — pressure, particle velocity, impedance and acoustic fundamentals.
- [OpenStax: Sound Intensity](https://openstax.org/books/university-physics-volume-1/pages/17-3-sound-intensity) — energy transport, intensity and logarithmic levels in an openly published physics textbook.
- [TU Delft: Fundamentals of Acoustics](https://www.ocw.tudelft.nl/wp-content/uploads/Lecture_2_-_Fundamentals_on_acoustics.pdf) — wave propagation, reflection and transmission lecture materials.
- [OpenStax: Normal Modes of a Standing Sound Wave](https://openstax.org/books/university-physics-volume-1/pages/17-4-normal-modes-of-a-standing-sound-wave) — interference and ideal air-column resonances.


---

## 40. Corrosion Engineering

### Learning map

Prerequisites: materials science, elementary chemistry, electrical charge, and measurement uncertainty. Learn to identify a corrosion mechanism, define the exposed area and environment, and distinguish a thermodynamic driving force from a measured reaction rate. The calculations connect electrical charge to metal loss and metal loss to average thinning. Use them with inspection evidence; they do not determine allowable pressure, a safe inspection interval, or the remaining strength of a locally damaged component.

### Theory

Corrosion is material degradation through interaction with its environment. In aqueous metallic corrosion, an anodic reaction releases electrons as metal atoms enter an oxidized state, while a cathodic reaction consumes electrons. For iron dissolving as ferrous ions, the anodic reaction is $\mathrm{Fe\rightarrow Fe^{2+}+2e^-}$. A possible cathodic reaction in aerated near-neutral water is $\mathrm{O_2+2H_2O+4e^-\rightarrow4OH^-}$. Different environments support different reactions, and the eventual rust composition need not equal the initially dissolved ionic species.

Electronic conduction through the metal and ionic conduction through the electrolyte complete the circuit. A freely corroding isolated specimen can have zero externally measured net current while anodic and cathodic partial currents continue internally. Their charge rates balance at the corrosion potential. Therefore a zero ammeter reading is not evidence of zero corrosion. A corrosion current inferred from electrochemical measurements requires a valid interpretation of the reactions, geometry, and measurement method.

Thermodynamics describes the direction favored by a reaction and its equilibrium potential. Kinetics describes how quickly it proceeds. Polarization, passive films, dissolved-oxygen transport, solution resistance, and surface condition can change the rate. The Nernst equation adjusts an equilibrium potential for activities; it does not calculate corrosion current. A material can have a favorable oxidation driving force yet corrode slowly because a protective film limits reaction. Conversely, local film breakdown can concentrate attack into a small area.

Uniform corrosion removes material over much of the exposed surface, making average mass loss a useful thickness indicator. Pitting concentrates penetration in cavities, so a small total mass loss can coexist with a deep local defect. Crevices can create chemically distinct sheltered regions under gaskets, deposits, or overlaps. An average thinning rate cannot reconstruct the deepest pit or establish whether a remaining ligament is structurally acceptable. AMPP's descriptions of [uniform corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/uniform-corrosion) and [pitting](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/pitting-corrosion) support this mechanism distinction.

Galvanic interaction requires electrically connected materials and a shared conducting environment. The resulting potentials and currents depend on the actual environment and surface states, not only on a table of standard potentials. A small anodic area coupled to a larger cathodic area can experience concentrated anodic current. Area ratio alone does not supply a numerical corrosion rate because polarization and transport also change the total current. AMPP explains these coupling conditions in its [galvanic-corrosion overview](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/galvanic-corrosion).

Other mechanisms include erosion-corrosion, selective dissolution, intergranular attack, corrosion fatigue, stress-corrosion cracking, and hydrogen-related damage. Their distinction matters because replacing lost thickness may not address cracking or the chemical cause. Mitigation can involve materials selection, drainage and crevice reduction, coatings, electrical isolation, chemistry control, inhibitors, or designed cathodic protection. Selection depends on service and inspection evidence; a corrosion allowance is only one possible response to a characterized mechanism.

### Formula handbook

Use time $t$ in s, current $I$ in A, charge $q$ in C, exposed area $A_e$ in $\mathrm{m^2}$, density $\rho$ in $\mathrm{kg/m^3}$, and metal molar mass $M$ in kg/mol. $F\approx96485.33212\ \mathrm{C/mol}$ is the Faraday constant, $R=8.314462618\ \mathrm{J/(mol\,K)}$, and $z$ is the electron count per stated metal-oxidation reaction.

**1. Accumulated charge:**

$$
q=\int_0^t I(\tau)\,d\tau;\qquad q=It\quad\text{for constant current}.
$$

**2. Mean anodic current density:**

$$
i_a=I_a/A_e.
$$

Use the anodic partial current and its participating area, not an unexplained net external current.

**3. Faraday metal-loss relation:**

$$
\Delta m=\eta_F\frac{Mq}{zF}.
$$

$\eta_F$ is the fraction of the specified charge attributed to that dissolution reaction. Set it to one only when that assumption is justified. Alloy dissolution may need separate species and valence accounting.

**4. Average depth removed from one stated exposed surface area:**

$$
\bar d=\frac{\Delta m}{\rho A_e}.
$$

If both faces of a thin coupon are exposed, include both in $A_e$. Their individual penetration is different from the total reduction of plate thickness.

**5. Average measured thinning rate and conversion:**

$$
\bar c=\frac{\bar d}{t},\qquad c_{\rm mm/year}=\bar c_{\rm m/s}(1000)(365\times24\times3600).
$$

The “year” here is explicitly 365 days. Extrapolation assumes unchanged exposure and mechanism.

**6. Convenient coupon units, with cleaned metal mass loss:**

$$
c_{\rm mm/year}=\frac{87.6\,\Delta m_{\rm mg}}{\rho_{\rm g/cm^3}A_{\rm cm^2}t_{\rm h}}.
$$

This is a unit-conversion formula, not an alternative physical law. Cleaning must remove corrosion products without counting unrelated metal removal as service loss.

**7. Uniform electrochemical penetration rate:**

$$
\dot d=\eta_F\frac{M i_a}{zF\rho}.
$$

The result is m/s. Local current concentration invalidates interpreting this mean as maximum penetration.

**8. Reaction quotient and Nernst equation:**

$$
\mathcal Q=\prod_j a_j^{\nu_j},\qquad E_{\rm eq}=E^\circ-\frac{RT}{zF}\ln\mathcal Q.
$$

$a_j$ are dimensionless activities and $\nu_j$ are positive for products and negative for reactants. Use a consistently written reduction half-reaction or complete cell reaction. Pure solid phases have unit activity in their standard states. Potential is in V; half-cell potentials require a stated reference. The [IUPAC definition](https://goldbook.iupac.org/terms/view/09068/plain) specifies equilibrium and activities.

**9. At 298.15 K, base-ten form:**

$$
E_{\rm eq}=E^\circ-\frac{0.05915935\ \mathrm V}{z}\log_{10}\mathcal Q.
$$

The numerical coefficient changes with temperature. Concentration ratios replace activities only under an appropriate ideal or calibrated approximation.

**10. Complete-cell reaction free energy:**

$$
\Delta_rG=-zFE_{\rm cell}.
$$

This gives J per mole of reaction as written for a reversible cell potential. It does not give the heat generation of an operating corroding surface.

**11. Complete-cell equilibrium constant:**

$$
\ln K=\frac{zFE^\circ_{\rm cell}}{RT}.
$$

This follows at equilibrium, where $E_{\rm cell}=0$ and $\mathcal Q=K$.

**12. Simple uniform-loss projection:**

$$
t_w(\tau)=t_{w,0}-c\tau.
$$

Wall thicknesses $t_w,t_{w,0}$ and rate/time units must match. This kinematic estimate is not a pressure-design equation or fitness-for-service assessment.

**13. Descriptive pitting factor:**

$$
PF=d_{\max}/\bar d\qquad(\bar d>0).
$$

It describes inspected penetration relative to average loss over the stated area. It does not predict future pit growth.

### Derivation

One mole of metal atoms undergoing an oxidation that transfers $z$ electrons per atom transfers $zF$ coulombs. Charge $q$ therefore corresponds to $q/(zF)$ moles of that reaction. Multiplying by molar mass and the attributed charge fraction gives Faraday's mass relation. Dividing by density gives volume lost; dividing by exposed area gives mean penetration. Every step has a physical boundary: measured current must represent the reaction, mass must mean original metal removed, and exposed area must include all contributing surfaces.

For the practical coupon formula, a loss in milligrams becomes grams by multiplying by $10^{-3}$. Division by density in g/cm³ and area in cm² gives centimetres of penetration. Multiplying by 10 gives millimetres; multiplying a per-hour rate by 8760 gives a 365-day annual rate. The combined multiplier is $10^{-3}\times10\times8760=87.6$. This derivation explains why changing any stated unit without changing the factor gives an incorrect rate.

### Worked examples

#### Example 1: charge, iron loss, and average thinning

Assume iron dissolves exclusively as $\mathrm{Fe^{2+}}$ with constant anodic current $I_a=0.00500$ A for 30 days, $\eta_F=1$, $M=0.055845$ kg/mol, $\rho=7870\ \mathrm{kg/m^3}$, and total participating area $A_e=0.0100\ \mathrm{m^2}$. The current is an assumed anodic dissolution current, not a direct open-circuit ammeter reading.

Time is $2{,}592{,}000$ s and charge is $12{,}960$ C. Mass loss is $0.055845(12960)/(2F)=0.003750576$ kg, or **3.75058 g**. Dividing by $7870(0.0100)$ gives average penetration **0.0476566 mm** over 30 days. A constant-rate annualization gives **0.579822 mm/year**. The current-density route, $i_a=0.500\ \mathrm{A/m^2}$ followed by Formula 7, gives the same result. Neither route supplies maximum pit depth or an acceptable operating pressure.

#### Example 2: equilibrium potential of a stated cell reaction

For $\mathrm{Zn(s)+Cu^{2+}\rightarrow Zn^{2+}+Cu(s)}$, assume supplied standard cell potential $E^\circ=1.100$ V at 298.15 K. The electron count is two. Let the dimensionless ionic activities be $a_{\mathrm{Zn^{2+}}}=1.00$ and $a_{\mathrm{Cu^{2+}}}=0.0100$, with pure metals at unit activity. Then $\mathcal Q=100$ and $E=1.100-(0.05915935/2)\log_{10}(100)=\mathbf{1.04084\ V}$. The reaction free energy is $-2FE=\mathbf{-200.852\ kJ/mol}$ of reaction. The positive potential favors the written reaction under these assumptions, but no current, metal-loss rate, or galvanic service-life prediction follows without kinetic and circuit information.

### Exercises

1. A cleaned iron coupon loses 2.00 g over 60 days. Its total exposed area is $0.0250\ \mathrm{m^2}$ and density is $7870\ \mathrm{kg/m^3}$. Find average loss and its constant-rate annualization.
2. Convert $1.00\ \mathrm{\mu A/cm^2}$ to $\mathrm{A/m^2}$, then calculate uniform iron penetration in mm/year for $z=2$, $M=0.055845$ kg/mol, $\rho=7870\ \mathrm{kg/m^3}$, and unit charge efficiency.
3. At 298.15 K, a two-electron cell reaction's quotient increases tenfold while its standard potential remains fixed. Find the change in equilibrium cell potential.

### Solutions

1. Average depth is $0.002/[7870(0.025)]=1.01652\times10^{-5}$ m, or **0.0101652 mm**. Multiplying by $365/60$ gives **0.0618382 mm/year**. This assumes the 60-day exposure is representative of the projected period.
2. One square centimetre is $10^{-4}\ \mathrm{m^2}$, so the current density is **0.0100 A/m²**. Formula 7 gives $3.67721\times10^{-13}$ m/s, equivalent to **0.0115964 mm/year**. A missing area conversion would cause a factor-of-10,000 error.
3. $\Delta E=-(0.05915935/2)\log_{10}(10)=\mathbf{-0.0295797\ V}$, or **−29.5797 mV**. Increasing the quotient favors products less strongly for the reaction convention used.

### Common mistakes

Confusing electrode potential with corrosion rate, using net external current as the dissolution current, and overlooking oxidation valence are fundamental errors. Keep oxide mass separate from metal mass loss. Do not extrapolate average loss into a localized defect depth or reuse a seawater galvanic ranking for every water chemistry. A coating defect can change the participating areas; simply specifying a coating does not prove galvanic isolation or complete protection.

### Applications and limits

For plant piping, record material identity, temperature, fluid chemistry, aeration, deposits, wet/dry duty, electrical connections, and inspection locations before selecting a model. Compare repeated thickness maps, coupon data, and mechanism evidence rather than relying on one average. Inspection intervals, corrosion allowances, cathodic-protection settings, and pressure adequacy need applicable project requirements and specialist assessment. This chapter provides an educational calculation basis and deliberately supplies no universal acceptance thickness or protection potential.

### Further reading

- [IUPAC Gold Book — Nernst equation](https://goldbook.iupac.org/terms/view/09068/plain): primary definition, activities, and potential convention.
- [AMPP — Uniform corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/uniform-corrosion): mechanism and general thinning.
- [AMPP — Pitting corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/pitting-corrosion): localized attack and detection concerns.
- [AMPP — Galvanic corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/galvanic-corrosion): electrical coupling and environmental context. Links checked 2026-11-07; linked content is not reproduced as a standards document here.


---

## 41. Welding Engineering

### Learning map

Prerequisites: materials science, heat transfer, manufacturing, stress analysis, and engineering drawings. Connect joining process, thermal cycle, metallurgy, geometry, loading, and inspection. Begin by distinguishing arc energy from heat transferred to the workpiece, and weld leg length from effective throat. The elementary calculations here estimate energy, geometry, and nominal stress. They do not qualify a procedure or establish a code-compliant weld size, fatigue life, or pressure boundary.

### Theory

Welding forms a joint through localized coalescence, with or without melting, pressure, or filler metal depending on the process. In common fusion welding, the weld pool solidifies while adjacent unmelted parent metal experiences a thermal cycle. That adjacent heat-affected zone, or HAZ, can undergo changes in grain structure, phases, hardness, toughness, and residual stress. A joint therefore contains more than a homogeneous block of deposited filler.

Process choice affects access, deposition, shielding, thermal input, defects, and automation. Gas tungsten arc welding uses a nonconsumable electrode and can add filler separately. Gas metal arc welding feeds a consumable wire. Shielded metal arc welding uses a coated consumable electrode, while submerged arc welding operates beneath granular flux. Laser and electron-beam processes concentrate energy differently; resistance and solid-state processes use other heat and pressure histories. A procedure valid for one process is not automatically transferable to another.

Heat input per unit length is one descriptor of a thermal cycle. The same nominal value can produce different temperature fields because plate thickness, joint geometry, travel speed, source distribution, preheat, and boundary heat losses differ. Faster cooling can promote hard microstructures in susceptible steels; excessively slow cooling can also impair desired properties in particular materials. Preheat and interpass control must therefore follow the material and procedure requirements. TWI explains why [increased heat input or preheat is not a universal remedy for hydrogen cracking](https://www.twi-global.com/technical-knowledge/faqs/faq-do-increased-preheat-and-heat-input-always-reduce-the-risk-of-hydrogen-cracking).

Hydrogen-assisted cracking depends on interacting material susceptibility, hydrogen, stress, and thermal history. Solidification cracking has a different mechanism associated with the final stages of freezing. Lack of fusion, incomplete penetration, porosity, undercut, and inclusions are also distinct discontinuities. Calling every imperfection a crack obscures its cause and the appropriate examination. Cleaning, fit-up, shielding, consumable handling, and repeatable parameters support quality, but acceptance requires the specified evaluation procedure.

Heating expands material locally; surrounding cooler material restrains that expansion. Plastic deformation and subsequent uneven contraction can leave distortion and residual stress after cooling. Clamping may reduce visible movement while increasing restraint, so zero visible distortion does not imply zero residual stress. TWI's [distortion explanation](https://www.twi-global.com/technical-knowledge/faqs/faq-what-causes-distortion) describes this thermal and mechanical interaction. A purely elastic expansion formula illustrates the strain scale; it cannot predict the final weld residual-stress field after melting, yielding, and phase transformation.

Joint design must provide a load path and fabrication access. Weld toes and roots introduce local stress concentrations. Cyclic performance depends on stress range, detail geometry, quality, environment, and the chosen fatigue assessment method. Simply selecting a stronger filler or enlarging a weld does not establish improved fatigue resistance at the governing location. Drawing symbols must distinguish leg and throat, weld side, length, pitch, contour, penetration requirements, and the applicable inspection basis.

### Formula handbook

Use current $I$ in A, voltage $U$ in V, travel speed $v$ in m/s, length $L$ in m, force $F$ in N, and stress in Pa unless a numerical unit conversion is explicitly stated.

**1. Electrical arc power:**

$$
P_{arc}=UI,\qquad \overline P_{arc}=\frac1T\int_0^T U(t)I(t)\,dt.
$$

For pulsed waveforms, the product of average voltage and average current need not equal average power.

**2. Arc energy per unit length, constant conditions:**

$$
E_{arc}=UI/v.
$$

The result is J/m. **3. Net heat transferred per length:**

$$
H=\eta_{th}UI/v.
$$

$\eta_{th}$ is the specified thermal efficiency fraction. A code or procedure may define its reporting convention differently; identify whether the reported quantity includes this factor.

**4. Explicit conversion with numerical travel speed $s$ in mm/min:**

$$
H_{\rm kJ/mm}=\frac{60\eta_{th}UI}{1000s}.
$$

**5. Arc-on time and transferred energy for a uniform run:**

$$
t_{arc}=L/v,\qquad Q_{net}=HL=\eta_{th}UI\,t_{arc}.
$$

Time is s and energy J; setup and interpass time are additional.

**6. Cooling interval and mean cooling rate:**

$$
t_{8/5}=t(T=500^\circ\mathrm C)-t(T=800^\circ\mathrm C),\qquad \overline{|\dot T|}=300/t_{8/5}.
$$

This defines a monotonic cooling segment in seconds, with rate K/s. It is a useful descriptor for some steel welds, not a universal metallurgical acceptance limit.

**7. Ideal equal-leg, flat-faced, right-angle fillet throat:**

$$
a=z\sin45^\circ=\frac z{\sqrt2}.
$$

$z$ is leg length and $a$ the theoretical root-to-face distance. This construction gives no extra penetration credit. Concavity, fit-up, fusion, and the governing design definition can change effective throat; see [TWI's throat-geometry discussion](https://www.twi-global.com/technical-knowledge/job-knowledge/design-part-2-091).

**8. Nominal throat area of several weld segments:**

$$
A_w=\sum_i a_iL_{e,i}.
$$

$L_{e,i}$ are effective lengths supplied by the model or governing design method, not automatically every visible millimetre of a bead.

**9. Centered direct loading, ideal uniform nominal shear:**

$$
\tau_{nom}=F/A_w.
$$

Load sharing assumes a symmetric or otherwise justified stiffness distribution. This equation excludes eccentric moment and local notch stresses.

**10. Elastic weld-line-group centroid and polar area moment:**

$$
\bar x=\frac{\int x\,a\,d\ell}{A_w},\qquad \bar y=\frac{\int y\,a\,d\ell}{A_w},\qquad J_w=\int(x^2+y^2)a\,d\ell.
$$

Coordinates in $J_w$ are measured from the group centroid. $J_w$ is in $\mathrm{m^4}$.

**11. Nominal in-plane moment loading in that line-group model:**

$$
M_z=Fe,\qquad \boldsymbol\tau_M=\frac{M_z}{J_w}(-y\mathbf e_x+x\mathbf e_y),\qquad \boldsymbol\tau=\frac{\mathbf F}{A_w}+\boldsymbol\tau_M.
$$

Here $e$ is a perpendicular eccentricity (m). Vector addition matters. This elastic nominal distribution is not a local three-dimensional throat stress or a code interaction rule.

**12. Ideal triangular fillet volume and mass:**

$$
A_f=z^2/2,\qquad V_f=A_fL,\qquad m_f=\rho V_f.
$$

$A_f$ is bead cross-sectional area, distinct from throat area $A_w$. The mass estimate excludes reinforcement, penetration, spatter, and dilution bookkeeping; it is not necessarily wire consumption.

**13. Constant-property thermal strain and free movement:**

$$
\varepsilon_{th}=\alpha\Delta T,\qquad \Delta L_{free}=\alpha L\Delta T.
$$

$\alpha$ is in K⁻¹. **14. Fully restrained, uniaxial elastic idealization:**

$$
\sigma_{th}=-E\alpha\Delta T.
$$

$E$ is modulus in Pa. The formula ceases to apply when yielding, creep, transformation, or restraint change becomes significant; it is not a weld residual-stress formula.

**15. Stress-range and generic power-law fatigue representation:**

$$
\Delta\sigma=\sigma_{max}-\sigma_{min},\qquad N(\Delta\sigma)^m=C.
$$

$N$ is cycles, and $C$ has the units required by the specified stress measure and fitted exponent $m$. Nominal, structural hot-spot, and notch-stress curves are not interchangeable. No fatigue class or allowable value is supplied here.

### Derivation

For constant power, a weld travels distance $dL=v\,dt$ while the arc supplies energy $dE=UI\,dt$. Dividing gives arc energy per length $UI/v$. Multiplication by thermal efficiency estimates the energy entering the workpiece. Integrating over a uniform run gives $Q_{net}=HL$, which must also equal net power times arc-on time. This equivalence is a useful independent unit check.

For an equal-leg flat fillet, the ideal cross-section is a right isosceles triangle. Its hypotenuse is $z\sqrt2$ and its area is $z^2/2$. Expressing that same area as half the hypotenuse times its perpendicular altitude gives $z^2/2=(z\sqrt2)a/2$, hence $a=z/\sqrt2$. The two-dimensional geometric result only identifies the nominal throat; sound fusion and usable effective length still need to be established.

### Worked examples

#### Example 1: arc energy, net heat input, and run time

Assume steady $U=24$ V, $I=180$ A, thermal efficiency $0.80$, and travel speed $v=0.00500$ m/s, equivalent to 300 mm/min. Arc power is **4320 W** and net transferred power is **3456 W**. Arc energy is $4320/0.005=864000$ J/m, or **0.8640 kJ/mm**. Net heat input is **0.6912 kJ/mm**.

For a 0.300 m run, arc-on time is $0.300/0.005=\mathbf{60.0\ s}$. Net energy is $3456(60)=\mathbf{207.36\ kJ}$, also $0.6912(300)$ kJ. These values do not determine HAZ hardness or cooling time without material, thickness, geometry, preheat, and heat-loss information.

#### Example 2: symmetric double-fillet nominal stress

Two identical longitudinal fillets transmit a centered 20.0 kN force parallel to their lengths. Assume equal stiffness, no eccentricity, flat faces, 6.00 mm legs, no penetration credit, and an already specified effective length of 100 mm per weld. Each theoretical throat is $6/\sqrt2=\mathbf{4.24264\ mm}$. Total throat area is $2(4.24264)(100)=\mathbf{848.528\ mm^2}$.

Uniform nominal shear is $20000/848.528=\mathbf{23.5702\ MPa}$. Each weld carries 10.0 kN, which reproduces the applied load when integrated over both throats. Ideal triangular bead volume is $2(6^2/2)(100)=3600\ \mathrm{mm^3}$; with supplied density $7850\ \mathrm{kg/m^3}$, ideal bead mass is **28.26 g**. The calculation supplies a nominal stress and geometric mass, not an allowable load or fatigue qualification.

### Exercises

1. At 22 V, 160 A, thermal efficiency 0.75, and travel speed 240 mm/min, calculate net heat input in kJ/mm.
2. Two symmetric longitudinal fillets each have 5 mm legs and 80 mm effective length. Under centered 12 kN loading parallel to the welds, find total throat area and nominal uniform shear.
3. A hypothetical uniform 0.500 m steel bar has $\alpha=12\times10^{-6}\ \mathrm{K^{-1}}$ and undergoes a 400 K temperature rise. Find free expansion. With $E=200$ GPa, find the fully restrained elastic stress prediction and explain why it cannot be asserted as an actual welding residual stress.

### Solutions

1. $H=60(0.75)(22)(160)/(1000\times240)=\mathbf{0.660\ kJ/mm}$. Omitting efficiency would instead report arc energy, 0.880 kJ/mm.
2. Throat is $5/\sqrt2=3.53553$ mm, total area is $2(3.53553)(80)=\mathbf{565.685\ mm^2}$, and shear is $12000/565.685=\mathbf{21.2132\ MPa}$. The stipulated symmetry and absence of eccentricity are essential.
3. Free expansion is $12\times10^{-6}(0.500)(400)=\mathbf{2.40\ mm}$. The ideal restrained stress is **−960 MPa**. This is an elastic-model result, not a credible universal material response: yielding and temperature-dependent properties can invalidate it. An actual weld also has nonuniform heating, cooling, melting, changing restraint, and metallurgical transformations.

### Common mistakes

Mixing mm/min with m/s creates large heat-input errors. A 6 mm leg is not a 6 mm throat. More convex reinforcement does not automatically add the assumed effective throat. Distinguish a procedure specification, its qualification evidence, and welder or operator qualification. Inspection can reveal relevant discontinuities but cannot by itself replace the required design and qualification evidence.

### Applications and limits

For a fabrication package, connect the drawing, joint preparation, material and filler identification, procedure, qualification records, fit-up, heat-treatment requirements, inspection plan, and acceptance criteria. Use the governing construction standard and its required edition. ASME's [official Section IX page](https://www.asme.org/codes-standards/find-codes-standards/bpvc-ix-bpvc-section-ix-welding-brazing-fusing-qualifications-%282%29) identifies its qualification subject matter; it does not make the elementary stress calculation here a complete structural or pressure design. No copyrighted qualification ranges, fatigue classes, or acceptance limits are reproduced.

### Further reading

- [TWI — hydrogen cracks in steels](https://www.twi-global.com/technical-knowledge/job-knowledge/defects-hydrogen-cracks-in-steels-identification-045): mechanisms and the distinction between arc energy and thermal heat input.
- [TWI — fillet throat geometry](https://www.twi-global.com/technical-knowledge/job-knowledge/design-part-2-091): leg, throat, face shape, and geometric interpretation.
- [TWI — causes of distortion](https://www.twi-global.com/technical-knowledge/faqs/faq-what-causes-distortion): thermal restraint, plasticity, and contraction.
- [ASME — BPVC Section IX](https://www.asme.org/codes-standards/find-codes-standards/bpvc-ix-bpvc-section-ix-welding-brazing-fusing-qualifications-%282%29): official publisher page; consult applicable project requirements for edition and scope. Links checked 2026-11-07.
