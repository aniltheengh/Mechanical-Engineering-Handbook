# 02 · Engineering mathematics

## Learning map

Prerequisites are algebra, trigonometry, and consistent units. This chapter connects calculus, vectors, matrices, differential equations, transforms, and probability to mechanical models. It is a reference and bridge to full mathematics courses, not a replacement for a multisemester mathematics sequence. Use it alongside dynamics, heat transfer, vibrations, controls, and numerical methods.

## Theory

Engineering equations describe relationships between quantities and their changes. A derivative is a local rate: displacement differentiates to velocity and then acceleration. An integral accumulates a distributed quantity: integrating force over displacement gives work, while integrating density over volume gives mass. Initial and boundary conditions connect a general law to a particular physical situation. An equation without those conditions may admit infinitely many solutions.

A vector carries both magnitude and direction. Components depend on the chosen coordinate basis; a physical vector does not. Dot products measure projections and work, while cross products express oriented area and moments. A component labelled radial or tangential may have a basis that changes with position; differentiating only its scalar magnitude then misses part of the motion.

A matrix represents a linear mapping after bases have been chosen. Stiffness, mass, damping, and coordinate transformations are examples. Solving $A\mathbf{x}=\mathbf{b}$ is fundamentally different from multiplying every component by a scalar. Singular matrices signal dependent constraints or unconstrained modes in many engineering models. Near-singularity can make an answer highly sensitive to small input errors even when an algorithm is implemented correctly.

Differential equations specify relationships involving derivatives. First-order storage systems describe tank levels, thermal capacitances, and simple electrical networks. Second-order systems describe masses and springs. Partial differential equations describe fields varying in both space and time. Linearity allows superposition: the response to a sum of inputs equals the sum of responses, provided initial/boundary conditions are handled consistently. Contact, large deformations, variable properties, and saturation often destroy that property.

Probability provides a language for uncertain outcomes. A probability model is a declared assumption about variation, not an automatic consequence of collecting numbers. The sample mean and spread summarize observations; inference requires attention to sampling, independence, and distribution. A fit to past data is not evidence that an extrapolation remains physically meaningful.

## Formula handbook

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

## Derivation

Consider a well-mixed body of mass $m$, constant specific heat $c$, exposed area $A$, and convection coefficient $h$. Assume uniform body temperature, fixed ambient temperature $T_\infty$, and no internal heat generation. Conservation of energy gives

$$
mc\frac{dT}{dt}=-hA(T-T_\infty).
$$

Define the excess temperature $\theta=T-T_\infty$ and time constant $\tau=mc/(hA)$. Separating variables gives $d\theta/\theta=-dt/\tau$. Integrating from time zero yields $\ln[\theta(t)/\theta(0)]=-t/\tau$, hence $\theta(t)=\theta(0)e^{-t/\tau}$. This solves the model, but the uniform-temperature assumption still requires a small internal-to-external thermal resistance ratio. A mathematically exact solution can describe a physically inappropriate model.

## Worked examples

### Example 1: Thermal response

A hypothetical lumped body has $m=2\ \mathrm{kg}$, $c=500\ \mathrm{J/(kg\,K)}$, $h=25\ \mathrm{W/(m^2K)}$, and $A=0.2\ \mathrm{m^2}$. Initially it is at 80 °C in 20 °C air. The time constant is $\tau=2(500)/(25\cdot0.2)=200\ \mathrm{s}$. At 300 s, $T=20+60e^{-1.5}=33.388\ {}^\circ\mathrm C$. At one time constant, 36.8% of the initial excess temperature remains. This numerical example assumes lumped validity rather than establishing it from a geometry and conductivity.

### Example 2: Coupled linear equations

Two algebraic force-balance equations in kN are $2x+y=5$ and $x+3y=5$, where $x,y$ are dimensionless load multipliers. The determinant is $2(3)-1=5$, so the solution is unique. Eliminate $x$: doubling the second equation and subtracting the first gives $5y=5$, so $y=1$ and $x=2$. Substitution gives $(5,5)$ exactly, a residual check that should accompany every matrix solve. A nonzero residual indicates numerical or transcription error, but a small residual alone does not imply small solution error for an ill-conditioned matrix.

## Exercises

1. For displacement $x(t)=3t^2-2t+1$ in metres with $t$ in seconds, find velocity and acceleration at 2 s.
2. Find the work by $F(x)=100+20x$ N over $0\leq x\leq2$ m, with the coefficient 20 in N/m.
3. Measurements are 9, 10, and 11 mm. Find mean, sample standard deviation, and estimated standard error of the mean assuming independence.

## Solutions

1. Differentiation gives $v=6t-2$ m/s and $a=6$ m/s². At 2 s, $v=10$ m/s and $a=6$ m/s². The polynomial coefficients carry the units required to make every term a length.
2. $W=\int_0^2(100+20x)\,dx=[100x+10x^2]_0^2=240$ J. Using only the final force would overestimate work.
3. $\bar x=10$ mm; $s=\sqrt{(1+0+1)/2}=1$ mm; $s/\sqrt3=0.577$ mm. A three-observation dataset gives a limited estimate of population variability.

## Common mistakes

Forgetting integration constants, mixing degrees and radians, discarding initial conditions in transforms, and treating a vector norm as a signed component are recurring problems. Never compute a matrix inverse merely to solve one linear system. Do not interpret a high coefficient of determination as proof of causation or as a valid extrapolation.

## Applications and limits

The main mathematical workflow is model, solve, substitute, and interpret. Check special cases such as zero forcing, long time, or vanishing coupling. They often reveal an incorrect sign sooner than a larger numerical calculation. Chapters on computational methods, FEA, CFD, and control introduce discretization and computational error separately from the mathematical model itself.

## Further reading

- [OpenStax Calculus Volume 1](https://openstax.org/details/books/calculus-volume-1), [Volume 2](https://openstax.org/details/books/calculus-volume-2), and [Volume 3](https://openstax.org/details/books/calculus-volume-3) — full publisher-hosted calculus texts.
- [MIT OCW 18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) — equations, transforms, systems, videos, and problem sets.
