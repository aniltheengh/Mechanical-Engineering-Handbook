# 42 · Continuum mechanics: deformation, stress, and balance

## Learning map

Prerequisites are vectors, matrices, differentiation, statics, and [strength of materials](06-strength-of-materials.md). This chapter connects material motion to strain, internal force to stress, and local equations to conservation. Learn to identify the reference and current configurations, distinguish finite deformation from its small-gradient approximation, and use a constitutive law within its assumptions. Continue to [finite element analysis](24-finite-element-analysis.md), [fluid mechanics](10-fluid-mechanics.md), or [composite materials](37-composite-materials.md) after understanding these shared foundations.

## Theory

A continuum replaces discrete atoms or particles by smoothly varying fields such as displacement, density, temperature, and stress. The averaging scale should be large enough to smooth relevant microstructure but small enough to resolve the engineering variation of interest. A crack surface, a material interface, or a shock may interrupt smoothness; separate regions and appropriate jump or interface conditions are then needed. Continuum theory does not mean every field is smooth everywhere.

The reference coordinate $\mathbf X$ labels a material particle. Its current position is $\mathbf x=\boldsymbol\chi(\mathbf X,t)$. Following the same label gives a material, or Lagrangian, description. Describing fields at fixed spatial locations gives an Eulerian description. These are different descriptions of the same motion, not competing physical laws. A reference configuration need not be stress free, so initial stress and material history may require separate specification.

The deformation gradient describes local stretching, shearing, and rotation of neighboring material lines. Its determinant measures local volume change. Strain measures isolate changes of lengths and angles from rigid motion. A body can undergo large displacement without much strain: a nearly rigid part can translate or rotate substantially. Conversely, a small absolute displacement across a very short length can create a large strain. The basic infinitesimal-strain approximation requires small displacement gradients, including small rotations relative to its reference.

Stress represents force transmitted across an imagined cut. Cauchy stress acts on area measured in the current configuration. The force on a cut depends on its normal, so one scalar stress cannot describe a general three-dimensional state. In an ordinary continuum without body couples or independent couple stresses, angular-momentum balance makes Cauchy stress symmetric. A traction vector usually has both normal and tangential components, even when the chosen coordinate directions are principal directions.

Balance laws constrain every admissible material response but do not identify the material. Constitutive equations supply the missing relationships, such as elastic stress versus strain, viscous stress versus deformation rate, or plastic evolution with history. Linear isotropic elasticity is useful for small elastic strains in a material with approximately direction-independent response. It does not automatically describe rubber at large stretch, yielding steel, or a fiber composite. Changing a strain measure inside Hooke's law without changing the corresponding stress and energy formulation is not a valid general finite-deformation model.

A boundary-value problem combines kinematics, balance, constitutive behavior, initial conditions when needed, and boundary conditions. Prescribe displacement components or their conjugate traction components appropriately; prescribing both arbitrarily at the same location usually overconstrains the problem. Support conditions must remove unwanted rigid modes. A computed field also needs compatibility: independently chosen strain components may fail to arise from any continuous displacement field. Finite-element convergence alone cannot repair an inconsistent physical model.

## Formula handbook

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

## Derivation

Take two neighboring particles separated initially by $d\mathbf X$. Their current separation is $d\mathbf x=\mathbf Fd\mathbf X$. Subtracting squared lengths gives $d\mathbf x\cdot d\mathbf x-d\mathbf X\cdot d\mathbf X=d\mathbf X^T(\mathbf F^T\mathbf F-\mathbf I)d\mathbf X$. Defining half the bracket as $\mathbf E_G$ measures this length change. Substituting $\mathbf F=\mathbf I+\mathbf H$ yields the exact decomposition in formula 4. For a rotation, $\mathbf F^T\mathbf F=\mathbf I$; the quadratic term cancels the misleading linearized strain when rotation is not small.

For momentum, integrate traction over the boundary of a material volume and add its body force. Replace traction by $\boldsymbol\sigma\mathbf n$ and apply the divergence theorem. Equality to the volume integral of $\rho\mathbf a$ holds for every sufficiently smooth subvolume, giving the local momentum equation. This derivation explains why spatial stress gradients have force-per-volume units and why a constant stress field can be in equilibrium with zero body force despite nonzero boundary tractions.

## Worked examples

### Example 1: finite stretch followed by rotation

An initially rectangular block measures 0.100 × 0.040 × 0.020 m and has density 7800 kg/m³. Apply stretches $(1.10,0.95,1.00)$ along its reference axes, then a $30^\circ$ rigid rotation about axis 3. With $\mathbf F=\mathbf R\operatorname{diag}(1.10,0.95,1.00)$,

$$
\mathbf F=\begin{bmatrix}0.95262794&-0.475&0\\0.55&0.82272413&0\\0&0&1\end{bmatrix}.
$$

The determinant is **1.045**, so volume rises from 0.0000800 to **0.00008360 m³**. Current density is **7464.1148 kg/m³** and mass remains **0.624000 kg**. Direct multiplication gives $\mathbf C=\operatorname{diag}(1.21,0.9025,1)$ and $\mathbf E_G=\operatorname{diag}(\mathbf{0.105000},\mathbf{-0.048750},0)$, exactly the same as before rotation. Reference-axis line lengths become 0.110, 0.038, and 0.020 m.

In contrast, the linearized tensor from this rotated mapping has $\epsilon_{11}=-0.0473721$, $\epsilon_{22}=-0.1772759$, and $\epsilon_{12}=0.037500$. These are not reliable small-strain approximations for this motion: rotation is large and the omitted quadratic term matters. No stress is inferred from this finite kinematic example without an appropriate constitutive law.

### Example 2: traction, invariants, and elastic strain

At a point, let Cauchy stress in MPa be

$$
\boldsymbol\sigma=\begin{bmatrix}120&30&0\\30&40&0\\0&0&20\end{bmatrix},\qquad
\mathbf n=(0.6,0.8,0)^T.
$$

Traction is **$(96,50,0)$ MPa**. Normal stress is **97.600 MPa** and the shear-traction vector is $(37.44,-28.08,0)$ MPa, of magnitude **46.800 MPa**. The principal stresses are **130, 30, and 20 MPa**, with $I_1=180$ MPa and von Mises stress **105.35654 MPa**.

For stipulated small-strain isotropic elasticity with $E=210$ GPa and $\nu=0.30$, $G=80.76923$ GPa and $K=175$ GPa. Normal strains are **0.0004857143**, **-0.00000952381**, and **-0.0001333333**. Tensor shear strain is **0.0001857143**, so engineering shear is **0.0003714286**. Volumetric strain to first order is **0.0003428571**. Energy density is **33190.476 J/m³**, counting both off-diagonal terms in the contraction. A constant field of this stress satisfies zero-body-force equilibrium if its boundary tractions are supplied; it is not automatically a solution for an arbitrarily supported component.

## Exercises

1. A body undergoes only a $90^\circ$ rotation about axis 3. Find $J$, Green–Lagrange strain, and the diagonal entries of the linearized strain computed from that rotation mapping.
2. A material with $E=200$ GPa and $\nu=0.25$ experiences uniform hydrostatic compression of 15 MPa. Find each normal strain, first-order volumetric strain, and von Mises stress.
3. In a static box $0\le x\le0.1$ m, $0\le y\le0.2$ m, $0\le z\le0.01$ m, take $\sigma_{xx}=\alpha x$, $\sigma_{xy}=\sigma_{yx}=\beta y$, with all other components zero, $\alpha=2000$ Pa/m, $\beta=1000$ Pa/m, and density 1000 kg/m³. Find the balancing body force per mass and the net body force.

## Solutions

1. The proper rotation has **$J=1$** and **$\mathbf E_G=\mathbf0$** because it preserves every length. Its linearized strain has diagonal **$(-1,-1,0)$**. Those false finite compression values demonstrate the failure of a small-rotation approximation, not physical deformation.
2. $K=133.3333$ GPa. Each normal strain is $-p/(3K)=\mathbf{-0.000037500}$. The sum is **-0.000112500**. Deviatoric stress is zero, so **$\sigma_{vm}=0$ MPa** despite the nonzero compressive pressure.
3. Divergence is $(\alpha+\beta,0,0)=(3000,0,0)$ N/m³. Thus **$\mathbf b=(-3,0,0)$ N/kg**. Volume is 0.000200 m³, so net body force is **$(-0.600000,0,0)$ N**. Integrating the given surface tractions returns the opposite resultant; this checks equilibrium, not every constitutive or compatibility requirement.

## Common mistakes

Using displacement magnitude alone to justify small strain misses large gradients and rotations. Mixing reference and current normals changes the meaning of traction. First Piola stress need not be symmetric even though Cauchy stress is. Omitting the factor of two between tensor and engineering shear corrupts elastic strain and energy. Confusing body force per mass with force per volume creates a density error. Finally, a hydrostatic state can have zero von Mises stress while still causing compression, volumetric strain, or pressure-sensitive material failure.

## Applications and limits

Continuum mechanics supplies the common framework behind structural, fluid, thermal-stress, and multiphysics models. Before choosing a solver, identify configuration, strain scale, material symmetry, compressibility, loading history, and boundary conditions. Check mass, force, moment, and energy consistency in addition to solver residuals. The models here omit material damage, plastic evolution, couple stresses, discontinuity conditions, and a complete finite-strain constitutive theory. Their purpose is to make those later choices explicit and testable, not to assign universal design allowables.

## Further reading

Primary access checked 7 November 2026. These links provide freely accessible author or university teaching material; no source text or illustrations are reproduced.

- [Allan F. Bower, Applied Mechanics of Solids: deformation measures](https://solidmechanics.org/Text/Chapter2_2/Chapter2_2.php) — author-hosted full web treatment of mappings, deformation gradients, strain, and rotation.
- [Allan F. Bower, Applied Mechanics of Solids: internal forces](https://solidmechanics.org/Text/Chapter2_3/Chapter2_3.php) — traction, Cauchy stress, and alternative stress measures.
- [MIT / Klaus-Jürgen Bathe: Lagrangian Continuum Mechanics Variables](https://ocw.mit.edu/courses/res-2-002-finite-element-procedures-for-solids-and-structures-spring-2010/resources/lecture-3-1/) — lecture resource on finite deformation, density, polar decomposition, and work-conjugate variables.
- [MIT 16.21: structural-analysis lecture notes](https://ocw.mit.edu/courses/16-21-techniques-for-structural-analysis-and-design-spring-2005/pages/lecture-notes/) — public notes on stress, momentum balance, deformation, elasticity, and boundary-value problems.
