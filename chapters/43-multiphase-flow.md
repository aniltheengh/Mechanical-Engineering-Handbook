# 43. Multiphase flow

## Learning map

Prerequisites: [fluid mechanics](10-fluid-mechanics.md), [pipe flow](11-pipe-flow-and-pumps.md), [thermodynamics](08-thermodynamics.md) and [mass transfer](17-mass-transfer.md). Learn to distinguish phase mass flow from phase occupancy, construct homogeneous and slip descriptions, conserve each phase, and assess a simple particle-settling model. The emphasis is on quantities that can be defined and checked before choosing a specialized pressure-drop or heat-transfer correlation.

The [visual guide](../VISUAL_GUIDE.md#gas-mass-quality-and-void-fraction) compares gas mass-flow quality with void fraction for three prescribed slip ratios. Use it to see why a small gas mass fraction can occupy a large part of a passage.

## Theory

A multiphase flow contains distinct material phases with interfaces: gas bubbles in water, liquid droplets in gas, solid particles in liquid, or combinations of these. Two chemical species do not necessarily form two phases; a fully mixed air stream is a gas phase containing several species. Conversely, liquid water and water vapor form two phases of one substance. Phase identity determines which conservation laws and equilibrium relations are appropriate.

**Flow quality** is a phase mass-flow fraction. **Void fraction** is the fraction of local volume, or a representative cross-sectional area, occupied by the gas phase. Their difference is particularly large when gas density is much lower than liquid density. A small gas mass flow can occupy a substantial fraction of the passage. In an air-water flow, the symbol $x$ below means gas mass-flow fraction; it does not imply boiling or saturation equilibrium.

Static quality describes the gas mass fraction contained in a representative local volume. It differs from flow quality when the phases move at different mean speeds. A fast gas phase can carry a specified mass flow through a smaller occupied area. Consequently, measuring mass flow alone does not determine gas holdup unless relative motion is known. The slip ratio supplies one possible additional relation, but its numerical value requires a model or measurement.

Superficial velocity divides each phase's volume flow by the entire passage area, as if that phase occupied the whole passage. It is useful for plotting operating conditions and describing flow maps. Actual phase velocity divides by the area occupied by that phase. Confusing the two can distort Reynolds numbers, interfacial forces and residence-time estimates. The sum of superficial velocities is a volumetric flux, not generally the velocity of either phase.

The homogeneous model assumes equal phase velocities and allows the mixture to be treated as one moving continuum for selected balances. Equal velocity does not automatically establish equal temperature or thermodynamic equilibrium. A homogeneous equilibrium model adds those assumptions where applicable. A slip model admits different velocities. A two-fluid model goes further by solving separate momentum and energy balances and requires interfacial drag, heat-transfer and mass-transfer closures. Adding equations without reliable closures does not guarantee better prediction.

Flow regime describes the spatial organization of phases. Gas-liquid examples include dispersed bubbles, elongated plugs, intermittent slugs, churn, annular liquid films and entrained droplets. Horizontal passages can develop stratification under gravity. Regime depends on geometry, inclination, phase properties and flow rates, rather than quality alone. An empirical map should be used within its tested conditions; a boundary on one map is not a universal physical constant.

Pressure change combines friction, gravity, acceleration and local disturbances. Gas expansion, evaporation or changing holdup can increase momentum flux even when the pipe area is constant. A pressure drop therefore need not be entirely frictional. In an upward line, gravity usually requires a pressure decrease along the flow; in a downward line it can produce pressure recovery. Intermittent slugs additionally create time-dependent loads that an average steady calculation does not capture.

## Formula handbook

Use subscripts $g$ and $l$ for gas and liquid, density $\rho$ in kg/m³, mass flow $\dot m$ in kg/s, area $A$ in m², speed in m/s and pressure in Pa. The one-dimensional relations use representative phase mean velocities and locally uniform phase properties. The slip formulas assume co-current flow with positive finite velocities.

1. Flow quality and static quality are different mass fractions:

$$
x=\frac{\dot m_g}{\dot m_g+\dot m_l},\qquad x_{st}=\frac{m_g}{m_g+m_l}.
$$

2. Gas area fraction and phase mass flow:

$$
\alpha=\frac{A_g}{A},\qquad \dot m_g=\rho_g\alpha A u_g,\qquad \dot m_l=\rho_l(1-\alpha)A u_l.
$$

Gas and liquid fractions sum to one. An area-averaged model must account consistently for nonuniform or fluctuating profiles.

3. Local volume-average mixture density and static quality:

$$
\rho_m=\alpha\rho_g+(1-\alpha)\rho_l,\qquad x_{st}=\frac{\alpha\rho_g}{\rho_m}.
$$

4. Superficial velocities and actual phase velocities:

$$
j_g=\frac{\dot m_g}{\rho_gA}=\alpha u_g,\qquad j_l=\frac{\dot m_l}{\rho_lA}=(1-\alpha)u_l,\qquad j=j_g+j_l.
$$

5. Total mass flux, in kg/(m² s):

$$
G=\frac{\dot m}{A}=\rho_gj_g+\rho_lj_l.
$$

6. Slip ratio and its relation to void fraction:

$$
S=\frac{u_g}{u_l},\qquad \alpha=\frac{x\rho_l}{x\rho_l+(1-x)\rho_gS},\qquad x_{st}=\frac{x}{x+S(1-x)}.
$$

The endpoint cases $x=0$ and $x=1$ are interpreted as single-phase limits; a velocity ratio for an absent phase is not physically measurable.

7. Homogeneous specialization, $S=1$:

$$
\frac1{\rho_h}=\frac{x}{\rho_g}+\frac{1-x}{\rho_l},\qquad u_g=u_l=j,\qquad G=\rho_hj,\qquad x_{st}=x.
$$

The reciprocal density uses mass fractions. The direct average in formula 3 uses volume fractions. With slip, $G/j$ is a transport ratio and need not equal local holdup density $\rho_m$.

8. Phase continuity in a constant-area one-dimensional passage:

$$
\frac{\partial(\alpha_k\rho_k)}{\partial t}+\frac{\partial(\alpha_k\rho_ku_k)}{\partial z}=\Gamma_k,\qquad \Gamma_g+\Gamma_l=0.
$$

$\Gamma_k$ is interphase mass production per mixture volume in kg/(m³ s), with no external mass injection. Adding phase equations cancels internal transfer.

9. Axial momentum flux for uniform phase profiles:

$$
\Pi=G^2\left[\frac{x^2}{\alpha\rho_g}+\frac{(1-x)^2}{(1-\alpha)\rho_l}\right],\qquad \Pi_h=G^2/\rho_h.
$$

Both have units Pa. Profile and fluctuation corrections may be needed beyond this approximation.

10. Steady constant-area mixture momentum balance along a passage of length $L$:

$$
p_{in}-p_{out}=\Delta p_f+\int_0^L\rho_mg\sin\theta\,dz+(\Pi_{out}-\Pi_{in})+\Delta p_{local}.
$$

$\theta$ is the angle above horizontal in the flow direction. Model local losses consistently without double-counting acceleration.

11. A homogeneous friction approximation and a separately defined multiplier:

$$
\left(-\frac{dp}{dz}\right)_{f,h}=\frac{f_DG^2}{2D_h\rho_h},\qquad \phi_{lo}^2=\frac{(-dp/dz)_{f,tp}}{(-dp/dz)_{f,lo}}.
$$

$f_D$ is the Darcy factor; $D_h$ is hydraulic diameter in m. The liquid-only reference $lo$ sends the **entire total mass flux** through the pipe as liquid. Effective viscosity and friction closures require a stated model; no universal mixture-viscosity averaging rule is implied.

12. Interfacial scaling parameters for a gas inclusion in liquid, of diameter $d$:

$$
We=\frac{\rho_lu_{rel}^2d}{\sigma},\qquad Eo=\frac{|\rho_l-\rho_g|gd^2}{\sigma}.
$$

Surface tension $\sigma$ is in N/m. These compare inertial and gravitational effects with surface tension; they do not alone identify a complete flow regime.

13. Rigid-sphere drag and particle Reynolds number:

$$
F_D=\tfrac12C_D\rho_fv_{rel}^2\frac{\pi d^2}{4},\qquad Re_p=\frac{\rho_f|v_{rel}|d}{\mu_f},\qquad C_D\simeq\frac{24}{Re_p}\quad(Re_p\ll1).
$$

Dynamic viscosity $\mu_f$ is in Pa s. Stokes drag is the creeping-flow limit, not a general sphere-drag law.

14. Terminal settling of an isolated rigid sphere in an effectively unbounded quiescent Newtonian fluid:

$$
v_t=\frac{(\rho_p-\rho_f)gd^2}{18\mu_f},\qquad F_D=3\pi\mu_fd|v_t|.
$$

Downward velocity is positive for a heavier particle. Check $Re_p$ using the calculated speed. The model excludes wall effects, particle interactions, deformation and significant noncontinuum effects.

15. Equilibrium vapor quality from enthalpy for a saturated, single-component two-phase mixture:

$$
x_{eq}=\frac{h-h_f}{h_g-h_f}.
$$

Enthalpies share one mass basis. This relation is not an air-water gas-fraction calculation and is not a literal phase fraction outside the two-phase equilibrium region.

## Derivation

Divide the two phase mass-flow expressions to obtain $x/(1-x)=\rho_g\alpha u_g/[\rho_l(1-\alpha)u_l]$. Substitute $S=u_g/u_l$ and solve for $\alpha$ to obtain formula 6. Setting $S=1$ converts mass-flow fractions into local mass fractions. A unit mass then occupies volume $x/\rho_g+(1-x)/\rho_l$, proving the homogeneous reciprocal-density formula. This route also explains why inserting flow quality into an arithmetic density average is incorrect.

For settling, the downward weight minus buoyancy is $(\rho_p-\rho_f)g\pi d^3/6$. At terminal speed it balances upward Stokes drag $3\pi\mu_fdv_t$. Cancelling common factors gives formula 14. The derivation assumes terminal force balance; the Reynolds check tests whether the drag law used to obtain that speed is self-consistent. A failed check means select a suitable drag relation and solve again, rather than retain the original answer.

## Worked examples

### Example 1: a homogeneous air-water mixture

A teaching model has total mass flow 1.000 kg/s, gas flow quality $x=0.001000$, area 0.0100 m², gas density 1.20 kg/m³ and liquid density 1000 kg/m³. Assume equal phase velocities and use these as local properties. Gas and liquid mass flows are **0.001000 kg/s** and **0.999000 kg/s**. Their superficial velocities are **0.0833333 m/s** and **0.0999000 m/s**. Thus common actual velocity is **0.183233 m/s**, gas void fraction is **0.454794**, and mixture density is **545.752 kg/m³**. Reconstructing total flow gives $\rho_hjA=1.000$ kg/s. Only 0.1% of the transported mass is gas, while about 45.48% of the modeled cross section is gas. This is a kinematic illustration, not evidence that a real mixture at these rates will remain homogeneous or avoid slugging.

### Example 2: slow settling of a small solid sphere

An isolated rigid sphere of diameter **20.0 micrometers** and density 2650 kg/m³ settles in still liquid of density 1000 kg/m³ and viscosity 0.00100 Pa s. Use $g=9.81$ m/s² and neglect walls and neighboring particles. Stokes settling gives **0.000359700 m/s**, or 0.359700 mm/s. Substitution into the particle Reynolds number gives **0.00719400**, well below unity and also below a conservative 0.1 screening value. Buoyant weight and drag both equal **$6.78019\times10^{-11}$ N**. Travel through 1.00 m at terminal speed takes **2780.09 s**, or **46.3349 min**. The travel estimate neglects the initial acceleration interval. A real suspension with flocs or many interacting particles need not settle at this isolated-sphere speed.

## Exercises

1. A homogeneous air-water flow has gas void fraction 0.100000, gas density 1.20 kg/m³ and liquid density 1000 kg/m³. Find gas flow quality and mixture density. Explain whether 10% gas occupancy means 10% gas mass.
2. Keep the phase mass flows, densities and total area of Example 1, but prescribe co-current slip ratio $S=2.000$. Find void fraction, actual phase velocities and static quality. Compare with the original homogeneous case.
3. Double the sphere diameter in Example 2 while retaining all other assumptions. Calculate the candidate terminal speed, Reynolds number and 1.00 m travel time. Check whether the Stokes approximation remains plausible.

## Solutions

1. Mixture density is $0.1(1.2)+0.9(1000)=\mathbf{900.120\ kg/m^3}$. Homogeneous quality is $0.1(1.2)/900.12=\mathbf{0.000133316}$, or **0.0133316%**. The low gas density explains the much smaller mass fraction.
2. Formula 6 gives **$\alpha=0.294325$**. The same superficial velocities divided by their occupied fractions give **$u_g=0.283133$ m/s** and **$u_l=0.141567$ m/s**, so their ratio is two. Static quality is **0.000500250**, while flow quality remains 0.001000. Faster gas occupies less area and less local mass inventory for the same transported gas mass rate.
3. Stokes speed scales with $d^2$, so it becomes **0.00143880 m/s**. Reynolds number scales with $d^3$ under this prediction, giving **0.0575520**. This remains small enough for a creeping-flow estimate, though less strongly asymptotic than before. Terminal travel time becomes **695.024 s**. Continuing the scaling to much larger diameters would eventually invalidate its own Reynolds assumption.

## Common mistakes

Do not equate mass quality with void fraction, or flow quality with static quality when slip exists. Use local gas density at the relevant absolute pressure and temperature. Distinguish superficial from actual velocity and total-mixture mass flux from liquid-phase mass flux. A mixture density alone does not establish a pressure-drop correlation. Check the particle Reynolds number after predicting settling; “small particle” is not a sufficient quantitative test. Rigid-sphere Stokes drag does not automatically describe a clean mobile-interface bubble.

## Applications and limits

These models help interpret aeration, gas entrainment, evaporators, condensers, slurries and sedimentation. Start by declaring phase properties, measurement bases, geometry, orientation and whether phase change occurs. Then select a closure justified for the regime and examine sensitivity to uncertain holdup or slip. Boiling dryout, compressible two-phase choking, severe slug loads, dense granular flow and non-Newtonian suspensions require additional treatment. Neither worked example establishes separator capacity, pump suitability or a pressure-system design rating.

## Further reading

- [MIT OCW: Notes on Two-Phase Flow, Boiling Heat Transfer, and Boiling Crises](https://ocw.mit.edu/courses/22-06-engineering-of-nuclear-systems-fall-2010/2e8614e58cc569d96acff67df51d9aef_MIT22_06F10_lec13.pdf) — definitions of quality, slip and void fraction, followed by homogeneous balances and flow-regime discussion.
- [TU Delft OCW: Sedimentation](https://ocw.tudelft.nl/wp-content/uploads/Sedimentation.pdf) — university lecture material on discrete settling, drag, applicability checks and the additional issues in sedimentation systems.
- [MIT OCW: Flow Past a Sphere and Settling](https://ocw.mit.edu/courses/12-090-introduction-to-fluid-motions-sediment-transport-and-current-generated-sedimentary-structures-fall-2006/7841d9b1681d6748fa2f5cbc6d6f1cb2_ch3.pdf) — deeper treatment of sphere drag and the restricted Stokes settling regime.
