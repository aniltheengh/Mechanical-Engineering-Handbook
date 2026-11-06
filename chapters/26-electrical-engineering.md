# 26. Electrical Engineering for Mechanical Engineers

## Learning map

Prerequisites: algebra, calculus, complex numbers, and energy conservation. Study DC resistive circuits, energy-storage elements, sinusoidal AC, and electromechanical conversion in that order. Mechanical applications include motor drives, heaters, sensors, solenoids, and instrument power. Circuit calculations describe idealized behavior; selecting real wiring, protection, isolation, and equipment requires the applicable electrical rules and manufacturer ratings.

## Theory

Voltage is electrical potential difference: energy transferred per unit charge. Current is the rate of charge flow. Resistance dissipates electrical energy as heat, while capacitance and inductance store recoverable energy in electric and magnetic fields. Define reference directions before writing equations. A negative solved current means the actual direction opposes the chosen reference; it is not automatically an error.

Kirchhoff's current law expresses charge conservation at a node in the lumped-circuit approximation. Kirchhoff's voltage law follows a closed-loop voltage balance when induced effects are represented appropriately by circuit elements. These approximations assume interconnection dimensions and propagation delays are small relative to the timescale of interest. High-frequency switching can invalidate a simple ideal-wire model through parasitic capacitance and inductance.

In sinusoidal steady state, phasors replace differentiation by multiplication by $j\omega$. Complex impedance describes both amplitude and phase. Use RMS magnitudes consistently for AC power. The apparent power rating of a source is not necessarily equal to its useful real-power output because reactive exchange and waveform distortion can increase current without the same increase in useful work.

A motor couples electrical and mechanical equations. Current produces torque; rotation produces a back electromotive force opposing the applied drive voltage. At startup, back EMF is small, so current can be high. Motor selection must therefore consider startup torque, speed range, continuous heating, intermittent duty, and drive limits, not only rated power.

## Formula handbook

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

## Derivation

Connect a constant voltage $V_s$ to a resistor and initially uncharged capacitor in series. Kirchhoff's voltage law gives $V_s=Ri+v_C$. Substitute $i=C\,dv_C/dt$ to obtain $RC\,dv_C/dt+v_C=V_s$. Separate variables and integrate with $v_C(0)=0$: $-\ln(1-v_C/V_s)=t/(RC)$. Exponentiating yields the step response above. At $t=\tau$, the capacitor has reached $1-e^{-1}=63.2\%$ of its final voltage. The initial current is $V_s/R$, and it decays toward zero. The capacitor voltage cannot jump in this ideal model without an impulse of current.

## Worked examples

**Example 1 — loaded sensor divider.** A $12\ \mathrm V$ source feeds $R_1=2\ \mathrm{k\Omega}$ and $R_2=1\ \mathrm{k\Omega}$. Unloaded output is $12(1000/3000)=4.00\ \mathrm V$. Add a $1\ \mathrm{k\Omega}$ instrument input across $R_2$. The lower equivalent resistance becomes $500\ \Omega$, and output becomes $12(500/2500)=2.40\ \mathrm V$. Supply current is $4.80\ \mathrm{mA}$, dividing into $2.40\ \mathrm{mA}$ in each lower branch. A high input impedance matters because the measurement circuit otherwise changes what it measures.

**Example 2 — three-phase motor input.** A balanced sinusoidal supply provides $V_{LL}=400\ \mathrm V$ and $I_L=10\ \mathrm A$ at power factor $0.85$. Real input is $\sqrt3(400)(10)(0.85)=5888.97\ \mathrm W$. With efficiency $0.90$, shaft power is $5300.08\ \mathrm W$. At $1500\ \mathrm{r/min}$, $\omega_m=2\pi(1500/60)=157.080\ \mathrm{rad/s}$, giving shaft torque $33.7413\ \mathrm{N\,m}$. These values assume measured current and stated operating-point efficiency, not an arbitrary motor nameplate prediction.

## Exercises

1. Find the current and power of a $24\ \mathrm V$ supply feeding a $12\ \Omega$ resistor.
2. For $R=10\ \mathrm{k\Omega}$ and $C=10\ \mathrm{\mu F}$, calculate the time constant and capacitor voltage at one time constant after a $5\ \mathrm V$ step.
3. A shaft supplies $10\ \mathrm{N\,m}$ at $1200\ \mathrm{r/min}$. Find mechanical power.

## Solutions

1. Current is $24/12=2\ \mathrm A$. Power is $VI=48\ \mathrm W$. A real resistor must have an appropriate thermal rating and cooling arrangement.
2. $\tau=10000(10\times10^{-6})=0.10\ \mathrm s$. Voltage is $5(1-e^{-1})=3.161\ \mathrm V$.
3. Angular speed is $40\pi\ \mathrm{rad/s}$. Power is $400\pi=1256.64\ \mathrm W$.

## Common mistakes

- Substituting revolutions per minute directly into $P=T\omega$.
- Treating VA as W for an AC load with power factor below unity.
- Using an unloaded divider equation after connecting a low-impedance load.
- Ignoring the energy stored in inductive loads when switching current off.
- Assuming electronic logic voltage is interchangeable with motor supply voltage.

## Applications and limits

These relations support motor sizing, sensor interfaces, power estimates, and troubleshooting low-voltage circuits. Real components add tolerances, temperature dependence, saturation, leakage, and switching losses. Electrical installation and protective-device design require appropriate standards and competent review. For a mechanical system, combine electrical losses with the thermal model: even a correctly sized shaft can be driven by a motor that overheats under its duty cycle.

## Further reading

- [MIT OpenCourseWare — Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/): full lecture and problem sequence.
- [University of Michigan CTMS — modeling and control examples](https://ctms.engin.umich.edu/CTMS/index.php?aux=Home): motor and electromechanical system modeling.
