# 06. Strength of materials

## Learning map

Prerequisites: statics, calculus, and material stress–strain behavior. Progress from axial members to torsion, bending, combined stress, deflection, and buckling. The central reasoning chain is external loads → internal resultants → stress and strain → displacement or failure criterion. A design can satisfy a stress limit while failing a stiffness, stability, fatigue, or connection requirement.

## Theory

Stress is the internal force intensity acting across an imagined cut. Normal stress acts perpendicular to that cut; shear stress acts within it. Stress is a tensor because both the cut orientation and force direction matter. Engineering strain measures deformation relative to an original length. For small deformations in a linearly elastic isotropic solid, stress and strain are related by Young's modulus, shear modulus, and Poisson's ratio.

Simple bar, shaft, and beam formulas are reduced models of three-dimensional continuum behavior. Their simplicity comes from assumptions about cross-section geometry, deformation, loading, and material properties. Away from localized load application, stress often becomes less sensitive to the exact load distribution, which motivates Saint-Venant-type reasoning. It does not eliminate stress concentration near holes, weld toes, threads, or abrupt changes in section.

Euler–Bernoulli beam theory assumes cross-sections remain plane and normal to the bent centerline. It is appropriate for slender beams with small rotations and negligible shear deflection. Short thick beams may need Timoshenko theory. Circular-shaft torsion formulas rely on circular geometry; noncircular sections warp and cannot generally use the same polar-moment relation.

Yielding and fracture are different failure mechanisms. Von Mises stress is commonly used to screen yielding of ductile isotropic metals, while brittle fracture often needs tensile stress and crack-based criteria. Buckling is a loss of stability and can occur below material yield stress. Slenderness, end restraint, geometric imperfections, and load eccentricity strongly affect its onset.

## Formula handbook

Use N, m, Pa, and radians consistently. $E,G$ are elastic moduli in Pa; $A$ is area in m²; $I,J$ have units m⁴.

**1. Average axial stress and engineering strain**:

$$
\sigma=\frac{N}{A},\qquad\epsilon=\frac{\Delta L}{L}.
$$

**2. Linear elastic relations**, for isotropic material:

$$
\sigma=E\epsilon,\qquad\tau=G\gamma,\qquad G=\frac{E}{2(1+\nu)}.
$$

**3. Axial deformation**, for a slender bar under centered load:

$$
\delta=\int_0^L\frac{N(x)}{E(x)A(x)}\,dx.
$$

**4. Circular-shaft torsion**:

$$
\tau(r)=\frac{Tr}{J},\qquad\theta=\frac{TL}{GJ},\qquad J_{\mathrm{solid}}=\frac{\pi d^4}{32}.
$$

**5. Elastic flexure**, with $y$ measured from the neutral axis:

$$
\sigma_x=-\frac{My}{I},\qquad I_{\mathrm{rectangle}}=\frac{bh^3}{12}.
$$

**6. Beam transverse shear**, where $Q$ is the first area moment above or below the evaluation level and $b$ is local width:

$$
\tau=\frac{VQ}{Ib}.
$$

**7. Load–shear–moment relations**, with downward $w$ positive and a matching beam sign convention:

$$
\frac{dV}{dx}=-w,\qquad\frac{dM}{dx}=V.
$$

**8. Small-deflection beam curvature**, with signed $M$ and deflection chosen consistently:

$$
EI\frac{d^2v}{dx^2}=M(x).
$$

**9. Cantilever with end force**, uniform $EI$:

$$
|\delta_{\mathrm{tip}}|=\frac{FL^3}{3EI},\qquad |\sigma_{\max}|=\frac{FLc}{I}.
$$

**10. Plane-stress principal values**:

$$
\sigma_{1,2}=\frac{\sigma_x+\sigma_y}{2}\pm\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}.
$$

**11. Plane-stress von Mises equivalent stress**:

$$
\sigma_{vm}=\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}.
$$

**12. Ideal Euler buckling**, for a straight slender elastic column:

$$
P_{cr}=\frac{\pi^2EI_{\min}}{(KL)^2}.
$$

The effective-length factor $K$ encodes idealized end restraint; it is not an arbitrary safety factor.

**13. Thin closed cylindrical pressure vessel**, far from ends and discontinuities:

$$
\sigma_h=\frac{pr}{t},\qquad\sigma_l=\frac{pr}{2t}.
$$

Here $p$ is pressure difference and $t\ll r$; these educational membrane equations are not a pressure-vessel design code.

## Derivation

For pure bending, plane sections rotate relative to one another. A fiber at signed distance $y$ from the neutral axis has axial strain $\epsilon_x=-y/\rho_c$, where $\rho_c$ is curvature radius. Linear elasticity gives $\sigma_x=-Ey/\rho_c$. The resultant moment magnitude is $M=\int_A E y^2/\rho_c\,dA=EI/\rho_c$. Eliminating curvature gives the flexure equation. This derivation shows why a hole changes bending stress through $I$ and why increasing section depth is particularly effective: rectangular $I$ increases as $h^3$.

## Worked examples

### Example 1: Cantilever bracket

A rectangular steel cantilever has length 0.50 m, width 0.040 m, vertical depth 0.060 m, and $E=200$ GPa. A 1000 N downward force acts at the free end. The second moment is $I=0.04(0.06)^3/12=7.20\times10^{-7}$ m⁴. Root moment is 500 N m, giving extreme-fiber stress $500(0.03)/I=20.833$ MPa. Tip deflection is $1000(0.5)^3/[3(200\times10^9)I]=0.28935$ mm downward. The root connection and local stress concentration require separate assessment.

### Example 2: Solid shaft

A 40 mm diameter shaft, 1 m long, transmits 400 N m with $G=80$ GPa. $J=\pi(0.04)^4/32=2.51327\times10^{-7}$ m⁴. Outer-surface shear stress is $400(0.02)/J=31.831$ MPa. Twist is $400/[80\times10^9J]=0.019894$ rad, or $1.140^\circ$. For this pure shear state, von Mises stress is $\sqrt3\tau=55.133$ MPa. Keyways and torque fluctuations are excluded.

## Exercises

1. A 2 m bar of area 500 mm² and modulus 200 GPa carries 50 kN tension. Find average stress and extension.
2. A plane-stress point has $\sigma_x=100$ MPa, $\sigma_y=0$, and $\tau_{xy}=30$ MPa. Find von Mises stress.
3. What happens to ideal Euler buckling load when an otherwise identical column length doubles?

## Solutions

1. $A=5\times10^{-4}$ m², so stress is 100 MPa. Extension is $NL/(EA)=0.001$ m, or 1 mm.
2. $\sigma_{vm}=\sqrt{100^2+3(30)^2}=112.694$ MPa. Directly adding normal and shear stress would be incorrect.
3. Buckling load scales with $1/L^2$, so it becomes one-quarter, with the same $E,I,K$ and elastic validity.

## Common mistakes

- Using area moment $I$ in kg m² instead of m⁴; mass moment and area moment are different quantities.
- Entering mm⁴ directly into an otherwise metre-based calculation.
- Taking average stress as the peak stress near a discontinuity.
- Confusing section modulus $I/c$ with second moment $I$.
- Checking yield alone when stiffness, fatigue, instability, or brittle fracture governs.

## Applications and limits

Use these models for first calculations of brackets, frames, shafts, rods, and idealized vessel membranes. Record load direction, support conditions, material state, and temperature. Compare with finite-element results by checking reactions and energy as well as peak stress; mesh-dependent stress at an ideal sharp corner is not a converged material failure prediction. Real design allowables and required margins depend on the governing application and material data.

## Further reading

- [MIT OCW: Mechanics and Materials I](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/) — solid mechanics foundations and assignments.
- [MIT OCW: Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) — linked open textbook and modules. These references are linked, not copied.
