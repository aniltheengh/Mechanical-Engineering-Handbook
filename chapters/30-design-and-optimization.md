# 30. Engineering Design and Optimization

## Learning map

Prerequisites: mechanics, materials, calculus, probability, and numerical methods. Design begins by defining a need and measurable requirements. Optimization selects decision variables to improve a stated objective while satisfying constraints. Learn to formulate a small problem and check its result manually before using a numerical optimizer. A mathematical optimum is only as useful as its objectives, constraints, and physical model.

## Theory

A design variable is something the designer may choose: a diameter, wall thickness, material, operating speed, or control gain. A parameter is an input treated as fixed during a particular optimization, such as required load or available envelope. A response is an output predicted from a candidate design, such as stress, cost, deflection, efficiency, or reliability. Confusing these roles can create a problem that is mathematically solvable but physically meaningless.

Constraints define feasibility. Equality constraints describe exact relationships, such as a required enclosed volume. Inequality constraints express limits, such as stress below an allowable value or mass below a budget. An active constraint is met at equality at the candidate optimum. Inactive constraints have remaining margin. Many efficient engineering designs sit at one or more active constraints, but manufacturing tolerances and uncertain loading may require intentional margin.

An objective function gives the optimization direction. Mass, cost, energy use, noise, and reliability often conflict. Combining them into a weighted sum requires explicit scales and value judgments. A Pareto-optimal design cannot improve one objective without worsening another, within the stated feasible set. There may be many such designs; choosing among them needs engineering and stakeholder judgment.

Optimization algorithms differ. Gradient methods use local derivative information and are efficient for smooth problems but may find a local solution. Enumeration and mixed-integer methods handle discrete choices. Heuristic searches may explore complicated spaces but do not automatically prove global optimality. Always test sensitivity, starting points, constraints, and the physical plausibility of the final design.

Robust design considers uncertain inputs and manufacturing variation. An optimum that works only at one exact parameter value may be inferior to a slightly heavier or more expensive design with dependable performance. Verification checks that the mathematical model and implementation are correct; prototype testing and measurements examine whether it represents the physical design adequately.

## Formula handbook

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

## Derivation

Consider a closed cylindrical container with fixed internal volume $V$ and negligible wall thickness for the geometry model. Surface area is $A_s=2\pi r^2+2\pi rh$, while $V=\pi r^2h$. Eliminate height to obtain $A_s(r)=2\pi r^2+2V/r$. Differentiation gives $dA_s/dr=4\pi r-2V/r^2$. Stationarity requires $r^3=V/(2\pi)$, so $h=V/(\pi r^2)=2r$. The second derivative is $4\pi+4V/r^3>0$ for positive radius. The stationary point is the unique minimum because area diverges as radius approaches zero or infinity. This is a geometric optimum; real pressure vessels require wall thickness, head geometry, supports, fabrication constraints, and code requirements that can change it substantially.

## Worked examples

**Example 1 — minimum-mass tension bar.** A steel tie has $L=2\ \mathrm m$, $P=30\ \mathrm{kN}$, $E=200\ \mathrm{GPa}$, and $\rho=7850\ \mathrm{kg/m^3}$. Limit stress to $150\ \mathrm{MPa}$ and extension to $0.5\ \mathrm{mm}$. Stress requires $A\ge30000/(150\times10^6)=200\ \mathrm{mm^2}$. Stiffness requires $A\ge30000(2)/(200\times10^9\times0.0005)=600\ \mathrm{mm^2}$. Since mass grows linearly with area, the continuous optimum is $A=600\ \mathrm{mm^2}$. Its mass is $9.42\ \mathrm{kg}$, stress $50\ \mathrm{MPa}$, and extension $0.5\ \mathrm{mm}$. Stiffness is active; strength is not. Connections, buckling under load reversal, and discrete available sections require additional constraints.

**Example 2 — minimum-area container.** Take $V=2\pi\times10^{-3}\ \mathrm{m^3}=6.283185\ \mathrm L$. From the derivation, $r=(V/(2\pi))^{1/3}=0.10\ \mathrm m$ and $h=0.20\ \mathrm m$. Surface area is $2\pi(0.10)^2+2\pi(0.10)(0.20)=0.188496\ \mathrm{m^2}$. At radius $0.08\ \mathrm m$, equal volume requires height $0.3125\ \mathrm m$ and area $0.197292\ \mathrm{m^2}$, which is larger. The comparison checks the direction of the stationary-point result.

## Exercises

1. If Example 1's extension limit becomes $1.0\ \mathrm{mm}$, determine the optimal continuous area and mass.
2. For $f(x)=x^2$ at $x=3$, calculate the central derivative using step $0.1$ and compare with the exact derivative.
3. Explain why minimizing mass with only a stress constraint can produce an unusable long slender compression member.

## Solutions

1. Stiffness now requires $300\ \mathrm{mm^2}$, still above the $200\ \mathrm{mm^2}$ stress bound. Mass becomes $7850(0.0003)(2)=4.71\ \mathrm{kg}$.
2. $[(3.1)^2-(2.9)^2]/0.2=(9.61-8.41)/0.2=6$, exactly equal to $2x$ here. Central difference is exact for this quadratic derivative in exact arithmetic.
3. Buckling can occur well below material yield. The missing stability constraint must include length, section stiffness, end restraint, imperfections, and the appropriate design method.

## Common mistakes

- Optimizing an unscaled mixture of metres, pascals, and currency without checking numerical conditioning.
- Reporting more precision than available manufacturing tolerances support.
- Treating optimizer success status as proof that all physical constraints were included.
- Comparing objectives with different functional requirements.
- Ignoring discrete sizes, minimum features, assembly, maintenance, and inspection access.

## Applications and limits

Optimization is useful for beam sizing, thermal systems, link geometry, machine layout, and operating strategy. Save the assumptions, bounds, objective definitions, and constraint margins with each result. Re-evaluate the chosen design with a separate calculation and, when appropriate, a higher-fidelity model or test. This chapter establishes formulation and small analytical examples; global, stochastic, topology, and multidisciplinary optimization need deeper study.

## Further reading

- [MIT OpenCourseWare — Multidisciplinary System Design Optimization](https://ocw.mit.edu/courses/ids-338j-multidisciplinary-system-design-optimization-spring-2010/): formulation, trade studies, and optimization methods.
- [NASA Handbook 7009A](https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/nasa-hdbk-7009a.pdf): model credibility and verification context.
