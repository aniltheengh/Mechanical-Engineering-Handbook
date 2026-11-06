# 27. Control Systems

## Learning map

Prerequisites: differential equations, Laplace transforms, mechanical dynamics, circuits, and complex numbers. First model the plant, then analyze its uncontrolled behavior, then choose a feedback structure. The goal is to obtain a useful response despite disturbances and uncertainty while respecting actuator and sensor limits. The University of Michigan control tutorials provide worked implementations; this chapter develops the underlying elementary relations independently.

## Theory

A control system compares a desired reference with a measured output and adjusts an input. The plant is the process being controlled, such as a motor, heated tank, or hydraulic actuator. The controller uses the error, and sometimes other measured states, to select an action. A sensor, filter, communication link, and actuator are part of the loop: their delays and limits affect stability.

Linear time-invariant models have coefficients that do not change with time and obey superposition. They are often obtained by linearizing a nonlinear plant near an operating point. The model may work well for small changes but fail during saturation, switching, backlash, large temperature changes, or flow reversal. State-space models describe internal states; transfer functions describe input-output behavior under specified initial-condition assumptions.

Feedback can reduce sensitivity to plant uncertainty and reject disturbances, but it can also amplify measurement noise or create oscillation. Increasing gain does not automatically improve performance. The loop gain has a frequency-dependent magnitude and phase, and the closed-loop poles determine stability for a finite-dimensional continuous-time LTI model. Delays add phase lag, making aggressive tuning harder.

Proportional action responds to the current error. Integral action accumulates error and can remove a constant steady offset when the closed loop is stable and the actuator has authority. Derivative action responds to rate of change and can add damping, but it is noise-sensitive. Real implementations commonly filter derivative action and prevent the integral state from continuing to grow when the actuator saturates. Controller tuning is therefore both a mathematical and an implementation problem.

## Formula handbook

Let $r$ be reference, $y$ measured output, $e$ error, and $u$ control input. Each has the physical units of its signal; controller gains must convert between those units.

$$
e(t)=r(t)-y(t),\qquad u(t)=K_pe(t)+K_i\int_0^t e(\tau)d\tau+K_d\frac{de}{dt}.
$$

For zero initial conditions, a plant transfer function is $G(s)=Y(s)/U(s)$. The Laplace variable $s$ has units $\mathrm{s^{-1}}$. **Unity negative feedback with controller $C(s)$:**

$$
T(s)=\frac{Y}{R}=\frac{C(s)G(s)}{1+C(s)G(s)},\qquad S(s)=\frac1{1+C(s)G(s)}.
$$

These are complementary sensitivity and sensitivity: $S+T=1$. **First-order plant and unit-step response:**

$$
G(s)=\frac K{\tau s+1},\qquad y(t)=K(1-e^{-t/\tau}),\quad t\ge0.
$$

$\tau>0$ is the time constant (s); $K$ has output/input units. **Standard second-order form:**

$$
G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}.
$$

$\omega_n$ is undamped natural frequency (rad/s), $\zeta$ damping ratio. For $0<\zeta<1$:

$$
\omega_d=\omega_n\sqrt{1-\zeta^2},\qquad t_p=\frac\pi{\omega_d},\qquad M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}.
$$

$M_p$ is overshoot as a fraction. A commonly useful approximate 2% settling time, for a dominant underdamped second-order response, is

$$
t_s\approx\frac4{\zeta\omega_n}.
$$

It is not a universal exact formula. **Final value theorem, only when its stability conditions hold:**

$$
\lim_{t\to\infty}e(t)=\lim_{s\to0}sE(s).
$$

**State-space representation:**

$$
\dot{\mathbf x}=\mathbf A\mathbf x+\mathbf B\mathbf u,\qquad \mathbf y=\mathbf C\mathbf x+\mathbf D\mathbf u.
$$

**Pure time delay:**

$$
G_d(s)=e^{-s\theta},\qquad \angle G_d(j\omega)=-\omega\theta.
$$

Delay $\theta$ is in seconds and phase in radians. **Forward-Euler integral update:**

$$
I_{k+1}=I_k+K_iT_se_k.
$$

$T_s$ is sample period; the digital implementation's stability must be checked separately.

## Derivation

For proportional control $u=K_p(r-y)$ and plant $\tau\dot y+y=Ku$, substitute the controller into the plant:

$$
\tau\dot y+(1+KK_p)y=KK_pr.
$$

Divide by $1+KK_p$ when it is nonzero. The closed-loop time constant is $\tau/(1+KK_p)$ and the steady reference gain is $KK_p/(1+KK_p)$. Thus proportional feedback speeds this ideal first-order plant for positive gain but leaves an offset for a constant reference. This result assumes no delay, saturation, additional poles, or sign reversal. It cannot justify increasing gain without limit on a physical actuator.

## Worked examples

**Example 1 — proportional temperature loop.** A normalized plant has $G(s)=2/(5s+1)$ and proportional controller $K_p=3$. The loop DC gain is $6$, giving $T(s)=6/(5s+7)$. The pole is $-7/5=-1.4\ \mathrm{s^{-1}}$, closed-loop time constant is $5/7=0.714286\ \mathrm s$, and a unit step tends to $6/7=0.857143$. The remaining error is $1/7=0.142857$. A faster response is not the same as zero steady error.

**Example 2 — underdamped response.** Let $\zeta=0.5$ and $\omega_n=10\ \mathrm{rad/s}$. Then $\omega_d=8.66025\ \mathrm{rad/s}$, peak time is $0.362760\ \mathrm s$, and overshoot is $e^{-\pi/\sqrt3}=0.163034$, or $16.3034\%$. The approximate 2% settling time is $4/(0.5\times10)=0.8\ \mathrm s$. This estimate should be checked against the actual time response if a precise requirement is imposed.

## Exercises

1. A first-order sensor has time constant $2\ \mathrm s$. What fraction of a step has it reached after $6\ \mathrm s$?
2. A delay of $0.10\ \mathrm s$ appears at angular frequency $10\ \mathrm{rad/s}$. Find its phase contribution in radians and degrees.
3. Why can an integral controller remain at maximum output after the error changes sign?

## Solutions

1. The fraction is $1-e^{-3}=0.950213$, or $95.02\%$.
2. Phase is $-\omega\theta=-1\ \mathrm{rad}=-57.296^\circ$. The delay magnitude is unity, yet it changes phase substantially.
3. During saturation the integral state may have accumulated a large value. It must unwind before the output leaves saturation. Anti-windup uses clamping or feedback from the actual limited actuator command to manage this state.

## Common mistakes

- Applying the final value theorem to an unstable closed loop.
- Using an unfiltered derivative on noisy measurement data.
- Treating a continuous-time design as unchanged after slow digital sampling.
- Forgetting whether the plant gain is positive or negative.
- Inferring stability from a short, apparently quiet simulation alone.

## Applications and limits

Speed, position, temperature, pressure, and liquid-level loops all use these ideas. Identify an operating region and disturbances, measure actuator limits, and begin with modest performance targets. Evaluate stability margins, transient response, noise sensitivity, and saturation recovery together. Higher-order, multivariable, nonlinear, and safety-related control systems require methods beyond these introductory formulas.

## Further reading

- [University of Michigan — Control Tutorials for MATLAB and Simulink](https://ctms.engin.umich.edu/CTMS/index.php?aux=Home): modeling, PID, frequency response, state space, and digital control.
- [University of Michigan — Classical Control lecture notes](https://seiler.engin.umich.edu/wp-content/uploads/sites/99/2020/01/ClassicalControl_Master.pdf): feedback theory and controller implementation issues.
