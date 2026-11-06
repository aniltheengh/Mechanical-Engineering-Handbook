# 24. Finite Element Analysis

## Learning map

Prerequisites: statics, strength of materials, calculus, matrices, and numerical linear algebra. The objective is to convert a physical boundary-value problem into an approximate algebraic system, then judge whether its answer is useful. Begin with an axial bar before studying beams, plates, shells, solids, heat conduction, or coupled fields. A colorful stress plot is an output of assumptions; it is not independent evidence that those assumptions describe a real part.

## Theory

A continuum has displacement at every material point. Finite element analysis replaces that infinite set by a finite collection of nodal unknowns. Shape functions interpolate between nodes, and an integral statement of equilibrium determines the nodal values. The mesh therefore approximates both geometry and the possible displacement fields. A finer mesh expands the space of admissible solutions but cannot correct the wrong material law, load, contact definition, or support.

For small-displacement linear elasticity, strain is linear in displacement gradients and stress is linear in strain. The stiffness matrix is constant, and load cases can be superposed. Plasticity, large rotations, changing contact, and stress stiffening break one or more of these assumptions. Nonlinear analysis then solves equilibrium incrementally and iteratively. Each load step needs convergence; convergence of the nonlinear iterations does not establish convergence with mesh size.

Essential boundary conditions prescribe displacement. Natural boundary conditions prescribe traction. A model without sufficient displacement constraints contains rigid-body modes and has a singular stiffness matrix. Excessive restraint can be equally misleading by creating fictitious reactions. Support a model according to the actual load path, allowing physically possible sliding, rotation, and thermal expansion.

Element choice matters. Truss elements carry axial force, beam elements represent section bending, shell elements represent thin surfaces, and solid elements resolve three-dimensional fields. A thin component meshed with poorly shaped low-order solids may be excessively stiff. Nearly incompressible materials can exhibit volumetric locking. Element formulations and integration schemes should be chosen for the deformation mode, not merely for meshing convenience.

## Formula handbook

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

## Derivation

For a uniform bar, substitute $u=N_1d_1+N_2d_2$ into $U=\frac12\int_0^L EA(du/dx)^2dx$. The derivative is constant, $(d_2-d_1)/L$, so $U=EA(d_2-d_1)^2/(2L)$. Differentiate total potential energy with respect to each free displacement. Setting each derivative to zero gives nodal equilibrium and the stiffness matrix above. With node 1 fixed and force $P$ at node 2, the remaining equation is $(EA/L)d_2=P$. Thus a single linear element gives the exact endpoint displacement for this particular uniform, end-loaded bar because the exact displacement is itself linear. It does not follow that one element is sufficient for a varying cross-section or distributed loading.

## Worked examples

**Example 1 — axial element.** A steel bar has $E=200\ \mathrm{GPa}$, $A=200\ \mathrm{mm^2}=2\times10^{-4}\ \mathrm{m^2}$, $L=1\ \mathrm m$, and $P=10\ \mathrm{kN}$. Its stiffness is $EA/L=40\ \mathrm{MN/m}$. Therefore $d_2=10000/(40\times10^6)=0.00025\ \mathrm m=0.250\ \mathrm{mm}$. Stress is $50.0\ \mathrm{MPa}$ and strain energy is $Pd_2/2=1.25\ \mathrm J$. The fixed-end reaction is $-10\ \mathrm{kN}$, balancing the applied force. A computed result should reproduce all four quantities.

**Example 2 — two elements in series.** Two bars each have $L=0.5\ \mathrm m$ and $E=200\ \mathrm{GPa}$. Their areas are $100$ and $200\ \mathrm{mm^2}$. A $5\ \mathrm{kN}$ load passes through both. The first extension is $0.125\ \mathrm{mm}$; the second is $0.0625\ \mathrm{mm}$. Consequently the middle-node displacement is $0.125\ \mathrm{mm}$ and the free end moves $0.1875\ \mathrm{mm}$. Stresses are $50$ and $25\ \mathrm{MPa}$. The same internal force in both bars follows from equilibrium, not from equal strain.

## Exercises

1. Double the cross-sectional area in Example 1. Find displacement and stress.
2. A model predicts tip displacements $1.20$, $1.10$, and $1.075\ \mathrm{mm}$ on successive meshes. Find the last relative change. Does it prove experimental accuracy?
3. An unconstrained three-dimensional solid model is subjected to a balanced force pair. Explain why its static stiffness matrix can remain singular.

## Solutions

1. Stiffness doubles. Displacement becomes $0.125\ \mathrm{mm}$ and stress becomes $25\ \mathrm{MPa}$, provided the load stays constant.
2. The last relative change is $0.025/1.075=0.02326$, or $2.33\%$. This only measures change under refinement. Material, geometry, and boundary-condition errors still require separate assessment.
3. Balanced loading does not remove the six rigid-body freedoms of a free three-dimensional body. The solution is not unique until a reference frame or physically appropriate constraints are supplied.

## Common mistakes

- Reading a stress maximum at a sharp re-entrant corner as a converged physical stress. A mathematical singularity can increase with refinement.
- Comparing nodally averaged stresses with element integration-point stresses without noting the difference.
- Treating a low equation residual as evidence of correct physics.
- Mixing millimetres and metres when entering modulus, density, and force.

## Applications and limits

Use analytical benchmarks, reaction balance, energy balance, deformation shape, and mesh refinement together. Record the quantity of interest before solving: deflection, fatigue stress range, natural frequency, contact pressure, or heat flow may need different meshes. For a weld toe or notch, a stress assessment procedure must define geometry and stress extraction consistently. A handbook example is not a fabrication or structural certification calculation. MIT's course provides a broader treatment of element formulations and nonlinear analysis; NASA's modeling handbook supplies a framework for simulation credibility, distinct from the original elementary derivation here.

## Further reading

- [MIT OpenCourseWare — Finite Element Analysis of Solids and Fluids I](https://ocw.mit.edu/courses/2-092-finite-element-analysis-of-solids-and-fluids-i-fall-2009/): lectures, problems, and solutions.
- [NASA Handbook 7009A — modeling and simulation implementation](https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/nasa-hdbk-7009a.pdf): verification, validation, and credibility context; check current project requirements separately.
