# 19. Kinematics of machines and mechanisms

## Learning map

Prerequisites: geometry, vectors, derivatives, statics, and dynamics. A mechanism imposes relationships between motions. Start with degrees of freedom and geometric closure, differentiate for velocity and acceleration, then use virtual work or dynamics to calculate forces. Common mechanisms include four-bars, slider-cranks, cams, gears, screw drives, and belt transmissions.

## Theory

A link is treated as rigid, and a joint restricts relative motion between links. Planar revolute and prismatic joints each permit one relative degree of freedom. A cam contact is a higher pair and generally constrains one relative planar motion when contact is maintained. Counting mobility is useful but can fail for special geometry, redundant constraints, or intermittent contact. Always test the actual constraint equations.

Position analysis is nonlinear and may have several assembly branches. A mechanism can satisfy the same input angle in an open or crossed configuration. Numerical solvers must track the intended branch continuously. A toggle position is a configuration where transmission becomes singular: finite input motion may correspond to very small output motion, and ideal static force ratios can become very large. Elasticity, friction, and clearances bound real forces.

Velocity analysis differentiates geometry; acceleration differentiates again and includes centripetal terms. The instantaneous center is a point of zero instantaneous velocity for relative planar motion, but it is not generally a fixed center of rotation and need not have zero acceleration. Using it for velocities does not automatically justify fixed-axis acceleration formulas.

Cam design must consider displacement, velocity, acceleration, and jerk. Abrupt acceleration changes can excite flexible structures. The pressure angle controls how effectively contact force produces useful follower force, while curvature controls contact geometry and possible undercutting. Gear backlash and joint clearance permit lost motion that ideal kinematic equations omit. Mechanism synthesis works backward from desired motion or positions to link dimensions; analysis checks the motion of a specified design.

## Formula handbook

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

## Derivation

In a slider-crank, the connecting rod's vertical projection cancels the crank's vertical projection: $l\sin\phi=r\sin\theta$. Its horizontal projection is therefore $l\cos\phi=\sqrt{l^2-r^2\sin^2\theta}$ for the selected assembly branch. Adding the crank's horizontal projection gives the exact slider-position equation. Differentiating this geometric equation produces velocity without assuming that the rod is infinitely long. The second harmonic in the long-rod approximation explains why piston motion differs from a pure sinusoid.

## Worked examples

### Example 1: Slider-crank position and speed

Let crank radius $r=0.050$ m, rod length $l=0.200$ m, crank angle $60^\circ$, and crank speed 10 rad/s. The rod's horizontal projection is $\sqrt{0.2^2-0.05^2\sin^260^\circ}=0.195256$ m. Thus slider position is $0.05\cos60^\circ+0.195256=0.220256$ m. The exact derivative gives $dx/d\theta=-0.0488454$ m/rad and velocity $-0.488454$ m/s. The negative sign means motion toward the crank center for increasing angle at this configuration.

### Example 2: Four-bar feasibility

A four-bar has lengths 30, 70, 80, and 100 mm, with the 100 mm link grounded. Four links and four revolute joints give $M=3(4-1)-2(4)=1$. Grashof comparison gives $30+100=130$ mm versus $70+80=150$ mm, so the strict inequality holds. If the 30 mm shortest link is adjacent to ground, this inversion can form a crank-rocker with the shortest link rotating fully. If the shortest link is instead opposite the ground, the inversion differs; length inequality alone does not name every link's motion.

## Exercises

1. A lead screw has 5 mm lead and rotates at 600 rpm. Find ideal linear speed.
2. A 40 mm crank and 160 mm rod form an inline slider-crank. Find slider positions at $0^\circ$ and $180^\circ$, and its stroke.
3. A cycloidal cam rises 20 mm over $\beta=\pi$ radians at constant 5 rad/s. Find its maximum follower speed.

## Solutions

1. 600 rpm is 10 rev/s, so speed is $5(10)=50$ mm/s, or 0.050 m/s.
2. Positions are $160+40=200$ mm and $160-40=120$ mm. Stroke is 80 mm, twice the crank radius.
3. The bracket $1-\cos(2\pi\theta/\beta)$ has maximum 2. Therefore maximum speed is $2h\omega/\beta=0.2/\pi=0.063662$ m/s.

## Common mistakes

- Using degrees directly in a derivative formula written for radians.
- Allowing a numerical solver to jump between assembly branches.
- Treating a mobility count as proof that every configuration is nonsingular.
- Assuming infinite force amplification at a toggle is a usable real design result.
- Confusing thread pitch with lead or ignoring cam-contact separation.

## Applications and limits

Mechanism analysis supports pumps, engines, presses, packaging machines, valves, and positioning equipment. Verify that the entire trajectory clears surrounding geometry and respects joint limits. Add dynamics for acceleration loads and flexibility for high-speed behavior. An ideal motion model can be correct while a real assembly binds because of tolerance, misalignment, or overconstraint; physical prototypes and measured motion close that gap.

## Further reading

- [MIT: FUNdaMentals of Design](https://meddevdesign.mit.edu/fundamentals-of-design/) — linkages and power-transmission lecture resources.
- [MIT OCW: Elements of Mechanical Design](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/) — mechanism integration and design problems. These materials are linked rather than copied.
