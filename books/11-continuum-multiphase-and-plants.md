# Continuum mechanics, multiphase flow, and process plants

Mechanical Engineering Handbook · Expanded edition · 2026-11-08

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [42 · Continuum mechanics: deformation, stress, and balance](../chapters/42-continuum-mechanics.md)
- [43. Multiphase flow](../chapters/43-multiphase-flow.md)
- [44. Process Plant Engineering](../chapters/44-process-plant-engineering.md)

---

## 42 · Continuum mechanics: deformation, stress, and balance

### Learning map

Prerequisites are vectors, matrices, differentiation, statics, and [strength of materials](../chapters/06-strength-of-materials.md). This chapter connects material motion to strain, internal force to stress, and local equations to conservation. Learn to identify the reference and current configurations, distinguish finite deformation from its small-gradient approximation, and use a constitutive law within its assumptions. Continue to [finite element analysis](../chapters/24-finite-element-analysis.md), [fluid mechanics](../chapters/10-fluid-mechanics.md), or [composite materials](../chapters/37-composite-materials.md) after understanding these shared foundations.

### Theory

A continuum replaces discrete atoms or particles by smoothly varying fields such as displacement, density, temperature, and stress. The averaging scale should be large enough to smooth relevant microstructure but small enough to resolve the engineering variation of interest. A crack surface, a material interface, or a shock may interrupt smoothness; separate regions and appropriate jump or interface conditions are then needed. Continuum theory does not mean every field is smooth everywhere.

The reference coordinate $\mathbf X$ labels a material particle. Its current position is $\mathbf x=\boldsymbol\chi(\mathbf X,t)$. Following the same label gives a material, or Lagrangian, description. Describing fields at fixed spatial locations gives an Eulerian description. These are different descriptions of the same motion, not competing physical laws. A reference configuration need not be stress free, so initial stress and material history may require separate specification.

The deformation gradient describes local stretching, shearing, and rotation of neighboring material lines. Its determinant measures local volume change. Strain measures isolate changes of lengths and angles from rigid motion. A body can undergo large displacement without much strain: a nearly rigid part can translate or rotate substantially. Conversely, a small absolute displacement across a very short length can create a large strain. The basic infinitesimal-strain approximation requires small displacement gradients, including small rotations relative to its reference.

Stress represents force transmitted across an imagined cut. Cauchy stress acts on area measured in the current configuration. The force on a cut depends on its normal, so one scalar stress cannot describe a general three-dimensional state. In an ordinary continuum without body couples or independent couple stresses, angular-momentum balance makes Cauchy stress symmetric. A traction vector usually has both normal and tangential components, even when the chosen coordinate directions are principal directions.

Balance laws constrain every admissible material response but do not identify the material. Constitutive equations supply the missing relationships, such as elastic stress versus strain, viscous stress versus deformation rate, or plastic evolution with history. Linear isotropic elasticity is useful for small elastic strains in a material with approximately direction-independent response. It does not automatically describe rubber at large stretch, yielding steel, or a fiber composite. Changing a strain measure inside Hooke's law without changing the corresponding stress and energy formulation is not a valid general finite-deformation model.

A boundary-value problem combines kinematics, balance, constitutive behavior, initial conditions when needed, and boundary conditions. Prescribe displacement components or their conjugate traction components appropriately; prescribing both arbitrarily at the same location usually overconstrains the problem. Support conditions must remove unwanted rigid modes. A computed field also needs compatibility: independently chosen strain components may fail to arise from any continuous displacement field. Finite-element convergence alone cannot repair an inconsistent physical model.

### Formula handbook

Coordinates and displacements are in m, time in s, density in kg/m³, and stress in Pa. Bold uppercase $\mathbf E_G$ below is Green–Lagrange strain; scalar $E$ is Young's modulus. The double contraction is $\mathbf A:\mathbf B=\sum_{ij}A_{ij}B_{ij}$, so both symmetric off-diagonal terms contribute.

**1. Motion, displacement, and deformation gradient**:

$$
\mathbf u=\mathbf x-\mathbf X,\qquad
F_{iJ}=\frac{\partial x_i}{\partial X_J},\qquad
d\mathbf x=\mathbf F\,d\mathbf X,\qquad
\mathbf F=\mathbf I+\mathbf H,\quad\mathbf H=\nabla_X\mathbf u.
$$

$\mathbf F$ and $\mathbf H$ are dimensionless. Uppercase material indices identify derivatives in the reference configuration.

**2. Local volume and mass conservation**, for a locally invertible, orientation-preserving motion without mass sources:

$$
J=\det\mathbf F>0,\qquad dv=J\,dV,\qquad\rho J=\rho_0.
$$

Positive $J$ is a necessary local condition; it alone does not rule out distant parts of a body intersecting.

**3. Finite strain measures**:

$$
\mathbf C=\mathbf F^T\mathbf F,\qquad
\mathbf B=\mathbf F\mathbf F^T,\qquad
\mathbf E_G=\tfrac12(\mathbf C-\mathbf I),\qquad
\mathbf e=\tfrac12(\mathbf I-\mathbf B^{-1}).
$$

$\mathbf E_G$ refers to reference directions; Euler–Almansi strain $\mathbf e$ refers to current directions. They are generally different numerical tensors.

**4. Infinitesimal strain and the omitted term**:

$$
\boldsymbol\epsilon=\tfrac12(\mathbf H+\mathbf H^T),\qquad
\boldsymbol\omega=\tfrac12(\mathbf H-\mathbf H^T),\qquad
\mathbf E_G=\boldsymbol\epsilon+\tfrac12\mathbf H^T\mathbf H.
$$

Small-gradient theory neglects the quadratic term. Engineering shear strain is $\gamma_{xy}=2\epsilon_{xy}$, not $\epsilon_{xy}$.

**5. Polar decomposition and line stretch**, for nonsingular $\mathbf F$ with $J>0$:

$$
\mathbf F=\mathbf R\mathbf U=\mathbf V\mathbf R,\qquad
\mathbf R^T\mathbf R=\mathbf I,\quad\det\mathbf R=1,\qquad
\lambda_{\mathbf N}=\sqrt{\mathbf N\cdot\mathbf C\mathbf N}.
$$

$\mathbf U,\mathbf V$ are positive-definite stretch tensors; $\mathbf N$ is a reference unit direction. Pure rigid rotation has $\mathbf C=\mathbf I$ and zero finite strain.

**6. Cauchy traction and its decomposition**, current unit normal $\mathbf n$:

$$
\mathbf t=\boldsymbol\sigma\mathbf n,\qquad
\sigma_n=\mathbf n\cdot\mathbf t,\qquad
\mathbf t_s=\mathbf t-\sigma_n\mathbf n.
$$

The scalar $\sigma_n$ is tensile positive. Shear-traction magnitude is $\|\mathbf t_s\|$.

**7. Area and stress transformations**, reference normal $\mathbf N$:

$$
\mathbf n\,da=J\mathbf F^{-T}\mathbf N\,dA,\qquad
\mathbf P=J\boldsymbol\sigma\mathbf F^{-T},\qquad
\mathbf S=\mathbf F^{-1}\mathbf P.
$$

$\mathbf P$ is first Piola–Kirchhoff stress and generally is not symmetric. $\mathbf S$ is second Piola–Kirchhoff stress; it is symmetric when Cauchy stress is symmetric. All have Pa units but act on different geometric measures.

**8. Spatial balances of mass and linear momentum**:

$$
\frac{D\rho}{Dt}+\rho\nabla_x\cdot\mathbf v=0,\qquad
\frac{\partial\sigma_{ij}}{\partial x_j}+\rho b_i=\rho a_i.
$$

$\mathbf b$ is body force per mass in N/kg, and $\mathbf a=D\mathbf v/Dt$. In static equilibrium acceleration is zero; body force per volume is $\rho\mathbf b$ in N/m³.

**9. Velocity gradient and deformation rate**, with the dot following a material particle:

$$
\mathbf L=\nabla_x\mathbf v=\dot{\mathbf F}\mathbf F^{-1},\qquad
\mathbf D=\tfrac12(\mathbf L+\mathbf L^T),\qquad
\dot J=J\operatorname{tr}\mathbf D.
$$

These rates have s⁻¹ units. The skew part of $\mathbf L$ describes local spin.

**10. Stress power identity**:

$$
\mathbf P:\dot{\mathbf F}=\mathbf S:\dot{\mathbf E}_G
=J\boldsymbol\sigma:\mathbf D.
$$

The left expressions are power per reference volume; $\boldsymbol\sigma:\mathbf D$ is power per current volume. Symmetric Cauchy stress and the stated conventional continuum are assumed.

**11. Small-strain isotropic elasticity**, with no thermal or initial strain:

$$
\boldsymbol\sigma=2G\boldsymbol\epsilon+\lambda_L\operatorname{tr}(\boldsymbol\epsilon)\mathbf I.
$$

$G$ is shear modulus; $\lambda_L$ is the first Lamé parameter, not a principal stretch.

**12. Modulus relations and stability range**:

$$
G=\frac E{2(1+\nu)},\qquad
K=\frac E{3(1-2\nu)},\qquad
\lambda_L=\frac{E\nu}{(1+\nu)(1-2\nu)}.
$$

Positive strain energy requires $E>0$ and $-1<\nu<1/2$ for this compressible isotropic model. Exact incompressibility needs a constraint and pressure variable; do not insert $\nu=1/2$ into the denominators.

**13. Inverse elastic relation**:

$$
\boldsymbol\epsilon=\frac{1+\nu}{E}\boldsymbol\sigma
-\frac\nu E\operatorname{tr}(\boldsymbol\sigma)\mathbf I.
$$

This is a three-dimensional relation. Plane stress sets selected stresses to zero; plane strain sets selected strains to zero and generally leaves a nonzero out-of-plane stress.

**14. Hydrostatic and deviatoric stress measures**:

$$
I_1=\operatorname{tr}\boldsymbol\sigma,\quad
\mathbf s=\boldsymbol\sigma-\frac{I_1}{3}\mathbf I,\quad
J_2=\tfrac12\mathbf s:\mathbf s,\quad
\sigma_{vm}=\sqrt{3J_2},\quad p=-I_1/3.
$$

$p$ is compression-positive pressure. Principal stresses are eigenvalues of symmetric $\boldsymbol\sigma$. Invariants do not change under a rigid coordinate rotation; von Mises stress is not a universal failure criterion.

**15. Linear elastic strain-energy density**, relative to the unstressed state:

$$
W=\tfrac12\boldsymbol\sigma:\boldsymbol\epsilon
=G\boldsymbol\epsilon:\boldsymbol\epsilon
+\tfrac12\lambda_L(\operatorname{tr}\boldsymbol\epsilon)^2.
$$

$W$ is J/m³. Reference/current volume differences are neglected consistently in this small-strain expression.

### Derivation

Take two neighboring particles separated initially by $d\mathbf X$. Their current separation is $d\mathbf x=\mathbf Fd\mathbf X$. Subtracting squared lengths gives $d\mathbf x\cdot d\mathbf x-d\mathbf X\cdot d\mathbf X=d\mathbf X^T(\mathbf F^T\mathbf F-\mathbf I)d\mathbf X$. Defining half the bracket as $\mathbf E_G$ measures this length change. Substituting $\mathbf F=\mathbf I+\mathbf H$ yields the exact decomposition in formula 4. For a rotation, $\mathbf F^T\mathbf F=\mathbf I$; the quadratic term cancels the misleading linearized strain when rotation is not small.

For momentum, integrate traction over the boundary of a material volume and add its body force. Replace traction by $\boldsymbol\sigma\mathbf n$ and apply the divergence theorem. Equality to the volume integral of $\rho\mathbf a$ holds for every sufficiently smooth subvolume, giving the local momentum equation. This derivation explains why spatial stress gradients have force-per-volume units and why a constant stress field can be in equilibrium with zero body force despite nonzero boundary tractions.

### Worked examples

#### Example 1: finite stretch followed by rotation

An initially rectangular block measures 0.100 × 0.040 × 0.020 m and has density 7800 kg/m³. Apply stretches $(1.10,0.95,1.00)$ along its reference axes, then a $30^\circ$ rigid rotation about axis 3. With $\mathbf F=\mathbf R\operatorname{diag}(1.10,0.95,1.00)$,

$$
\mathbf F=\begin{bmatrix}0.95262794&-0.475&0\\0.55&0.82272413&0\\0&0&1\end{bmatrix}.
$$

The determinant is **1.045**, so volume rises from 0.0000800 to **0.00008360 m³**. Current density is **7464.1148 kg/m³** and mass remains **0.624000 kg**. Direct multiplication gives $\mathbf C=\operatorname{diag}(1.21,0.9025,1)$ and $\mathbf E_G=\operatorname{diag}(\mathbf{0.105000},\mathbf{-0.048750},0)$, exactly the same as before rotation. Reference-axis line lengths become 0.110, 0.038, and 0.020 m.

In contrast, the linearized tensor from this rotated mapping has $\epsilon_{11}=-0.0473721$, $\epsilon_{22}=-0.1772759$, and $\epsilon_{12}=0.037500$. These are not reliable small-strain approximations for this motion: rotation is large and the omitted quadratic term matters. No stress is inferred from this finite kinematic example without an appropriate constitutive law.

#### Example 2: traction, invariants, and elastic strain

At a point, let Cauchy stress in MPa be

$$
\boldsymbol\sigma=\begin{bmatrix}120&30&0\\30&40&0\\0&0&20\end{bmatrix},\qquad
\mathbf n=(0.6,0.8,0)^T.
$$

Traction is **$(96,50,0)$ MPa**. Normal stress is **97.600 MPa** and the shear-traction vector is $(37.44,-28.08,0)$ MPa, of magnitude **46.800 MPa**. The principal stresses are **130, 30, and 20 MPa**, with $I_1=180$ MPa and von Mises stress **105.35654 MPa**.

For stipulated small-strain isotropic elasticity with $E=210$ GPa and $\nu=0.30$, $G=80.76923$ GPa and $K=175$ GPa. Normal strains are **0.0004857143**, **-0.00000952381**, and **-0.0001333333**. Tensor shear strain is **0.0001857143**, so engineering shear is **0.0003714286**. Volumetric strain to first order is **0.0003428571**. Energy density is **33190.476 J/m³**, counting both off-diagonal terms in the contraction. A constant field of this stress satisfies zero-body-force equilibrium if its boundary tractions are supplied; it is not automatically a solution for an arbitrarily supported component.

### Exercises

1. A body undergoes only a $90^\circ$ rotation about axis 3. Find $J$, Green–Lagrange strain, and the diagonal entries of the linearized strain computed from that rotation mapping.
2. A material with $E=200$ GPa and $\nu=0.25$ experiences uniform hydrostatic compression of 15 MPa. Find each normal strain, first-order volumetric strain, and von Mises stress.
3. In a static box $0\le x\le0.1$ m, $0\le y\le0.2$ m, $0\le z\le0.01$ m, take $\sigma_{xx}=\alpha x$, $\sigma_{xy}=\sigma_{yx}=\beta y$, with all other components zero, $\alpha=2000$ Pa/m, $\beta=1000$ Pa/m, and density 1000 kg/m³. Find the balancing body force per mass and the net body force.

### Solutions

1. The proper rotation has **$J=1$** and **$\mathbf E_G=\mathbf0$** because it preserves every length. Its linearized strain has diagonal **$(-1,-1,0)$**. Those false finite compression values demonstrate the failure of a small-rotation approximation, not physical deformation.
2. $K=133.3333$ GPa. Each normal strain is $-p/(3K)=\mathbf{-0.000037500}$. The sum is **-0.000112500**. Deviatoric stress is zero, so **$\sigma_{vm}=0$ MPa** despite the nonzero compressive pressure.
3. Divergence is $(\alpha+\beta,0,0)=(3000,0,0)$ N/m³. Thus **$\mathbf b=(-3,0,0)$ N/kg**. Volume is 0.000200 m³, so net body force is **$(-0.600000,0,0)$ N**. Integrating the given surface tractions returns the opposite resultant; this checks equilibrium, not every constitutive or compatibility requirement.

### Common mistakes

Using displacement magnitude alone to justify small strain misses large gradients and rotations. Mixing reference and current normals changes the meaning of traction. First Piola stress need not be symmetric even though Cauchy stress is. Omitting the factor of two between tensor and engineering shear corrupts elastic strain and energy. Confusing body force per mass with force per volume creates a density error. Finally, a hydrostatic state can have zero von Mises stress while still causing compression, volumetric strain, or pressure-sensitive material failure.

### Applications and limits

Continuum mechanics supplies the common framework behind structural, fluid, thermal-stress, and multiphysics models. Before choosing a solver, identify configuration, strain scale, material symmetry, compressibility, loading history, and boundary conditions. Check mass, force, moment, and energy consistency in addition to solver residuals. The models here omit material damage, plastic evolution, couple stresses, discontinuity conditions, and a complete finite-strain constitutive theory. Their purpose is to make those later choices explicit and testable, not to assign universal design allowables.

### Further reading

Primary access checked 7 November 2026. These links provide freely accessible author or university teaching material; no source text or illustrations are reproduced.

- [Allan F. Bower, Applied Mechanics of Solids: deformation measures](https://solidmechanics.org/Text/Chapter2_2/Chapter2_2.php) — author-hosted full web treatment of mappings, deformation gradients, strain, and rotation.
- [Allan F. Bower, Applied Mechanics of Solids: internal forces](https://solidmechanics.org/Text/Chapter2_3/Chapter2_3.php) — traction, Cauchy stress, and alternative stress measures.
- [MIT / Klaus-Jürgen Bathe: Lagrangian Continuum Mechanics Variables](https://ocw.mit.edu/courses/res-2-002-finite-element-procedures-for-solids-and-structures-spring-2010/resources/lecture-3-1/) — lecture resource on finite deformation, density, polar decomposition, and work-conjugate variables.
- [MIT 16.21: structural-analysis lecture notes](https://ocw.mit.edu/courses/16-21-techniques-for-structural-analysis-and-design-spring-2005/pages/lecture-notes/) — public notes on stress, momentum balance, deformation, elasticity, and boundary-value problems.


---

## 43. Multiphase flow

### Learning map

Prerequisites: [fluid mechanics](../chapters/10-fluid-mechanics.md), [pipe flow](../chapters/11-pipe-flow-and-pumps.md), [thermodynamics](../chapters/08-thermodynamics.md) and [mass transfer](../chapters/17-mass-transfer.md). Learn to distinguish phase mass flow from phase occupancy, construct homogeneous and slip descriptions, conserve each phase, and assess a simple particle-settling model. The emphasis is on quantities that can be defined and checked before choosing a specialized pressure-drop or heat-transfer correlation.

The [visual guide](../VISUAL_GUIDE.md#gas-mass-quality-and-void-fraction) compares gas mass-flow quality with void fraction for three prescribed slip ratios. Use it to see why a small gas mass fraction can occupy a large part of a passage.

### Theory

A multiphase flow contains distinct material phases with interfaces: gas bubbles in water, liquid droplets in gas, solid particles in liquid, or combinations of these. Two chemical species do not necessarily form two phases; a fully mixed air stream is a gas phase containing several species. Conversely, liquid water and water vapor form two phases of one substance. Phase identity determines which conservation laws and equilibrium relations are appropriate.

**Flow quality** is a phase mass-flow fraction. **Void fraction** is the fraction of local volume, or a representative cross-sectional area, occupied by the gas phase. Their difference is particularly large when gas density is much lower than liquid density. A small gas mass flow can occupy a substantial fraction of the passage. In an air-water flow, the symbol $x$ below means gas mass-flow fraction; it does not imply boiling or saturation equilibrium.

Static quality describes the gas mass fraction contained in a representative local volume. It differs from flow quality when the phases move at different mean speeds. A fast gas phase can carry a specified mass flow through a smaller occupied area. Consequently, measuring mass flow alone does not determine gas holdup unless relative motion is known. The slip ratio supplies one possible additional relation, but its numerical value requires a model or measurement.

Superficial velocity divides each phase's volume flow by the entire passage area, as if that phase occupied the whole passage. It is useful for plotting operating conditions and describing flow maps. Actual phase velocity divides by the area occupied by that phase. Confusing the two can distort Reynolds numbers, interfacial forces and residence-time estimates. The sum of superficial velocities is a volumetric flux, not generally the velocity of either phase.

The homogeneous model assumes equal phase velocities and allows the mixture to be treated as one moving continuum for selected balances. Equal velocity does not automatically establish equal temperature or thermodynamic equilibrium. A homogeneous equilibrium model adds those assumptions where applicable. A slip model admits different velocities. A two-fluid model goes further by solving separate momentum and energy balances and requires interfacial drag, heat-transfer and mass-transfer closures. Adding equations without reliable closures does not guarantee better prediction.

Flow regime describes the spatial organization of phases. Gas-liquid examples include dispersed bubbles, elongated plugs, intermittent slugs, churn, annular liquid films and entrained droplets. Horizontal passages can develop stratification under gravity. Regime depends on geometry, inclination, phase properties and flow rates, rather than quality alone. An empirical map should be used within its tested conditions; a boundary on one map is not a universal physical constant.

Pressure change combines friction, gravity, acceleration and local disturbances. Gas expansion, evaporation or changing holdup can increase momentum flux even when the pipe area is constant. A pressure drop therefore need not be entirely frictional. In an upward line, gravity usually requires a pressure decrease along the flow; in a downward line it can produce pressure recovery. Intermittent slugs additionally create time-dependent loads that an average steady calculation does not capture.

### Formula handbook

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

### Derivation

Divide the two phase mass-flow expressions to obtain $x/(1-x)=\rho_g\alpha u_g/[\rho_l(1-\alpha)u_l]$. Substitute $S=u_g/u_l$ and solve for $\alpha$ to obtain formula 6. Setting $S=1$ converts mass-flow fractions into local mass fractions. A unit mass then occupies volume $x/\rho_g+(1-x)/\rho_l$, proving the homogeneous reciprocal-density formula. This route also explains why inserting flow quality into an arithmetic density average is incorrect.

For settling, the downward weight minus buoyancy is $(\rho_p-\rho_f)g\pi d^3/6$. At terminal speed it balances upward Stokes drag $3\pi\mu_fdv_t$. Cancelling common factors gives formula 14. The derivation assumes terminal force balance; the Reynolds check tests whether the drag law used to obtain that speed is self-consistent. A failed check means select a suitable drag relation and solve again, rather than retain the original answer.

### Worked examples

#### Example 1: a homogeneous air-water mixture

A teaching model has total mass flow 1.000 kg/s, gas flow quality $x=0.001000$, area 0.0100 m², gas density 1.20 kg/m³ and liquid density 1000 kg/m³. Assume equal phase velocities and use these as local properties. Gas and liquid mass flows are **0.001000 kg/s** and **0.999000 kg/s**. Their superficial velocities are **0.0833333 m/s** and **0.0999000 m/s**. Thus common actual velocity is **0.183233 m/s**, gas void fraction is **0.454794**, and mixture density is **545.752 kg/m³**. Reconstructing total flow gives $\rho_hjA=1.000$ kg/s. Only 0.1% of the transported mass is gas, while about 45.48% of the modeled cross section is gas. This is a kinematic illustration, not evidence that a real mixture at these rates will remain homogeneous or avoid slugging.

#### Example 2: slow settling of a small solid sphere

An isolated rigid sphere of diameter **20.0 micrometers** and density 2650 kg/m³ settles in still liquid of density 1000 kg/m³ and viscosity 0.00100 Pa s. Use $g=9.81$ m/s² and neglect walls and neighboring particles. Stokes settling gives **0.000359700 m/s**, or 0.359700 mm/s. Substitution into the particle Reynolds number gives **0.00719400**, well below unity and also below a conservative 0.1 screening value. Buoyant weight and drag both equal **$6.78019\times10^{-11}$ N**. Travel through 1.00 m at terminal speed takes **2780.09 s**, or **46.3349 min**. The travel estimate neglects the initial acceleration interval. A real suspension with flocs or many interacting particles need not settle at this isolated-sphere speed.

### Exercises

1. A homogeneous air-water flow has gas void fraction 0.100000, gas density 1.20 kg/m³ and liquid density 1000 kg/m³. Find gas flow quality and mixture density. Explain whether 10% gas occupancy means 10% gas mass.
2. Keep the phase mass flows, densities and total area of Example 1, but prescribe co-current slip ratio $S=2.000$. Find void fraction, actual phase velocities and static quality. Compare with the original homogeneous case.
3. Double the sphere diameter in Example 2 while retaining all other assumptions. Calculate the candidate terminal speed, Reynolds number and 1.00 m travel time. Check whether the Stokes approximation remains plausible.

### Solutions

1. Mixture density is $0.1(1.2)+0.9(1000)=\mathbf{900.120\ kg/m^3}$. Homogeneous quality is $0.1(1.2)/900.12=\mathbf{0.000133316}$, or **0.0133316%**. The low gas density explains the much smaller mass fraction.
2. Formula 6 gives **$\alpha=0.294325$**. The same superficial velocities divided by their occupied fractions give **$u_g=0.283133$ m/s** and **$u_l=0.141567$ m/s**, so their ratio is two. Static quality is **0.000500250**, while flow quality remains 0.001000. Faster gas occupies less area and less local mass inventory for the same transported gas mass rate.
3. Stokes speed scales with $d^2$, so it becomes **0.00143880 m/s**. Reynolds number scales with $d^3$ under this prediction, giving **0.0575520**. This remains small enough for a creeping-flow estimate, though less strongly asymptotic than before. Terminal travel time becomes **695.024 s**. Continuing the scaling to much larger diameters would eventually invalidate its own Reynolds assumption.

### Common mistakes

Do not equate mass quality with void fraction, or flow quality with static quality when slip exists. Use local gas density at the relevant absolute pressure and temperature. Distinguish superficial from actual velocity and total-mixture mass flux from liquid-phase mass flux. A mixture density alone does not establish a pressure-drop correlation. Check the particle Reynolds number after predicting settling; “small particle” is not a sufficient quantitative test. Rigid-sphere Stokes drag does not automatically describe a clean mobile-interface bubble.

### Applications and limits

These models help interpret aeration, gas entrainment, evaporators, condensers, slurries and sedimentation. Start by declaring phase properties, measurement bases, geometry, orientation and whether phase change occurs. Then select a closure justified for the regime and examine sensitivity to uncertain holdup or slip. Boiling dryout, compressible two-phase choking, severe slug loads, dense granular flow and non-Newtonian suspensions require additional treatment. Neither worked example establishes separator capacity, pump suitability or a pressure-system design rating.

### Further reading

- [MIT OCW: Notes on Two-Phase Flow, Boiling Heat Transfer, and Boiling Crises](https://ocw.mit.edu/courses/22-06-engineering-of-nuclear-systems-fall-2010/2e8614e58cc569d96acff67df51d9aef_MIT22_06F10_lec13.pdf) — definitions of quality, slip and void fraction, followed by homogeneous balances and flow-regime discussion.
- [TU Delft OCW: Sedimentation](https://ocw.tudelft.nl/wp-content/uploads/Sedimentation.pdf) — university lecture material on discrete settling, drag, applicability checks and the additional issues in sedimentation systems.
- [MIT OCW: Flow Past a Sphere and Settling](https://ocw.mit.edu/courses/12-090-introduction-to-fluid-motions-sediment-transport-and-current-generated-sedimentary-structures-fall-2006/7841d9b1681d6748fa2f5cbc6d6f1cb2_ch3.pdf) — deeper treatment of sphere drag and the restricted Stokes settling regime.


---

## 44. Process Plant Engineering

### Learning map

Prerequisites: thermodynamics, fluid mechanics, heat transfer, instrumentation, and elementary differential equations. This chapter connects a process requirement to balances, drawings, equipment interfaces, controls, and an operating record. Follow a water-blending system from its stream table into a tank model and utility requirement. The aim is to understand what the plant must do and how its documents express that intent. Pressure design, relief sizing, hazardous-area classification, and construction-code compliance require separate work beyond these introductory models.

### Theory

A process basis states the required service and its conditions. Define capacity, product quality, feed composition and variability, utility availability, operating schedule, and the boundary between the project and existing facilities. Separate normal operation from startup, shutdown, cleaning, standby, and credible disturbances. A nominal flow alone cannot establish tank volume, pumping duty, heater capacity, or control behavior. Identify what is measured, specified, assumed, and still unknown before selecting equipment.

Process documents describe different aspects of the same system. A process flow diagram, or PFD, communicates major equipment and material and energy streams, normally supported by stream data. A piping and instrumentation diagram, or P&ID, describes functional equipment, piping, valves, instrumentation, and their connections using the project's conventions. A physical layout establishes space, elevation, access, routing, and interfaces. A P&ID is not a scale drawing, and a convincing 3D arrangement does not prove that its process or control logic works. [Northwestern's PFD teaching page](https://processdesign.mccormick.northwestern.edu/index.php/Process_flow_diagram) explains process-stream information; the [archived DOE drawing handbook](https://www.energy.gov/ehss/articles/doe-hdbk-10162-93) provides historical training in drawings and symbols rather than a current mandatory project standard.

Balances need a declared control volume and basis. Total mass is conserved for ordinary nonnuclear processes. Individual species may be generated or consumed by reaction, whereas an inert tracer is conserved if it neither reacts, adsorbs, evaporates, nor separates. Steady operation means the chosen inventories no longer change with time; it does not mean there is no material flowing. Recycles can create large internal flows while leaving the overall plant balance unchanged. Count only streams crossing the selected boundary.

Energy balances use a consistent enthalpy reference and include relevant heat and work. Temperature averaging is valid only for the stated property and mixing assumptions. Phase changes, chemical reactions, heat of mixing, heat loss, or appreciably different heat capacities can defeat a simple arithmetic average. For two streams of the same dilute liquid with constant equal heat capacity, the adiabatic outlet temperature is mass-flow weighted. The [University of Michigan energy-balance material](https://public.websites.umich.edu/~elements/7e/11chap/summary.html) develops the broader open-system balance.

Tank residence and mixing describe different behavior. Nominal hydraulic residence time is working liquid volume divided by throughput. Mixing time describes how rapidly spatial concentration differences are reduced. The ideal stirred-tank model assumes the outlet concentration equals the uniform tank concentration immediately; it does not calculate impeller performance. Real short circuits, dead regions, density stratification, or poor inlet placement can invalidate that assumption. [MIT's residence-time lecture](https://ocw.mit.edu/courses/10-37-chemical-and-biological-reaction-engineering-spring-2007/resources/lec10_03092007_w/) discusses nonideal mixing and tracer interpretation.

Piping and utilities are coupled to equipment. Flow through a branch depends on pressure boundaries, elevation, resistance, valve position, and the connected machine characteristic. A cooling-water flow requirement also needs inlet temperature, return conditions, available differential pressure, and water quality. Instrument air needs more than a pressure number: consumption, cleanliness, availability, and loss-of-air behavior affect actuators. State electrical loads and operating combinations before treating installed motor ratings as coincident plant demand.

Control design assigns each measured variable, manipulated variable, operating target, and limit. Level control may adjust an outlet while inlet ratio control maintains composition. Temperature control may adjust a utility valve, but saturation, transport delay, and sensor placement constrain the response. A transmitter tag does not specify its calibration range or an interlock's full logic. Record sequences and cause-and-effect behavior separately, including startup permissives, abnormal signals, manual modes, and restoration after interruption.

Maintainability belongs in the design basis. Operators need access to instruments and valves, removal paths for equipment, and means to drain, vent, clean, inspect, and isolate the relevant sections under approved procedures. A replaceable pump is not maintainable if its motor cannot be removed through the surrounding pipework. Equipment, line, instrument, and document identifiers should remain consistent across calculations, P&IDs, layout, specifications, and revision records. Changes to one interface can require changes to several documents.

### Formula handbook

Use inventory $M$ in kg, mass flow $\dot m$ in kg/s, volumetric flow $Q_v$ in $\mathrm{m^3/s}$, volume $V$ in $\mathrm{m^3}$, concentration $C$ in $\mathrm{kg/m^3}$, and time $t$ in s. Heat rate $\dot Q_h$ and shaft work rate $\dot W_s$ are in W; $\dot Q_h>0$ enters the system and $\dot W_s>0$ leaves as shaft work.

**1. Total mass inventory:**

$$
\frac{dM}{dt}=\sum_{in}\dot m_i-\sum_{out}\dot m_j.
$$

**2. Species inventory with mass fraction $w_k$:**

$$
\frac{d(Mw_k)}{dt}=\sum_{in}\dot m_iw_{k,i}-\sum_{out}\dot m_jw_{k,j}+\dot m_{k,gen}.
$$

$\dot m_{k,gen}$ is net generation in kg/s; it is zero for the conservative tracer used below.

**3. Steady open-system energy balance:**

$$
0=\dot Q_h-\dot W_s+\sum_{in}\dot m_i\left(h_i+\frac{u_i^2}{2}+gz_i\right)-\sum_{out}\dot m_j\left(h_j+\frac{u_j^2}{2}+gz_j\right).
$$

Specific enthalpy $h$ is J/kg, velocity $u$ m/s, and elevation $z$ m. Enthalpies must use one consistent reference and include required phase or reaction effects.

**4. Steady, nonreactive, adiabatic mixing with one outlet and constant equal $c_p$:**

$$
\dot m_o=\sum_i\dot m_i,\qquad T_o=\frac{\sum_i\dot m_iT_i}{\dot m_o}.
$$

Neglect kinetic, potential, and shaft-work effects and heat of mixing. A common Celsius reference is valid here because the common offset cancels through mass conservation.

**5. Conservative mass-fraction blending:**

$$
w_o=\frac{\sum_i\dot m_iw_i}{\dot m_o}.
$$

Do not substitute volume fractions without a density and mixing-volume model.

**6. Constant-density tank level, vertical constant area $A_T$:**

$$
A_T\frac{d\ell}{dt}=\sum Q_{v,in}-\sum Q_{v,out}.
$$

Level $\ell$ is m; variable-area vessels require $dV/d\ell$ instead of constant $A_T$.

**7. Nominal hydraulic residence time:**

$$
\tau=V/Q_v.
$$

Use working liquid volume and actual throughput. This is not a universal minimum contact time or impeller mixing time.

**8. Ideal constant-volume, constant-flow stirred tank with conservative solute:**

$$
V\frac{dC}{dt}=Q_v(C_{in}-C),\qquad C_{out}=C.
$$

**9. Constant inlet after a step, initial concentration $C_0$:**

$$
C(t)=C_{in}+(C_0-C_{in})e^{-t/\tau}.
$$

**10. Time to complete fraction $f$ of the initial-to-final change:**

$$
t_f=-\tau\ln(1-f),\qquad0<f<1.
$$

**11. Ideal stirred-tank residence-time probability density:**

$$
E(t)=\frac1\tau e^{-t/\tau},\qquad \int_0^\infty E(t)dt=1,\qquad \int_0^\infty tE(t)dt=\tau.
$$

$E(t)$ has units $\mathrm{s^{-1}}$. Individual fluid elements have different residence times.

**12. Pipe section and steady junction continuity:**

$$
u=\frac{4Q_v}{\pi D^2},\qquad \sum Q_{v,in}=\sum Q_{v,out}.
$$

The volumetric junction form assumes equal constant density. Head losses and pump characteristics must also be satisfied; continuity alone cannot determine every branch flow.

**13. Single-phase utility duty with constant heat capacity:**

$$
|\dot Q_h|=\dot m_u c_{p,u}|T_{u,out}-T_{u,in}|.
$$

$c_{p,u}$ is J/(kg K). Available temperature approach and exchanger conductance impose additional constraints.

**14. Ideal linear 4–20 mA scaling:**

$$
I_{\rm mA}=4+16\frac{x-x_L}{x_U-x_L}.
$$

$x_L,x_U$ are configured engineering-unit range limits. This mapping describes valid measurement span; out-of-range and fault behavior depend on the device and configuration.

### Derivation

Take a tank filled to constant working volume with a liquid whose density is effectively constant. Equal inlet and outlet volume flow preserves that volume. For a conservative solute, accumulation is $d(VC)/dt$, entering mass rate is $Q_vC_{in}$, and leaving rate is $Q_vC$ because ideal mixing makes outlet and bulk concentrations equal. Constant $V$ gives the differential equation above.

For constant inlet concentration, set $y=C-C_{in}$. The balance becomes $dy/dt=-y/\tau$. Integrating with $y(0)=C_0-C_{in}$ gives the exponential response. The initial value and long-time limit are recovered directly. With a clean initial tank and a step to $C_{in}$, cumulative solute discharged by time $t$ is

$$
m_{out}(t)=Q_vC_{in}\left[t-\tau(1-e^{-t/\tau})\right].
$$

Meanwhile inventory is $VC_{in}(1-e^{-t/\tau})$. Adding them gives $Q_vC_{in}t$, exactly the cumulative input. This integral balance checks the dynamic solution independently of a plotted curve. It also explains why one residence time does not replace all original liquid: the ideal step response has reached only $1-e^{-1}$ of its final change.

### Worked examples

#### Example 1: water blending and downstream heating

Mix two dilute aqueous streams steadily. Stream 1 supplies 1.50 kg/s at 20°C with conservative tracer mass fraction 0.00100; stream 2 supplies 0.500 kg/s at 80°C with tracer fraction 0.00400. Assume identical constant $c_p=4180\ \mathrm{J/(kg\,K)}$, negligible heat of mixing, adiabatic blending, no phase change, and negligible work, speed, and elevation effects.

Total outlet flow is **2.00 kg/s**. The outlet temperature is $[1.5(20)+0.5(80)]/2=\mathbf{35.0^\circ C}$. Tracer flow is $1.5(0.001)+0.5(0.004)=0.00350$ kg/s; dividing by total flow gives **0.001750 kg/kg**, or **1750 mg/kg**. A consistent 0°C sensible-enthalpy reference gives inlet energy rates 125.4 and 167.2 kW, totaling **292.6 kW**, equal to $2(4180)(35)$ W at the outlet.

A separate downstream heater raising this blend to 60°C needs $2(4180)(60-35)=\mathbf{209.0\ kW}$ delivered to the liquid. This is thermal duty, not electrical or fuel input without the heater efficiency and losses. Changing the boundary to include the heater adds that energy stream to the balance.

#### Example 2: a tracer step through a stirred tank

An ideal tank contains 1.20 m³ of initially tracer-free water. Constant inlet and outlet flows are 0.00200 m³/s. At $t=0$, inlet tracer concentration steps to 0.100 kg/m³, equivalent to 100 mg/L. Assume conservative solute, instant uniform mixing, constant volume, and no measurement delay.

Residence time is $\tau=1.20/0.00200=\mathbf{600\ s}$. After 600 s, outlet concentration is $0.100(1-e^{-1})=0.0632121\ \mathrm{kg/m^3}$, or **63.2121 mg/L**. Reaching 95% of the final change takes $-600\ln(0.05)=\mathbf{1797.44\ s}$, or **29.9573 min**.

By 600 s, input tracer mass is **0.120000 kg**. Tank inventory is $1.20(0.0632120559)=\mathbf{0.0758545\ kg}$, and integrated discharge is **0.0441455 kg**. Their sum closes the mass balance. These results characterize this ideal flow model; they do not prove real tank mixing, disinfection contact time, or sensor response.

### Exercises

1. Adiabatically blend 0.800 kg/s of water at 15°C with 1.20 kg/s at 65°C. With equal constant $c_p=4180\ \mathrm{J/(kg\,K)}$, find blend temperature and additional heat needed to reach 55°C.
2. A 2.00 m³ ideal stirred tank initially has tracer concentration 0.200 kg/m³. Clean water enters at 0.00500 m³/s with equal outflow. Find the time for concentration to fall to 10% of its initial value and tracer mass then remaining.
3. Cooling water removes 84.0 kW while warming by 8.00 K. Use $c_p=4200\ \mathrm{J/(kg\,K)}$ and density 1000 kg/m³. Find mass flow, volume flow, speed in a 50.0 mm internal-diameter pipe, and ideal transmitter output for a linear range of 0–5.00 L/s mapped to 4–20 mA.

### Solutions

1. Temperature is $[0.8(15)+1.2(65)]/2=\mathbf{45.0^\circ C}$. Heating duty is $2(4180)(55-45)=\mathbf{83.60\ kW}$. A simple average of inlet temperatures would be wrong because their mass flows differ.
2. Here $\tau=400$ s and $C/C_0=e^{-t/400}$. Thus $t=400\ln10=\mathbf{921.034\ s}$, or **15.3506 min**. Remaining concentration is 0.0200 kg/m³ and inventory is **0.0400 kg**. The discharged tracer accounts for the other 0.360 kg of initial inventory.
3. Mass flow is $84000/(4200\times8)=\mathbf{2.50\ kg/s}$ and volume flow **0.00250 m³/s**, or 2.50 L/s. Pipe speed is $4(0.00250)/(\pi0.05^2)=\mathbf{1.27324\ m/s}$. Half-span flow gives **12.0 mA**. Utility pressure, exchanger temperature approach, and instrumentation accuracy remain separate checks.

### Common mistakes

Confusing working volume with total tank capacity, residence time with mixing time, or mass fraction with mg/L changes the model. Do not equate a pressure transmitter range with allowable equipment pressure. A control valve's nominal diameter does not establish its installed flow characteristic. Flow arrows on a P&ID describe intended function; actual reverse-flow possibilities require analysis. Keep assumed steady balances separate from transient filling, draining, and startup behavior.

### Applications and limits

For a small water-treatment skid, prepare a process basis, stream table, balances, PFD, P&ID, equipment and line lists, utility schedule, instrument ranges, control narrative, layout, and verification record. Cross-check tag numbers and revisions before release. Compare measured flow, temperature, inventory, and response with predictions and measurement uncertainty. Record deviations and resolve their causes. The [integrated pumping capstone](../CAPSTONE.md) extends the interface discussion. These models neither select construction materials and pressure ratings nor replace qualified review, commissioning, or a documented operational procedure.

### Further reading

- [Northwestern process-design teaching — Process flow diagram](https://processdesign.mccormick.northwestern.edu/index.php/Process_flow_diagram): stream and equipment information on PFDs.
- [U.S. DOE — Engineering Symbology, Prints, and Drawings](https://www.energy.gov/ehss/articles/doe-hdbk-10162-93): archived training handbook and drawing interpretation; not a current mandatory design code.
- [University of Michigan — Steady-state energy balance](https://public.websites.umich.edu/~elements/7e/11chap/summary.html): open-system energy-balance development, including reactive extensions beyond this chapter.
- [MIT OpenCourseWare — Nonideal reactor mixing patterns](https://ocw.mit.edu/courses/10-37-chemical-and-biological-reaction-engineering-spring-2007/resources/lec10_03092007_w/): residence-time distributions and alternatives to ideal mixing. Primary-source links checked 2026-11-07.
