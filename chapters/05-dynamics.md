# 05. Engineering dynamics

## Learning map

Prerequisites: statics, vectors, derivatives, integrals, and elementary differential equations. Learn to separate kinematics, which describes motion, from kinetics, which relates motion to force and mass. Use particle models before rigid bodies. Choose force–acceleration, work–energy, or impulse–momentum according to the quantities available. Vibration and mechanism analysis build directly on these tools.

## Theory

Newton's laws apply directly in inertial frames. A frame fixed to an accelerating vehicle requires additional inertial terms if treated as though it were inertial. Position, velocity, and acceleration are vectors; speed is the magnitude of velocity. A body moving at constant speed around a curve still accelerates because its velocity direction changes.

A particle model ignores size and rotation. A rigid body preserves distances between its material points and can translate and rotate simultaneously. Its center of mass obeys the translational equation of motion even when the body rotates. The angular equation is particularly simple about the center of mass for planar motion, or about a fixed axis whose direction does not change. General three-dimensional rotation requires the inertia tensor and gyroscopic terms.

Work–energy eliminates time when force can be expressed along displacement. Constraint forces can do zero work on a selected system even while producing substantial accelerations. An ideal stationary pin does no work at its fixed point; friction at a sliding contact generally does. In rolling without slipping on a stationary rigid surface, the instantaneous contact point has zero velocity, but rolling resistance and deformation can still dissipate energy in real hardware.

Impulse–momentum is useful when forces act over short intervals or their time histories are known. Momentum is conserved only for a system with zero net external impulse. Kinetic energy need not be conserved in a collision. A coefficient of restitution relates the relative normal separation speed to the relative normal approach speed, not the absolute velocities of an arbitrary reference frame.

## Formula handbook

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

## Derivation

For a particle moving along one coordinate, Newton's law is $F=ma$. Substitute $a=v\,dv/dx$ and multiply by $dx$. Integration gives $\int F\,dx=\int mv\,dv=\tfrac12m(v_2^2-v_1^2)$. Thus the work–energy theorem is a rearrangement of the force law, not an additional independent physical law for this model. Conservative forces can be moved into a potential energy $V$, giving $T_1+V_1+W_{nc}=T_2+V_2$.

For a rolling wheel, translation and rotation are linked by $v_G=R\omega$ only under no-slip conditions. Substitution into kinetic energy gives $T=\tfrac12(m+I_G/R^2)v_G^2$. Rotational inertia therefore increases the effective inertia seen in the translational coordinate.

## Worked examples

### Example 1: Accelerating cart

A 15 kg cart starts from rest on a horizontal track. A constant 80 N drive force opposes 20 N of resistance. Net force is 60 N, so $a=60/15=4$ m/s². After 3 s, speed is 12 m/s and travel is 18 m. Work by the net force is $60(18)=1080$ J; kinetic energy is $15(12^2)/2=1080$ J. Agreement checks both the force and displacement calculation. Resistance was assumed constant over this speed range.

### Example 2: Spinning a disk

A uniform 10 kg disk of radius 0.20 m rotates about its fixed central axis. A net torque of 4 N m acts for 2 s from rest. Its inertia is $I=mR^2/2=0.20$ kg m², so $\alpha=20$ rad/s², final speed is 40 rad/s, and rotation is 40 rad. Torque work is $4(40)=160$ J, matching $I\omega^2/2=160$ J. Angular impulse is 8 N m s, matching $I\omega=8$ kg m²/s.

## Exercises

1. A particle moves in a circle of radius 2 m at constant speed 6 m/s. Find its acceleration magnitude and direction.
2. A 5 kg body initially moves at 3 m/s. A collinear positive impulse of 20 N s acts on it. Find final velocity.
3. A uniform solid cylinder rolls without slip at 4 m/s. Its mass is 6 kg. Find total kinetic energy.

## Solutions

1. $a_n=v^2/r=36/2=18$ m/s² toward the center. Tangential acceleration is zero.
2. $5v_2-5(3)=20$, giving $v_2=7$ m/s in the original positive direction.
3. $I_G=mR^2/2$ and $\omega=v/R$. Translation contributes 48 J and rotation 24 J, for 72 J total; the radius cancels.

## Common mistakes

- Equating zero speed at one instant with zero acceleration.
- Using $\sum M_O=I_O\alpha$ about an arbitrary accelerating point without the necessary extra terms.
- Omitting rotational kinetic energy for a rolling body.
- Conserving mechanical energy while ignoring friction, impact loss, or actuator work.
- Applying constant-acceleration equations when force changes strongly with position or speed.

## Applications and limits

Dynamics predicts actuator demand, stopping distances, rotating-machine startup, and mechanism loads. Rigid models exclude elastic waves and structural deformation; fast impacts may require flexible-body or wave models. A prescribed acceleration profile requires force capacity at every instant, not merely adequate average energy. Numerical integration should preserve the expected energy or dissipation trend and should be checked by reducing the time step.

## Further reading

Linked course resources are for deeper study; no source passages are reproduced.

- [MIT OCW: Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) — lectures, worked demonstrations, problems, and solutions.
- [MIT OCW: Design and Manufacturing I](https://ocw.mit.edu/courses/2-007-design-and-manufacturing-i-spring-2009/) — applying dynamics to machines and design projects.
