# 29. Robotics

## Learning map

Prerequisites: vectors, matrices, rigid-body mechanics, mechanisms, control, and programming. Study coordinate frames and forward kinematics before inverse kinematics, Jacobians, dynamics, and planning. Robotics combines geometry with time-dependent force and motion. A robot that can geometrically reach a point may still lack sufficient torque, avoidable collisions, acceptable conditioning, or the sensing needed to reach it reliably.

## Theory

A robot configuration specifies its independent joint coordinates. A task-space pose specifies the position and orientation of a tool or body. Forward kinematics maps joint coordinates to pose. Inverse kinematics asks which joint coordinates produce a desired pose; solutions may be multiple, absent, or continuous. Joint limits and obstacles further restrict feasible solutions.

Coordinate frames make geometric statements precise. A vector's components depend on the frame in which they are expressed. Rotation matrices map components between orthonormal frames and preserve lengths and angles. A homogeneous transformation combines rotation and translation, allowing serial-chain transformations to be composed with matrix multiplication. Matrix order matters because rotations and translations generally do not commute.

The Jacobian maps small joint velocities to task velocities. A singular configuration loses some instantaneous task directions or requires unbounded joint rates in an attempted inverse mapping. This does not necessarily mean the robot breaks or cannot move at all; it means the local mapping has lost rank. Near singularities, measurement errors and limited actuators can produce poor tracking.

Dynamics adds inertia, gravity, Coriolis and centrifugal effects, friction, and external loads. A path is geometric; a trajectory assigns time to that path. The same geometric path can be easy or impossible depending on acceleration, speed, motor torque, and thermal duty. Trajectory generation must therefore consider mechanical and electrical limits together.

Mobile robots add constraints imposed by wheel contact. A differential-drive base cannot translate sideways instantaneously in its ideal no-slip model, although it can reach many poses through combinations of turning and forward motion. Wheel odometry accumulates error from slip, unequal effective radii, and imperfect geometry; absolute sensing or environmental observations can correct drift.

## Formula handbook

Angles are in radians unless stated. For a planar two-link arm, $l_1,l_2$ are lengths (m), $\theta_1,\theta_2$ joint angles, and $x,y$ tool coordinates (m).

**Forward kinematics:**

$$
x=l_1\cos\theta_1+l_2\cos(\theta_1+\theta_2),\qquad y=l_1\sin\theta_1+l_2\sin(\theta_1+\theta_2).
$$

**Position inverse kinematics:**

$$
c_2=\frac{x^2+y^2-l_1^2-l_2^2}{2l_1l_2},\quad \theta_2=\operatorname{atan2}(\pm\sqrt{1-c_2^2},c_2).
$$

Real solutions require $|c_2|\le1$. Then

$$
\theta_1=\operatorname{atan2}(y,x)-\operatorname{atan2}(l_2\sin\theta_2,l_1+l_2\cos\theta_2).
$$

**Two-link planar Jacobian:**

$$
\begin{bmatrix}\dot x\\\dot y\end{bmatrix}=\mathbf J\begin{bmatrix}\dot\theta_1\\\dot\theta_2\end{bmatrix},\qquad
\mathbf J=\begin{bmatrix}-l_1\sin\theta_1-l_2\sin(\theta_1+\theta_2)&-l_2\sin(\theta_1+\theta_2)\\l_1\cos\theta_1+l_2\cos(\theta_1+\theta_2)&l_2\cos(\theta_1+\theta_2)\end{bmatrix}.
$$

**Singularity measure for this arm:**

$$
\det\mathbf J=l_1l_2\sin\theta_2.
$$

**General rigid transform:**

$$
\mathbf T=\begin{bmatrix}\mathbf R&\mathbf p\\\mathbf0^T&1\end{bmatrix},\qquad \mathbf R^T\mathbf R=\mathbf I,\quad \det\mathbf R=1.
$$

**Serial composition and inverse:**

$$
\mathbf T_{ac}=\mathbf T_{ab}\mathbf T_{bc},\qquad \mathbf T^{-1}=\begin{bmatrix}\mathbf R^T&-\mathbf R^T\mathbf p\\\mathbf0^T&1\end{bmatrix}.
$$

**Quasistatic joint load from a task-space force:**

$$
\boldsymbol\tau=\mathbf J^T\mathbf F.
$$

Use consistent frames and signs; $\mathbf F$ is in N and torques in N m. **Manipulator dynamics:**

$$
\mathbf M(\mathbf q)\ddot{\mathbf q}+\mathbf C(\mathbf q,\dot{\mathbf q})\dot{\mathbf q}+\mathbf g(\mathbf q)=\boldsymbol\tau+\mathbf J^T\mathbf F_{\rm ext}.
$$

Friction may be added separately. **Differential-drive kinematics:**

$$
v=\frac r2(\omega_R+\omega_L),\qquad \dot\psi=\frac r b(\omega_R-\omega_L).
$$

$r$ is wheel radius (m), $b$ wheel separation (m), and wheel speeds are rad/s. **Cubic rest-to-rest scalar motion over duration $T$:**

$$
q(t)=q_0+(q_f-q_0)(3s^2-2s^3),\qquad s=t/T,\quad0\le s\le1.
$$

This gives zero endpoint velocity but nonzero endpoint acceleration; jerk-continuous motion needs a different construction.

## Derivation

Differentiate the forward-kinematics equations with respect to time. Every term containing $\theta_1+\theta_2$ produces $(\dot\theta_1+\dot\theta_2)$. Collect coefficients of the two joint rates to obtain the Jacobian. Its transpose force relation follows from virtual work: $\boldsymbol\tau^T\delta\mathbf q=\mathbf F^T\delta\mathbf x$, while $\delta\mathbf x=\mathbf J\delta\mathbf q$. Therefore $\boldsymbol\tau^T\delta\mathbf q=\mathbf F^T\mathbf J\delta\mathbf q$ for arbitrary virtual joint motion, implying $\boldsymbol\tau=\mathbf J^T\mathbf F$. This establishes a direct connection between differential geometry and actuator loading.

## Worked examples

**Example 1 — two-link position.** Let $l_1=0.4\ \mathrm m$, $l_2=0.3\ \mathrm m$, $\theta_1=30^\circ$, and $\theta_2=60^\circ$. The second link points at $90^\circ$ from the global horizontal. Hence $x=0.4\cos30^\circ+0.3\cos90^\circ=0.346410\ \mathrm m$ and $y=0.4\sin30^\circ+0.3\sin90^\circ=0.500000\ \mathrm m$. The Jacobian determinant is $0.4(0.3)\sin60^\circ=0.103923\ \mathrm{m^2}$, which is nonzero. The arm is not singular for planar position at this configuration.

**Example 2 — differential drive.** A base has $r=0.05\ \mathrm m$, $b=0.30\ \mathrm m$, $\omega_R=12\ \mathrm{rad/s}$, and $\omega_L=8\ \mathrm{rad/s}$. Forward speed is $0.05(20)/2=0.50\ \mathrm{m/s}$ and yaw rate is $0.05(4)/0.30=0.666667\ \mathrm{rad/s}$. The instantaneous turning radius is $v/\dot\psi=0.75\ \mathrm m$. In $3\ \mathrm s$ of constant wheel speeds, heading changes by $2.00\ \mathrm{rad}$. These results assume rolling without slip.

## Exercises

1. For $l_1=0.4\ \mathrm m$ and $l_2=0.3\ \mathrm m$, what radial distances are geometrically reachable without joint limits?
2. At $\theta_1=0$ and $\theta_2=90^\circ$, with both links $0.5\ \mathrm m$, find joint torques corresponding to tool force $(0,10)\ \mathrm N$ using $\boldsymbol\tau=\mathbf J^T\mathbf F$.
3. A cubic rest-to-rest move covers $0.20\ \mathrm m$ in $2\ \mathrm s$. Find its maximum speed.

## Solutions

1. The distance from the first joint lies between $|l_1-l_2|=0.10\ \mathrm m$ and $l_1+l_2=0.70\ \mathrm m$. Collision and orientation constraints can shrink this set.
2. The second row of the Jacobian is $(0.5,0)$. Thus the specified force maps to $(5,0)\ \mathrm{N\,m}$. The balancing actuator torque has the opposite sign if the force is defined as an externally applied load.
3. $\dot q=(\Delta q/T)(6s-6s^2)$ peaks at $s=1/2$. Maximum speed is $1.5\Delta q/T=0.15\ \mathrm{m/s}$.

## Common mistakes

- Mixing degrees and radians in software.
- Combining a Jacobian in one frame with a force expressed in another.
- Assuming inverse kinematics returns one unique solution.
- Treating a collision-free path as a torque-feasible trajectory.
- Treating commanded wheel travel as measured ground travel.

## Applications and limits

The formulas support pick-and-place arms, inspection manipulators, mobile bases, and educational prototypes. Real robots require joint limits, collision checking, braking behavior, payload inertia, compliance, sensing, and appropriate safeguards. The ideal models establish a starting point for simulation and measured experiments; they do not qualify a machine for operation near people.

## Further reading

- [Modern Robotics — Mechanics, Planning, and Control](https://modernrobotics.northwestern.edu/): author-hosted book resources, videos, exercises, and software.
- [Modern Robotics author-hosted preprint](https://hades.mech.northwestern.edu/images/9/90/MR-tablet-temporary.pdf): full mathematical treatment; consult the author site for current versions and reuse conditions.
