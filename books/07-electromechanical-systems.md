# Electrical, control, mechatronics, and robotics

Mechanical Engineering Handbook · Expanded edition · 2026-11-07

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [26. Electrical Engineering for Mechanical Engineers](../chapters/26-electrical-engineering.md)
- [27. Control Systems](../chapters/27-control-systems.md)
- [28. Mechatronics and Instrumentation](../chapters/28-mechatronics.md)
- [29. Robotics](../chapters/29-robotics.md)

---

## 26. Electrical Engineering for Mechanical Engineers

### Learning map

Prerequisites: algebra, calculus, complex numbers, and energy conservation. Study DC resistive circuits, energy-storage elements, sinusoidal AC, and electromechanical conversion in that order. Mechanical applications include motor drives, heaters, sensors, solenoids, and instrument power. Circuit calculations describe idealized behavior; selecting real wiring, protection, isolation, and equipment requires the applicable electrical rules and manufacturer ratings.

### Theory

Voltage is electrical potential difference: energy transferred per unit charge. Current is the rate of charge flow. Resistance dissipates electrical energy as heat, while capacitance and inductance store recoverable energy in electric and magnetic fields. Define reference directions before writing equations. A negative solved current means the actual direction opposes the chosen reference; it is not automatically an error.

Kirchhoff's current law expresses charge conservation at a node in the lumped-circuit approximation. Kirchhoff's voltage law follows a closed-loop voltage balance when induced effects are represented appropriately by circuit elements. These approximations assume interconnection dimensions and propagation delays are small relative to the timescale of interest. High-frequency switching can invalidate a simple ideal-wire model through parasitic capacitance and inductance.

In sinusoidal steady state, phasors replace differentiation by multiplication by $j\omega$. Complex impedance describes both amplitude and phase. Use RMS magnitudes consistently for AC power. The apparent power rating of a source is not necessarily equal to its useful real-power output because reactive exchange and waveform distortion can increase current without the same increase in useful work.

A motor couples electrical and mechanical equations. Current produces torque; rotation produces a back electromotive force opposing the applied drive voltage. At startup, back EMF is small, so current can be high. Motor selection must therefore consider startup torque, speed range, continuous heating, intermittent duty, and drive limits, not only rated power.

### Formula handbook

Let $V$ or $v$ be voltage (V), $I$ or $i$ current (A), $R$ resistance ($\Omega$), $C$ capacitance (F), $L$ inductance (H), $t$ time (s), and $\omega$ angular frequency (rad/s). Lowercase often denotes an instantaneous quantity.

**Ohm's law and resistive power:**

$$
V=IR,\qquad P=VI=I^2R=V^2/R.
$$

The last two expressions apply to a resistor with consistent DC or RMS quantities. **Node and loop equations:**

$$
\sum I_{\rm entering}=\sum I_{\rm leaving},\qquad \sum_{\rm loop}V=0.
$$

**Series and parallel resistors:**

$$
R_s=\sum_iR_i,\qquad \frac1{R_p}=\sum_i\frac1{R_i}.
$$

**Unloaded two-resistor voltage divider:**

$$
V_o=V_s\frac{R_2}{R_1+R_2}.
$$

A load across $R_2$ changes it to $R_2\parallel R_L$. **Capacitor and inductor laws under passive sign convention:**

$$
i=C\frac{dv}{dt},\quad E_C=\tfrac12CV^2,\qquad v=L\frac{di}{dt},\quad E_L=\tfrac12LI^2.
$$

Stored energies $E_C,E_L$ are in joules. **Initially uncharged series RC step response:**

$$
v_C(t)=V_s(1-e^{-t/(RC)}),\qquad \tau=RC.
$$

**Sinusoidal RMS and impedance:**

$$
V_{\rm rms}=V_{\rm peak}/\sqrt2,\quad Z_R=R,\quad Z_L=j\omega L,\quad Z_C=1/(j\omega C).
$$

**Single-phase sinusoidal power:**

$$
P=V_{\rm rms}I_{\rm rms}\cos\phi,\quad Q=V_{\rm rms}I_{\rm rms}\sin\phi,\quad |S|=V_{\rm rms}I_{\rm rms}.
$$

$P$ is in W, $Q$ in var, and $|S|$ in VA. **Balanced sinusoidal three-phase real power:**

$$
P=\sqrt3V_{LL}I_L\cos\phi.
$$

$V_{LL}$ is line-to-line RMS voltage and $I_L$ line current. **Idealized permanent-magnet DC motor:**

$$
v=Ri+L\frac{di}{dt}+k_e\omega_m,\quad T=k_ti,\quad J\dot\omega_m=T-T_L-b\omega_m.
$$

$T,T_L$ are torque (N m), $J$ inertia ($\mathrm{kg\,m^2}$), and $b$ viscous damping ($\mathrm{N\,m\,s/rad}$). The torque constant $k_t$ is in N m/A and back-EMF constant $k_e$ in V s/rad; use compatible SI conventions. **Shaft power and efficiency:**

$$
P_{\rm shaft}=T\omega_m,\qquad \eta=P_{\rm shaft}/P_{\rm electrical}.
$$

### Derivation

Connect a constant voltage $V_s$ to a resistor and initially uncharged capacitor in series. Kirchhoff's voltage law gives $V_s=Ri+v_C$. Substitute $i=C\,dv_C/dt$ to obtain $RC\,dv_C/dt+v_C=V_s$. Separate variables and integrate with $v_C(0)=0$: $-\ln(1-v_C/V_s)=t/(RC)$. Exponentiating yields the step response above. At $t=\tau$, the capacitor has reached $1-e^{-1}=63.2\%$ of its final voltage. The initial current is $V_s/R$, and it decays toward zero. The capacitor voltage cannot jump in this ideal model without an impulse of current.

### Worked examples

**Example 1 — loaded sensor divider.** A $12\ \mathrm V$ source feeds $R_1=2\ \mathrm{k\Omega}$ and $R_2=1\ \mathrm{k\Omega}$. Unloaded output is $12(1000/3000)=4.00\ \mathrm V$. Add a $1\ \mathrm{k\Omega}$ instrument input across $R_2$. The lower equivalent resistance becomes $500\ \Omega$, and output becomes $12(500/2500)=2.40\ \mathrm V$. Supply current is $4.80\ \mathrm{mA}$, dividing into $2.40\ \mathrm{mA}$ in each lower branch. A high input impedance matters because the measurement circuit otherwise changes what it measures.

**Example 2 — three-phase motor input.** A balanced sinusoidal supply provides $V_{LL}=400\ \mathrm V$ and $I_L=10\ \mathrm A$ at power factor $0.85$. Real input is $\sqrt3(400)(10)(0.85)=5888.97\ \mathrm W$. With efficiency $0.90$, shaft power is $5300.08\ \mathrm W$. At $1500\ \mathrm{r/min}$, $\omega_m=2\pi(1500/60)=157.080\ \mathrm{rad/s}$, giving shaft torque $33.7413\ \mathrm{N\,m}$. These values assume measured current and stated operating-point efficiency, not an arbitrary motor nameplate prediction.

### Exercises

1. Find the current and power of a $24\ \mathrm V$ supply feeding a $12\ \Omega$ resistor.
2. For $R=10\ \mathrm{k\Omega}$ and $C=10\ \mathrm{\mu F}$, calculate the time constant and capacitor voltage at one time constant after a $5\ \mathrm V$ step.
3. A shaft supplies $10\ \mathrm{N\,m}$ at $1200\ \mathrm{r/min}$. Find mechanical power.

### Solutions

1. Current is $24/12=2\ \mathrm A$. Power is $VI=48\ \mathrm W$. A real resistor must have an appropriate thermal rating and cooling arrangement.
2. $\tau=10000(10\times10^{-6})=0.10\ \mathrm s$. Voltage is $5(1-e^{-1})=3.161\ \mathrm V$.
3. Angular speed is $40\pi\ \mathrm{rad/s}$. Power is $400\pi=1256.64\ \mathrm W$.

### Common mistakes

- Substituting revolutions per minute directly into $P=T\omega$.
- Treating VA as W for an AC load with power factor below unity.
- Using an unloaded divider equation after connecting a low-impedance load.
- Ignoring the energy stored in inductive loads when switching current off.
- Assuming electronic logic voltage is interchangeable with motor supply voltage.

### Applications and limits

These relations support motor sizing, sensor interfaces, power estimates, and troubleshooting low-voltage circuits. Real components add tolerances, temperature dependence, saturation, leakage, and switching losses. Electrical installation and protective-device design require appropriate standards and competent review. For a mechanical system, combine electrical losses with the thermal model: even a correctly sized shaft can be driven by a motor that overheats under its duty cycle.

### Further reading

- [MIT OpenCourseWare — Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/): full lecture and problem sequence.
- [University of Michigan CTMS — modeling and control examples](https://ctms.engin.umich.edu/CTMS/index.php?aux=Home): motor and electromechanical system modeling.


---

## 27. Control Systems

### Learning map

Prerequisites: differential equations, Laplace transforms, mechanical dynamics, circuits, and complex numbers. First model the plant, then analyze its uncontrolled behavior, then choose a feedback structure. The goal is to obtain a useful response despite disturbances and uncertainty while respecting actuator and sensor limits. The University of Michigan control tutorials provide worked implementations; this chapter develops the underlying elementary relations independently.

### Theory

A control system compares a desired reference with a measured output and adjusts an input. The plant is the process being controlled, such as a motor, heated tank, or hydraulic actuator. The controller uses the error, and sometimes other measured states, to select an action. A sensor, filter, communication link, and actuator are part of the loop: their delays and limits affect stability.

Linear time-invariant models have coefficients that do not change with time and obey superposition. They are often obtained by linearizing a nonlinear plant near an operating point. The model may work well for small changes but fail during saturation, switching, backlash, large temperature changes, or flow reversal. State-space models describe internal states; transfer functions describe input-output behavior under specified initial-condition assumptions.

Feedback can reduce sensitivity to plant uncertainty and reject disturbances, but it can also amplify measurement noise or create oscillation. Increasing gain does not automatically improve performance. The loop gain has a frequency-dependent magnitude and phase, and the closed-loop poles determine stability for a finite-dimensional continuous-time LTI model. Delays add phase lag, making aggressive tuning harder.

Proportional action responds to the current error. Integral action accumulates error and can remove a constant steady offset when the closed loop is stable and the actuator has authority. Derivative action responds to rate of change and can add damping, but it is noise-sensitive. Real implementations commonly filter derivative action and prevent the integral state from continuing to grow when the actuator saturates. Controller tuning is therefore both a mathematical and an implementation problem.

### Formula handbook

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

### Derivation

For proportional control $u=K_p(r-y)$ and plant $\tau\dot y+y=Ku$, substitute the controller into the plant:

$$
\tau\dot y+(1+KK_p)y=KK_pr.
$$

Divide by $1+KK_p$ when it is nonzero. The closed-loop time constant is $\tau/(1+KK_p)$ and the steady reference gain is $KK_p/(1+KK_p)$. Thus proportional feedback speeds this ideal first-order plant for positive gain but leaves an offset for a constant reference. This result assumes no delay, saturation, additional poles, or sign reversal. It cannot justify increasing gain without limit on a physical actuator.

### Worked examples

**Example 1 — proportional temperature loop.** A normalized plant has $G(s)=2/(5s+1)$ and proportional controller $K_p=3$. The loop DC gain is $6$, giving $T(s)=6/(5s+7)$. The pole is $-7/5=-1.4\ \mathrm{s^{-1}}$, closed-loop time constant is $5/7=0.714286\ \mathrm s$, and a unit step tends to $6/7=0.857143$. The remaining error is $1/7=0.142857$. A faster response is not the same as zero steady error.

**Example 2 — underdamped response.** Let $\zeta=0.5$ and $\omega_n=10\ \mathrm{rad/s}$. Then $\omega_d=8.66025\ \mathrm{rad/s}$, peak time is $0.362760\ \mathrm s$, and overshoot is $e^{-\pi/\sqrt3}=0.163034$, or $16.3034\%$. The approximate 2% settling time is $4/(0.5\times10)=0.8\ \mathrm s$. This estimate should be checked against the actual time response if a precise requirement is imposed.

### Exercises

1. A first-order sensor has time constant $2\ \mathrm s$. What fraction of a step has it reached after $6\ \mathrm s$?
2. A delay of $0.10\ \mathrm s$ appears at angular frequency $10\ \mathrm{rad/s}$. Find its phase contribution in radians and degrees.
3. Why can an integral controller remain at maximum output after the error changes sign?

### Solutions

1. The fraction is $1-e^{-3}=0.950213$, or $95.02\%$.
2. Phase is $-\omega\theta=-1\ \mathrm{rad}=-57.296^\circ$. The delay magnitude is unity, yet it changes phase substantially.
3. During saturation the integral state may have accumulated a large value. It must unwind before the output leaves saturation. Anti-windup uses clamping or feedback from the actual limited actuator command to manage this state.

### Common mistakes

- Applying the final value theorem to an unstable closed loop.
- Using an unfiltered derivative on noisy measurement data.
- Treating a continuous-time design as unchanged after slow digital sampling.
- Forgetting whether the plant gain is positive or negative.
- Inferring stability from a short, apparently quiet simulation alone.

### Applications and limits

Speed, position, temperature, pressure, and liquid-level loops all use these ideas. Identify an operating region and disturbances, measure actuator limits, and begin with modest performance targets. Evaluate stability margins, transient response, noise sensitivity, and saturation recovery together. Higher-order, multivariable, nonlinear, and safety-related control systems require methods beyond these introductory formulas.

### Further reading

- [University of Michigan — Control Tutorials for MATLAB and Simulink](https://ctms.engin.umich.edu/CTMS/index.php?aux=Home): modeling, PID, frequency response, state space, and digital control.
- [University of Michigan — Classical Control lecture notes](https://seiler.engin.umich.edu/wp-content/uploads/sites/99/2020/01/ClassicalControl_Master.pdf): feedback theory and controller implementation issues.


---

## 28. Mechatronics and Instrumentation

### Learning map

Prerequisites: circuits, mechanics, measurement uncertainty, programming, and control. Mechatronics combines a physical mechanism, sensing, computation, and actuation into one working system. Follow the signal from the physical quantity to sensor output, analog conditioning, sampling, numerical processing, drive command, and mechanical response. A successful design considers the complete chain instead of optimizing each part independently.

### Theory

A sensor converts a physical quantity into a measurable signal. Its sensitivity is the change in output per change in input. Offset, gain error, nonlinearity, hysteresis, drift, resolution, and noise describe different imperfections. Calibration determines a relationship under stated conditions; it does not guarantee that the relationship holds indefinitely or outside the calibrated range.

An analog-to-digital converter samples a voltage and assigns a finite code. Sampling discretizes time; quantization discretizes amplitude. A large nominal bit count does not automatically mean accurate measurement because reference errors, front-end noise, input loading, and nonlinearity remain. The quantization conventions below use uniform bins and their midpoints; a real ADC's data sheet specifies transition levels and endpoint behavior.

Before sampling, an analog anti-alias filter limits unwanted high-frequency content. Once a high-frequency disturbance has aliased into the signal band, a subsequent digital low-pass filter generally cannot distinguish it from a real low-frequency signal. Sampling rate must also leave room for practical filter transition bands, timing jitter, and control delay.

Actuation converts an electrical, pneumatic, or hydraulic command into force, motion, or heat. A PWM driver switches power rapidly while adjusting duty ratio. The load's electrical and mechanical dynamics may average the switching, but peak current and switching losses still exist. A motor gearbox trades speed for torque while adding efficiency loss, backlash, compliance, and reflected inertia.

Embedded software must handle timing, units, communication failures, and limits as part of the physical design. The same numerical command can produce different real motion if supply voltage falls or a load jams. Use measured feedback when the required quantity cannot be inferred reliably from the command alone.

### Formula handbook

Let $x$ be a physical input and $v$ sensor voltage (V). **Linear calibration:**

$$
v=ax+b,\qquad x=\frac{v-b}{a}.
$$

$a$ is sensitivity (V per input unit), and $b$ offset (V). **Ideal uniform $N$-bit ADC step:**

$$
q=\frac{V_{\max}-V_{\min}}{2^N}.
$$

With midpoint reconstruction and no saturation, quantization error satisfies

$$
|e_q|\le q/2,\qquad \sigma_q=q/\sqrt{12}.
$$

The standard deviation assumes a uniform error distribution; deterministic signals need not satisfy that statistical model. **Ideal full-scale sine quantization SNR:**

$$
\mathrm{SNR}_{\rm dB}\approx6.02N+1.76.
$$

This excludes other noise, clipping, and distortion. **Sampling condition for a strictly band-limited signal:**

$$
f_s>2f_{\max},\qquad T_s=1/f_s.
$$

Frequencies are in Hz and $T_s$ in seconds. **First-order RC low-pass cutoff:**

$$
f_c=\frac1{2\pi RC}.
$$

**PWM duty and ideal unipolar average voltage:**

$$
D=\frac{t_{\rm on}}{T},\qquad \overline V=DV_s.
$$

For a resistor switched between $V_s$ and zero, actual mean power is

$$
\overline P=\frac{D V_s^2}{R}.
$$

It is not $(\overline V)^2/R$. **Ideal gear speed relation and torque with efficiency:**

$$
\omega_o=\frac{\omega_m}{G},\qquad T_o=\eta G T_m.
$$

$G>1$ denotes reduction ratio. **Load inertia reflected through an ideal rigid gear:**

$$
J_{\rm reflected}=\frac{J_L}{G^2}.
$$

**Encoder angular increment:**

$$
\Delta\theta=\frac{2\pi}{N_c}.
$$

$N_c$ is actual counted transitions per revolution, including the chosen decoding mode. **First-order digital low-pass filter:**

$$
y_k=\alpha x_k+(1-\alpha)y_{k-1},\qquad 0<\alpha\le1.
$$

For a matched sampled exponential pole, $\alpha=1-e^{-T_s/\tau}$. This filter adds lag.

### Derivation

An ideal $N$-bit converter has $2^N$ possible codes. Dividing its voltage span by the number of bins gives $q$. If each bin is represented by its midpoint, the largest distance to that midpoint is $q/2$. Under a uniform error assumption, variance is

$$
\sigma_q^2=\frac1q\int_{-q/2}^{q/2}e^2de=\frac{q^2}{12}.
$$

The calculation explains why adding a bit halves ideal quantization step. It does not halve every real measurement error. For example, a fixed reference-voltage error scales all readings independently of bit count. This distinction is central when deciding whether a better ADC or a better sensor and reference will improve a system.

### Worked examples

**Example 1 — pressure measurement resolution.** A linear pressure sensor produces $0.5$ to $4.5\ \mathrm V$ for $0$ to $1000\ \mathrm{kPa}$. Its sensitivity is $0.004\ \mathrm{V/kPa}$. A 12-bit ADC spans $0$ to $5\ \mathrm V$, so $q=5/4096=0.001220703\ \mathrm V$. The pressure increment is $q/a=0.305176\ \mathrm{kPa}$, with ideal midpoint quantization bound $\pm0.152588\ \mathrm{kPa}$. At $2.5\ \mathrm V$, the inferred pressure is $(2.5-0.5)/0.004=500\ \mathrm{kPa}$. These are resolution figures, not an accuracy specification for the sensor assembly.

**Example 2 — geared motor.** A motor supplies $0.20\ \mathrm{N\,m}$ at $3000\ \mathrm{r/min}$ through a $20{:}1$ reducer with efficiency $0.80$. Output speed is $150\ \mathrm{r/min}$ and output torque is $0.80(20)(0.20)=3.20\ \mathrm{N\,m}$. Motor shaft power is $0.20[2\pi(3000/60)]=62.8319\ \mathrm W$; output power is $50.2655\ \mathrm W$. A load inertia of $0.040\ \mathrm{kg\,m^2}$ reflects as $0.040/20^2=0.000100\ \mathrm{kg\,m^2}$ in the ideal kinematic inertia relation. Add motor and gear inertia separately.

### Exercises

1. A 10-bit ADC spans $0$ to $3.3\ \mathrm V$. Find its ideal bin width.
2. A $12\ \mathrm V$ source supplies a $6\ \Omega$ heater by PWM at $D=0.25$. Find average voltage and average heating power.
3. An encoder provides 600 cycles per revolution and is decoded on four transitions per cycle. Find angular count increment in degrees.

### Solutions

1. $q=3.3/1024=0.00322266\ \mathrm V$, or $3.223\ \mathrm{mV}$.
2. Average voltage is $3\ \mathrm V$. Heating power is $D V_s^2/R=0.25(144)/6=6\ \mathrm W$. Squaring the average voltage would incorrectly give $1.5\ \mathrm W$.
3. $N_c=2400$ counts/revolution, so the increment is $360/2400=0.15^\circ$. Mechanical backlash and encoder mounting can dominate actual position uncertainty.

### Common mistakes

- Confusing resolution, repeatability, and accuracy.
- Using $2^N-1$ in a bin-width formula without stating an endpoint convention.
- Assuming PWM duty is directly proportional to motor speed under every load.
- Ignoring sensor settling time, communication latency, and sample timestamp.
- Choosing a fast controller without measuring actual loop execution time.

### Applications and limits

Mechatronics supports automated inspection, temperature regulation, positioning, and small robotic machines. A useful commissioning record includes wiring, signal ranges, calibration data, unit conversions, sample period, actuator limits, and observed failure behavior. The examples are component-level models. Real performance requires electrical noise control, thermal design, measured response, and mechanically safe limits.

### Further reading

- [Analog Devices — noise and distortion in data converters](https://www.analog.com/en/resources/technical-articles/2022/07/16/11/45/managing-noise-in-the-signal-chain-part-2-noise-and-distortion-in-data-converters.html): ADC quantization and practical noise context.
- [STMicroelectronics — Understanding and minimising ADC conversion errors](https://www.st.com/resource/en/application_note/an1636-understanding-and-minimising-adc-conversion-errors-stmicroelectronics.pdf): converter error mechanisms and practical design guidance.
- [University of Michigan CTMS](https://ctms.engin.umich.edu/CTMS/index.php?aux=Home): motor and sampled-control examples.


---

## 29. Robotics

### Learning map

Prerequisites: vectors, matrices, rigid-body mechanics, mechanisms, control, and programming. Study coordinate frames and forward kinematics before inverse kinematics, Jacobians, dynamics, and planning. Robotics combines geometry with time-dependent force and motion. A robot that can geometrically reach a point may still lack sufficient torque, avoidable collisions, acceptable conditioning, or the sensing needed to reach it reliably.

### Theory

A robot configuration specifies its independent joint coordinates. A task-space pose specifies the position and orientation of a tool or body. Forward kinematics maps joint coordinates to pose. Inverse kinematics asks which joint coordinates produce a desired pose; solutions may be multiple, absent, or continuous. Joint limits and obstacles further restrict feasible solutions.

Coordinate frames make geometric statements precise. A vector's components depend on the frame in which they are expressed. Rotation matrices map components between orthonormal frames and preserve lengths and angles. A homogeneous transformation combines rotation and translation, allowing serial-chain transformations to be composed with matrix multiplication. Matrix order matters because rotations and translations generally do not commute.

The Jacobian maps small joint velocities to task velocities. A singular configuration loses some instantaneous task directions or requires unbounded joint rates in an attempted inverse mapping. This does not necessarily mean the robot breaks or cannot move at all; it means the local mapping has lost rank. Near singularities, measurement errors and limited actuators can produce poor tracking.

Dynamics adds inertia, gravity, Coriolis and centrifugal effects, friction, and external loads. A path is geometric; a trajectory assigns time to that path. The same geometric path can be easy or impossible depending on acceleration, speed, motor torque, and thermal duty. Trajectory generation must therefore consider mechanical and electrical limits together.

Mobile robots add constraints imposed by wheel contact. A differential-drive base cannot translate sideways instantaneously in its ideal no-slip model, although it can reach many poses through combinations of turning and forward motion. Wheel odometry accumulates error from slip, unequal effective radii, and imperfect geometry; absolute sensing or environmental observations can correct drift.

### Formula handbook

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

### Derivation

Differentiate the forward-kinematics equations with respect to time. Every term containing $\theta_1+\theta_2$ produces $(\dot\theta_1+\dot\theta_2)$. Collect coefficients of the two joint rates to obtain the Jacobian. Its transpose force relation follows from virtual work: $\boldsymbol\tau^T\delta\mathbf q=\mathbf F^T\delta\mathbf x$, while $\delta\mathbf x=\mathbf J\delta\mathbf q$. Therefore $\boldsymbol\tau^T\delta\mathbf q=\mathbf F^T\mathbf J\delta\mathbf q$ for arbitrary virtual joint motion, implying $\boldsymbol\tau=\mathbf J^T\mathbf F$. This establishes a direct connection between differential geometry and actuator loading.

### Worked examples

**Example 1 — two-link position.** Let $l_1=0.4\ \mathrm m$, $l_2=0.3\ \mathrm m$, $\theta_1=30^\circ$, and $\theta_2=60^\circ$. The second link points at $90^\circ$ from the global horizontal. Hence $x=0.4\cos30^\circ+0.3\cos90^\circ=0.346410\ \mathrm m$ and $y=0.4\sin30^\circ+0.3\sin90^\circ=0.500000\ \mathrm m$. The Jacobian determinant is $0.4(0.3)\sin60^\circ=0.103923\ \mathrm{m^2}$, which is nonzero. The arm is not singular for planar position at this configuration.

**Example 2 — differential drive.** A base has $r=0.05\ \mathrm m$, $b=0.30\ \mathrm m$, $\omega_R=12\ \mathrm{rad/s}$, and $\omega_L=8\ \mathrm{rad/s}$. Forward speed is $0.05(20)/2=0.50\ \mathrm{m/s}$ and yaw rate is $0.05(4)/0.30=0.666667\ \mathrm{rad/s}$. The instantaneous turning radius is $v/\dot\psi=0.75\ \mathrm m$. In $3\ \mathrm s$ of constant wheel speeds, heading changes by $2.00\ \mathrm{rad}$. These results assume rolling without slip.

### Exercises

1. For $l_1=0.4\ \mathrm m$ and $l_2=0.3\ \mathrm m$, what radial distances are geometrically reachable without joint limits?
2. At $\theta_1=0$ and $\theta_2=90^\circ$, with both links $0.5\ \mathrm m$, find joint torques corresponding to tool force $(0,10)\ \mathrm N$ using $\boldsymbol\tau=\mathbf J^T\mathbf F$.
3. A cubic rest-to-rest move covers $0.20\ \mathrm m$ in $2\ \mathrm s$. Find its maximum speed.

### Solutions

1. The distance from the first joint lies between $|l_1-l_2|=0.10\ \mathrm m$ and $l_1+l_2=0.70\ \mathrm m$. Collision and orientation constraints can shrink this set.
2. The second row of the Jacobian is $(0.5,0)$. Thus the specified force maps to $(5,0)\ \mathrm{N\,m}$. The balancing actuator torque has the opposite sign if the force is defined as an externally applied load.
3. $\dot q=(\Delta q/T)(6s-6s^2)$ peaks at $s=1/2$. Maximum speed is $1.5\Delta q/T=0.15\ \mathrm{m/s}$.

### Common mistakes

- Mixing degrees and radians in software.
- Combining a Jacobian in one frame with a force expressed in another.
- Assuming inverse kinematics returns one unique solution.
- Treating a collision-free path as a torque-feasible trajectory.
- Treating commanded wheel travel as measured ground travel.

### Applications and limits

The formulas support pick-and-place arms, inspection manipulators, mobile bases, and educational prototypes. Real robots require joint limits, collision checking, braking behavior, payload inertia, compliance, sensing, and appropriate safeguards. The ideal models establish a starting point for simulation and measured experiments; they do not qualify a machine for operation near people.

### Further reading

- [Modern Robotics — Mechanics, Planning, and Control](https://modernrobotics.northwestern.edu/): author-hosted book resources, videos, exercises, and software.
- [Modern Robotics author-hosted preprint](https://hades.mech.northwestern.edu/images/9/90/MR-tablet-temporary.pdf): full mathematical treatment; consult the author site for current versions and reuse conditions.
