# 03 · Numerical methods and engineering computation

## Learning map

Use algebra, calculus, and basic programming to solve engineering equations that lack a convenient closed form. The central skills are selecting a stable algorithm, quantifying approximation error, and checking the output independently. This chapter prepares you for FEA, CFD, optimization, and time-domain simulation.

## Theory

A numerical answer contains several possible errors. Modelling error arises from idealizing the real system. Input error comes from uncertain geometry, loads, or material properties. Discretization error appears when continuous space or time is replaced by a finite representation. Iteration error remains when a nonlinear or linear solve is stopped early. Roundoff arises from finite-precision arithmetic. Refining a mesh attacks only some of these errors.

Root finding solves $f(x)=0$. Bracketing methods retain an interval containing a root when continuity and opposite endpoint signs hold. Newton's method uses a local tangent and can converge rapidly near a simple root, but it may leave the physical domain, encounter a nearly zero derivative, or converge to an unwanted root. A robust engineering solver combines bounds, residual checks, and physical constraints.

Numerical integration approximates an area from sampled values. The trapezoidal rule uses straight segments, while Simpson's rule integrates local quadratics. Neither can resolve a narrow peak that was never sampled. Numerical differentiation is particularly sensitive to noise because subtraction amplifies measurement and roundoff errors. Reducing the spacing indefinitely is not a reliable route to better derivatives.

Time integration propagates an initial state. Accuracy and stability are different. A method may be formally accurate as the time step tends to zero but become unstable at a practical step. A stiff system contains widely separated decay rates; an explicit method may need tiny steps for stability even when the slow behaviour is the quantity of interest. Implicit methods exchange a solve at each step for a larger stability region.

Verification asks whether the equations were solved correctly. Validation compares the model with appropriate observations of the physical system. Code running without an exception proves neither. Maintain units, input provenance, boundary conditions, convergence evidence, and checks of conserved quantities beside the final plot.

## Formula handbook

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

## Derivation

For the test equation $\dot y=-ay$, with $a>0$ in s⁻¹, explicit Euler gives $y_{n+1}=(1-ah)y_n$. Repetition gives $y_n=(1-ah)^ny_0$. The exact solution decays. To prevent discrete growth, require $|1-ah|\leq1$, or $0\leq ah\leq2$. Strict decay needs $0<ah<2$. Values between 1 and 2 create alternating signs, which may be mathematically stable but physically unacceptable for a nonnegative temperature excess or concentration. Backward Euler instead gives $y_{n+1}=y_n/(1+ah)$, which decays monotonically for any positive step, although a large step can still be inaccurate.

## Worked examples

### Example 1: Newton's square root

Solve $x^2-2=0$ for the positive root starting at $x_0=1.5$. Newton gives $x_{k+1}=(x_k+2/x_k)/2$. The first two iterates are $x_1=1.416666667$ and $x_2=1.414215686$. The second residual is $x_2^2-2=6.0073\times10^{-6}$. A third iteration gives $x_3=1.414213562375$ with residual about $4.5\times10^{-12}$. Check both the residual and the positive physical domain; a residual alone would also accept the negative root.

### Example 2: Cooling by Euler steps

Let $\dot\theta=-0.5\theta$, $\theta(0)=10$ K. With $h=0.2$ s, five explicit Euler steps reach 1 s: $\theta_5=10(0.9)^5=5.9049$ K. The exact value is $10e^{-0.5}=6.0653066$ K, so the absolute error is 0.1604066 K. Halving to 0.1 s gives $10(0.95)^{10}=5.9873694$ K and error 0.0779372 K. The error reduction factor is about 2.06, consistent with first-order convergence here. This experiment checks the integrator against an exact solution, not against a real cooling object.

## Exercises

1. Integrate $x^2$ from 0 to 2 with one Simpson panel using nodes 0, 1, 2.
2. How many bisection updates reduce an initial interval of length 1 to length at most $10^{-3}$?
3. For $\dot y=-100y$, identify the strict explicit-Euler decay bound and the non-oscillatory step bound.

## Solutions

1. $I=(1/3)(0+4\cdot1+4)=8/3$. Simpson is exact for this polynomial; that does not imply exactness for every function.
2. Require $2^{-n}\leq10^{-3}$, so $n\geq\log_2(1000)=9.966$ and choose 10 updates. The resulting interval length is $0.0009765625$.
3. Strict decay needs $0<h<0.02$ s. A nonnegative amplification factor additionally needs $h\leq0.01$ s. At 0.02 s the oscillation magnitude does not decay.

## Common mistakes

Using a step-change stopping rule without checking the residual can falsely report convergence. A coarse and fine solution can agree accidentally. A small residual in an ill-conditioned system may coexist with a large solution error. Do not apply high-order interpolation across discontinuities or fit noisy data with a high-degree polynomial merely because it passes through every sample.

## Applications and limits

Use analytical benchmarks before a complex simulation. Preserve at least three resolutions when estimating convergence order. Compare integrated mass, momentum, or energy with the expected balance. Report the discretization and solver settings with numerical results, because reproducibility depends on more than the final decimal value. The accompanying verification scripts intentionally use small problems whose expected answers can be checked independently.

## Further reading

- [Berkeley Python Numerical Methods, Newton–Raphson](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html) — textbook explanations and executable examples.
- [Georgia Tech numerical root-finding theory](https://aeresources.gatech.edu/num_meth/Webpage/Root_Finding/Theory/Theory.php) — engineering context for bracketing and open methods.
