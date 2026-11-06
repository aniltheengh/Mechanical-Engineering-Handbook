# Mechanics, materials, and machine design

Mechanical Engineering Handbook · First edition · 2026-11-06

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [04. Engineering statics](../chapters/04-statics.md)
- [05. Engineering dynamics](../chapters/05-dynamics.md)
- [06. Strength of materials](../chapters/06-strength-of-materials.md)
- [07. Materials science and selection](../chapters/07-materials-science.md)
- [18. Machine elements and mechanical design](../chapters/18-machine-design.md)
- [19. Kinematics of machines and mechanisms](../chapters/19-mechanisms.md)
- [20. Mechanical vibrations](../chapters/20-vibrations.md)
- [34 · Tribology: friction, lubrication, and wear](../chapters/34-tribology.md)

---

## 04. Engineering statics

### Learning map

Prerequisites: vectors, trigonometry, SI units, and elementary integration. The goal is to turn a physical assembly into free-body diagrams, determine support reactions and member forces, and recognize when equilibrium alone cannot determine the answer. Statics supplies the loads used in strength, machine design, piping-support, and foundation calculations. Study particles first, rigid bodies second, and assemblies third.

### Theory

A body is in static equilibrium when its linear and angular accelerations vanish. This is a statement about the resultant external force and moment; it does not mean that every internal stress is zero. A support carries a reaction because it prevents a particular displacement. An ideal planar roller provides one normal force, a pin two force components, and a fixed end two force components plus a moment. These are models of actual contact stiffness and connection behavior.

A free-body diagram isolates a selected body, replaces removed connections by their forces, and shows dimensions needed for moment arms. Weight acts at the center of mass. A cable pulls along its own axis; an ideal frictionless pulley changes direction without changing cable tension. A two-force member carries collinear end forces only when it has exactly two applied forces and negligible self-weight. A truss idealization therefore requires pin joints and joint-applied loads.

There are three independent equilibrium equations for a planar rigid body and six in three dimensions. More unknowns generally require deformation compatibility and constitutive laws. Merely counting equations is insufficient: support geometry may leave a mechanism or make equations dependent. A beam with two horizontal rollers, for example, has no horizontal restraint regardless of equation counting.

Distributed loads may be replaced by a statically equivalent resultant for external reactions. That replacement does not preserve local bending and shear everywhere inside the loaded interval. Static friction is a variable reaction that opposes impending relative motion. It reaches its limiting magnitude only at impending slip. After motion begins, a separate kinetic-friction model is needed.

### Formula handbook

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

### Derivation

Consider a simply supported beam of span $L$, with a downward point load $P$ a distance $a$ from the left support and a uniform downward load $w$ over the entire span. Replace the distributed load by $wL$ acting at $L/2$. Taking moments about the left support eliminates its unknown reaction:

$$
R_B L-Pa-wL(L/2)=0.
$$

Thus $R_B=Pa/L+wL/2$. Vertical equilibrium gives $R_A=P+wL-R_B$. This derivation explains why increasing the distance of a point load from the left support increases the right reaction. Setting $P=0$ recovers equal reactions for a symmetric uniform load; setting $a=0$ makes the point load act directly into the left support.

### Worked examples

#### Example 1: Beam support reactions

Let $L=6$ m, $P=12$ kN at $a=2$ m, and $w=2$ kN/m. The distributed load is 12 kN at the midpoint. Moment equilibrium gives $R_B=(12\times2+12\times3)/6=10$ kN. Force equilibrium then gives $R_A=24-10=14$ kN. The residual moment is $10\times6-12\times2-12\times3=0$ kN m. These are external reactions; determining the largest bending stress still requires a section-force analysis and a section geometry.

#### Example 2: Crate on an incline

An 80 kg crate rests on a $25^\circ$ incline with $\mu_s=0.50$. Use $g=9.81$ m/s². Normal equilibrium gives $N=mg\cos25^\circ=711.27$ N. Downslope weight is $mg\sin25^\circ=331.67$ N. The maximum available static friction is 355.64 N, so equilibrium is possible. Actual friction is 331.67 N upslope, not 355.64 N. The limiting slope is $\arctan0.50=26.565^\circ$, assuming the crate does not tip first.

### Exercises

1. A 4 m beam has an 8 kN point load 1 m from its left support. Find both vertical reactions.
2. A triangular load increases from zero to 3 kN/m over 6 m. Find its resultant and location from the zero-load end.
3. A horizontal 100 N force acts in the positive $x$ direction at point $(0,0.4)$ m. Find its moment about the origin, including sign.

### Solutions

1. Right reaction is $8(1)/4=2$ kN; left reaction is $8-2=6$ kN. Check that the larger reaction is closer to the load.
2. The resultant is the triangle area, $3(6)/2=9$ kN. It acts at $2(6)/3=4$ m from the zero-load end.
3. $M_z=xF_y-yF_x=0-0.4(100)=-40$ N m. The negative sign means clockwise.

### Common mistakes

- Mixing a distance along the force with the perpendicular moment arm.
- Treating friction as $\mu_sN$ before proving impending slip.
- Including internal joint forces twice on a whole-assembly free-body diagram.
- Replacing a distributed load by a resultant before calculating internal forces within its footprint.
- Solving three planar equations without checking whether the support arrangement is stable.

### Applications and limits

Use statics for slow-loaded brackets, pipe supports, cranes at rest, and initial machine load paths. Verify the actual operating load cases: startup, shutdown, wind, thermal movement, fluid transients, and lifting can invalidate a purely static representation. Large deformation may change moment arms enough to require equilibrium on the deformed shape. For indeterminate structures, proceed to compatibility and stiffness methods rather than adding invented reaction assumptions.

### Further reading

These are linked learning resources; their text and figures are not reproduced here.

- [MIT OCW: Mechanics and Materials I](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/) — equilibrium, compatibility, and constitutive modeling.
- [MIT OCW: Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) — free-body diagrams and the transition from equilibrium to motion.


---

## 05. Engineering dynamics

### Learning map

Prerequisites: statics, vectors, derivatives, integrals, and elementary differential equations. Learn to separate kinematics, which describes motion, from kinetics, which relates motion to force and mass. Use particle models before rigid bodies. Choose force–acceleration, work–energy, or impulse–momentum according to the quantities available. Vibration and mechanism analysis build directly on these tools.

### Theory

Newton's laws apply directly in inertial frames. A frame fixed to an accelerating vehicle requires additional inertial terms if treated as though it were inertial. Position, velocity, and acceleration are vectors; speed is the magnitude of velocity. A body moving at constant speed around a curve still accelerates because its velocity direction changes.

A particle model ignores size and rotation. A rigid body preserves distances between its material points and can translate and rotate simultaneously. Its center of mass obeys the translational equation of motion even when the body rotates. The angular equation is particularly simple about the center of mass for planar motion, or about a fixed axis whose direction does not change. General three-dimensional rotation requires the inertia tensor and gyroscopic terms.

Work–energy eliminates time when force can be expressed along displacement. Constraint forces can do zero work on a selected system even while producing substantial accelerations. An ideal stationary pin does no work at its fixed point; friction at a sliding contact generally does. In rolling without slipping on a stationary rigid surface, the instantaneous contact point has zero velocity, but rolling resistance and deformation can still dissipate energy in real hardware.

Impulse–momentum is useful when forces act over short intervals or their time histories are known. Momentum is conserved only for a system with zero net external impulse. Kinetic energy need not be conserved in a collision. A coefficient of restitution relates the relative normal separation speed to the relative normal approach speed, not the absolute velocities of an arbitrary reference frame.

### Formula handbook

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

### Derivation

For a particle moving along one coordinate, Newton's law is $F=ma$. Substitute $a=v\,dv/dx$ and multiply by $dx$. Integration gives $\int F\,dx=\int mv\,dv=\tfrac12m(v_2^2-v_1^2)$. Thus the work–energy theorem is a rearrangement of the force law, not an additional independent physical law for this model. Conservative forces can be moved into a potential energy $V$, giving $T_1+V_1+W_{nc}=T_2+V_2$.

For a rolling wheel, translation and rotation are linked by $v_G=R\omega$ only under no-slip conditions. Substitution into kinetic energy gives $T=\tfrac12(m+I_G/R^2)v_G^2$. Rotational inertia therefore increases the effective inertia seen in the translational coordinate.

### Worked examples

#### Example 1: Accelerating cart

A 15 kg cart starts from rest on a horizontal track. A constant 80 N drive force opposes 20 N of resistance. Net force is 60 N, so $a=60/15=4$ m/s². After 3 s, speed is 12 m/s and travel is 18 m. Work by the net force is $60(18)=1080$ J; kinetic energy is $15(12^2)/2=1080$ J. Agreement checks both the force and displacement calculation. Resistance was assumed constant over this speed range.

#### Example 2: Spinning a disk

A uniform 10 kg disk of radius 0.20 m rotates about its fixed central axis. A net torque of 4 N m acts for 2 s from rest. Its inertia is $I=mR^2/2=0.20$ kg m², so $\alpha=20$ rad/s², final speed is 40 rad/s, and rotation is 40 rad. Torque work is $4(40)=160$ J, matching $I\omega^2/2=160$ J. Angular impulse is 8 N m s, matching $I\omega=8$ kg m²/s.

### Exercises

1. A particle moves in a circle of radius 2 m at constant speed 6 m/s. Find its acceleration magnitude and direction.
2. A 5 kg body initially moves at 3 m/s. A collinear positive impulse of 20 N s acts on it. Find final velocity.
3. A uniform solid cylinder rolls without slip at 4 m/s. Its mass is 6 kg. Find total kinetic energy.

### Solutions

1. $a_n=v^2/r=36/2=18$ m/s² toward the center. Tangential acceleration is zero.
2. $5v_2-5(3)=20$, giving $v_2=7$ m/s in the original positive direction.
3. $I_G=mR^2/2$ and $\omega=v/R$. Translation contributes 48 J and rotation 24 J, for 72 J total; the radius cancels.

### Common mistakes

- Equating zero speed at one instant with zero acceleration.
- Using $\sum M_O=I_O\alpha$ about an arbitrary accelerating point without the necessary extra terms.
- Omitting rotational kinetic energy for a rolling body.
- Conserving mechanical energy while ignoring friction, impact loss, or actuator work.
- Applying constant-acceleration equations when force changes strongly with position or speed.

### Applications and limits

Dynamics predicts actuator demand, stopping distances, rotating-machine startup, and mechanism loads. Rigid models exclude elastic waves and structural deformation; fast impacts may require flexible-body or wave models. A prescribed acceleration profile requires force capacity at every instant, not merely adequate average energy. Numerical integration should preserve the expected energy or dissipation trend and should be checked by reducing the time step.

### Further reading

Linked course resources are for deeper study; no source passages are reproduced.

- [MIT OCW: Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) — lectures, worked demonstrations, problems, and solutions.
- [MIT OCW: Design and Manufacturing I](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/) — applying dynamics to machines and design projects.


---

## 06. Strength of materials

### Learning map

Prerequisites: statics, calculus, and material stress–strain behavior. Progress from axial members to torsion, bending, combined stress, deflection, and buckling. The central reasoning chain is external loads → internal resultants → stress and strain → displacement or failure criterion. A design can satisfy a stress limit while failing a stiffness, stability, fatigue, or connection requirement.

### Theory

Stress is the internal force intensity acting across an imagined cut. Normal stress acts perpendicular to that cut; shear stress acts within it. Stress is a tensor because both the cut orientation and force direction matter. Engineering strain measures deformation relative to an original length. For small deformations in a linearly elastic isotropic solid, stress and strain are related by Young's modulus, shear modulus, and Poisson's ratio.

Simple bar, shaft, and beam formulas are reduced models of three-dimensional continuum behavior. Their simplicity comes from assumptions about cross-section geometry, deformation, loading, and material properties. Away from localized load application, stress often becomes less sensitive to the exact load distribution, which motivates Saint-Venant-type reasoning. It does not eliminate stress concentration near holes, weld toes, threads, or abrupt changes in section.

Euler–Bernoulli beam theory assumes cross-sections remain plane and normal to the bent centerline. It is appropriate for slender beams with small rotations and negligible shear deflection. Short thick beams may need Timoshenko theory. Circular-shaft torsion formulas rely on circular geometry; noncircular sections warp and cannot generally use the same polar-moment relation.

Yielding and fracture are different failure mechanisms. Von Mises stress is commonly used to screen yielding of ductile isotropic metals, while brittle fracture often needs tensile stress and crack-based criteria. Buckling is a loss of stability and can occur below material yield stress. Slenderness, end restraint, geometric imperfections, and load eccentricity strongly affect its onset.

### Formula handbook

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

### Derivation

For pure bending, plane sections rotate relative to one another. A fiber at signed distance $y$ from the neutral axis has axial strain $\epsilon_x=-y/\rho_c$, where $\rho_c$ is curvature radius. Linear elasticity gives $\sigma_x=-Ey/\rho_c$. The resultant moment magnitude is $M=\int_A E y^2/\rho_c\,dA=EI/\rho_c$. Eliminating curvature gives the flexure equation. This derivation shows why a hole changes bending stress through $I$ and why increasing section depth is particularly effective: rectangular $I$ increases as $h^3$.

### Worked examples

#### Example 1: Cantilever bracket

A rectangular steel cantilever has length 0.50 m, width 0.040 m, vertical depth 0.060 m, and $E=200$ GPa. A 1000 N downward force acts at the free end. The second moment is $I=0.04(0.06)^3/12=7.20\times10^{-7}$ m⁴. Root moment is 500 N m, giving extreme-fiber stress $500(0.03)/I=20.833$ MPa. Tip deflection is $1000(0.5)^3/[3(200\times10^9)I]=0.28935$ mm downward. The root connection and local stress concentration require separate assessment.

#### Example 2: Solid shaft

A 40 mm diameter shaft, 1 m long, transmits 400 N m with $G=80$ GPa. $J=\pi(0.04)^4/32=2.51327\times10^{-7}$ m⁴. Outer-surface shear stress is $400(0.02)/J=31.831$ MPa. Twist is $400/[80\times10^9J]=0.019894$ rad, or $1.140^\circ$. For this pure shear state, von Mises stress is $\sqrt3\tau=55.133$ MPa. Keyways and torque fluctuations are excluded.

### Exercises

1. A 2 m bar of area 500 mm² and modulus 200 GPa carries 50 kN tension. Find average stress and extension.
2. A plane-stress point has $\sigma_x=100$ MPa, $\sigma_y=0$, and $\tau_{xy}=30$ MPa. Find von Mises stress.
3. What happens to ideal Euler buckling load when an otherwise identical column length doubles?

### Solutions

1. $A=5\times10^{-4}$ m², so stress is 100 MPa. Extension is $NL/(EA)=0.001$ m, or 1 mm.
2. $\sigma_{vm}=\sqrt{100^2+3(30)^2}=112.694$ MPa. Directly adding normal and shear stress would be incorrect.
3. Buckling load scales with $1/L^2$, so it becomes one-quarter, with the same $E,I,K$ and elastic validity.

### Common mistakes

- Using area moment $I$ in kg m² instead of m⁴; mass moment and area moment are different quantities.
- Entering mm⁴ directly into an otherwise metre-based calculation.
- Taking average stress as the peak stress near a discontinuity.
- Confusing section modulus $I/c$ with second moment $I$.
- Checking yield alone when stiffness, fatigue, instability, or brittle fracture governs.

### Applications and limits

Use these models for first calculations of brackets, frames, shafts, rods, and idealized vessel membranes. Record load direction, support conditions, material state, and temperature. Compare with finite-element results by checking reactions and energy as well as peak stress; mesh-dependent stress at an ideal sharp corner is not a converged material failure prediction. Real design allowables and required margins depend on the governing application and material data.

### Further reading

- [MIT OCW: Mechanics and Materials I](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/) — solid mechanics foundations and assignments.
- [MIT OCW: Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) — linked open textbook and modules. These references are linked, not copied.


---

## 07. Materials science and selection

### Learning map

Prerequisites: chemistry fundamentals, stress and strain, energy, and temperature. Connect atomic bonding to microstructure, processing, properties, and service performance. Study elastic and plastic deformation, phase equilibrium, diffusion, fracture, fatigue, and creep. A material name alone is not a specification: composition, product form, heat treatment, orientation, and test conditions matter.

### Theory

Metals, ceramics, polymers, and composites possess different bonding and structural mechanisms. Metallic bonding permits dislocation motion, making many metals ductile. Ceramics often resist elastic deformation and high temperature but tolerate little tensile crack growth. Polymers have time- and temperature-dependent chain mobility. Composite properties depend on constituent materials, fiber direction, interfaces, and manufacturing defects.

Elastic deformation recovers after unloading; plastic deformation leaves a permanent component. Yield stress describes a chosen transition or proof criterion, whereas ultimate tensile strength is the maximum engineering stress in a tensile test. After necking begins, engineering and true stresses differ substantially because deformation is no longer uniform. Hardness is a local indentation response and cannot be converted universally into tensile strength.

Microstructure includes grain size, phases, precipitates, dislocation density, porosity, and texture. Strengthening often obstructs dislocation motion through grain boundaries, solute atoms, precipitates, or cold work. Increasing strength can reduce ductility or fracture tolerance, so maximizing one property is rarely the whole design objective. Heat treatment changes microstructure through temperature-time history; a phase diagram alone does not predict transformation speed.

An equilibrium phase diagram identifies stable phases at specified composition and temperature. A tie line gives phase compositions, while the lever rule gives phase fractions. Diffusion transports atoms down a chemical-potential gradient; simple concentration-gradient laws are useful approximations. Phase transformations require both thermodynamic driving force and kinetic pathways.

Failure depends on environment and duration. Fatigue can initiate under repeated stress below monotonic yield. Creep accumulates with time under sustained stress, especially at elevated homologous temperature. Corrosion, hydrogen, irradiation, and wear can change properties or introduce flaws. Material selection should therefore begin with a service envelope and credible failure modes, then use traceable data for the actual product condition.

### Formula handbook

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

### Derivation

For a binary alloy containing phases $\alpha$ and $\beta$, conservation gives $f_\alpha+f_\beta=1$ and $C_0=f_\alpha C_\alpha+f_\beta C_\beta$. Eliminating $f_\beta$ yields the lever rule. If $C_0$ approaches $C_\alpha$, the amount of $\beta$ approaches zero. The result requires the tie-line endpoint compositions, not the overall alloy composition substituted into both phase terms. A phase diagram supplies equilibrium endpoints; real cooling can preserve nonequilibrium structures.

### Worked examples

#### Example 1: Thermal movement and restraint

A 2 m bar has $\alpha_T=11\times10^{-6}$ K⁻¹ and $E=200$ GPa. For a 60 K temperature rise, its free extension is $11\times10^{-6}(2)(60)=1.32$ mm. If perfectly restrained while remaining elastic, stress is $-200\times10^9(11\times10^{-6})(60)=-132$ MPa. These are two different boundary-condition cases: the bar cannot simultaneously achieve the full free extension and the fully restrained stress. Real support flexibility produces an intermediate response.

#### Example 2: Critical crack-size estimate

Assume $K_{IC}=50$ MPa m$^{1/2}$, tensile stress 150 MPa, and approximately constant $Y=1.12$. Then $a_c=(50/(1.12\times150))^2/\pi=0.028195$ m, or 28.195 mm. This is the crack-length parameter used by the assumed geometry, not automatically a full crack length. A finite plate may require a size-dependent $Y$. The result is only meaningful if small-scale yielding and the toughness test's validity conditions hold.

### Exercises

1. A tie line has $C_\alpha=10$ and $C_\beta=50$ mass %. Find phase mass fractions for an alloy at 30 mass %.
2. Under the ideal axial composite model, $V_f=0.60$, $E_f=200$ GPa, and $E_m=3$ GPa. Find $E_L$.
3. Under the same crack geometry and toughness, how does critical crack size change when applied tensile stress doubles?

### Solutions

1. $f_\alpha=(50-30)/(50-10)=0.50$ and $f_\beta=0.50$. Both mass and composition balances are satisfied.
2. $E_L=0.6(200)+0.4(3)=121.2$ GPa. This is an axial modulus, not an isotropic modulus for the composite.
3. $a_c\propto1/\sigma^2$, so the critical size becomes one-quarter. This conclusion assumes $Y$ remains unchanged.

### Common mistakes

- Selecting a material from strength alone while ignoring toughness, corrosion, weldability, and temperature.
- Treating a phase diagram as a cooling-time diagram.
- Using engineering stress beyond necking as though area remained uniform.
- Mixing MPa m$^{1/2}$ with a crack length in mm without conversion.
- Treating tabulated typical properties as guaranteed design allowables for every product.

### Applications and limits

Use property-based screening to reduce candidate materials, then evaluate manufacturing and service constraints. A stainless steel may resist one water chemistry and suffer localized attack in another. A polymer may support a short test yet creep during years of use. Qualification needs the actual material condition, representative loading, environmental exposure, and an appropriate inspection strategy. This chapter explains models; it does not assign universal allowable stresses.

### Further reading

- [MIT OCW: Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) — open modules connecting microstructure and mechanical behavior.
- [MIT OCW: Kinetic Processes in Materials](https://ocw.mit.edu/courses/3-21-kinetic-processes-in-materials-spring-2006/) — diffusion and transformation theory. Resources are linked for study, not reproduced.


---

## 18. Machine elements and mechanical design

### Learning map

Prerequisites: statics, dynamics, strength of materials, materials science, and manufacturing. Follow power from actuator to load, calculate forces at every interface, and check each component for strength, stiffness, life, fit, and serviceability. This chapter covers shafts, gears, rolling bearings, bolts, springs, and fatigue screening. Detailed product selection requires the relevant manufacturer's data and applicable design standards.

### Theory

A machine is a load path and a motion path. A gearbox changes torque and speed, while shafts, keys, splines, bearings, housings, and fasteners transmit the resulting loads. Power balance alone does not determine bearing forces: tooth pressure angle, shaft spacing, overhangs, and external loads determine reactions. Deflection can spoil alignment even when nominal stresses are low.

Gear ratio sets ideal kinematic relations. Real gears also require tooth-root fatigue, contact fatigue, scuffing, lubrication, backlash, and manufacturing accuracy checks. A pitch-circle force calculation is an input to those checks. Bearing dynamic rating life is a statistical fatigue measure under specified assumptions; it is not a promise that every bearing lasts that long. Contamination, poor lubrication, excessive preload, installation damage, or electrical erosion may cause earlier failure.

A preloaded bolted joint initially compresses the clamped members. An external separating load increases bolt tension and reduces member compression according to their stiffnesses. While contact remains, the bolt does not generally receive the entire external load increment. Once the joint separates, that model changes. Torque tightening is sensitive to friction, so a single torque coefficient is a rough preload estimate rather than a universal law.

Helical compression springs store energy largely through torsion of their wire. Curvature increases local stress, requiring a correction such as the Wahl factor for the stated spring geometry. Active coil count differs from total coils, and coil bind, buckling, surge, end seating, and fatigue may govern. Fatigue assessment separates mean and alternating stress and uses experimentally supported material and surface data.

### Formula handbook

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

### Derivation

For an ideal gear pair, equal pitch-line speed gives $\omega_1r_1=\omega_2r_2$. Equal tangential force gives $T_1/r_1=T_2/r_2$. Combining these equations shows that torque multiplies by the same ratio by which speed decreases, leaving power unchanged. Real loss changes torque through $\eta$, but it does not change the geometric speed ratio when teeth remain engaged without slip. This separates kinematic constraints from energy efficiency.

### Worked examples

#### Example 1: Gear reduction

A 5 kW motor runs at 1500 rpm and drives a 20-tooth pinion meshing with a 60-tooth gear. Pinion pitch diameter is 0.060 m. Input torque is $5000/[2\pi(1500)/60]=31.831$ N m. The ratio is 3, output speed is 500 rpm, and ideal output torque is 95.493 N m. Tangential tooth force is $2(31.831)/0.060=1061.03$ N. For a specified $20^\circ$ pressure angle, radial force is 386.18 N. Actual tooth capacity is not established by these forces alone.

#### Example 2: Ball-bearing basic life

A ball bearing has $C=20$ kN, equivalent dynamic load $P_b=5$ kN, and speed 1200 rpm. Basic life is $(20/5)^3=64$ million revolutions. Hour conversion gives $64\times10^6/[60(1200)]=888.89$ h. Halving load would increase this model's life by a factor of eight. Actual selection must also assess static load, minimum load, speed, lubrication, contamination, mounting, and duty-cycle variation.

### Exercises

1. A joint has preload 20 kN and stiffness fraction $C_j=0.20$. A 10 kN separating force is applied. Find bolt tension and remaining clamp force.
2. Stress cycles between 20 and 100 MPa. Find mean and alternating components.
3. An ideal 4:1 speed reduction receives 8 N m at 1200 rpm. Find output speed and torque.

### Solutions

1. Bolt tension is $20+0.2(10)=22$ kN. Clamp force is $20-0.8(10)=12$ kN, still positive, so the contact assumption remains possible.
2. Mean stress is 60 MPa and alternating stress 40 MPa. The stress ratio is $20/100=0.20$.
3. Output speed is 300 rpm and torque is 32 N m. Both sides transmit approximately 1005.31 W in the ideal model.

### Common mistakes

- Treating catalog dynamic load rating as the maximum allowable static load.
- Selecting bearings using shaft torque instead of bearing reaction forces.
- Using a gear ratio to multiply both speed and torque.
- Ignoring joint separation when applying bolt load sharing.
- Calling a nominal fatigue stress acceptable without accounting for surface, size, notch, temperature, and reliability effects.

### Applications and limits

Use these relations to size a first design, identify dominant loads, and choose candidate components. Then close the loop through tolerances, alignment, lubrication, assembly, maintenance, and testing. Review the manufacturer's current calculation method for the actual part family. A complete machine-element design includes failure modes and lifecycle evidence beyond a single stress or life equation.

### Further reading

- [MIT OCW: Elements of Mechanical Design](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/) — machine-element modeling, integration, and projects.
- [MIT: FUNdaMentals of Design](https://meddevdesign.mit.edu/fundamentals-of-design/) — linked lectures and design spreadsheets.
- [SKF: Rolling Bearings catalog](https://www.skf.com/binaries/pub12/Images/0901d196802809de-Rolling-bearings---17000_1-EN_tcm_12-121486.pdf) — manufacturer definitions and selection limitations. Linked material is not reproduced.


---

## 19. Kinematics of machines and mechanisms

### Learning map

Prerequisites: geometry, vectors, derivatives, statics, and dynamics. A mechanism imposes relationships between motions. Start with degrees of freedom and geometric closure, differentiate for velocity and acceleration, then use virtual work or dynamics to calculate forces. Common mechanisms include four-bars, slider-cranks, cams, gears, screw drives, and belt transmissions.

### Theory

A link is treated as rigid, and a joint restricts relative motion between links. Planar revolute and prismatic joints each permit one relative degree of freedom. A cam contact is a higher pair and generally constrains one relative planar motion when contact is maintained. Counting mobility is useful but can fail for special geometry, redundant constraints, or intermittent contact. Always test the actual constraint equations.

Position analysis is nonlinear and may have several assembly branches. A mechanism can satisfy the same input angle in an open or crossed configuration. Numerical solvers must track the intended branch continuously. A toggle position is a configuration where transmission becomes singular: finite input motion may correspond to very small output motion, and ideal static force ratios can become very large. Elasticity, friction, and clearances bound real forces.

Velocity analysis differentiates geometry; acceleration differentiates again and includes centripetal terms. The instantaneous center is a point of zero instantaneous velocity for relative planar motion, but it is not generally a fixed center of rotation and need not have zero acceleration. Using it for velocities does not automatically justify fixed-axis acceleration formulas.

Cam design must consider displacement, velocity, acceleration, and jerk. Abrupt acceleration changes can excite flexible structures. The pressure angle controls how effectively contact force produces useful follower force, while curvature controls contact geometry and possible undercutting. Gear backlash and joint clearance permit lost motion that ideal kinematic equations omit. Mechanism synthesis works backward from desired motion or positions to link dimensions; analysis checks the motion of a specified design.

### Formula handbook

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

### Derivation

In a slider-crank, the connecting rod's vertical projection cancels the crank's vertical projection: $l\sin\phi=r\sin\theta$. Its horizontal projection is therefore $l\cos\phi=\sqrt{l^2-r^2\sin^2\theta}$ for the selected assembly branch. Adding the crank's horizontal projection gives the exact slider-position equation. Differentiating this geometric equation produces velocity without assuming that the rod is infinitely long. The second harmonic in the long-rod approximation explains why piston motion differs from a pure sinusoid.

### Worked examples

#### Example 1: Slider-crank position and speed

Let crank radius $r=0.050$ m, rod length $l=0.200$ m, crank angle $60^\circ$, and crank speed 10 rad/s. The rod's horizontal projection is $\sqrt{0.2^2-0.05^2\sin^260^\circ}=0.195256$ m. Thus slider position is $0.05\cos60^\circ+0.195256=0.220256$ m. The exact derivative gives $dx/d\theta=-0.0488454$ m/rad and velocity $-0.488454$ m/s. The negative sign means motion toward the crank center for increasing angle at this configuration.

#### Example 2: Four-bar feasibility

A four-bar has lengths 30, 70, 80, and 100 mm, with the 100 mm link grounded. Four links and four revolute joints give $M=3(4-1)-2(4)=1$. Grashof comparison gives $30+100=130$ mm versus $70+80=150$ mm, so the strict inequality holds. If the 30 mm shortest link is adjacent to ground, this inversion can form a crank-rocker with the shortest link rotating fully. If the shortest link is instead opposite the ground, the inversion differs; length inequality alone does not name every link's motion.

### Exercises

1. A lead screw has 5 mm lead and rotates at 600 rpm. Find ideal linear speed.
2. A 40 mm crank and 160 mm rod form an inline slider-crank. Find slider positions at $0^\circ$ and $180^\circ$, and its stroke.
3. A cycloidal cam rises 20 mm over $\beta=\pi$ radians at constant 5 rad/s. Find its maximum follower speed.

### Solutions

1. 600 rpm is 10 rev/s, so speed is $5(10)=50$ mm/s, or 0.050 m/s.
2. Positions are $160+40=200$ mm and $160-40=120$ mm. Stroke is 80 mm, twice the crank radius.
3. The bracket $1-\cos(2\pi\theta/\beta)$ has maximum 2. Therefore maximum speed is $2h\omega/\beta=0.2/\pi=0.063662$ m/s.

### Common mistakes

- Using degrees directly in a derivative formula written for radians.
- Allowing a numerical solver to jump between assembly branches.
- Treating a mobility count as proof that every configuration is nonsingular.
- Assuming infinite force amplification at a toggle is a usable real design result.
- Confusing thread pitch with lead or ignoring cam-contact separation.

### Applications and limits

Mechanism analysis supports pumps, engines, presses, packaging machines, valves, and positioning equipment. Verify that the entire trajectory clears surrounding geometry and respects joint limits. Add dynamics for acceleration loads and flexibility for high-speed behavior. An ideal motion model can be correct while a real assembly binds because of tolerance, misalignment, or overconstraint; physical prototypes and measured motion close that gap.

### Further reading

- [MIT: FUNdaMentals of Design](https://meddevdesign.mit.edu/fundamentals-of-design/) — linkages and power-transmission lecture resources.
- [MIT OCW: Elements of Mechanical Design](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/) — mechanism integration and design problems. These materials are linked rather than copied.


---

## 20. Mechanical vibrations

### Learning map

Prerequisites: dynamics, differential equations, complex numbers, and elementary matrix algebra. Begin with a single-degree-of-freedom mass–spring–damper, then study forced response, isolation, rotating imbalance, and multiple modes. Distinguish excitation frequency, natural frequency, and observed response frequency. The aim is to predict motion, transmitted loads, and resonance sensitivity rather than merely calculate one natural frequency.

### Theory

Vibration exchanges kinetic and potential energy. A mass stores kinetic energy, a spring stores strain energy, and a damper dissipates energy. Linear viscous damping assumes force proportional to relative velocity; it is an approximation for many real mechanisms. Coulomb friction, material hysteresis, backlash, and fluid drag can produce qualitatively different behavior.

The free response depends on initial displacement and velocity. An underdamped system oscillates with a decaying envelope; a critically damped system returns without oscillation in the ideal model; an overdamped system also does not oscillate but contains two real decay rates. A constant gravity load shifts the equilibrium position and does not change the natural frequency of an ideal linear vertical spring.

Forced response contains a transient plus a steady response. Near resonance, small damping can permit large amplitude. The maximum displacement-response frequency is not exactly the undamped natural frequency when damping is present. Resonance is a relationship among forcing, modal properties, and damping, not a universal condition that every spinning machine automatically reaches at one specific speed.

Isolation means reducing transmission between a vibrating source and its support. A soft mount can reduce high-frequency force transmission yet amplify motion during passage through resonance. Damping reduces the resonant peak but can increase high-frequency force transmission for the basic viscous isolator. Travel, stability, static deflection, startup, and shutdown therefore belong in an isolation design.

Real structures have multiple modes. Each mode has a shape and natural frequency, and forcing couples to it according to spatial distribution. A sensor at a modal node may miss a mode. A frequency spectrum is evidence of response, not by itself a diagnosis of the cause; speed tracking, phase, operating conditions, and a physical model help distinguish imbalance, misalignment, looseness, and structural resonance.

### Formula handbook

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

### Derivation

Represent harmonic force and displacement by the real parts of $F_0e^{i\omega t}$ and $\hat Xe^{i\omega t}$. Substitution into the equation of motion gives $(k-m\omega^2+ic\omega)\hat X=F_0$. Taking magnitude gives the amplitude formula, while the complex argument gives phase lag. At low frequency, stiffness dominates and $X\approx F_0/k$. At high frequency, inertia dominates and $X\approx F_0/(m\omega^2)$ for constant forcing amplitude. Rotating imbalance has forcing amplitude proportional to $\omega^2$, so that last displacement trend changes.

### Worked examples

#### Example 1: Free decay

Take $m=2$ kg, $k=800$ N/m, and $c=8$ N s/m. The undamped natural frequency is 20 rad/s, or 3.18310 Hz. Critical damping is 80 N s/m, so $\zeta=0.10$. The damped frequency is $20\sqrt{0.99}=19.89975$ rad/s. After one second the exponential envelope is $e^{-0.1(20)(1)}=0.135335$ times its initial envelope value. This envelope ratio is not generally the ratio of the actual displacements at arbitrary times because the cosine and sine also change.

#### Example 2: Harmonic displacement

Apply $F(t)=10\cos(10t)$ N to the same oscillator. Frequency ratio is 0.5 and static displacement amplitude is $10/800=0.0125$ m. Dynamic stiffness magnitude is $\sqrt{(800-2\times10^2)^2+(8\times10)^2}=605.310$ N/m. Thus steady displacement amplitude is 0.0165205 m, or 16.5205 mm. Phase lag is $\operatorname{atan2}(80,600)=0.132552$ rad, or $7.59464^\circ$. The total response still depends on initial conditions until the transient decays.

### Exercises

1. How does natural frequency change if mass increases by a factor of four while stiffness remains fixed?
2. An undamped 5 kg mass is attached to a 2000 N/m spring. Find natural frequency in rad/s and Hz.
3. A viscously damped isolator operates at $r=3$ and $\zeta=0.10$. Calculate force transmissibility.

### Solutions

1. Since $\omega_n\propto m^{-1/2}$, frequency halves.
2. $\omega_n=\sqrt{2000/5}=20$ rad/s and $f_n=20/(2\pi)=3.18310$ Hz.
3. $T_F=\sqrt{1+0.6^2}/\sqrt{(1-9)^2+0.6^2}=0.145365$. Transmitted harmonic force is about 14.5% of excitation amplitude under the stated model.

### Common mistakes

- Mixing Hz with rad/s in mass and stiffness formulas.
- Using peak-to-peak displacement where an amplitude is required.
- Assuming a large resonant response proves the forcing itself is large.
- Applying the constant-force resonance formula to a speed-dependent imbalance force without adjustment.
- Ignoring mounting travel and startup resonance when selecting soft isolators.

### Applications and limits

Use vibration models for machine mounts, rotating equipment, structures, instruments, and condition monitoring. Linear models are local approximations around an operating point. Contact loss, large motion, nonlinear springs, and dry friction require extended models. Measure damping when it materially controls the prediction; it is often more uncertain than mass or stiffness. Validate mode shapes and response levels as well as natural frequencies.

### Further reading

- [MIT OCW: Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) — single- and multiple-DOF vibration modules.
- [MIT OCW: Elements of Mechanical Design](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/) — stiffness, machine integration, and dynamic performance. External materials are linked rather than reproduced.


---

## 34 · Tribology: friction, lubrication, and wear

### Learning map

Prerequisites are statics, fluid viscosity, stress, and heat transfer. Tribology studies interacting surfaces in relative motion. It connects machine design to the condition of contacts, lubricants, contamination, and wear debris. After this chapter, distinguish a friction estimate from a lubrication model and a calibrated wear model from a universal service-life prediction.

### Theory

Real surfaces touch through asperities rather than over their complete apparent area. Local pressures can be much greater than the nominal load divided by projected area. Friction can arise from adhesion, deformation, ploughing, and viscous shear. A coefficient of friction is a property of the interacting system and its condition, not a permanent material constant. Surface finish, temperature, speed, humidity, contamination, and running-in can change it.

Static friction adjusts to oppose impending relative motion up to a limiting magnitude. Kinetic friction is often approximated with a constant coefficient, but velocity dependence, stick-slip, and transition effects may matter. Rolling contact reduces some sliding losses, yet bearing contacts can still contain microslip, hysteretic loss, lubricant churning, and fatigue.

Lubrication regimes are distinguished by how the load is supported. In boundary lubrication, surface films and asperity contacts dominate. In mixed lubrication, fluid pressure and asperity contacts both carry load. In full-film lubrication, a fluid film largely separates the surfaces. Hydrodynamic pressure arises from viscous flow through a converging gap; hydrostatic bearings receive pressure from an external supply. Elastohydrodynamic contacts combine elastic deformation with strong pressure effects on viscosity, as in many rolling bearings and gears.

Wear is progressive material loss or damage associated with surface interaction. Abrasive wear involves cutting or ploughing; adhesive wear involves junction formation and transfer; fatigue wear develops through repeated contact loading; corrosive wear involves chemistry; erosion involves particle or fluid impact. More than one mechanism can operate at once. A test that reproduces only the nominal pressure may fail to reproduce the real wear mechanism.

Lubricant selection must consider viscosity at operating temperature, additives, compatibility with seals and materials, contamination control, oxidation, supply, and maintenance. Increasing viscosity can improve film formation but increase viscous losses and impair cold starts. The Stribeck curve organizes friction trends with operating conditions; it is not a universal numerical design curve independent of geometry.

### Formula handbook

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

### Derivation

For a flat moving plate separated from a fixed plate by a uniform Newtonian film, take steady flow, no pressure gradient, negligible inertia, and no slip. The momentum equation reduces to $d^2u/dy^2=0$. Integrating twice gives $u=C_1y+C_2$. Boundary conditions $u(0)=0$ and $u(h)=U$ give $u=Uy/h$. Therefore $\tau=\mu U/h$, total force $F=\tau A$, and power $P=FU=\mu AU^2/h$. Halving the gap doubles the ideal viscous loss at fixed speed and viscosity. Real contacts may instead heat the lubricant and change viscosity, so the constant-property prediction is not automatically self-consistent.

### Worked examples

#### Example 1: Viscous sliding loss

A plate of area 0.01 m² moves at 2 m/s across a 0.1 mm oil film. Assume $\mu=0.08\ \mathrm{Pa\,s}$, parallel surfaces, and negligible pressure gradient. Convert $h=10^{-4}$ m. Shear stress is $0.08(2)/10^{-4}=1600$ Pa; force is $1600(0.01)=16$ N; power is $16(2)=32$ W. The contact must reject this heat at steady state. This estimate does not establish film stability or account for edges, starvation, or heating-induced viscosity change.

#### Example 2: Calibrated wear estimate

A laboratory wear model uses $k=2\times10^{-6}$, $W=500$ N, $L=10000$ m, and $H=2\times10^9$ Pa. Archard's relation gives $V=2\times10^{-6}(500)(10000)/(2\times10^9)=5\times10^{-9}$ m³, or 5 mm³. If spread uniformly over 100 mm², mean depth is 0.05 mm. This is a model result for the supplied coefficient, not a material's guaranteed wear rate. A different lubricant, abrasive contamination, or transition of mechanism can invalidate the coefficient entirely.

### Exercises

1. A block has normal load 200 N and static friction coefficient 0.30. What tangential force initiates slip in the ideal Coulomb model?
2. If the film gap in Example 1 doubles with all other parameters unchanged, find drag power.
3. Two surfaces have $R_q=0.2$ and 0.3 micrometres. A calculated minimum film thickness is 0.5 micrometres. Find $\lambda$ and explain what it cannot prove.

### Solutions

1. The limiting force is $\mu_sN=60$ N. Below this value, actual static friction balances the applied tangential load rather than remaining at 60 N.
2. Since $P\propto1/h$, power becomes 16 W. The changed gap may also alter load support in a real bearing, outside this simple Couette model.
3. $\lambda=0.5/\sqrt{0.2^2+0.3^2}=1.387$. This suggests substantial surface interaction may need consideration; it does not certify separation everywhere or establish wear life. Roughness statistics, film prediction, alignment, and transient loading remain relevant.

### Common mistakes

Using a dry friction coefficient for a lubricated contact, treating hardness in MPa as Pa, and confusing dynamic with kinematic viscosity are major errors. Archard's coefficient must come from a comparable contact and be defined with its units. A polished surface is not always optimal: lubricant retention, texture direction, and surface chemistry matter.

### Applications and limits

For bearings, seals, gears, guides, clutches, and brakes, combine contact mechanics, lubrication, thermal balance, and contamination control. Record the observed damage mechanism before choosing a corrective action. Vibration, oil debris, temperature, and inspection provide complementary evidence. A lower friction coefficient does not automatically imply lower wear or higher reliability. Manufacturer limits and representative testing are necessary for real selection.

### Further reading

- [ESA, Space Tribology Handbook overview](https://www.esa.int/esapub/bulletin/bullet94/ROB.pdf) — institutional overview of tribological phenomena and space-specific considerations; not the full handbook.
- [ASM Handbook Volume 18 publisher contents](https://www.asminternational.org/wp-content/uploads/files/27533578/27533578-toc.pdf) — topic map for a commercial reference; this link is a contents preview, not a free full textbook.
