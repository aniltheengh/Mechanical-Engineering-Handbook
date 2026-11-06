# Computational engineering and optimization

Mechanical Engineering Handbook · First edition · 2026-11-06

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [24. Finite Element Analysis](../chapters/24-finite-element-analysis.md)
- [25. Computational Fluid Dynamics](../chapters/25-computational-fluid-dynamics.md)
- [30. Engineering Design and Optimization](../chapters/30-design-and-optimization.md)

---

## 24. Finite Element Analysis

### Learning map

Prerequisites: statics, strength of materials, calculus, matrices, and numerical linear algebra. The objective is to convert a physical boundary-value problem into an approximate algebraic system, then judge whether its answer is useful. Begin with an axial bar before studying beams, plates, shells, solids, heat conduction, or coupled fields. A colorful stress plot is an output of assumptions; it is not independent evidence that those assumptions describe a real part.

### Theory

A continuum has displacement at every material point. Finite element analysis replaces that infinite set by a finite collection of nodal unknowns. Shape functions interpolate between nodes, and an integral statement of equilibrium determines the nodal values. The mesh therefore approximates both geometry and the possible displacement fields. A finer mesh expands the space of admissible solutions but cannot correct the wrong material law, load, contact definition, or support.

For small-displacement linear elasticity, strain is linear in displacement gradients and stress is linear in strain. The stiffness matrix is constant, and load cases can be superposed. Plasticity, large rotations, changing contact, and stress stiffening break one or more of these assumptions. Nonlinear analysis then solves equilibrium incrementally and iteratively. Each load step needs convergence; convergence of the nonlinear iterations does not establish convergence with mesh size.

Essential boundary conditions prescribe displacement. Natural boundary conditions prescribe traction. A model without sufficient displacement constraints contains rigid-body modes and has a singular stiffness matrix. Excessive restraint can be equally misleading by creating fictitious reactions. Support a model according to the actual load path, allowing physically possible sliding, rotation, and thermal expansion.

Element choice matters. Truss elements carry axial force, beam elements represent section bending, shell elements represent thin surfaces, and solid elements resolve three-dimensional fields. A thin component meshed with poorly shaped low-order solids may be excessively stiff. Nearly incompressible materials can exhibit volumetric locking. Element formulations and integration schemes should be chosen for the deformation mode, not merely for meshing convenience.

### Formula handbook

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

### Derivation

For a uniform bar, substitute $u=N_1d_1+N_2d_2$ into $U=\frac12\int_0^L EA(du/dx)^2dx$. The derivative is constant, $(d_2-d_1)/L$, so $U=EA(d_2-d_1)^2/(2L)$. Differentiate total potential energy with respect to each free displacement. Setting each derivative to zero gives nodal equilibrium and the stiffness matrix above. With node 1 fixed and force $P$ at node 2, the remaining equation is $(EA/L)d_2=P$. Thus a single linear element gives the exact endpoint displacement for this particular uniform, end-loaded bar because the exact displacement is itself linear. It does not follow that one element is sufficient for a varying cross-section or distributed loading.

### Worked examples

**Example 1 — axial element.** A steel bar has $E=200\ \mathrm{GPa}$, $A=200\ \mathrm{mm^2}=2\times10^{-4}\ \mathrm{m^2}$, $L=1\ \mathrm m$, and $P=10\ \mathrm{kN}$. Its stiffness is $EA/L=40\ \mathrm{MN/m}$. Therefore $d_2=10000/(40\times10^6)=0.00025\ \mathrm m=0.250\ \mathrm{mm}$. Stress is $50.0\ \mathrm{MPa}$ and strain energy is $Pd_2/2=1.25\ \mathrm J$. The fixed-end reaction is $-10\ \mathrm{kN}$, balancing the applied force. A computed result should reproduce all four quantities.

**Example 2 — two elements in series.** Two bars each have $L=0.5\ \mathrm m$ and $E=200\ \mathrm{GPa}$. Their areas are $100$ and $200\ \mathrm{mm^2}$. A $5\ \mathrm{kN}$ load passes through both. The first extension is $0.125\ \mathrm{mm}$; the second is $0.0625\ \mathrm{mm}$. Consequently the middle-node displacement is $0.125\ \mathrm{mm}$ and the free end moves $0.1875\ \mathrm{mm}$. Stresses are $50$ and $25\ \mathrm{MPa}$. The same internal force in both bars follows from equilibrium, not from equal strain.

### Exercises

1. Double the cross-sectional area in Example 1. Find displacement and stress.
2. A model predicts tip displacements $1.20$, $1.10$, and $1.075\ \mathrm{mm}$ on successive meshes. Find the last relative change. Does it prove experimental accuracy?
3. An unconstrained three-dimensional solid model is subjected to a balanced force pair. Explain why its static stiffness matrix can remain singular.

### Solutions

1. Stiffness doubles. Displacement becomes $0.125\ \mathrm{mm}$ and stress becomes $25\ \mathrm{MPa}$, provided the load stays constant.
2. The last relative change is $0.025/1.075=0.02326$, or $2.33\%$. This only measures change under refinement. Material, geometry, and boundary-condition errors still require separate assessment.
3. Balanced loading does not remove the six rigid-body freedoms of a free three-dimensional body. The solution is not unique until a reference frame or physically appropriate constraints are supplied.

### Common mistakes

- Reading a stress maximum at a sharp re-entrant corner as a converged physical stress. A mathematical singularity can increase with refinement.
- Comparing nodally averaged stresses with element integration-point stresses without noting the difference.
- Treating a low equation residual as evidence of correct physics.
- Mixing millimetres and metres when entering modulus, density, and force.

### Applications and limits

Use analytical benchmarks, reaction balance, energy balance, deformation shape, and mesh refinement together. Record the quantity of interest before solving: deflection, fatigue stress range, natural frequency, contact pressure, or heat flow may need different meshes. For a weld toe or notch, a stress assessment procedure must define geometry and stress extraction consistently. A handbook example is not a fabrication or structural certification calculation. MIT's course provides a broader treatment of element formulations and nonlinear analysis; NASA's modeling handbook supplies a framework for simulation credibility, distinct from the original elementary derivation here.

### Further reading

- [MIT OpenCourseWare — Finite Element Analysis of Solids and Fluids I](https://ocw.mit.edu/courses/2-092-finite-element-analysis-of-solids-and-fluids-i-fall-2009/): lectures, problems, and solutions.
- [NASA Handbook 7009A — modeling and simulation implementation](https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/nasa-hdbk-7009a.pdf): verification, validation, and credibility context; check current project requirements separately.


---

## 25. Computational Fluid Dynamics

### Learning map

Prerequisites: fluid mechanics, heat transfer, differential equations, numerical methods, and linear algebra. Learn conservation in a single control volume, then connect many volumes. The learning target is to understand what a CFD solver approximates, which numerical choices affect the result, and how to check an engineering quantity such as pressure loss. The equations below emphasize incompressible Newtonian flow; compressible reacting and multiphase flows require additional models.

### Theory

CFD discretizes mass, momentum, energy, and sometimes species transport. In a finite-volume method, each cell is a small control volume. Face fluxes connect neighboring cells. A properly assembled interior face contributes equal and opposite flux to the two adjacent cells, so local conservation survives assembly. Finite-difference methods instead approximate derivatives at points, while finite-element methods use an integral residual statement and basis functions.

Diffusion smooths gradients. Advection transports information with the flow and requires particular attention to direction and boundedness. First-order upwind schemes are robust for many simple transport problems but smear sharp fronts. Central interpolation can be more accurate in smooth regions yet can produce oscillations for advection-dominated problems. Higher order is useful only when the mesh and solution are suitable.

In incompressible flow, pressure enforces continuity rather than coming from an ideal-gas equation of state. Velocity and pressure must be coupled so that momentum and continuity are both satisfied. Boundary conditions also require consistency: a sealed fixed-volume domain cannot have an unbalanced imposed inflow without some other physical accommodation.

Turbulent motion contains many interacting scales. Direct numerical simulation resolves them, which can be extremely costly. Reynolds-averaged models predict mean quantities and introduce closure assumptions for turbulent transport; large-eddy simulation resolves larger scales and models smaller ones. Selecting a turbulence model does not remove the need to check inlet turbulence, near-wall treatment, separation, and applicability to the actual flow.

Verification asks whether the equations are implemented and solved with adequate numerical accuracy. Validation asks whether the chosen physical model matches appropriate measured reality. NASA's tutorial explicitly separates iterative, spatial, and temporal convergence. A calculation with tiny residuals can still be far from the physical answer if its model or boundary data are unsuitable.

### Formula handbook

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

### Derivation

Integrate a conservation law over one fixed cell. The divergence theorem converts the volume integral of flux divergence into a boundary surface integral. Approximate each face integral by a face flux times its area. The resulting equation states that accumulation equals inflow minus outflow plus internal generation. Shared-face fluxes cancel when the cell equations are summed, explaining global conservation. Accuracy now depends on how face variables and gradients are reconstructed and how the time derivative is advanced.

For the diffusion update, rearrange as $\phi_i^{n+1}=(1-2Fo)\phi_i^n+Fo\phi_{i+1}^n+Fo\phi_{i-1}^n$. When $0\le Fo\le1/2$, all weights are nonnegative and sum to one. The new value lies between neighboring old values. This supplies an intuitive boundedness explanation for this specific stability restriction.

### Worked examples

**Example 1 — explicit diffusion time step.** A one-dimensional thermal model uses $\alpha=10^{-5}\ \mathrm{m^2/s}$ and $\Delta x=0.002\ \mathrm m$. The limit is $\Delta t\le\Delta x^2/(2\alpha)=0.20\ \mathrm s$. Choose $\Delta t=0.10\ \mathrm s$, giving $Fo=0.25$. With neighboring temperatures $100$, $0$, and $0\ ^\circ\mathrm C$, the central temperature after one step is $0+0.25(0-0+100)=25\ ^\circ\mathrm C$. Temperature differences may use Celsius because the offset cancels.

**Example 2 — observed grid order.** A pressure drop is $104$, $101$, and $100.25\ \mathrm{Pa}$ on grids of spacing $4h$, $2h$, and $h$. The ratio of differences is $3/0.75=4$. Thus $p_{\rm obs}=\ln4/\ln2=2$ and $q_{\rm ext}=100.25+(100.25-101)/3=100.00\ \mathrm{Pa}$. Estimated finest-grid error relative to the extrapolate is $0.25\%$. This is a numerical estimate under the assumed error model, not a measurement uncertainty or proof that the flow model is correct.

### Exercises

1. For $u=2\ \mathrm{m/s}$ and $\Delta x=0.01\ \mathrm m$, find the maximum time step for the stated explicit upwind scheme.
2. If the diffusion grid spacing is halved, how does the permissible explicit time step change?
3. A steady model has $2.00\ \mathrm{kg/s}$ inflow and $1.98\ \mathrm{kg/s}$ outflow. Find the imbalance relative to inlet flow and explain the issue.

### Solutions

1. $\Delta t\le\Delta x/u=0.005\ \mathrm s$. Other coupled equations may impose a stricter condition.
2. The limit depends on $\Delta x^2$, so it becomes one quarter as large.
3. The imbalance is $(2.00-1.98)/2.00=1\%$. A steady source-free mass balance should close; inspect convergence, integrated boundary fluxes, and definitions before accepting pressure or heat-transfer predictions.

### Common mistakes

- Applying a one-dimensional explicit stability formula to every solver.
- Refining a mesh while changing geometry or boundary conditions, then calling the result a clean mesh study.
- Comparing turbulence results without checking wall resolution and wall-model requirements.
- Reporting many digits from uncertain inlet data or an unresolved separated flow.

### Applications and limits

Useful applications include duct pressure loss, cooling, mixing, aerodynamic loads, and pump flow paths. Start with a benchmark such as fully developed laminar pipe flow or conduction through a slab. Monitor the engineering output as well as residuals and conservation. Transient flows need time-step refinement and sufficient sampling duration. The formulas here explain elementary schemes; they are not a replacement for the numerical and modeling documentation of a specific solver.

### Further reading

- [MIT OpenCourseWare — Numerical Fluid Mechanics](https://ocw.mit.edu/courses/2-29-numerical-fluid-mechanics-spring-2015/): numerical methods, notes, and assignments.
- [NASA — CFD verification and validation tutorial](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html): separate convergence and validation tasks.
- [NASA — spatial grid convergence](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html): Richardson extrapolation and convergence assessment.


---

## 30. Engineering Design and Optimization

### Learning map

Prerequisites: mechanics, materials, calculus, probability, and numerical methods. Design begins by defining a need and measurable requirements. Optimization selects decision variables to improve a stated objective while satisfying constraints. Learn to formulate a small problem and check its result manually before using a numerical optimizer. A mathematical optimum is only as useful as its objectives, constraints, and physical model.

### Theory

A design variable is something the designer may choose: a diameter, wall thickness, material, operating speed, or control gain. A parameter is an input treated as fixed during a particular optimization, such as required load or available envelope. A response is an output predicted from a candidate design, such as stress, cost, deflection, efficiency, or reliability. Confusing these roles can create a problem that is mathematically solvable but physically meaningless.

Constraints define feasibility. Equality constraints describe exact relationships, such as a required enclosed volume. Inequality constraints express limits, such as stress below an allowable value or mass below a budget. An active constraint is met at equality at the candidate optimum. Inactive constraints have remaining margin. Many efficient engineering designs sit at one or more active constraints, but manufacturing tolerances and uncertain loading may require intentional margin.

An objective function gives the optimization direction. Mass, cost, energy use, noise, and reliability often conflict. Combining them into a weighted sum requires explicit scales and value judgments. A Pareto-optimal design cannot improve one objective without worsening another, within the stated feasible set. There may be many such designs; choosing among them needs engineering and stakeholder judgment.

Optimization algorithms differ. Gradient methods use local derivative information and are efficient for smooth problems but may find a local solution. Enumeration and mixed-integer methods handle discrete choices. Heuristic searches may explore complicated spaces but do not automatically prove global optimality. Always test sensitivity, starting points, constraints, and the physical plausibility of the final design.

Robust design considers uncertain inputs and manufacturing variation. An optimum that works only at one exact parameter value may be inferior to a slightly heavier or more expensive design with dependable performance. Verification checks that the mathematical model and implementation are correct; prototype testing and measurements examine whether it represents the physical design adequately.

### Formula handbook

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

### Derivation

Consider a closed cylindrical container with fixed internal volume $V$ and negligible wall thickness for the geometry model. Surface area is $A_s=2\pi r^2+2\pi rh$, while $V=\pi r^2h$. Eliminate height to obtain $A_s(r)=2\pi r^2+2V/r$. Differentiation gives $dA_s/dr=4\pi r-2V/r^2$. Stationarity requires $r^3=V/(2\pi)$, so $h=V/(\pi r^2)=2r$. The second derivative is $4\pi+4V/r^3>0$ for positive radius. The stationary point is the unique minimum because area diverges as radius approaches zero or infinity. This is a geometric optimum; real pressure vessels require wall thickness, head geometry, supports, fabrication constraints, and code requirements that can change it substantially.

### Worked examples

**Example 1 — minimum-mass tension bar.** A steel tie has $L=2\ \mathrm m$, $P=30\ \mathrm{kN}$, $E=200\ \mathrm{GPa}$, and $\rho=7850\ \mathrm{kg/m^3}$. Limit stress to $150\ \mathrm{MPa}$ and extension to $0.5\ \mathrm{mm}$. Stress requires $A\ge30000/(150\times10^6)=200\ \mathrm{mm^2}$. Stiffness requires $A\ge30000(2)/(200\times10^9\times0.0005)=600\ \mathrm{mm^2}$. Since mass grows linearly with area, the continuous optimum is $A=600\ \mathrm{mm^2}$. Its mass is $9.42\ \mathrm{kg}$, stress $50\ \mathrm{MPa}$, and extension $0.5\ \mathrm{mm}$. Stiffness is active; strength is not. Connections, buckling under load reversal, and discrete available sections require additional constraints.

**Example 2 — minimum-area container.** Take $V=2\pi\times10^{-3}\ \mathrm{m^3}=6.283185\ \mathrm L$. From the derivation, $r=(V/(2\pi))^{1/3}=0.10\ \mathrm m$ and $h=0.20\ \mathrm m$. Surface area is $2\pi(0.10)^2+2\pi(0.10)(0.20)=0.188496\ \mathrm{m^2}$. At radius $0.08\ \mathrm m$, equal volume requires height $0.3125\ \mathrm m$ and area $0.197292\ \mathrm{m^2}$, which is larger. The comparison checks the direction of the stationary-point result.

### Exercises

1. If Example 1's extension limit becomes $1.0\ \mathrm{mm}$, determine the optimal continuous area and mass.
2. For $f(x)=x^2$ at $x=3$, calculate the central derivative using step $0.1$ and compare with the exact derivative.
3. Explain why minimizing mass with only a stress constraint can produce an unusable long slender compression member.

### Solutions

1. Stiffness now requires $300\ \mathrm{mm^2}$, still above the $200\ \mathrm{mm^2}$ stress bound. Mass becomes $7850(0.0003)(2)=4.71\ \mathrm{kg}$.
2. $[(3.1)^2-(2.9)^2]/0.2=(9.61-8.41)/0.2=6$, exactly equal to $2x$ here. Central difference is exact for this quadratic derivative in exact arithmetic.
3. Buckling can occur well below material yield. The missing stability constraint must include length, section stiffness, end restraint, imperfections, and the appropriate design method.

### Common mistakes

- Optimizing an unscaled mixture of metres, pascals, and currency without checking numerical conditioning.
- Reporting more precision than available manufacturing tolerances support.
- Treating optimizer success status as proof that all physical constraints were included.
- Comparing objectives with different functional requirements.
- Ignoring discrete sizes, minimum features, assembly, maintenance, and inspection access.

### Applications and limits

Optimization is useful for beam sizing, thermal systems, link geometry, machine layout, and operating strategy. Save the assumptions, bounds, objective definitions, and constraint margins with each result. Re-evaluate the chosen design with a separate calculation and, when appropriate, a higher-fidelity model or test. This chapter establishes formulation and small analytical examples; global, stochastic, topology, and multidisciplinary optimization need deeper study.

### Further reading

- [MIT OpenCourseWare — Multidisciplinary System Design Optimization](https://ocw.mit.edu/courses/ids-338j-multidisciplinary-system-design-optimization-spring-2010/): formulation, trade studies, and optimization methods.
- [NASA Handbook 7009A](https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/nasa-hdbk-7009a.pdf): model credibility and verification context.
