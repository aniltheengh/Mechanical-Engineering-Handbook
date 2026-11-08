# Mechanical Engineering Formula Handbook

Generated from the 44 chapter formula sections. Read the linked chapter for derivations, examples, and additional assumptions. Symbols are local to each chapter; SI is the default. This reference does not supply code-compliant design rules or proprietary property tables.

## 01 · Units, dimensions, and engineering estimates

[Full chapter](../chapters/01-units-and-dimensional-analysis.md)

1. Weight: $W=mg$, with $W$ in N, $m$ in kg, and local $g$ in m/s².
2. Density: $\rho=m/V$ in kg/m³; specific weight $\gamma=\rho g$ in N/m³.
3. Pressure: $p=F_\perp/A$ in Pa for uniform normal force over area $A$ in m².
4. Absolute pressure: $p_{\mathrm{abs}}=p_{\mathrm{gauge}}+p_{\mathrm{ambient}}$. A vacuum gauge may use a different sign convention.
5. Absolute temperature: $T/\mathrm{K}=t/{}^\circ\mathrm{C}+273.15$. Temperature differences have the same numerical size in K and °C.
6. Rotational speed: $\omega=2\pi n/60$, where $n$ is the numerical speed in revolutions per minute and $\omega$ is in rad/s.
7. Shaft power: $P=\tau\omega$, where torque $\tau$ is in N m and $P$ in W.
8. Hydraulic power: $P_h=\rho gQH$, where $Q$ is volumetric flow in m³/s and $H$ is head in m. Input power is $P_{\mathrm{in}}=P_h/\eta$ for total efficiency $\eta$.
9. Relative deviation: $e_r=(x-x_{\mathrm{ref}})/x_{\mathrm{ref}}$ for nonzero reference; percent deviation is $100e_r$.
10. For a differentiable measurement model $y=f(x_1,\ldots,x_n)$, first-order uncertainty propagation is

$$
u_y^2\approx\sum_i\left(\frac{\partial f}{\partial x_i}\right)^2u_i^2+2\sum_{i<j}\frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j}\operatorname{cov}(x_i,x_j).
$$

The derivatives are evaluated at the reported estimates. Large uncertainties or strongly nonlinear models require more careful propagation.

11. For independent inputs in $y=C\prod_i x_i^{a_i}$, the small-uncertainty approximation is $(u_y/y)^2\approx\sum_i(a_i u_i/x_i)^2$.
12. Buckingham's dimensional theorem gives $n-r$ independent dimensionless groups when $n$ dimensional variables have a dimension matrix of rank $r$. A dimensionless group does not itself establish a causal law.

Useful exact conversions: $1\ \mathrm{L}=10^{-3}\ \mathrm{m^3}$, $1\ \mathrm{bar}=10^5\ \mathrm{Pa}$, $1\ \mathrm{MPa}=1\ \mathrm{N/mm^2}$, and $1\ \mathrm{kWh}=3.6\ \mathrm{MJ}$. Metric prefixes multiply the entire unit: $(1\ \mathrm{mm})^2=10^{-6}\ \mathrm{m^2}$.

## 02 · Engineering mathematics

[Full chapter](../chapters/02-engineering-mathematics.md)

1. Chain rule: $d[f(g(x))]/dx=f'(g(x))g'(x)$.
2. Integration by parts: $\int u\,dv=uv-\int v\,du$; preserve boundary terms in a definite integral.
3. Taylor expansion near $a$: $f(a+h)=f(a)+hf'(a)+h^2f''(a)/2+O(h^3)$ for sufficiently smooth $f$.
4. Dot product: $\mathbf{a}\cdot\mathbf{b}=\sum_i a_ib_i=\|\mathbf a\|\|\mathbf b\|\cos\theta$ in an orthonormal basis.
5. Moment: $\mathbf{M}_O=\mathbf{r}\times\mathbf{F}$ in N m, with $\mathbf r$ measured from point $O$ to the force line.
6. Gradient: $\nabla T=(\partial_xT,\partial_yT,\partial_zT)$ in K/m for a temperature field.
7. Divergence theorem: $\int_V\nabla\cdot\mathbf q\,dV=\oint_{\partial V}\mathbf q\cdot\mathbf n\,dA$ for a sufficiently regular field and boundary, using outward normal $\mathbf n$.
8. Eigenproblem: $A\mathbf v=\lambda\mathbf v$. For undamped structural vibration, $K\boldsymbol\phi=\omega^2M\boldsymbol\phi$.
9. First-order constant-coefficient response, $\tau\dot y+y=Ku_0$, is $y(t)=Ku_0+[y(0)-Ku_0]e^{-t/\tau}$ for constant input and $\tau>0$.
10. Laplace derivative rule: $\mathcal L\{\dot y\}=sY(s)-y(0^-)$. Initial conditions must not be silently discarded.
11. Fourier representation with period $T$: $f(t)=a_0/2+\sum_{n=1}^{\infty}[a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)]$, where $\omega_0=2\pi/T$ and coefficient integrals are over one period.
12. Sample statistics: $\bar x=\sum_i x_i/n$ and $s^2=\sum_i(x_i-\bar x)^2/(n-1)$ for $n>1$.
13. For independent observations with common variance, the standard error of the mean is estimated as $s/\sqrt n$. Serial correlation invalidates this simple expression.
14. Least squares minimizes $\|A\mathbf x-\mathbf b\|_2^2$. A stationary point satisfies $A^TA\mathbf x=A^T\mathbf b$, but QR or SVD is usually preferable for numerical solution because normal equations square the condition number.

The symbols $s$ and $T$ have different meanings in transforms, statistics, and physics. Read local definitions. Trigonometric derivatives use angles in radians. Exponential and logarithm arguments must be dimensionless.

## 03 · Numerical methods and engineering computation

[Full chapter](../chapters/03-numerical-methods.md)

1. Bisection midpoint: $c=(a+b)/2$. A sign-changing bracket of initial length $L_0$ has length $L_0/2^n$ after $n$ updates; its midpoint error is at most half the retained interval length.
2. Newton iteration: $x_{k+1}=x_k-f(x_k)/f'(x_k)$, requiring a usable derivative and a suitable starting point.
3. Secant iteration: $x_{k+1}=x_k-f(x_k)(x_k-x_{k-1})/[f(x_k)-f(x_{k-1})]$ when the denominator is nonzero.
4. Linear interpolation: $y(x)=y_0+(y_1-y_0)(x-x_0)/(x_1-x_0)$ for distinct endpoints. Extrapolation requires an additional modelling justification.
5. Central derivative: $f'(x)\approx[f(x+h)-f(x-h)]/(2h)$, with truncation error $O(h^2)$ for smooth data.
6. Composite trapezoidal rule for equal spacing $h=(b-a)/n$:

$$
\int_a^b f(x)\,dx\approx h\left[\frac{f_0+f_n}{2}+\sum_{i=1}^{n-1}f_i\right].
$$

7. Composite Simpson rule for an even number $n$ of equal subintervals:

$$
\int_a^b f(x)\,dx\approx\frac h3\left[f_0+f_n+4\sum_{i\ \mathrm{odd}}f_i+2\sum_{\substack{i\ \mathrm{even}\\0<i<n}}f_i\right].
$$

8. Explicit Euler: $y_{n+1}=y_n+h f(t_n,y_n)$ for $\dot y=f(t,y)$. Its global error is generally $O(h)$ under regularity and stability conditions.
9. Backward Euler: $y_{n+1}=y_n+h f(t_{n+1},y_{n+1})$, an implicit equation.
10. Classical RK4 uses $k_1=f(t,y)$, $k_2=f(t+h/2,y+hk_1/2)$, $k_3=f(t+h/2,y+hk_2/2)$, $k_4=f(t+h,y+hk_3)$, then $y_{n+1}=y+h(k_1+2k_2+2k_3+k_4)/6$.
11. Linear-system residual: $\mathbf r=\mathbf b-A\mathbf x$. A useful relative backward-error indicator is $\|\mathbf r\|/(\|A\|\|\mathbf x\|+\|\mathbf b\|)$.
12. Richardson extrapolation: $q_*\approx q_{h/2}+(q_{h/2}-q_h)/(2^p-1)$ when a common asymptotic error model $q_h=q_*+Ch^p+\cdots$ is justified.
13. Observed order for three successively halved steps: $p_{\mathrm{obs}}=\log_2| (q_h-q_{h/2})/(q_{h/2}-q_{h/4}) |$, provided the differences are meaningful and not dominated by cancellation.

Here $h$ is a step in the independent variable, with corresponding units. It is not necessarily a length. Tolerances for force residual, displacement update, and energy imbalance have different physical meanings and should be specified separately.

## 04. Engineering statics

[Full chapter](../chapters/04-statics.md)

All positions are in m, forces in N, and moments in N m. Positive planar moments are counterclockwise unless a drawing states otherwise.

**1. Cartesian components**, for a force at angle $\theta$ from positive $x$:

$$
F_x=F\cos\theta,\qquad F_y=F\sin\theta.
$$

**2. Moment about point O**, with $\mathbf r$ measured from O to the force application point:

$$
\mathbf M_O=\mathbf r\times\mathbf F,\qquad M_{O,z}=xF_y-yF_x.
$$

**3. Rigid-body equilibrium**, valid in an inertial reference frame:

$$
\sum\mathbf F=\mathbf0,\qquad\sum\mathbf M_O=\mathbf0.
$$

**4. Equivalent distributed load**, for signed intensity $w(x)$ in N/m and nonzero resultant:

$$
W=\int_a^b w(x)\,dx,\qquad \bar x=\frac{\int_a^b xw(x)\,dx}{W}.
$$

**5. Uniform and triangular loads**, over length $L$, with triangle increasing from zero at $x=0$:

$$
W_{\mathrm{uniform}}=wL,\quad\bar x=L/2;\qquad W_{\mathrm{triangle}}=w_{\max}L/2,\quad\bar x=2L/3.
$$

**6. Composite-area centroid**, with holes assigned negative area:

$$
\bar x=\frac{\sum A_i x_i}{\sum A_i},\qquad\bar y=\frac{\sum A_i y_i}{\sum A_i}.
$$

**7. Dry static friction**, for compressive contact normal $N\ge0$:

$$
|F_f|\le\mu_sN,\qquad \tan\phi=\mu_s.
$$

**8. Impending belt slip**, with flexible belt, Coulomb friction, and contact angle $\beta$ in radians:

$$
\frac{T_{\mathrm{tight}}}{T_{\mathrm{slack}}}=e^{\mu\beta}.
$$

**9. Hydrostatic force on a plane surface**, for constant density $\rho$, gauge pressure zero at the free surface, and centroid depth $h_c$:

$$
F_R=\rho g h_c A.
$$

**10. Three-dimensional equilibrium in components**:

$$
\sum F_x=\sum F_y=\sum F_z=0,\qquad\sum M_x=\sum M_y=\sum M_z=0.
$$

## 05. Engineering dynamics

[Full chapter](../chapters/05-dynamics.md)

Use $x,r$ in m, time $t$ in s, mass $m$ in kg, force $F$ in N, angular velocity $\omega$ in rad/s, and mass moment of inertia $I$ in kg m².

**1. Rectilinear kinematics**:

$$
v=\frac{dx}{dt},\qquad a=\frac{dv}{dt}=v\frac{dv}{dx}.
$$

**2. Constant acceleration only**:

$$
v=v_0+at,\qquad x=x_0+v_0t+\tfrac12at^2,\qquad v^2=v_0^2+2a(x-x_0).
$$

**3. Tangential and normal acceleration**, with path radius of curvature $\rho_c$:

$$
\mathbf a=\dot v\,\mathbf e_t+\frac{v^2}{\rho_c}\mathbf e_n.
$$

**4. Polar-coordinate acceleration**:

$$
\mathbf a=(\ddot r-r\dot\theta^2)\mathbf e_r+(r\ddot\theta+2\dot r\dot\theta)\mathbf e_\theta.
$$

**5. Constant-mass Newton equation**:

$$
\sum\mathbf F=m\mathbf a_G.
$$

**6. Planar rigid-body angular equation about its center of mass**:

$$
\sum M_G=I_G\alpha.
$$

**7. Parallel-axis theorem**, for parallel axes separated by $d$:

$$
I_O=I_G+md^2.
$$

**8. Planar rigid-body kinetic energy**:

$$
T=\tfrac12mv_G^2+\tfrac12I_G\omega^2.
$$

**9. Planar rigid-body work–energy and power**, with resultant external force $\mathbf F_R$, center-of-mass position $\mathbf r_G$, and total external moment $M_G$ about the center of mass:

$$
T_2-T_1=\int_1^2\mathbf F_R\cdot d\mathbf r_G+\int_1^2 M_G\,d\theta,\qquad P=\mathbf F_R\cdot\mathbf v_G+M_G\omega.
$$

Here $M_G$ includes the moments of all external forces and applied couples about G. This is one equivalent representation of their total work. Alternatively, sum each applied force's work at its own application point and the work of applied couples; do not add that individual-force sum to the resultant-force/moment expression.

**10. Linear impulse–momentum**:

$$
m\mathbf v_2-m\mathbf v_1=\int_{t_1}^{t_2}\sum\mathbf F\,dt.
$$

**11. Relative rigid-body motion**, for points A and B:

$$
\mathbf v_B=\mathbf v_A+\boldsymbol\omega\times\mathbf r_{B/A},\qquad
\mathbf a_B=\mathbf a_A+\boldsymbol\alpha\times\mathbf r_{B/A}+\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r_{B/A}).
$$

**12. Lagrange equation**, for independent generalized coordinates $q_i$ and nonconservative generalized force $Q_i$:

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}=Q_i,\qquad L=T-V.
$$

## 06. Strength of materials

[Full chapter](../chapters/06-strength-of-materials.md)

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

## 07. Materials science and selection

[Full chapter](../chapters/07-materials-science.md)

**1. Engineering stress and strain**, with original area $A_0$ and length $L_0$:

$$
\sigma_e=F/A_0,\qquad\epsilon_e=(L-L_0)/L_0.
$$

**2. True measures**, with instantaneous area $A$ and uniform uniaxial deformation:

$$
\sigma_t=F/A,\qquad\epsilon_t=\ln(L/L_0).
$$

Before necking, approximately constant plastic volume gives $\sigma_t\approx\sigma_e(1+\epsilon_e)$.

**3. Elastic energy density**, for uniaxial linear elasticity:

$$
u_e=\tfrac12\sigma\epsilon=\frac{\sigma^2}{2E}.
$$

$u_e$ is J/m³, and stress and modulus are Pa.

**4. Free thermal expansion**, for approximately constant coefficient $\alpha_T$ in K⁻¹:

$$
\Delta L=\alpha_T L_0\Delta T.
$$

**5. Completely restrained uniaxial thermal stress**, assuming elastic behavior and no relaxation:

$$
\sigma_T=-E\alpha_T\Delta T.
$$

Heating produces compression in this sign convention.

**6. Binary two-phase lever rule**, with composition coordinate $C_\alpha<C_0<C_\beta$:

$$
f_\alpha=\frac{C_\beta-C_0}{C_\beta-C_\alpha},\qquad f_\beta=1-f_\alpha.
$$

The fractions use the same mass or mole basis as the composition coordinate.

**7. One-dimensional Fick laws**, constant diffusivity $D$ in m²/s:

$$
J=-D\frac{\partial C}{\partial x},\qquad \frac{\partial C}{\partial t}=D\frac{\partial^2C}{\partial x^2}.
$$

If $C$ is mol/m³, flux $J$ is mol/(m² s).

**8. Arrhenius diffusivity**, with molar activation energy $Q_d$:

$$
D=D_0\exp\left(-\frac{Q_d}{RT}\right).
$$

Use absolute $T$ in K and matching J/mol units for $Q_d$ and $R$.

**9. Hall–Petch empirical relation**, within its calibrated grain-size regime:

$$
\sigma_y=\sigma_0+k_y d_g^{-1/2}.
$$

Grain size $d_g$ is m; $k_y$ then has units Pa m$^{1/2}$.

**10. Mode-I stress intensity**, for a geometry with crack length parameter $a$:

$$
K_I=Y\sigma\sqrt{\pi a},\qquad a_c=\frac1\pi\left(\frac{K_{IC}}{Y\sigma}\right)^2.
$$

$K_I,K_{IC}$ are Pa m$^{1/2}$. The geometry factor $Y$ and plane-strain toughness assumptions must match the specimen and loading.

**11. Empirical steady creep law**:

$$
\dot\epsilon_c=A_c\sigma^n\exp\left(-\frac{Q_c}{RT}\right).
$$

$A_c$ has unit-dependent dimensions and must be calibrated for the stated material and stress units.

**12. Axial aligned continuous-fiber composite**, under ideal iso-strain loading:

$$
E_L=V_fE_f+(1-V_f)E_m.
$$

This rule does not predict transverse strength, interface failure, or a laminate's complete constitutive behavior.

## 18. Machine elements and mechanical design

[Full chapter](../chapters/18-machine-design.md)

**1. Rotary power**, with torque $T$ in N m and speed $n$ in rpm:

$$
P=T\omega,\qquad\omega=\frac{2\pi n}{60}.
$$

**2. External gear-pair ratio**, using magnitudes and tooth counts $z$:

$$
i=\frac{z_2}{z_1}=\frac{n_1}{n_2},\qquad T_2=\eta i T_1.
$$

Two external gears reverse rotational direction; $\eta$ is mesh efficiency.

**3. Spur-gear dimensions and loads**, module $m_g$ in m and pressure angle $\phi$:

$$
d=m_gz,\qquad F_t=\frac{2T}{d},\qquad F_r=F_t\tan\phi.
$$

**4. Solid shaft stresses**, nominal bending moment $M$ and torque $T$:

$$
\sigma_b=\frac{32M}{\pi d^3},\qquad\tau_t=\frac{16T}{\pi d^3}.
$$

Apply appropriate stress-concentration and fatigue effects separately.

**5. Basic rolling-bearing rating life**, with dynamic rating $C$ and equivalent dynamic load $P_b$ in the same force units:

$$
L_{10}=\left(\frac{C}{P_b}\right)^p,\qquad L_{10h}=\frac{10^6}{60n}L_{10}.
$$

$L_{10}$ is in millions of revolutions, corresponding to 90% population survival under the model; $p=3$ for ball bearings and $10/3$ for rollers. SKF provides the model and its applicability qualifications in its [rolling-bearing catalog](https://www.skf.com/binaries/pub12/Images/0901d196802809de-Rolling-bearings---17000_1-EN_tcm_12-121486.pdf).

**6. Joint load-sharing factor**, bolt stiffness $k_b$ and member stiffness $k_m$:

$$
C_j=\frac{k_b}{k_b+k_m},\qquad F_b=F_i+C_jF_e,\qquad F_c=F_i-(1-C_j)F_e.
$$

$F_i$ is preload, $F_e$ external separating force, and $F_c$ remaining clamp force; valid while contact persists and stiffnesses remain linear.

**7. Approximate tightening torque**:

$$
T_{\mathrm{tighten}}\approx K_T F_i d.
$$

$K_T$ is an empirical nut factor sensitive to thread and bearing friction.

**8. Close-coiled round-wire compression-spring rate**:

$$
k_s=\frac{Gd_w^4}{8D^3N_a},\qquad\delta=F/k_s.
$$

$D$ is mean coil diameter, $d_w$ wire diameter, and $N_a$ active turns. Use m and Pa for $k_s$ in N/m.

**9. Spring stress correction**, spring index $C_s=D/d_w$:

$$
K_w=\frac{4C_s-1}{4C_s-4}+\frac{0.615}{C_s},\qquad\tau_{\max}=K_w\frac{8FD}{\pi d_w^3}.
$$

This conventional expression assumes ordinary close-coiled spring geometry, not arbitrary curved wire.

**10. Mean and alternating stress**:

$$
\sigma_m=\frac{\sigma_{\max}+\sigma_{\min}}2,\qquad\sigma_a=\frac{\sigma_{\max}-\sigma_{\min}}2.
$$

**11. Modified Goodman screening**, tensile mean stress and corrected endurance strength $S_e$:

$$
\frac{\sigma_a}{S_e}+\frac{\sigma_m}{S_{ut}}\le\frac1{n_f}.
$$

$S_{ut}$ is ultimate strength and $n_f$ a chosen fatigue design factor. This linear approximation is not universal, particularly for compressive mean stresses or materials without an endurance limit.

**12. Linear cumulative damage estimate**:

$$
D_f=\sum_i\frac{n_i}{N_i}.
$$

Miner's estimate uses cycles experienced $n_i$ and corresponding constant-amplitude lives $N_i$; order effects and interactions are excluded.

## 19. Kinematics of machines and mechanisms

[Full chapter](../chapters/19-mechanisms.md)

Use lengths in m, angles in radians for differentiation, and angular rates in rad/s.

**1. Planar mobility count**, including the ground link:

$$
M=3(n-1)-2j_1-j_2.
$$

$n$ is links, $j_1$ one-DOF lower pairs, and $j_2$ higher pairs imposing one constraint. This generic count assumes independent constraints.

**2. Four-bar vector closure**:

$$
r_2e^{i\theta_2}+r_3e^{i\theta_3}-r_4e^{i\theta_4}-r_1=0.
$$

Ground is along the real axis; solve real and imaginary parts for the unknown angles.

**3. Four-bar velocity closure**:

$$
ir_2\omega_2e^{i\theta_2}+ir_3\omega_3e^{i\theta_3}-ir_4\omega_4e^{i\theta_4}=0.
$$

**4. Grashof length condition**, with shortest $s$, longest $l$, and other lengths $p,q$:

$$
s+l\le p+q.
$$

For a realizable planar four-bar, this classifies full-rotation potential; the grounded link and assembly branch determine the specific inversion. Equality is a special change-point case.

**5. Inline slider-crank position**, positive slider coordinate measured from the crank center toward the slider:

$$
x=r\cos\theta+\sqrt{l^2-r^2\sin^2\theta}.
$$

Here $l>r$ and the positive square-root branch is selected.

**6. Slider velocity**, for crank speed $\omega=\dot\theta$:

$$
\dot x=\left[-r\sin\theta-\frac{r^2\sin\theta\cos\theta}{\sqrt{l^2-r^2\sin^2\theta}}\right]\omega.
$$

**7. Long-rod slider approximation**, $r/l\ll1$:

$$
x\approx l+r\cos\theta-\frac{r^2}{4l}(1-\cos2\theta).
$$

**8. Rigid-link relative velocity**:

$$
\mathbf v_B-\mathbf v_A=\boldsymbol\omega\times\mathbf r_{B/A}.
$$

**9. Ideal quasistatic virtual work**, with a consistent positive force/coordinate convention:

$$
\tau\,d\theta+F\,dx=0,\qquad\tau=-F\frac{dx}{d\theta}.
$$

Inertia, friction, and elastic storage are excluded.

**10. Cycloidal cam rise**, lift $h$, rise angle $\beta$, and $0\le\theta\le\beta$:

$$
y=h\left[\frac\theta\beta-\frac1{2\pi}\sin\left(\frac{2\pi\theta}\beta\right)\right].
$$

**11. Cycloidal follower velocity**, constant cam speed $\omega$:

$$
\dot y=\frac{h\omega}{\beta}\left[1-\cos\left(\frac{2\pi\theta}\beta\right)\right].
$$

**12. Ideal screw motion**, lead $p_l$ in m/revolution:

$$
x=\frac{p_l\theta}{2\pi},\qquad v=\frac{p_l\omega}{2\pi}.
$$

For a multistart thread, lead is pitch times number of starts.

## 20. Mechanical vibrations

[Full chapter](../chapters/20-vibrations.md)

Let mass $m$ be kg, stiffness $k$ N/m, damping $c$ N s/m, displacement $x$ m, and force $F$ N.

**1. Single-DOF equation about static equilibrium**:

$$
m\ddot x+c\dot x+kx=F(t).
$$

**2. Undamped natural frequency**:

$$
\omega_n=\sqrt{k/m},\qquad f_n=\omega_n/(2\pi).
$$

**3. Critical damping and damping ratio**:

$$
c_c=2\sqrt{km},\qquad\zeta=c/c_c.
$$

**4. Underdamped free response**, for $0\le\zeta<1$:

$$
x(t)=e^{-\zeta\omega_nt}\left[A\cos\omega_dt+B\sin\omega_dt\right],\qquad\omega_d=\omega_n\sqrt{1-\zeta^2}.
$$

Constants $A,B$ follow from the initial conditions, including the derivative of the exponential.

**5. Logarithmic decrement**, from successive same-sign displacement peaks:

$$
\delta_{\log}=\ln\frac{x_j}{x_{j+1}}=\frac{2\pi\zeta}{\sqrt{1-\zeta^2}}.
$$

**6. Harmonic-force amplitude**, $F(t)=F_0\cos\omega t$:

$$
X=\frac{F_0}{\sqrt{(k-m\omega^2)^2+(c\omega)^2}}.
$$

**7. Dynamic magnification and phase lag**:

$$
\frac{X}{F_0/k}=\frac1{\sqrt{(1-r^2)^2+(2\zeta r)^2}},\qquad\phi=\operatorname{atan2}(2\zeta r,1-r^2),\qquad r=\omega/\omega_n.
$$

**8. Displacement-response peak frequency**, for $\zeta<1/\sqrt2$ and constant force amplitude:

$$
\omega_{\mathrm{peak}}=\omega_n\sqrt{1-2\zeta^2}.
$$

**9. Force transmissibility**, force-excited mass with spring and damper connected to fixed ground:

$$
T_F=\frac{\sqrt{1+(2\zeta r)^2}}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}.
$$

The transmitted force amplitude is $T_FF_0$; $T_F<1$ when $r>\sqrt2$ in this model.

**10. Base-excited relative motion**, $z=x-y$ for base displacement $y$:

$$
m\ddot z+c\dot z+kz=-m\ddot y.
$$

**11. Rotating-imbalance force amplitude**, eccentric mass $m_e$ and offset $e$:

$$
F_0=m_e e\omega^2.
$$

**12. Undamped multi-DOF eigenproblem**:

$$
\mathbf M\ddot{\mathbf x}+\mathbf K\mathbf x=\mathbf0,\qquad(\mathbf K-\omega_j^2\mathbf M)\boldsymbol\phi_j=\mathbf0.
$$

**13. Energy decay rate for a free viscously damped oscillator**:

$$
E=\tfrac12m\dot x^2+\tfrac12kx^2,\qquad\dot E=-c\dot x^2\le0.
$$

## 34 · Tribology: friction, lubrication, and wear

[Full chapter](../chapters/34-tribology.md)

1. Coulomb static limit: $|F_t|\leq\mu_sN$, where normal force $N$ and tangential force $F_t$ are in N. Equality describes impending slip.
2. A simple sliding model is $F_t=\mu_kN$ in magnitude, with friction opposite relative motion.
3. Frictional heat generation: $P_f=F_t v$ in W for sliding speed $v$ in m/s. Heat partition between bodies requires a thermal model.
4. For a uniformly loaded circular friction surface with inner and outer radii $r_i,r_o$, the effective radius under uniform pressure is $r_m=(2/3)(r_o^3-r_i^3)/(r_o^2-r_i^2)$. Torque is $T=\mu Nr_m$ per friction interface.
5. Under the ideal uniform-wear assumption for an annular interface, $r_m=(r_o+r_i)/2$. Do not interchange this assumption with uniform pressure.
6. Newtonian shear: $\tau=\mu\,du/dy$, with dynamic viscosity $\mu$ in Pa s. In a simple parallel Couette film of thickness $h$, $\tau=\mu U/h$.
7. Couette drag power over area $A$: $P=\mu A U^2/h$, assuming constant viscosity and no pressure-driven contribution.
8. Kinematic viscosity: $\nu=\mu/\rho$ in m²/s. One centistoke is $10^{-6}\ \mathrm{m^2/s}$.
9. Specific film ratio: $\lambda=h_{\min}/\sqrt{R_{q1}^2+R_{q2}^2}$, using minimum film thickness and RMS roughnesses in consistent length units. Regime boundaries are approximate, not universal guarantees.
10. Archard's simplified wear law: $V=kWL/H$, where $V$ is removed volume in m³, load $W$ in N, sliding distance $L$ in m, hardness $H$ in Pa, and $k$ a dimensionless calibrated wear coefficient. Alternative definitions of wear coefficient have different units.
11. For uniform wear over area $A$, mean depth is $d=V/A$; actual scars are rarely perfectly uniform.
12. In a stationary-coordinate thin incompressible film, the one-dimensional Reynolds equation for constant viscosity and spatially uniform surface velocities $U_1,U_2$ is

$$
\frac{d}{dx}\left(h^3\frac{dp}{dx}\right)=6\mu(U_1+U_2)\frac{dh}{dx}+12\mu\frac{\partial h}{\partial t}.
$$

It assumes a thin film, negligible inertia, no slip, and appropriate pressure/cavitation boundary conditions. The steady form omits the squeeze term. The gap $h$ is in m, pressure $p$ in Pa, and $x$ in m.

## 08. Thermodynamics

[Full chapter](../chapters/08-thermodynamics.md)

Use heat $Q>0$ into a system and work $W>0$ done by it. Specific quantities are in J/kg, rates in W, mass in kg, pressure in Pa and absolute temperature in K.

1. Ideal-gas state equation, with gas-specific $R$ in J/(kg K):

$$
pV=mRT,\qquad pv=RT.
$$

2. Enthalpy and caloric changes for an ideal gas:

$$
h=u+pv,\qquad \Delta u=\int_{T_1}^{T_2}c_v(T)\,dT,\qquad \Delta h=\int_{T_1}^{T_2}c_p(T)\,dT.
$$

3. Ideal-gas heat-capacity relation and ratio:

$$
c_p-c_v=R,\qquad \gamma=c_p/c_v.
$$

4. Closed-system first law, including kinetic and potential energy:

$$
\Delta U+\Delta KE+\Delta PE=Q-W.
$$

5. Boundary work for a quasi-equilibrium simple compressible process:

$$
W_b=\int_{V_1}^{V_2}p\,dV.
$$

For a strongly irreversible expansion, use the appropriate external resisting pressure and a mechanically consistent boundary model, not an assumed equilibrium gas path.

6. Steady one-inlet, one-outlet energy balance, with $V_f$ denoting flow speed:

$$
\dot Q-\dot W_s=\dot m\left[h_2-h_1+\frac{V_{f,2}^2-V_{f,1}^2}{2}+g(z_2-z_1)\right].
$$

7. Closed-system entropy balance, boundary temperatures $T_b$:

$$
\Delta S=\int\frac{\delta Q}{T_b}+S_{gen},\qquad S_{gen}\geq0.
$$

8. Constant-heat-capacity ideal-gas entropy change:

$$
s_2-s_1=c_p\ln(T_2/T_1)-R\ln(p_2/p_1).
$$

9. Isentropic ideal-gas relation, constant $\gamma$:

$$
\frac{T_{2s}}{T_1}=\left(\frac{p_2}{p_1}\right)^{(\gamma-1)/\gamma}.
$$

10. Adiabatic compressor and turbine isentropic efficiencies:

$$
\eta_c=\frac{h_{2s}-h_1}{h_2-h_1},\qquad \eta_t=\frac{h_1-h_2}{h_1-h_{2s}}.
$$

11. Saturated mixture property, for $y=v,u,h,s$:

$$
y=y_f+x(y_g-y_f),\qquad 0\leq x\leq1.
$$

12. Exergy destruction for environmental temperature $T_0$:

$$
E_{D}=T_0S_{gen}.
$$

## 09. Power cycles

[Full chapter](../chapters/09-power-cycles.md)

Use specific heat and work in J/kg, enthalpy in J/kg, temperature in K and power in W. Magnitudes $q_{in},q_{out},w_t,w_c,w_p$ below are positive unless stated otherwise.

1. Cycle energy and thermal efficiency:

$$
w_{net}=q_{in}-q_{out},\qquad \eta_{th}=w_{net}/q_{in}.
$$

2. Reversible two-reservoir limit:

$$
\eta_{Carnot}=1-T_L/T_H.
$$

3. Cold-air-standard Otto efficiency, compression ratio $r=V_{max}/V_{min}$:

$$
\eta_{Otto}=1-\frac{1}{r^{\gamma-1}}.
$$

4. Cold-air-standard Diesel efficiency, cutoff ratio $r_c=V_3/V_2$:

$$
\eta_{Diesel}=1-\frac{1}{r^{\gamma-1}}\frac{r_c^\gamma-1}{\gamma(r_c-1)}.
$$

5. Ideal Brayton efficiency, pressure ratio $r_p=p_2/p_1=p_3/p_4$:

$$
\eta_{Brayton}=1-r_p^{-(\gamma-1)/\gamma}.
$$

6. Ideal Brayton state temperatures, constant $\gamma$:

$$
T_2=T_1r_p^{(\gamma-1)/\gamma},\qquad T_4=T_3r_p^{-(\gamma-1)/\gamma}.
$$

7. Compressor and turbine specific work, constant $c_p$:

$$
w_c=c_p(T_2-T_1),\qquad w_t=c_p(T_3-T_4),\qquad w_{net}=w_t-w_c.
$$

8. Brayton heat input and back-work ratio:

$$
q_{in}=c_p(T_3-T_2),\qquad BWR=w_c/w_t.
$$

9. Ideal Brayton pressure ratio for maximum specific net work with fixed $T_1,T_3$:

$$
r_{p,opt}=\left(T_3/T_1\right)^{\gamma/[2(\gamma-1)]}.
$$

10. Rankine pump approximation for incompressible liquid, pump efficiency $\eta_p$:

$$
w_p\simeq v_f(p_2-p_1)/\eta_p.
$$

11. Rankine states: 1 condenser exit, 2 pump exit, 3 turbine inlet, 4 turbine exit:

$$
q_{in}=h_3-h_2,\quad q_{out}=h_4-h_1,\quad w_t=h_3-h_4,\quad \eta_{th}=\frac{w_t-w_p}{q_{in}}.
$$

12. Net power and fuel conversion:

$$
\dot W_{net}=\dot m w_{net},\qquad \eta_{fuel}=\frac{\dot W_{net}}{\dot m_f H_f}.
$$

$H_f$ is a specified higher or lower heating value in J/kg; never mix its basis between comparisons. Plant auxiliaries must be included for plant-net power.

## 12. Heat transfer

[Full chapter](../chapters/12-heat-transfer.md)

Use heat rate $\dot Q$ in W, heat flux $q''$ in W/m2, conductivity $k$ in W/(m K), convection coefficient $h$ in W/(m2 K), and resistance in K/W.

1. Fourier's law in one direction:

$$
q_x''=-k\frac{dT}{dx}.
$$

2. Constant-conductivity plane-wall resistance:

$$
R_{wall}=\frac{L}{kA},\qquad \dot Q=\frac{T_1-T_2}{R_{wall}}.
$$

3. Cylindrical-wall resistance, length $L_z$:

$$
R_{cyl}=\frac{\ln(r_o/r_i)}{2\pi kL_z}.
$$

4. Convection relation and resistance:

$$
\dot Q=hA(T_s-T_\infty),\qquad R_{conv}=\frac1{hA}.
$$

5. Series thermal circuit without internal generation:

$$
\dot Q=\frac{T_{hot}-T_{cold}}{\sum R_i}.
$$

6. Small gray surface in large isothermal surroundings, temperatures in K:

$$
\dot Q_{rad}=\varepsilon\sigma A(T_s^4-T_{sur}^4),\qquad \sigma\simeq5.670374419\times10^{-8}\ \mathrm{W/(m^2K^4)}.
$$

7. Constant-property heat equation in a stationary solid:

$$
\rho c_p\frac{\partial T}{\partial t}=k\nabla^2T+\dot q'''.
$$

$\dot q'''$ is volumetric generation in W/m3.

8. Thermal diffusivity, Biot number and Fourier number:

$$
\alpha=\frac{k}{\rho c_p},\qquad Bi=\frac{hL_c}{k},\qquad Fo=\frac{\alpha t}{L_c^2}.
$$

For lumped analysis, $L_c=V/A_s$. Other analytical solutions can define their own characteristic length.

9. Lumped cooling under constant properties, $h$ and ambient temperature:

$$
\frac{T(t)-T_\infty}{T_i-T_\infty}=e^{-t/\tau},\qquad \tau=\frac{mc_p}{hA_s}.
$$

10. Convection dimensionless groups:

$$
Nu=\frac{hL}{k_f},\qquad Pr=\frac{\nu}{\alpha_f},\qquad Ra=\frac{g\beta|T_s-T_\infty|L^3}{\nu\alpha_f}.
$$

$k_f,\alpha_f$ are fluid properties; $\beta$ is volumetric thermal expansion coefficient in 1/K.

11. Straight uniform fin with an adiabatic tip and constant properties:

$$
m_f=\sqrt{\frac{hP}{kA_c}},\qquad \dot Q_f=\sqrt{hPkA_c}(T_b-T_\infty)\tanh(m_fL),\qquad \eta_f=\frac{\tanh(m_fL)}{m_fL}.
$$

$P$ is wetted perimeter, $A_c$ cross-sectional area and $L$ fin length.

12. Critical insulation radius for a long cylinder with constant external $h$:

$$
r_{crit}=k_{ins}/h.
$$

This limited model balances added conduction resistance against increased convecting area; it does not imply that insulation generally increases heat loss.

## 13. Heat exchangers

[Full chapter](../chapters/13-heat-exchangers.md)

Use heat rate $\dot Q$ in W, $c_p$ in J/(kg K), capacity rates $C$ in W/K, overall coefficient $U$ in W/(m2 K), and area in m2.

1. Adiabatic steady exchanger balance without shaft work:

$$
\dot Q=\dot m_h(h_{h,in}-h_{h,out})=\dot m_c(h_{c,out}-h_{c,in}).
$$

2. Constant-$c_p$ single-phase form:

$$
\dot Q=C_h(T_{h,in}-T_{h,out})=C_c(T_{c,out}-T_{c,in}),\qquad C=\dot m c_p.
$$

3. Plane-wall resistance on one common area basis:

$$
\frac1U=\frac1{h_h}+R_{f,h}''+\frac{\delta}{k_w}+R_{f,c}''+\frac1{h_c}.
$$

$R_f''$ is fouling resistance in m2 K/W. Tubular walls require the appropriate area ratios and logarithmic conduction resistance.

4. LMTD heat-transfer relation:

$$
\dot Q=UA F\Delta T_{lm},\qquad \Delta T_{lm}=\frac{\Delta T_1-\Delta T_2}{\ln(\Delta T_1/\Delta T_2)}.
$$

$F=1$ for ideal single-pass parallel or counterflow; correction factors depend on other arrangements.

5. Counterflow terminal differences:

$$
\Delta T_1=T_{h,in}-T_{c,out},\qquad \Delta T_2=T_{h,out}-T_{c,in}.
$$

6. Parallel-flow terminal differences:

$$
\Delta T_1=T_{h,in}-T_{c,in},\qquad \Delta T_2=T_{h,out}-T_{c,out}.
$$

7. Capacity ratio and transfer units:

$$
C_{min}=\min(C_h,C_c),\quad C_r=C_{min}/C_{max},\quad NTU=UA/C_{min}.
$$

8. Maximum theoretical duty and effectiveness:

$$
\dot Q_{max}=C_{min}(T_{h,in}-T_{c,in}),\qquad \varepsilon=\dot Q/\dot Q_{max}.
$$

9. Ideal counterflow effectiveness for $C_r\ne1$:

$$
\varepsilon=\frac{1-e^{-NTU(1-C_r)}}{1-C_r e^{-NTU(1-C_r)}}.
$$

10. Counterflow equal-capacity limit:

$$
\varepsilon=\frac{NTU}{1+NTU}\qquad(C_r=1).
$$

11. Parallel-flow effectiveness:

$$
\varepsilon=\frac{1-e^{-NTU(1+C_r)}}{1+C_r}.
$$

12. One stream at approximately constant phase-change temperature:

$$
C_r\to0,\qquad \varepsilon=1-e^{-NTU}.
$$

13. Approximate pumping requirement for an incompressible stream:

$$
P_{pump}=\Delta p\,Q_v/\eta_p.
$$

$Q_v$ is volume flow, distinguished from thermal duty. Extra thermal area or tighter channels can increase this cost.

## 15. Refrigeration and HVAC

[Full chapter](../chapters/15-refrigeration-and-hvac.md)

Refrigerant enthalpies may be in kJ/kg when mass flow is kg/s and resulting powers are kW. State 1 is evaporator outlet/compressor inlet, 2 compressor outlet, 3 condenser outlet and 4 expansion-valve outlet.

1. Vapor-compression specific cooling and compressor work:

$$
q_L=h_1-h_4,\qquad w_c=h_2-h_1.
$$

2. Throttling approximation, negligible heat, work and kinetic changes:

$$
h_4=h_3.
$$

3. Condenser duty and cycle energy balance:

$$
q_H=h_2-h_3=q_L+w_c.
$$

4. Refrigeration and heat-pump COP:

$$
COP_R=\frac{q_L}{w_c},\qquad COP_{HP}=\frac{q_H}{w_c}=COP_R+1.
$$

The last equality applies to the same defined cycle boundary; external auxiliaries can change system-level comparisons.

5. Reversible two-reservoir limits, all temperatures in K:

$$
COP_{R,rev}=\frac{T_L}{T_H-T_L},\qquad COP_{HP,rev}=\frac{T_H}{T_H-T_L}.
$$

6. Cooling rate and compressor power:

$$
\dot Q_L=\dot m_rq_L,\qquad P_c=\dot m_rw_c.
$$

7. Relative humidity, under the ideal-mixture approximation:

$$
\varphi=\frac{p_v}{p_{ws}(T)},\qquad 0\leq\varphi\leq1
$$

for ordinary unsaturated or saturated equilibrium air. Supersaturation requires separate treatment.

8. Humidity ratio:

$$
w=0.62198\frac{p_v}{p-p_v}.
$$

Pressures use the same units; $w$ is kg water per kg dry air.

9. Approximate moist-air enthalpy, $T_C$ in degrees Celsius:

$$
h_{ma}=1.006T_C+w(2501+1.86T_C)\quad\mathrm{kJ/kg_{dry\ air}}.
$$

This common moderate-temperature approximation uses a stated conventional reference and does not describe all high-temperature or high-pressure humid gases.

10. Dew-point relation:

$$
p_{ws}(T_{dp})=p_v.
$$

11. Coil load and condensate rate, ignoring condensate sensible-enthalpy correction in the load estimate:

$$
\dot Q_{coil}\simeq\dot m_{da}(h_{in}-h_{out}),\qquad \dot m_{cond}=\dot m_{da}(w_{in}-w_{out}).
$$

12. Adiabatic two-stream mixing without condensation:

$$
w_m=\frac{\dot m_{da,1}w_1+\dot m_{da,2}w_2}{\dot m_{da,1}+\dot m_{da,2}},\qquad h_m=\frac{\dot m_{da,1}h_1+\dot m_{da,2}h_2}{\dot m_{da,1}+\dot m_{da,2}}.
$$

13. Sensible load and sensible heat ratio:

$$
\dot Q_s\simeq\dot m c_p\Delta T,\qquad SHR=\frac{\dot Q_s}{\dot Q_s+\dot Q_l}.
$$

Keep dry-air and total-mixture mass bases consistent with the selected heat capacity.

## 16. Combustion and internal-combustion engines

[Full chapter](../chapters/16-combustion-and-engines.md)

Use mass flow in kg/s, heating value in J/kg, torque in N m, angular speed in rad/s, displacement in m3 and power in W unless otherwise specified.

1. Complete hydrocarbon reaction with oxygen, per mole fuel:

$$
\mathrm{C_xH_y}+\left(x+\frac y4\right)\mathrm{O_2}\rightarrow x\mathrm{CO_2}+\frac y2\mathrm{H_2O}.
$$

For a simplified molar dry-air model, append approximately 3.76 mol of nitrogen for each mole of oxygen on both sides.

2. Stoichiometric air-fuel mass ratio using oxygen mass fraction $Y_{O_2,air}$:

$$
AFR_{st}=\frac{m_{O_2,st}/m_f}{Y_{O_2,air}}.
$$

3. Excess-air ratio and equivalence ratio:

$$
\lambda=\frac{AFR}{AFR_{st}},\qquad \phi=\frac1\lambda,\qquad \%\text{ excess air}=100(\lambda-1).
$$

4. Fuel energy input and brake thermal efficiency:

$$
\dot E_f=\dot m_f H_f,\qquad \eta_b=\frac{P_b}{\dot m_fH_f}.
$$

5. Torque-speed power relation:

$$
P_b=\tau\omega=\tau\frac{2\pi N}{60}.
$$

$N$ is in rpm. Name the shaft at which torque is measured.

6. Brake-specific fuel consumption, using $P_b$ in kW:

$$
BSFC=\frac{3600\dot m_f}{P_b}\quad\mathrm{kg/kWh}.
$$

7. Total displacement for $n_c$ cylinders of bore $B$ and stroke $S$:

$$
V_d=n_c\frac{\pi B^2S}{4}.
$$

8. Mean effective pressure:

$$
MEP=\frac{W_{cycle}}{V_d},\qquad BMEP=\frac{4\pi\tau}{V_d}\quad\text{for a four-stroke engine}.
$$

For the analogous two-stroke expression, replace $4\pi$ with $2\pi$.

9. Four-stroke volumetric efficiency using the selected fresh-air reference density:

$$
\eta_v=\frac{\dot m_a}{\rho_{ref}V_d(N/120)}.
$$

10. Mean piston speed:

$$
\overline V_p=2S\frac{N}{60}.
$$

11. Mechanical efficiency on a consistent boundary:

$$
\eta_m=P_b/P_i,\qquad P_f=P_i-P_b.
$$

12. Steady adiabatic reacting-flow energy balance with negligible work, speed and elevation changes:

$$
\sum_{reactants}n_i\left(\bar h_{f,i}^{\circ}+\Delta\bar h_i\right)=\sum_{products}n_j\left(\bar h_{f,j}^{\circ}+\Delta\bar h_j\right).
$$

$\bar h_f^\circ$ is molar standard formation enthalpy and $\Delta\bar h$ is sensible enthalpy from that reference. Do not add a fuel heating value a second time if formation enthalpies already account for reaction energy.

13. Approximate constant-product, constant-heat-capacity flame-temperature rise:

$$
T_{ad}-T_{in}\simeq\frac{Q_{release}}{\sum_j n_j\bar c_{p,j}}.
$$

This simplified estimate neglects dissociation, temperature-dependent heat capacity and unequal reactant inlet temperatures.

## 10. Fluid mechanics

[Full chapter](../chapters/10-fluid-mechanics.md)

Use density $\rho$ in kg/m3, speed $V$ in m/s, dynamic viscosity $\mu$ in Pa s, pressure $p$ in Pa, length in m and force in N.

1. Hydrostatics, upward coordinate $z$, constant density over depth $h$:

$$
\frac{dp}{dz}=-\rho g,\qquad p=p_0+\rho gh.
$$

2. Hydrostatic force on a plane area, measured against a uniform reference pressure:

$$
F=\rho g h_c A.
$$

Here $h_c$ is centroid depth. For a vertical plane, center-of-pressure depth is

$$
h_{cp}=h_c+\frac{I_G}{h_cA},
$$

where $I_G$ is the second moment of area about its horizontal centroidal axis.

3. Buoyant force in a uniform-density fluid:

$$
F_B=\rho g V_{disp}.
$$

4. Volume and mass flow for a section with mean normal speed:

$$
Q=AV,\qquad \dot m=\rho Q.
$$

5. Steady mass conservation:

$$
\sum\dot m_{in}=\sum\dot m_{out}.
$$

6. Steady vector momentum balance for uniform port profiles:

$$
\sum\mathbf F=\sum_{out}\dot m\mathbf V-\sum_{in}\dot m\mathbf V.
$$

7. Bernoulli relation under the assumptions given above:

$$
\frac{p}{\rho g}+\frac{V^2}{2g}+z=\text{constant along a streamline}.
$$

8. Newtonian simple-shear law and kinematic viscosity:

$$
\tau=\mu\frac{du}{dy},\qquad \nu=\mu/\rho.
$$

9. Incompressible Newtonian momentum equation, constant viscosity:

$$
\rho\left(\frac{\partial\mathbf u}{\partial t}+\mathbf u\cdot\nabla\mathbf u\right)=-\nabla p+\mu\nabla^2\mathbf u+\rho\mathbf g,\qquad \nabla\cdot\mathbf u=0.
$$

10. Reynolds, Mach and Froude numbers:

$$
Re=\frac{\rho VL}{\mu},\qquad Ma=\frac{V}{a},\qquad Fr=\frac{V}{\sqrt{gL}}.
$$

$L$ must match the geometry and comparison; $a$ is local sound speed.

11. Drag force, with declared reference area $A_{ref}$:

$$
F_D=\frac12\rho V^2 C_D A_{ref}.
$$

12. Surface-tension pressure jump for a spherical liquid droplet:

$$
\Delta p=2\sigma/R.
$$

Here $\sigma$ is surface tension in N/m. A thin soap bubble has two interfaces and a different factor.

## 11. Pipe flow and pumps

[Full chapter](../chapters/11-pipe-flow-and-pumps.md)

Use $Q$ in m3/s, pipe diameter $D$ and head in m, $p$ in Pa, $\rho$ in kg/m3 and $\mu$ in Pa s. $g=9.81$ m/s2 is used in examples.

1. Mean pipe speed and Reynolds number:

$$
V=\frac{4Q}{\pi D^2},\qquad Re=\frac{\rho VD}{\mu}.
$$

2. Darcy-Weisbach straight-pipe head loss:

$$
h_f=f_D\frac{L}{D}\frac{V^2}{2g}.
$$

3. Fully developed laminar circular-pipe friction factor:

$$
f_D=\frac{64}{Re}.
$$

4. Colebrook equation for ordinary turbulent pipe flow:

$$
\frac1{\sqrt{f_D}}=-2\log_{10}\left(\frac{\epsilon/D}{3.7}+\frac{2.51}{Re\sqrt{f_D}}\right).
$$

$\epsilon$ is effective roughness. Transitional flow needs special attention rather than uncritical interpolation.

5. Local fitting losses, with each $V_i$ matching its coefficient:

$$
h_m=\sum_i K_i\frac{V_i^2}{2g}.
$$

6. Energy balance between boundary sections, no turbine:

$$
H_p=\frac{p_2-p_1}{\rho g}+z_2-z_1+\frac{\alpha_2V_2^2-\alpha_1V_1^2}{2g}+h_f+h_m.
$$

$\alpha$ is the kinetic-energy correction; reservoir surface velocities are often negligible.

7. Hydraulic, shaft and electrical powers:

$$
P_h=\rho gQH_p,\qquad P_s=P_h/\eta_p,\qquad P_e=P_s/\eta_m.
$$

8. Approximate turbulent system curve for fixed geometry:

$$
H_{sys}=H_{static}+CQ^2.
$$

$C$ has units s2/m5 and includes the assumed loss behavior.

9. Available NPSH at pump suction flange, with its elevation datum:

$$
NPSH_A=\frac{p_{s,abs}}{\rho g}+\frac{V_s^2}{2g}-\frac{p_v}{\rho g}.
$$

10. For an open suction reservoir with negligible surface speed:

$$
NPSH_A=\frac{p_{atm}-p_v}{\rho g}+z_{surface}-z_{pump}-h_{L,suction}.
$$

11. Same impeller, approximately homologous speed changes:

$$
\frac{Q_2}{Q_1}=\frac{N_2}{N_1},\qquad \frac{H_2}{H_1}=\left(\frac{N_2}{N_1}\right)^2,\qquad \frac{P_2}{P_1}\simeq\left(\frac{N_2}{N_1}\right)^3.
$$

12. Rapid liquid velocity change, ideal Joukowsky pressure rise:

$$
\Delta p=\rho a\Delta V.
$$

$a$ is the coupled liquid-pipe wave speed, not automatically the free-liquid sound speed. The relation describes a rapid event before reflection details are resolved.

## 14. Turbomachinery

[Full chapter](../chapters/14-turbomachinery.md)

Let $C$ be absolute velocity, $W$ relative velocity, $U$ blade speed, $r$ radius, $\omega$ angular speed in rad/s, and $C_\theta$ absolute tangential velocity. Speeds are in m/s.

1. Velocity triangles:

$$
\mathbf C=\mathbf U+\mathbf W,\qquad U=\omega r.
$$

2. Rotation-rate conversion, $N$ in revolutions per minute:

$$
\omega=\frac{2\pi N}{60}.
$$

3. Torque applied by a rotor to the fluid, for steady uniform stations:

$$
\tau=\dot m(r_2C_{\theta2}-r_1C_{\theta1}).
$$

4. Euler specific work delivered to fluid:

$$
w_E=U_2C_{\theta2}-U_1C_{\theta1},\qquad P_E=\dot m w_E.
$$

5. Euler head and useful pump head with hydraulic efficiency $\eta_h$:

$$
H_E=w_E/g,\qquad H=\eta_hH_E.
$$

6. Incompressible hydraulic power and total pump efficiency:

$$
P_h=\rho gQH,\qquad \eta_p=P_h/P_{shaft}.
$$

7. Stagnation enthalpy and ideal-gas stagnation temperature with constant $c_p$:

$$
h_0=h+\frac{C^2}{2},\qquad T_0=T+\frac{C^2}{2c_p}.
$$

8. Adiabatic rotor energy balance neglecting elevation:

$$
h_{02}-h_{01}=w_E.
$$

For a turbine, useful extracted work has the opposite sign: $w_t=h_{01}-h_{02}$.

9. Total-to-total isentropic efficiencies:

$$
\eta_c=\frac{h_{02s}-h_{01}}{h_{02}-h_{01}},\qquad \eta_t=\frac{h_{01}-h_{02}}{h_{01}-h_{02s}}.
$$

10. One consistent set of incompressible similarity coefficients:

$$
\phi=\frac{Q}{\omega D^3},\qquad \psi=\frac{gH}{\omega^2D^2},\qquad \lambda=\frac{P}{\rho\omega^3D^5}.
$$

Reference diameter $D$ and power basis must be declared. Alternative conventions may include numerical constants.

11. Fixed-diameter affinity laws at similar conditions:

$$
Q\propto N,\qquad H\propto N^2,\qquad P\propto N^3.
$$

12. Dimensionless specific speed:

$$
\Omega_s=\frac{\omega\sqrt Q}{(gH)^{3/4}}.
$$

13. A common definition of compressor corrected quantities relative to reference conditions:

$$
\dot m_{corr}=\dot m\frac{\sqrt{T_{01}/T_{ref}}}{p_{01}/p_{ref}},\qquad N_{corr}=\frac{N}{\sqrt{T_{01}/T_{ref}}}.
$$

Map definitions vary; use the manufacturer's exact reference states and units.

## 17. Mass transfer

[Full chapter](../chapters/17-mass-transfer.md)

Use diffusivity $D_{AB}$ in m2/s, concentration $c_A$ in mol/m3, molar flux in mol/(m2 s), transfer coefficient $k_c$ in m/s, and time in s. Mass-concentration equations have analogous forms when the basis is used consistently.

1. Binary Fickian diffusive molar flux relative to the molar-average velocity, constant total concentration $c$:

$$
\mathbf J_A=-cD_{AB}\nabla y_A=-D_{AB}\nabla c_A.
$$

2. Total molar flux through a stationary plane:

$$
N_A=J_A+y_A(N_A+N_B).
$$

3. Steady one-dimensional diffusion through a slab, constant $D$ and equimolar counterdiffusion or no bulk transport:

$$
N_A=D_{AB}\frac{c_{A,1}-c_{A,2}}{L},\qquad \dot n_A=AN_A.
$$

4. Species balance with constant diffusivity, incompressible mixture and molar production rate $r_A$:

$$
\frac{\partial c_A}{\partial t}+\mathbf u\cdot\nabla c_A=D_{AB}\nabla^2c_A+r_A.
$$

5. Characteristic diffusion time:

$$
t_D\sim L^2/D_{AB}.
$$

This is an order-of-magnitude timescale; exact approach times depend on geometry and boundary conditions.

6. Film transfer law:

$$
N_A=k_c(c_{A,s}-c_{A,b}).
$$

Subscripts $s$ and $b$ denote interface and bulk; sign follows the chosen direction.

7. Sherwood, Schmidt and mass Peclet numbers:

$$
Sh=\frac{k_cL}{D_{AB}},\qquad Sc=\frac{\nu}{D_{AB}},\qquad Pe_m=\frac{VL}{D_{AB}}=Re\,Sc.
$$

8. First-order reaction-diffusion comparison, rate constant $k_r$ in 1/s:

$$
Da_D=\frac{k_rL^2}{D_{AB}}.
$$

9. Gas-liquid interfacial equilibrium in one specified concentration convention:

$$
c_{A,g}^{*}=m\,c_{A,l}.
$$

Here $m$ is the dimensionless gas-to-liquid concentration partition ratio for both concentrations in mol/m3. Other Henry-law conventions have different units and reciprocal forms.

10. Two-film overall coefficient on the gas concentration basis:

$$
N_A=K_g(c_{A,g,b}-m c_{A,l,b}),\qquad \frac1{K_g}=\frac1{k_g}+\frac{m}{k_l}.
$$

11. Well-mixed batch liquid with constant equilibrium concentration and no reaction:

$$
\frac{dC}{dt}=k_La(C^*-C),\qquad C(t)=C^*-(C^*-C_0)e^{-k_Lat}.
$$

$k_La$ is in 1/s; $C$ may be mass concentration if every term uses that basis.

12. Binary ideal-gas diffusion of A through stagnant B, constant pressure and temperature:

$$
N_A=\frac{D_{AB}c}{L}\ln\left(\frac{1-y_{A,2}}{1-y_{A,1}}\right),\qquad N_B=0.
$$

13. Simple solution-diffusion membrane model:

$$
N_A=\frac{\mathcal P_A}{L}(p_{A,1}-p_{A,2}),\qquad \mathcal P_A=D_AS_A.
$$

Solubility $S_A$ is mol/(m3 Pa), so permeability $\mathcal P_A$ is mol/(m s Pa). Actual membranes may show nonlinear sorption and coupled transport.

## 21. Manufacturing processes and production

[Full chapter](../chapters/21-manufacturing.md)

**1. Turning cutting speed**, diameter $D$ in mm, spindle speed $n$ rpm, and speed $V_c$ m/min:

$$
V_c=\frac{\pi Dn}{1000}.
$$

**2. Turning feed speed and cutting time**, feed $f$ mm/rev and cutting travel $L_c$ mm:

$$
v_f=fn,\qquad t_c=\frac{L_c}{fn}.
$$

$v_f$ is mm/min and $t_c$ min; travel must include required approach and overrun.

**3. Approximate turning removal rate**, radial depth of cut $a_p$ mm:

$$
Q_v\approx1000V_cfa_p.
$$

$Q_v$ is mm³/min; this conventional relation treats surface speed as representative through the cut.

**4. Milling feed speed**, $z$ cutting teeth and feed per tooth $f_z$ mm/tooth:

$$
v_f=f_zzn.
$$

**5. Cutting power**, specific cutting energy $u_s$ J/m³ and removal rate in m³/s:

$$
P_c=u_sQ_v,\qquad P_{\mathrm{input}}=P_c/\eta.
$$

Specific energy varies with material, chip thickness, geometry, and condition.

**6. Taylor tool-life approximation**, under fixed tool, work material, feed, and depth conditions:

$$
V_cT^n=C_T.
$$

The empirical exponent $n$ here is not spindle speed; units of $C_T$ depend on chosen speed and time units.

**7. Idealized turning roughness**, feed $f$ and tool nose radius $r_e$ in matching length units:

$$
R_a\approx\frac{f^2}{32r_e}.
$$

This geometric estimate excludes built-up edge, vibration, wear, and material tearing.

**8. Chvorinov-type solidification estimate**:

$$
t_s=C_m\left(\frac VA\right)^n.
$$

$V$ is casting volume and $A$ cooling area; exponent is often approximated as 2 for a calibrated mold system. $C_m$ is process-specific and unit-dependent.

**9. Ideal true forming strain**, uniform compression from height $h_0$ to $h$:

$$
\epsilon=\ln(h_0/h),\qquad A_0h_0\approx Ah.
$$

**10. Instantaneous ideal homogeneous upsetting force**, current flow stress $\sigma_f(\epsilon)$ and current area $A$:

$$
F_{\mathrm{ideal}}(\epsilon)\approx\sigma_f(\epsilon)A(\epsilon).
$$

For a work-hardening material, evaluate the current flow stress and increasing area throughout the stroke to estimate the peak ideal load. The strain-averaged flow stress $\bar\sigma_f=(1/\epsilon)\int_0^\epsilon\sigma_f(\eta)\,d\eta$ is useful for plastic-work estimates. Substituting it into $\bar\sigma_f A$ gives only a rough representative load, not generally the instantaneous or peak force. Friction, barreling, and redundant deformation generally increase actual load.

**11. Net welding heat input per length**, voltage $U$, current $I$, travel speed $v$ m/s:

$$
H=\frac{\eta_wUI}{v}.
$$

$H$ is J/m; $\eta_w$ is the process-dependent thermal efficiency.

**12. Batch cost and break-even quantity**:

$$
C(N)=C_F+c_vN,\qquad N_* =\frac{C_{F,A}-C_{F,B}}{c_{v,B}-c_{v,A}}.
$$

Both alternatives must produce equivalent acceptable parts; include tooling, scrap, inspection, and postprocessing consistently.

## 22. Metrology, uncertainty, and quality

[Full chapter](../chapters/22-metrology.md)

**1. Sample mean and sample standard deviation**, $n>1$ observations:

$$
\bar x=\frac1n\sum x_i,\qquad s=\sqrt{\frac{\sum(x_i-\bar x)^2}{n-1}}.
$$

**2. Standard uncertainty of an independent-observation mean**:

$$
u_A(\bar x)=\frac{s}{\sqrt n}.
$$

Autocorrelated readings require a different effective information model.

**3. Rectangular distribution**, half-width $a$ around its center:

$$
u=a/\sqrt3.
$$

**4. Digital rounding resolution**, increment $q$ and uniform rounding error:

$$
u_{\mathrm{res}}=q/\sqrt{12}.
$$

**5. Linearized combined uncertainty**, $y=f(x_1,\ldots,x_n)$:

$$
u_c^2(y)=\sum_i c_i^2u^2(x_i)+2\sum_{i<j}c_ic_j\operatorname{cov}(x_i,x_j),\qquad c_i=\frac{\partial f}{\partial x_i}.
$$

Sensitivity coefficients carry the units needed to convert each input contribution into output units.

**6. Expanded uncertainty**:

$$
U=ku_c.
$$

Coverage factor $k$ is not automatically 2; distribution, effective degrees of freedom, and desired coverage matter. NIST explains the evaluation and reporting framework in [Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297).

**7. First-order thermal length correction**, constant expansion coefficient $\alpha_T$:

$$
L(T)\approx L(T_0)[1+\alpha_T(T-T_0)].
$$

**8. Abbe offset error**, offset $h$ and small angular error $\theta$:

$$
e_A=h\tan\theta\approx h\theta.
$$

Use radians in the small-angle approximation.

**9. Cosine projection error**, projected length $L_m=L\cos\theta$:

$$
e_C=L_m-L=L(\cos\theta-1)\approx-\tfrac12L\theta^2.
$$

**10. Process potential capability**, normal stable distribution with standard deviation $\sigma$:

$$
C_p=\frac{USL-LSL}{6\sigma}.
$$

**11. Centering-sensitive capability**:

$$
C_{pk}=\min\left(\frac{USL-\mu}{3\sigma},\frac{\mu-LSL}{3\sigma}\right).
$$

**12. Arithmetic mean roughness**, over the defined evaluation length after the required filtering:

$$
R_a=\frac1L\int_0^L|z(x)|\,dx.
$$

Roughness depends on measurement direction, filtering, and evaluation conventions; a single number does not describe all surface functionality.

## 23. CAD, engineering drawing, and tolerances

[Full chapter](../chapters/23-cad-and-engineering-drawing.md)

Use one stated length unit throughout each model and drawing. Formulas below describe geometry and elementary tolerances, not complete GD&T acceptance rules.

**1. Drawing scale**:

$$
S=\frac{L_{\mathrm{drawing}}}{L_{\mathrm{actual}}}.
$$

Written dimensions govern; never infer an unspecified production dimension by measuring a printed view.

**2. Homogeneous point transformation**:

$$
\begin{bmatrix}\mathbf p'\\1\end{bmatrix}=\begin{bmatrix}\mathbf R&\mathbf t\\\mathbf0^T&1\end{bmatrix}\begin{bmatrix}\mathbf p\\1\end{bmatrix}.
$$

$\mathbf R$ is a dimensionless rotation matrix and $\mathbf t$ a translation in the point's length unit.

**3. Planar rotation**:

$$
x'=x\cos\theta-y\sin\theta,\qquad y'=x\sin\theta+y\cos\theta.
$$

**4. Bolt-circle coordinates**, center $(x_c,y_c)$, radius $R$, $N$ holes:

$$
\theta_i=\theta_0+\frac{2\pi i}{N},\qquad x_i=x_c+R\cos\theta_i,\qquad y_i=y_c+R\sin\theta_i.
$$

**5. Arc length and chord**:

$$
s=R\theta,\qquad c=2R\sin(\theta/2).
$$

Use radians for $s=R\theta$.

**6. Conical taper**, large diameter $D$, small diameter $d$, length $L$:

$$
\tan\alpha=\frac{D-d}{2L}.
$$

$\alpha$ is the half-angle, not the included cone angle.

**7. Hole–shaft clearance limits**:

$$
C_{\min}=D_{h,\min}-D_{s,\max},\qquad C_{\max}=D_{h,\max}-D_{s,\min}.
$$

Negative clearance indicates interference for that combination.

**8. Linear dimension chain**, signed coefficients $a_i$:

$$
Y=\sum_i a_iX_i,\qquad T_{Y,\mathrm{worst}}=\sum_i|a_i|T_i.
$$

$T_i$ are symmetric half-width tolerances around nominal values.

**9. Independent statistical stack**, using standard deviations rather than arbitrary drawing tolerances:

$$
\sigma_Y=\sqrt{\sum_i a_i^2\sigma_i^2}.
$$

Add covariance terms if component dimensions are correlated.

**10. Coordinate-based diametral position deviation**, for a measured axis point relative to its basic location:

$$
p_{xy}=2\sqrt{(x-x_b)^2+(y-y_b)^2}.
$$

This simple two-dimensional calculation alone does not evaluate full axis orientation, datum establishment, material modifiers, or all requirements of a position tolerance.

**11. Approximate sheet bend allowance**:

$$
BA=\theta(R_i+K_bt).
$$

$R_i$ is inside bend radius, $t$ thickness, and $K_b$ a calibrated neutral-axis factor; angle is radians. Real bend tables depend on material and tooling.

**12. Uniform-density mass estimate**:

$$
m=\rho V,\qquad\mathbf r_G=\frac{\sum_i m_i\mathbf r_i}{\sum_i m_i}.
$$

Use actual material assignment, units, and modeled components; suppressed or simplified features can alter mass properties.

## 24. Finite Element Analysis

[Full chapter](../chapters/24-finite-element-analysis.md)

Let $u$ be axial displacement (m), $x$ position (m), $E$ Young's modulus (Pa), $A$ area ($\mathrm{m^2}$), $L$ element length (m), $P$ force (N), and $\mathbf d$ the nodal displacement vector (m).

**Linear interpolation, two-node bar:**

$$
u(x)=N_1d_1+N_2d_2,\qquad N_1=1-x/L,\quad N_2=x/L.
$$

**Small axial strain and elastic stress:**

$$
\varepsilon=\frac{du}{dx}=\mathbf B\mathbf d,\qquad \mathbf B=[-1/L\quad1/L],\qquad \sigma=E\varepsilon.
$$

Strain is dimensionless; stress is in Pa. Thermal or initial strain must be subtracted before applying the elastic constitutive relation.

**Element stiffness, constant $E,A$:**

$$
\mathbf k_e=\int_0^L\mathbf B^TEA\mathbf B\,dx=\frac{EA}{L}\begin{bmatrix}1&-1\\-1&1\end{bmatrix}.
$$

Stiffness entries have units N/m. Assembly adds contributions at shared global degrees of freedom:

$$
\mathbf K\mathbf d=\mathbf f.
$$

After partitioning free ($f$) and prescribed ($c$) displacements:

$$
\mathbf K_{ff}\mathbf d_f=\mathbf f_f-\mathbf K_{fc}\mathbf d_c.
$$

**Reactions, using the original unmodified matrices:**

$$
\mathbf r=\mathbf K\mathbf d-\mathbf f.
$$

**Strain energy and total potential energy:**

$$
U=\tfrac12\mathbf d^T\mathbf K\mathbf d,\qquad \Pi=U-\mathbf d^T\mathbf f.
$$

Both are in joules for force-displacement problems. **Uniform axial bar benchmark:**

$$
\delta=\frac{PL}{EA},\qquad \sigma=\frac PA.
$$

**Linear dynamics:**

$$
\mathbf M\ddot{\mathbf d}+\mathbf C\dot{\mathbf d}+\mathbf K\mathbf d=\mathbf f(t).
$$

Mass $\mathbf M$ has units kg; damping $\mathbf C$ has units N s/m. Undamped free-vibration modes satisfy

$$
(\mathbf K-\omega^2\mathbf M)\boldsymbol\phi=\mathbf0.
$$

**Relative mesh change for a nonzero scalar quantity $q$:**

$$
\epsilon_q=\frac{|q_{\rm fine}-q_{\rm coarse}|}{|q_{\rm fine}|}.
$$

This is a comparison between two meshes, not a guaranteed error bound.

## 25. Computational Fluid Dynamics

[Full chapter](../chapters/25-computational-fluid-dynamics.md)

Let $\rho$ be density ($\mathrm{kg/m^3}$), $\mathbf u$ velocity (m/s), $p$ pressure (Pa), $\mu$ dynamic viscosity (Pa s), $\nu=\mu/\rho$ kinematic viscosity ($\mathrm{m^2/s}$), and $t$ time (s).

**General mass conservation:**

$$
\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf u)=0.
$$

For constant density, $\nabla\cdot\mathbf u=0$. **Constant-property incompressible Newtonian momentum:**

$$
\rho\left(\frac{\partial\mathbf u}{\partial t}+\mathbf u\cdot\nabla\mathbf u\right)=-\nabla p+\mu\nabla^2\mathbf u+\rho\mathbf g.
$$

**Scalar advection-diffusion, constant diffusivity $\alpha$ ($\mathrm{m^2/s}$):**

$$
\frac{\partial\phi}{\partial t}+\mathbf u\cdot\nabla\phi=\alpha\nabla^2\phi+s_\phi.
$$

For temperature, $\alpha=k/(\rho c_p)$, where $k$ is thermal conductivity ($\mathrm{W/(m\,K)}$), $c_p$ specific heat ($\mathrm{J/(kg\,K)}$), and $s_\phi$ has units K/s. **Finite-volume mass balance in a fixed cell:**

$$
\frac{d(\rho V)}{dt}+\sum_f\rho_f(\mathbf u_f\cdot\mathbf n_f)A_f=0.
$$

$V$ is cell volume ($\mathrm{m^3}$), $A_f$ face area ($\mathrm{m^2}$), and $\mathbf n_f$ the outward normal. **Centered second derivative, uniform grid:**

$$
\frac{\partial^2\phi}{\partial x^2}\approx\frac{\phi_{i+1}-2\phi_i+\phi_{i-1}}{\Delta x^2}.
$$

**One-dimensional explicit upwind transport for $u>0$:**

$$
\phi_i^{n+1}=\phi_i^n-C(\phi_i^n-\phi_{i-1}^n),\qquad C=\frac{u\Delta t}{\Delta x}.
$$

For this particular linear scheme, stability requires $0\le C\le1$. **Explicit one-dimensional centered diffusion:**

$$
\phi_i^{n+1}=\phi_i^n+Fo(\phi_{i+1}^n-2\phi_i^n+\phi_{i-1}^n),\quad Fo=\frac{\alpha\Delta t}{\Delta x^2}\le\frac12.
$$

The diffusion limit changes with spatial dimension and scheme. **Dimensionless flow measures:**

$$
Re=\frac{UL}{\nu},\qquad Pe=\frac{UL}{\alpha},\qquad y^+=\frac{u_\tau y}{\nu},\quad u_\tau=\sqrt{\frac{|\tau_w|}{\rho}}.
$$

$U$ and $L$ are stated characteristic scales; $y$ is wall distance and $\tau_w$ wall shear (Pa). **Equal-ratio, monotonic, asymptotic three-grid estimate:**

$$
p_{\rm obs}=\frac{\ln|(q_3-q_2)/(q_2-q_1)|}{\ln r},\qquad q_{\rm ext}=q_1+\frac{q_1-q_2}{r^{p_{\rm obs}}-1}.
$$

Here 1 is finest, 3 coarsest, and $r=h_2/h_1=h_3/h_2>1$. It is not applicable blindly to oscillatory or non-asymptotic data.

## 30. Engineering Design and Optimization

[Full chapter](../chapters/30-design-and-optimization.md)

Let $\mathbf x$ be the design vector, $f$ the objective, $g_i$ inequality functions, and $h_j$ equality functions. **Constrained formulation:**

$$
\min_{\mathbf x}f(\mathbf x),\qquad g_i(\mathbf x)\le0,\quad h_j(\mathbf x)=0.
$$

Each function must have stated units or be dimensionless. **Scaling:**

$$
\widetilde x_i=\frac{x_i}{x_{i,\rm ref}},\qquad \widetilde g_i=\frac{g_i}{g_{i,\rm ref}}.
$$

Reference scales are positive and representative. **Unconstrained interior stationarity:**

$$
\nabla f(\mathbf x^*)=\mathbf0.
$$

A positive-definite Hessian at a stationary point gives a strict local minimum for a twice continuously differentiable objective. **Lagrangian:**

$$
\mathcal L=f+\sum_i\lambda_i g_i+\sum_j\nu_jh_j.
$$

Under suitable constraint qualifications, the Karush-Kuhn-Tucker necessary conditions include

$$
\nabla_{\mathbf x}\mathcal L=\mathbf0,\quad g_i\le0,\quad h_j=0,\quad\lambda_i\ge0,\quad\lambda_i g_i=0.
$$

These are not a universal guarantee of a global optimum. **Forward and central sensitivities:**

$$
\frac{\partial f}{\partial x_i}\approx\frac{f(\mathbf x+\Delta x_i\mathbf e_i)-f(\mathbf x)}{\Delta x_i},
$$

$$
\frac{\partial f}{\partial x_i}\approx\frac{f(\mathbf x+\Delta x_i\mathbf e_i)-f(\mathbf x-\Delta x_i\mathbf e_i)}{2\Delta x_i}.
$$

Too-small steps can amplify roundoff or solver noise. **Dimensionless sensitivity for nonzero $f,x_i$:**

$$
S_i=\frac{x_i}{f}\frac{\partial f}{\partial x_i}.
$$

**First-order independent-input uncertainty propagation:**

$$
\sigma_f^2\approx\sum_i\left(\frac{\partial f}{\partial x_i}\right)^2\sigma_{x_i}^2.
$$

Correlated inputs need covariance terms. **Uniform axial bar design relations:**

$$
m=\rho AL,\qquad \sigma=P/A,\qquad \delta=PL/(EA).
$$

Here $m$ is kg, $\rho$ density ($\mathrm{kg/m^3}$), $A$ area ($\mathrm{m^2}$), $L$ length (m), $P$ axial force (N), and $E$ modulus (Pa). **Weighted dimensionless objective:**

$$
F(\mathbf x)=\sum_k w_k\frac{f_k(\mathbf x)}{f_{k,\rm ref}},\qquad w_k\ge0.
$$

The weights state preferences; they are not properties of nature.

## 26. Electrical Engineering for Mechanical Engineers

[Full chapter](../chapters/26-electrical-engineering.md)

Let $V$ or $v$ be voltage (V), $I$ or $i$ current (A), $R$ resistance ($\Omega$), $C$ capacitance (F), $L$ inductance (H), $t$ time (s), and $\omega$ angular frequency (rad/s). Lowercase often denotes an instantaneous quantity.

**Ohm's law and resistive power:**

$$
V=IR,\qquad P=VI=I^2R=V^2/R.
$$

The last two expressions apply to a resistor with consistent DC or RMS quantities. **Node and loop equations:**

$$
\sum I_{\rm entering}=\sum I_{\rm leaving},\qquad \sum_{\rm loop}V=0.
$$

**Series and parallel resistors:**

$$
R_s=\sum_iR_i,\qquad \frac1{R_p}=\sum_i\frac1{R_i}.
$$

**Unloaded two-resistor voltage divider:**

$$
V_o=V_s\frac{R_2}{R_1+R_2}.
$$

A load across $R_2$ changes it to $R_2\parallel R_L$. **Capacitor and inductor laws under passive sign convention:**

$$
i=C\frac{dv}{dt},\quad E_C=\tfrac12CV^2,\qquad v=L\frac{di}{dt},\quad E_L=\tfrac12LI^2.
$$

Stored energies $E_C,E_L$ are in joules. **Initially uncharged series RC step response:**

$$
v_C(t)=V_s(1-e^{-t/(RC)}),\qquad \tau=RC.
$$

**Sinusoidal RMS and impedance:**

$$
V_{\rm rms}=V_{\rm peak}/\sqrt2,\quad Z_R=R,\quad Z_L=j\omega L,\quad Z_C=1/(j\omega C).
$$

**Single-phase sinusoidal power:**

$$
P=V_{\rm rms}I_{\rm rms}\cos\phi,\quad Q=V_{\rm rms}I_{\rm rms}\sin\phi,\quad |S|=V_{\rm rms}I_{\rm rms}.
$$

$P$ is in W, $Q$ in var, and $|S|$ in VA. **Balanced sinusoidal three-phase real power:**

$$
P=\sqrt3V_{LL}I_L\cos\phi.
$$

$V_{LL}$ is line-to-line RMS voltage and $I_L$ line current. **Idealized permanent-magnet DC motor:**

$$
v=Ri+L\frac{di}{dt}+k_e\omega_m,\quad T=k_ti,\quad J\dot\omega_m=T-T_L-b\omega_m.
$$

$T,T_L$ are torque (N m), $J$ inertia ($\mathrm{kg\,m^2}$), and $b$ viscous damping ($\mathrm{N\,m\,s/rad}$). The torque constant $k_t$ is in N m/A and back-EMF constant $k_e$ in V s/rad; use compatible SI conventions. **Shaft power and efficiency:**

$$
P_{\rm shaft}=T\omega_m,\qquad \eta=P_{\rm shaft}/P_{\rm electrical}.
$$

## 27. Control Systems

[Full chapter](../chapters/27-control-systems.md)

Let $r$ be reference, $y$ measured output, $e$ error, and $u$ control input. Each has the physical units of its signal; controller gains must convert between those units.

$$
e(t)=r(t)-y(t),\qquad u(t)=K_pe(t)+K_i\int_0^t e(\tau)d\tau+K_d\frac{de}{dt}.
$$

For zero initial conditions, a plant transfer function is $G(s)=Y(s)/U(s)$. The Laplace variable $s$ has units $\mathrm{s^{-1}}$. **Unity negative feedback with controller $C(s)$:**

$$
T(s)=\frac{Y}{R}=\frac{C(s)G(s)}{1+C(s)G(s)},\qquad S(s)=\frac1{1+C(s)G(s)}.
$$

These are complementary sensitivity and sensitivity: $S+T=1$. **First-order plant and unit-step response:**

$$
G(s)=\frac K{\tau s+1},\qquad y(t)=K(1-e^{-t/\tau}),\quad t\ge0.
$$

$\tau>0$ is the time constant (s); $K$ has output/input units. **Standard second-order form:**

$$
G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}.
$$

$\omega_n$ is undamped natural frequency (rad/s), $\zeta$ damping ratio. For $0<\zeta<1$:

$$
\omega_d=\omega_n\sqrt{1-\zeta^2},\qquad t_p=\frac\pi{\omega_d},\qquad M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}.
$$

$M_p$ is overshoot as a fraction. A commonly useful approximate 2% settling time, for a dominant underdamped second-order response, is

$$
t_s\approx\frac4{\zeta\omega_n}.
$$

It is not a universal exact formula. **Final value theorem, only when its stability conditions hold:**

$$
\lim_{t\to\infty}e(t)=\lim_{s\to0}sE(s).
$$

**State-space representation:**

$$
\dot{\mathbf x}=\mathbf A\mathbf x+\mathbf B\mathbf u,\qquad \mathbf y=\mathbf C\mathbf x+\mathbf D\mathbf u.
$$

**Pure time delay:**

$$
G_d(s)=e^{-s\theta},\qquad \angle G_d(j\omega)=-\omega\theta.
$$

Delay $\theta$ is in seconds and phase in radians. **Forward-Euler integral update:**

$$
I_{k+1}=I_k+K_iT_se_k.
$$

$T_s$ is sample period; the digital implementation's stability must be checked separately.

## 28. Mechatronics and Instrumentation

[Full chapter](../chapters/28-mechatronics.md)

Let $x$ be a physical input and $v$ sensor voltage (V). **Linear calibration:**

$$
v=ax+b,\qquad x=\frac{v-b}{a}.
$$

$a$ is sensitivity (V per input unit), and $b$ offset (V). **Ideal uniform $N$-bit ADC step:**

$$
q=\frac{V_{\max}-V_{\min}}{2^N}.
$$

With midpoint reconstruction and no saturation, quantization error satisfies

$$
|e_q|\le q/2,\qquad \sigma_q=q/\sqrt{12}.
$$

The standard deviation assumes a uniform error distribution; deterministic signals need not satisfy that statistical model. **Ideal full-scale sine quantization SNR:**

$$
\mathrm{SNR}_{\rm dB}\approx6.02N+1.76.
$$

This excludes other noise, clipping, and distortion. **Sampling condition for a strictly band-limited signal:**

$$
f_s>2f_{\max},\qquad T_s=1/f_s.
$$

Frequencies are in Hz and $T_s$ in seconds. **First-order RC low-pass cutoff:**

$$
f_c=\frac1{2\pi RC}.
$$

**PWM duty and ideal unipolar average voltage:**

$$
D=\frac{t_{\rm on}}{T},\qquad \overline V=DV_s.
$$

For a resistor switched between $V_s$ and zero, actual mean power is

$$
\overline P=\frac{D V_s^2}{R}.
$$

It is not $(\overline V)^2/R$. **Ideal gear speed relation and torque with efficiency:**

$$
\omega_o=\frac{\omega_m}{G},\qquad T_o=\eta G T_m.
$$

$G>1$ denotes reduction ratio. **Load inertia reflected through an ideal rigid gear:**

$$
J_{\rm reflected}=\frac{J_L}{G^2}.
$$

**Encoder angular increment:**

$$
\Delta\theta=\frac{2\pi}{N_c}.
$$

$N_c$ is actual counted transitions per revolution, including the chosen decoding mode. **First-order digital low-pass filter:**

$$
y_k=\alpha x_k+(1-\alpha)y_{k-1},\qquad 0<\alpha\le1.
$$

For a matched sampled exponential pole, $\alpha=1-e^{-T_s/\tau}$. This filter adds lag.

## 29. Robotics

[Full chapter](../chapters/29-robotics.md)

Angles are in radians unless stated. For a planar two-link arm, $l_1,l_2$ are lengths (m), $\theta_1,\theta_2$ joint angles, and $x,y$ tool coordinates (m).

**Forward kinematics:**

$$
x=l_1\cos\theta_1+l_2\cos(\theta_1+\theta_2),\qquad y=l_1\sin\theta_1+l_2\sin(\theta_1+\theta_2).
$$

**Position inverse kinematics:**

$$
c_2=\frac{x^2+y^2-l_1^2-l_2^2}{2l_1l_2},\quad \theta_2=\operatorname{atan2}(\pm\sqrt{1-c_2^2},c_2).
$$

Real solutions require $|c_2|\le1$. Then

$$
\theta_1=\operatorname{atan2}(y,x)-\operatorname{atan2}(l_2\sin\theta_2,l_1+l_2\cos\theta_2).
$$

**Two-link planar Jacobian:**

$$
\begin{bmatrix}\dot x\\\dot y\end{bmatrix}=\mathbf J\begin{bmatrix}\dot\theta_1\\\dot\theta_2\end{bmatrix},\qquad
\mathbf J=\begin{bmatrix}-l_1\sin\theta_1-l_2\sin(\theta_1+\theta_2)&-l_2\sin(\theta_1+\theta_2)\\l_1\cos\theta_1+l_2\cos(\theta_1+\theta_2)&l_2\cos(\theta_1+\theta_2)\end{bmatrix}.
$$

**Singularity measure for this arm:**

$$
\det\mathbf J=l_1l_2\sin\theta_2.
$$

**General rigid transform:**

$$
\mathbf T=\begin{bmatrix}\mathbf R&\mathbf p\\\mathbf0^T&1\end{bmatrix},\qquad \mathbf R^T\mathbf R=\mathbf I,\quad \det\mathbf R=1.
$$

**Serial composition and inverse:**

$$
\mathbf T_{ac}=\mathbf T_{ab}\mathbf T_{bc},\qquad \mathbf T^{-1}=\begin{bmatrix}\mathbf R^T&-\mathbf R^T\mathbf p\\\mathbf0^T&1\end{bmatrix}.
$$

**Quasistatic joint load from a task-space force:**

$$
\boldsymbol\tau=\mathbf J^T\mathbf F.
$$

Use consistent frames and signs; $\mathbf F$ is in N and torques in N m. **Manipulator dynamics:**

$$
\mathbf M(\mathbf q)\ddot{\mathbf q}+\mathbf C(\mathbf q,\dot{\mathbf q})\dot{\mathbf q}+\mathbf g(\mathbf q)=\boldsymbol\tau+\mathbf J^T\mathbf F_{\rm ext}.
$$

Friction may be added separately. **Differential-drive kinematics:**

$$
v=\frac r2(\omega_R+\omega_L),\qquad \dot\psi=\frac r b(\omega_R-\omega_L).
$$

$r$ is wheel radius (m), $b$ wheel separation (m), and wheel speeds are rad/s. **Cubic rest-to-rest scalar motion over duration $T$:**

$$
q(t)=q_0+(q_f-q_0)(3s^2-2s^3),\qquad s=t/T,\quad0\le s\le1.
$$

This gives zero endpoint velocity but nonzero endpoint acceleration; jerk-continuous motion needs a different construction.

## 31. Reliability and Maintenance

[Full chapter](../chapters/31-reliability-and-maintenance.md)

Let $T$ be time to failure, $t\ge0$ elapsed time, $F$ cumulative failure probability, $f$ probability density, and $R$ reliability.

$$
F(t)=P(T\le t),\qquad R(t)=1-F(t),\qquad f(t)=\frac{dF}{dt}=-\frac{dR}{dt}.
$$

Probabilities are dimensionless; $f$ has reciprocal-time units. **Hazard and cumulative hazard:**

$$
h(t)=\frac{f(t)}{R(t)},\qquad H(t)=\int_0^th(\tau)d\tau,\qquad R(t)=e^{-H(t)}.
$$

**Exponential constant-hazard model:**

$$
R(t)=e^{-\lambda t},\qquad f(t)=\lambda e^{-\lambda t},\qquad \mathrm{MTTF}=1/\lambda.
$$

$\lambda$ is in reciprocal hours if $t$ is in hours; units must match. **General nonnegative lifetime mean:**

$$
E[T]=\int_0^\infty R(t)\,dt.
$$

**Two-parameter Weibull model:**

$$
R(t)=e^{-(t/\eta)^\beta},\qquad h(t)=\frac\beta\eta\left(\frac t\eta\right)^{\beta-1}.
$$

$\eta>0$ is scale (time), $\beta>0$ dimensionless shape. **Independent series system:**

$$
R_s(t)=\prod_iR_i(t).
$$

**Independent active parallel system, success if any component works:**

$$
R_p(t)=1-\prod_i[1-R_i(t)].
$$

**Long-run inherent availability under a stationary alternating uptime/repair model:**

$$
A_i=\frac{\mathrm{MTBF}}{\mathrm{MTBF}+\mathrm{MTTR}}.
$$

Here MTBF denotes mean operating time between failures, and MTTR mean corrective repair time. Logistics or administrative delays require an operational availability definition. **Observed uptime fraction:**

$$
A_{\rm observed}=\frac{t_{\rm up}}{t_{\rm up}+t_{\rm down}}.
$$

**Independent repeated Bernoulli trials:**

$$
P(K=k)=\binom nkp^k(1-p)^{n-k}.
$$

This describes counts under the trial assumptions; it is not directly a life-distribution model. **Expected failure consequence for mutually exclusive outcomes:**

$$
E[C]=\sum_i p_iC_i.
$$

Expected cost does not capture every safety or operational requirement.

## 32. Engineering Economics

[Full chapter](../chapters/32-engineering-economics.md)

Let $P$ be present value, $F$ future value, $A$ uniform end-of-period amount, $i$ effective discount rate per period, and $n$ number of periods. Currency units are arbitrary but must be consistent.

**Single amount:**

$$
F=P(1+i)^n,\qquad P=\frac F{(1+i)^n}.
$$

**Uniform series present worth, $i\ne0$:**

$$
P=A\frac{1-(1+i)^{-n}}i.
$$

**Capital recovery factor and annual equivalent:**

$$
\mathrm{CRF}=\frac{i(1+i)^n}{(1+i)^n-1},\qquad A=P\,\mathrm{CRF}.
$$

**Sinking-fund factor:**

$$
A=F\frac i{(1+i)^n-1}.
$$

At $i=0$, use limiting values $P=nA$ and $A=P/n$, avoiding division by zero. **Net present value:**

$$
\mathrm{NPV}=\sum_{t=0}^{n}\frac{CF_t}{(1+i)^t}.
$$

Positive $CF_t$ is net receipt; an initial investment is usually negative. **Equivalent annual cost with initial cost $C_0$, annual operating cost $C_a$, and terminal salvage $S$:**

$$
\mathrm{EAC}=C_0\mathrm{CRF}+C_a-S\frac i{(1+i)^n-1}.
$$

**Nominal-real rate consistency with general inflation $f$:**

$$
1+i_{\rm nominal}=(1+i_{\rm real})(1+f).
$$

**Simple payback for constant positive annual net savings $B$:**

$$
t_{\rm payback}=C_0/B.
$$

**Annual electrical energy and cost:**

$$
E_{\rm annual}=P_{\rm kW}h_{\rm annual},\qquad C_E=E_{\rm annual}c_E.
$$

$E$ is in kWh, $h$ hours/year, and $c_E$ currency/kWh. **Break-even production quantity:**

$$
Q_{\rm BE}=\frac{C_{F,2}-C_{F,1}}{c_{V,1}-c_{V,2}}.
$$

Fixed costs $C_F$ and variable costs $c_V$ must refer to the same period and output basis; the denominator must be nonzero. **Internal rate of return:**

$$
0=\sum_{t=0}^n\frac{CF_t}{(1+i_{\rm IRR})^t}.
$$

Finding a root does not guarantee it is unique or the correct comparison metric.

## 33. Energy Systems and Environmental Accounting

[Full chapter](../chapters/33-energy-and-environment.md)

Let $P$ be power (W), $E$ energy (J), $t$ time (s), and $\eta$ dimensionless efficiency. **Energy from variable power:**

$$
E=\int_0^T P(t)dt,\qquad 1\ \mathrm{kWh}=3.6\times10^6\ \mathrm J.
$$

**Conversion efficiency and simple sequential chain:**

$$
\eta=\frac{E_{\rm useful}}{E_{\rm input}},\qquad \eta_{\rm chain}=\prod_i\eta_i.
$$

The product assumes the output of one stage is the input of the next and no unaccounted parallel streams. **Wind kinetic power and extracted shaft power:**

$$
P_{\rm wind}=\tfrac12\rho A U^3,\qquad P_{\rm shaft}=C_P P_{\rm wind}.
$$

$\rho$ is air density ($\mathrm{kg/m^3}$), $A$ rotor area ($\mathrm{m^2}$), $U$ undisturbed wind speed (m/s), and $C_P$ power coefficient. The ideal unconfined actuator-disk limit is $C_P\le16/27$ under its assumptions. **Hydraulic power:**

$$
P_h=\rho gQH,\qquad P_{\rm electric}=\frac{P_h}{\eta_p\eta_m}.
$$

$Q$ is volumetric flow ($\mathrm{m^3/s}$), $H$ head (m), and pump and motor efficiencies refer to the operating point. **Approximate photovoltaic power at a stated condition:**

$$
P_{\rm PV}=G A\eta_{\rm PV}.
$$

$G$ is irradiance ($\mathrm{W/m^2}$); $\eta_{\rm PV}$ includes only explicitly stated losses. **Capacity factor:**

$$
CF=\frac{E_{\rm annual}}{P_{\rm rated}T_{\rm year}}.
$$

Use matching energy/time units. **Thermal work-potential upper bound for heat from a constant-temperature reservoir:**

$$
W_{\max}=Q\left(1-\frac{T_0}{T_h}\right),\qquad T_h>T_0.
$$

Temperatures are absolute kelvin. **Operational emissions accounting:**

$$
m_{\rm CO_2e}=\sum_i E_i\,EF_i.
$$

If $E_i$ is kWh and $EF_i$ is kg CO2e/kWh, the result is kg CO2e. **Inventory normalized by functional output:**

$$
I_{\rm unit}=\frac{I_{\rm materials}+I_{\rm manufacture}+I_{\rm operation}+I_{\rm end}}{N_{\rm functional\ units}}.
$$

All numerator terms need the same impact metric and allocation basis. **Discounted levelized energy cost:**

$$
\mathrm{LCOE}=\frac{\sum_{t=0}^n C_t/(1+i)^t}{\sum_{t=0}^n E_t/(1+i)^t}.
$$

State timing, included costs, and currency basis. This metric alone does not represent time-dependent energy value or grid integration cost.

## 35 · Systems engineering and integrated design

[Full chapter](../chapters/35-systems-engineering.md)

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

## 36 · Fracture mechanics and fatigue crack growth

[Full chapter](../chapters/36-fracture-mechanics.md)

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

## 37 · Composite materials and laminated plates

[Full chapter](../chapters/37-composite-materials.md)

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

## 38. Compressible flow

[Full chapter](../chapters/38-compressible-flow.md)

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

## 39. Engineering acoustics

[Full chapter](../chapters/39-engineering-acoustics.md)

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

## 40. Corrosion Engineering

[Full chapter](../chapters/40-corrosion-engineering.md)

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

## 41. Welding Engineering

[Full chapter](../chapters/41-welding-engineering.md)

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

## 42 · Continuum mechanics: deformation, stress, and balance

[Full chapter](../chapters/42-continuum-mechanics.md)

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

## 43. Multiphase flow

[Full chapter](../chapters/43-multiphase-flow.md)

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

## 44. Process Plant Engineering

[Full chapter](../chapters/44-process-plant-engineering.md)

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
