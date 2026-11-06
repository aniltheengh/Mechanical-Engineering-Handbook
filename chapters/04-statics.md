# 04. Engineering statics

## Learning map

Prerequisites: vectors, trigonometry, SI units, and elementary integration. The goal is to turn a physical assembly into free-body diagrams, determine support reactions and member forces, and recognize when equilibrium alone cannot determine the answer. Statics supplies the loads used in strength, machine design, piping-support, and foundation calculations. Study particles first, rigid bodies second, and assemblies third.

## Theory

A body is in static equilibrium when its linear and angular accelerations vanish. This is a statement about the resultant external force and moment; it does not mean that every internal stress is zero. A support carries a reaction because it prevents a particular displacement. An ideal planar roller provides one normal force, a pin two force components, and a fixed end two force components plus a moment. These are models of actual contact stiffness and connection behavior.

A free-body diagram isolates a selected body, replaces removed connections by their forces, and shows dimensions needed for moment arms. Weight acts at the center of mass. A cable pulls along its own axis; an ideal frictionless pulley changes direction without changing cable tension. A two-force member carries collinear end forces only when it has exactly two applied forces and negligible self-weight. A truss idealization therefore requires pin joints and joint-applied loads.

There are three independent equilibrium equations for a planar rigid body and six in three dimensions. More unknowns generally require deformation compatibility and constitutive laws. Merely counting equations is insufficient: support geometry may leave a mechanism or make equations dependent. A beam with two horizontal rollers, for example, has no horizontal restraint regardless of equation counting.

Distributed loads may be replaced by a statically equivalent resultant for external reactions. That replacement does not preserve local bending and shear everywhere inside the loaded interval. Static friction is a variable reaction that opposes impending relative motion. It reaches its limiting magnitude only at impending slip. After motion begins, a separate kinetic-friction model is needed.

## Formula handbook

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

## Derivation

Consider a simply supported beam of span $L$, with a downward point load $P$ a distance $a$ from the left support and a uniform downward load $w$ over the entire span. Replace the distributed load by $wL$ acting at $L/2$. Taking moments about the left support eliminates its unknown reaction:

$$
R_B L-Pa-wL(L/2)=0.
$$

Thus $R_B=Pa/L+wL/2$. Vertical equilibrium gives $R_A=P+wL-R_B$. This derivation explains why increasing the distance of a point load from the left support increases the right reaction. Setting $P=0$ recovers equal reactions for a symmetric uniform load; setting $a=0$ makes the point load act directly into the left support.

## Worked examples

### Example 1: Beam support reactions

Let $L=6$ m, $P=12$ kN at $a=2$ m, and $w=2$ kN/m. The distributed load is 12 kN at the midpoint. Moment equilibrium gives $R_B=(12\times2+12\times3)/6=10$ kN. Force equilibrium then gives $R_A=24-10=14$ kN. The residual moment is $10\times6-12\times2-12\times3=0$ kN m. These are external reactions; determining the largest bending stress still requires a section-force analysis and a section geometry.

### Example 2: Crate on an incline

An 80 kg crate rests on a $25^\circ$ incline with $\mu_s=0.50$. Use $g=9.81$ m/s². Normal equilibrium gives $N=mg\cos25^\circ=711.27$ N. Downslope weight is $mg\sin25^\circ=331.67$ N. The maximum available static friction is 355.64 N, so equilibrium is possible. Actual friction is 331.67 N upslope, not 355.64 N. The limiting slope is $\arctan0.50=26.565^\circ$, assuming the crate does not tip first.

## Exercises

1. A 4 m beam has an 8 kN point load 1 m from its left support. Find both vertical reactions.
2. A triangular load increases from zero to 3 kN/m over 6 m. Find its resultant and location from the zero-load end.
3. A horizontal 100 N force acts in the positive $x$ direction at point $(0,0.4)$ m. Find its moment about the origin, including sign.

## Solutions

1. Right reaction is $8(1)/4=2$ kN; left reaction is $8-2=6$ kN. Check that the larger reaction is closer to the load.
2. The resultant is the triangle area, $3(6)/2=9$ kN. It acts at $2(6)/3=4$ m from the zero-load end.
3. $M_z=xF_y-yF_x=0-0.4(100)=-40$ N m. The negative sign means clockwise.

## Common mistakes

- Mixing a distance along the force with the perpendicular moment arm.
- Treating friction as $\mu_sN$ before proving impending slip.
- Including internal joint forces twice on a whole-assembly free-body diagram.
- Replacing a distributed load by a resultant before calculating internal forces within its footprint.
- Solving three planar equations without checking whether the support arrangement is stable.

## Applications and limits

Use statics for slow-loaded brackets, pipe supports, cranes at rest, and initial machine load paths. Verify the actual operating load cases: startup, shutdown, wind, thermal movement, fluid transients, and lifting can invalidate a purely static representation. Large deformation may change moment arms enough to require equilibrium on the deformed shape. For indeterminate structures, proceed to compatibility and stiffness methods rather than adding invented reaction assumptions.

## Further reading

These are linked learning resources; their text and figures are not reproduced here.

- [MIT OCW: Mechanics and Materials I](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/) — equilibrium, compatibility, and constitutive modeling.
- [MIT OCW: Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) — free-body diagrams and the transition from equilibrium to motion.
