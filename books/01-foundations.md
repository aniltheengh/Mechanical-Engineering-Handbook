# Engineering foundations

Mechanical Engineering Handbook · Expanded edition · 2026-11-07

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [01 · Units, dimensions, and engineering estimates](../chapters/01-units-and-dimensional-analysis.md)
- [02 · Engineering mathematics](../chapters/02-engineering-mathematics.md)
- [03 · Numerical methods and engineering computation](../chapters/03-numerical-methods.md)

---

## 01 · Units, dimensions, and engineering estimates

### Learning map

Start here before using any formula in this handbook. You need arithmetic, powers, and elementary algebra. The goal is to translate a physical question into quantities with consistent units, estimate the answer before calculating, and attach a defensible statement of uncertainty. Continue to engineering mathematics and then statics or thermodynamics.

### Theory

A quantity is more than a number. A pipe diameter of 50 means nothing until a unit is supplied. The quantity equation describes physics independently of the selected units; a numerical equation may contain conversion factors tied to one unit convention. In this handbook, equations are quantity equations unless explicitly labelled otherwise. Convert all inputs into a consistent system before substitution.

The seven SI base quantities are time (second, s), length (metre, m), mass (kilogram, kg), electric current (ampere, A), thermodynamic temperature (kelvin, K), amount of substance (mole, mol), and luminous intensity (candela, cd). Force, energy, pressure, and power are derived quantities. A newton is kg m/s², a joule is N m, a pascal is N/m², and a watt is J/s. A torque and an energy have the same dimensions, but they are different physical quantities; reporting torque in N m preserves that distinction.

Mass is not weight. Mass expresses inertia, while weight is a gravitational force. The local acceleration $g$ varies; $9.81\ \mathrm{m/s^2}$ is an ordinary engineering approximation, not a universal exact constant. Density is mass per volume and specific weight is weight per volume. Similarly, pressure and stress have the same units but refer to different physical descriptions.

Dimensional consistency is necessary but insufficient. Both $mv^2$ and $mv^2/2$ have energy dimensions. Only the physical derivation determines the factor. An empirical correlation may also require dimensionless inputs, a specified geometry, and a limited experimental range. Never repair an inconsistent expression merely by inserting a numerical constant without understanding its units.

An estimate should expose the scale controlling the outcome. For lifting water, the important quantities are mass flow, height, gravity, and efficiency. Fine details about pipe roughness cannot rescue a calculation that uses litres per minute as cubic metres per second. Establish the dominant balance first, then refine the model.

Uncertainty describes imperfect knowledge of an input or result. Error is the difference from a reference value; its true value is often unknown. Standard uncertainty is expressed as a standard-deviation-equivalent quantity. Repeated measurements help estimate random variation, but do not automatically remove calibration bias. Correlated inputs require covariance terms; treating every measurement as independent can underestimate or overestimate uncertainty.

### Formula handbook

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

### Derivation

Suppose drag $F$ depends on density $\rho$, speed $U$, diameter $D$, and dynamic viscosity $\mu$. Their dimensions are $MLT^{-2}$, $ML^{-3}$, $LT^{-1}$, $L$, and $ML^{-1}T^{-1}$. Five variables with three independent dimensions imply two dimensionless groups. Dividing force by $\rho U^2D^2$ removes all dimensions, while $\rho UD/\mu$ is already dimensionless. Therefore dimensional analysis permits

$$
\frac{F}{\rho U^2D^2}=\Phi\left(\frac{\rho UD}{\mu}\right).
$$

It does not determine the function $\Phi$. Surface roughness, compressibility, or free-surface effects add variables and groups if they matter physically. Omitting them at the start is a modelling assumption, not a mathematical consequence.

### Worked examples

#### Example 1: Water-lifting power

A pump lifts water at 120 L/min through 18 m of total head. Use $\rho=998\ \mathrm{kg/m^3}$, $g=9.81\ \mathrm{m/s^2}$, and total efficiency 0.65. Convert the flow: $Q=120(10^{-3})/60=0.002\ \mathrm{m^3/s}$. Then $P_h=998(9.81)(0.002)(18)=352.45\ \mathrm{W}$ and $P_{\mathrm{in}}=542.24\ \mathrm{W}$. The efficiency correction must increase the required input power. This is a duty estimate, not a motor selection including start-up, service conditions, or operating margin.

#### Example 2: Area uncertainty

A measured diameter is $d=20.00\ \mathrm{mm}$ with standard uncertainty $u_d=0.05\ \mathrm{mm}$. For $A=\pi d^2/4$, $A=314.159\ \mathrm{mm^2}$. The sensitivity is $dA/dd=\pi d/2$, so $u_A=(\pi20/2)(0.05)=1.571\ \mathrm{mm^2}$. Relative standard uncertainty is $2u_d/d=0.005=0.5\%$. Report about $314.2\ \mathrm{mm^2}$ with standard uncertainty $1.6\ \mathrm{mm^2}$, specifying the uncertainty meaning rather than silently calling it a guaranteed bound.

### Exercises

1. A shaft transmits 25 N m at 1440 rpm. Find power in kW.
2. A gauge reads 250 kPa and ambient pressure is 98 kPa. Find absolute pressure.
3. Density is obtained from independent measurements with relative standard uncertainties 1% in mass and 2% in volume. Estimate its relative standard uncertainty.

### Solutions

1. $\omega=2\pi(1440)/60=150.796\ \mathrm{rad/s}$ and $P=25\omega=3.770\ \mathrm{kW}$. Rpm cannot be substituted directly into $P=\tau\omega$.
2. $p_{\mathrm{abs}}=250+98=348\ \mathrm{kPa}$. The ambient datum must be stated.
3. Because $\rho=mV^{-1}$, $u_\rho/\rho=\sqrt{0.01^2+0.02^2}=0.02236$, or 2.24%. This result assumes independence and a suitable linear approximation.

### Common mistakes

Confusing kW with kWh, entering millimetres into an equation otherwise using metres, using Celsius in a temperature ratio, and mixing gauge and absolute pressure can each change an answer by orders of magnitude. Excess decimal places do not create measurement precision. A dimensionless number can still have a convention: the Darcy and Fanning friction factors differ by four.

### Applications and limits

Use a short calculation record: sketch the system, state the quantity sought, list input sources and units, write the physical model, substitute values, check the dimensions, estimate the scale, and record assumptions. Similarity arguments help plan experiments, but matching one dimensionless group does not guarantee full similarity. This chapter establishes calculation discipline for every later volume.

### Further reading

- [BIPM, SI Brochure](https://www.bipm.org/en/publications/si-brochure/) — official unit definitions and notation; the publisher page provides the current edition and updates.
- [NIST Technical Note 1297, uncertainty propagation](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty) — full treatment of sensitivity coefficients and covariance. The examples here are original.


---

## 02 · Engineering mathematics

### Learning map

Prerequisites are algebra, trigonometry, and consistent units. This chapter connects calculus, vectors, matrices, differential equations, transforms, and probability to mechanical models. It is a reference and bridge to full mathematics courses, not a replacement for a multisemester mathematics sequence. Use it alongside dynamics, heat transfer, vibrations, controls, and numerical methods.

### Theory

Engineering equations describe relationships between quantities and their changes. A derivative is a local rate: displacement differentiates to velocity and then acceleration. An integral accumulates a distributed quantity: integrating force over displacement gives work, while integrating density over volume gives mass. Initial and boundary conditions connect a general law to a particular physical situation. An equation without those conditions may admit infinitely many solutions.

A vector carries both magnitude and direction. Components depend on the chosen coordinate basis; a physical vector does not. Dot products measure projections and work, while cross products express oriented area and moments. A component labelled radial or tangential may have a basis that changes with position; differentiating only its scalar magnitude then misses part of the motion.

A matrix represents a linear mapping after bases have been chosen. Stiffness, mass, damping, and coordinate transformations are examples. Solving $A\mathbf{x}=\mathbf{b}$ is fundamentally different from multiplying every component by a scalar. Singular matrices signal dependent constraints or unconstrained modes in many engineering models. Near-singularity can make an answer highly sensitive to small input errors even when an algorithm is implemented correctly.

Differential equations specify relationships involving derivatives. First-order storage systems describe tank levels, thermal capacitances, and simple electrical networks. Second-order systems describe masses and springs. Partial differential equations describe fields varying in both space and time. Linearity allows superposition: the response to a sum of inputs equals the sum of responses, provided initial/boundary conditions are handled consistently. Contact, large deformations, variable properties, and saturation often destroy that property.

Probability provides a language for uncertain outcomes. A probability model is a declared assumption about variation, not an automatic consequence of collecting numbers. The sample mean and spread summarize observations; inference requires attention to sampling, independence, and distribution. A fit to past data is not evidence that an extrapolation remains physically meaningful.

### Formula handbook

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

### Derivation

Consider a well-mixed body of mass $m$, constant specific heat $c$, exposed area $A$, and convection coefficient $h$. Assume uniform body temperature, fixed ambient temperature $T_\infty$, and no internal heat generation. Conservation of energy gives

$$
mc\frac{dT}{dt}=-hA(T-T_\infty).
$$

Define the excess temperature $\theta=T-T_\infty$ and time constant $\tau=mc/(hA)$. Separating variables gives $d\theta/\theta=-dt/\tau$. Integrating from time zero yields $\ln[\theta(t)/\theta(0)]=-t/\tau$, hence $\theta(t)=\theta(0)e^{-t/\tau}$. This solves the model, but the uniform-temperature assumption still requires a small internal-to-external thermal resistance ratio. A mathematically exact solution can describe a physically inappropriate model.

### Worked examples

#### Example 1: Thermal response

A hypothetical lumped body has $m=2\ \mathrm{kg}$, $c=500\ \mathrm{J/(kg\,K)}$, $h=25\ \mathrm{W/(m^2K)}$, and $A=0.2\ \mathrm{m^2}$. Initially it is at 80 °C in 20 °C air. The time constant is $\tau=2(500)/(25\cdot0.2)=200\ \mathrm{s}$. At 300 s, $T=20+60e^{-1.5}=33.388\ {}^\circ\mathrm C$. At one time constant, 36.8% of the initial excess temperature remains. This numerical example assumes lumped validity rather than establishing it from a geometry and conductivity.

#### Example 2: Coupled linear equations

Two algebraic force-balance equations in kN are $2x+y=5$ and $x+3y=5$, where $x,y$ are dimensionless load multipliers. The determinant is $2(3)-1=5$, so the solution is unique. Eliminate $x$: doubling the second equation and subtracting the first gives $5y=5$, so $y=1$ and $x=2$. Substitution gives $(5,5)$ exactly, a residual check that should accompany every matrix solve. A nonzero residual indicates numerical or transcription error, but a small residual alone does not imply small solution error for an ill-conditioned matrix.

### Exercises

1. For displacement $x(t)=3t^2-2t+1$ in metres with $t$ in seconds, find velocity and acceleration at 2 s.
2. Find the work by $F(x)=100+20x$ N over $0\leq x\leq2$ m, with the coefficient 20 in N/m.
3. Measurements are 9, 10, and 11 mm. Find mean, sample standard deviation, and estimated standard error of the mean assuming independence.

### Solutions

1. Differentiation gives $v=6t-2$ m/s and $a=6$ m/s². At 2 s, $v=10$ m/s and $a=6$ m/s². The polynomial coefficients carry the units required to make every term a length.
2. $W=\int_0^2(100+20x)\,dx=[100x+10x^2]_0^2=240$ J. Using only the final force would overestimate work.
3. $\bar x=10$ mm; $s=\sqrt{(1+0+1)/2}=1$ mm; $s/\sqrt3=0.577$ mm. A three-observation dataset gives a limited estimate of population variability.

### Common mistakes

Forgetting integration constants, mixing degrees and radians, discarding initial conditions in transforms, and treating a vector norm as a signed component are recurring problems. Never compute a matrix inverse merely to solve one linear system. Do not interpret a high coefficient of determination as proof of causation or as a valid extrapolation.

### Applications and limits

The main mathematical workflow is model, solve, substitute, and interpret. Check special cases such as zero forcing, long time, or vanishing coupling. They often reveal an incorrect sign sooner than a larger numerical calculation. Chapters on computational methods, FEA, CFD, and control introduce discretization and computational error separately from the mathematical model itself.

### Further reading

- [OpenStax Calculus Volume 1](https://openstax.org/details/books/calculus-volume-1), [Volume 2](https://openstax.org/details/books/calculus-volume-2), and [Volume 3](https://openstax.org/details/books/calculus-volume-3) — full publisher-hosted calculus texts.
- [MIT OCW 18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) — equations, transforms, systems, videos, and problem sets.


---

## 03 · Numerical methods and engineering computation

### Learning map

Use algebra, calculus, and basic programming to solve engineering equations that lack a convenient closed form. The central skills are selecting a stable algorithm, quantifying approximation error, and checking the output independently. This chapter prepares you for FEA, CFD, optimization, and time-domain simulation.

### Theory

A numerical answer contains several possible errors. Modelling error arises from idealizing the real system. Input error comes from uncertain geometry, loads, or material properties. Discretization error appears when continuous space or time is replaced by a finite representation. Iteration error remains when a nonlinear or linear solve is stopped early. Roundoff arises from finite-precision arithmetic. Refining a mesh attacks only some of these errors.

Root finding solves $f(x)=0$. Bracketing methods retain an interval containing a root when continuity and opposite endpoint signs hold. Newton's method uses a local tangent and can converge rapidly near a simple root, but it may leave the physical domain, encounter a nearly zero derivative, or converge to an unwanted root. A robust engineering solver combines bounds, residual checks, and physical constraints.

Numerical integration approximates an area from sampled values. The trapezoidal rule uses straight segments, while Simpson's rule integrates local quadratics. Neither can resolve a narrow peak that was never sampled. Numerical differentiation is particularly sensitive to noise because subtraction amplifies measurement and roundoff errors. Reducing the spacing indefinitely is not a reliable route to better derivatives.

Time integration propagates an initial state. Accuracy and stability are different. A method may be formally accurate as the time step tends to zero but become unstable at a practical step. A stiff system contains widely separated decay rates; an explicit method may need tiny steps for stability even when the slow behaviour is the quantity of interest. Implicit methods exchange a solve at each step for a larger stability region.

Verification asks whether the equations were solved correctly. Validation compares the model with appropriate observations of the physical system. Code running without an exception proves neither. Maintain units, input provenance, boundary conditions, convergence evidence, and checks of conserved quantities beside the final plot.

### Formula handbook

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

### Derivation

For the test equation $\dot y=-ay$, with $a>0$ in s⁻¹, explicit Euler gives $y_{n+1}=(1-ah)y_n$. Repetition gives $y_n=(1-ah)^ny_0$. The exact solution decays. To prevent discrete growth, require $|1-ah|\leq1$, or $0\leq ah\leq2$. Strict decay needs $0<ah<2$. Values between 1 and 2 create alternating signs, which may be mathematically stable but physically unacceptable for a nonnegative temperature excess or concentration. Backward Euler instead gives $y_{n+1}=y_n/(1+ah)$, which decays monotonically for any positive step, although a large step can still be inaccurate.

### Worked examples

#### Example 1: Newton's square root

Solve $x^2-2=0$ for the positive root starting at $x_0=1.5$. Newton gives $x_{k+1}=(x_k+2/x_k)/2$. The first two iterates are $x_1=1.416666667$ and $x_2=1.414215686$. The second residual is $x_2^2-2=6.0073\times10^{-6}$. A third iteration gives $x_3=1.414213562375$ with residual about $4.5\times10^{-12}$. Check both the residual and the positive physical domain; a residual alone would also accept the negative root.

#### Example 2: Cooling by Euler steps

Let $\dot\theta=-0.5\theta$, $\theta(0)=10$ K. With $h=0.2$ s, five explicit Euler steps reach 1 s: $\theta_5=10(0.9)^5=5.9049$ K. The exact value is $10e^{-0.5}=6.0653066$ K, so the absolute error is 0.1604066 K. Halving to 0.1 s gives $10(0.95)^{10}=5.9873694$ K and error 0.0779372 K. The error reduction factor is about 2.06, consistent with first-order convergence here. This experiment checks the integrator against an exact solution, not against a real cooling object.

### Exercises

1. Integrate $x^2$ from 0 to 2 with one Simpson panel using nodes 0, 1, 2.
2. How many bisection updates reduce an initial interval of length 1 to length at most $10^{-3}$?
3. For $\dot y=-100y$, identify the strict explicit-Euler decay bound and the non-oscillatory step bound.

### Solutions

1. $I=(1/3)(0+4\cdot1+4)=8/3$. Simpson is exact for this polynomial; that does not imply exactness for every function.
2. Require $2^{-n}\leq10^{-3}$, so $n\geq\log_2(1000)=9.966$ and choose 10 updates. The resulting interval length is $0.0009765625$.
3. Strict decay needs $0<h<0.02$ s. A nonnegative amplification factor additionally needs $h\leq0.01$ s. At 0.02 s the oscillation magnitude does not decay.

### Common mistakes

Using a step-change stopping rule without checking the residual can falsely report convergence. A coarse and fine solution can agree accidentally. A small residual in an ill-conditioned system may coexist with a large solution error. Do not apply high-order interpolation across discontinuities or fit noisy data with a high-degree polynomial merely because it passes through every sample.

### Applications and limits

Use analytical benchmarks before a complex simulation. Preserve at least three resolutions when estimating convergence order. Compare integrated mass, momentum, or energy with the expected balance. Report the discretization and solver settings with numerical results, because reproducibility depends on more than the final decimal value. The accompanying verification scripts intentionally use small problems whose expected answers can be checked independently.

### Further reading

- [Berkeley Python Numerical Methods, Newton–Raphson](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html) — textbook explanations and executable examples.
- [Georgia Tech numerical root-finding theory](https://aeresources.gatech.edu/num_meth/Webpage/Root_Finding/Theory/Theory.php) — engineering context for bracketing and open methods.
