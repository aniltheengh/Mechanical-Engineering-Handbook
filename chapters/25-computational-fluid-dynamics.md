# 25. Computational Fluid Dynamics

## Learning map

Prerequisites: fluid mechanics, heat transfer, differential equations, numerical methods, and linear algebra. Learn conservation in a single control volume, then connect many volumes. The learning target is to understand what a CFD solver approximates, which numerical choices affect the result, and how to check an engineering quantity such as pressure loss. The equations below emphasize incompressible Newtonian flow; compressible reacting and multiphase flows require additional models.

## Theory

CFD discretizes mass, momentum, energy, and sometimes species transport. In a finite-volume method, each cell is a small control volume. Face fluxes connect neighboring cells. A properly assembled interior face contributes equal and opposite flux to the two adjacent cells, so local conservation survives assembly. Finite-difference methods instead approximate derivatives at points, while finite-element methods use an integral residual statement and basis functions.

Diffusion smooths gradients. Advection transports information with the flow and requires particular attention to direction and boundedness. First-order upwind schemes are robust for many simple transport problems but smear sharp fronts. Central interpolation can be more accurate in smooth regions yet can produce oscillations for advection-dominated problems. Higher order is useful only when the mesh and solution are suitable.

In incompressible flow, pressure enforces continuity rather than coming from an ideal-gas equation of state. Velocity and pressure must be coupled so that momentum and continuity are both satisfied. Boundary conditions also require consistency: a sealed fixed-volume domain cannot have an unbalanced imposed inflow without some other physical accommodation.

Turbulent motion contains many interacting scales. Direct numerical simulation resolves them, which can be extremely costly. Reynolds-averaged models predict mean quantities and introduce closure assumptions for turbulent transport; large-eddy simulation resolves larger scales and models smaller ones. Selecting a turbulence model does not remove the need to check inlet turbulence, near-wall treatment, separation, and applicability to the actual flow.

Verification asks whether the equations are implemented and solved with adequate numerical accuracy. Validation asks whether the chosen physical model matches appropriate measured reality. NASA's tutorial explicitly separates iterative, spatial, and temporal convergence. A calculation with tiny residuals can still be far from the physical answer if its model or boundary data are unsuitable.

## Formula handbook

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

## Derivation

Integrate a conservation law over one fixed cell. The divergence theorem converts the volume integral of flux divergence into a boundary surface integral. Approximate each face integral by a face flux times its area. The resulting equation states that accumulation equals inflow minus outflow plus internal generation. Shared-face fluxes cancel when the cell equations are summed, explaining global conservation. Accuracy now depends on how face variables and gradients are reconstructed and how the time derivative is advanced.

For the diffusion update, rearrange as $\phi_i^{n+1}=(1-2Fo)\phi_i^n+Fo\phi_{i+1}^n+Fo\phi_{i-1}^n$. When $0\le Fo\le1/2$, all weights are nonnegative and sum to one. The new value lies between neighboring old values. This supplies an intuitive boundedness explanation for this specific stability restriction.

## Worked examples

**Example 1 — explicit diffusion time step.** A one-dimensional thermal model uses $\alpha=10^{-5}\ \mathrm{m^2/s}$ and $\Delta x=0.002\ \mathrm m$. The limit is $\Delta t\le\Delta x^2/(2\alpha)=0.20\ \mathrm s$. Choose $\Delta t=0.10\ \mathrm s$, giving $Fo=0.25$. With neighboring temperatures $100$, $0$, and $0\ ^\circ\mathrm C$, the central temperature after one step is $0+0.25(0-0+100)=25\ ^\circ\mathrm C$. Temperature differences may use Celsius because the offset cancels.

**Example 2 — observed grid order.** A pressure drop is $104$, $101$, and $100.25\ \mathrm{Pa}$ on grids of spacing $4h$, $2h$, and $h$. The ratio of differences is $3/0.75=4$. Thus $p_{\rm obs}=\ln4/\ln2=2$ and $q_{\rm ext}=100.25+(100.25-101)/3=100.00\ \mathrm{Pa}$. Estimated finest-grid error relative to the extrapolate is $0.25\%$. This is a numerical estimate under the assumed error model, not a measurement uncertainty or proof that the flow model is correct.

## Exercises

1. For $u=2\ \mathrm{m/s}$ and $\Delta x=0.01\ \mathrm m$, find the maximum time step for the stated explicit upwind scheme.
2. If the diffusion grid spacing is halved, how does the permissible explicit time step change?
3. A steady model has $2.00\ \mathrm{kg/s}$ inflow and $1.98\ \mathrm{kg/s}$ outflow. Find the imbalance relative to inlet flow and explain the issue.

## Solutions

1. $\Delta t\le\Delta x/u=0.005\ \mathrm s$. Other coupled equations may impose a stricter condition.
2. The limit depends on $\Delta x^2$, so it becomes one quarter as large.
3. The imbalance is $(2.00-1.98)/2.00=1\%$. A steady source-free mass balance should close; inspect convergence, integrated boundary fluxes, and definitions before accepting pressure or heat-transfer predictions.

## Common mistakes

- Applying a one-dimensional explicit stability formula to every solver.
- Refining a mesh while changing geometry or boundary conditions, then calling the result a clean mesh study.
- Comparing turbulence results without checking wall resolution and wall-model requirements.
- Reporting many digits from uncertain inlet data or an unresolved separated flow.

## Applications and limits

Useful applications include duct pressure loss, cooling, mixing, aerodynamic loads, and pump flow paths. Start with a benchmark such as fully developed laminar pipe flow or conduction through a slab. Monitor the engineering output as well as residuals and conservation. Transient flows need time-step refinement and sufficient sampling duration. The formulas here explain elementary schemes; they are not a replacement for the numerical and modeling documentation of a specific solver.

## Further reading

- [MIT OpenCourseWare — Numerical Fluid Mechanics](https://ocw.mit.edu/courses/2-29-numerical-fluid-mechanics-spring-2015/): numerical methods, notes, and assignments.
- [NASA — CFD verification and validation tutorial](https://www.grc.nasa.gov/www/wind/valid/tutorial/tutorial.html): separate convergence and validation tasks.
- [NASA — spatial grid convergence](https://www.grc.nasa.gov/www/wind/valid/tutorial/spatconv.html): Richardson extrapolation and convergence assessment.
