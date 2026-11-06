# 28. Mechatronics and Instrumentation

## Learning map

Prerequisites: circuits, mechanics, measurement uncertainty, programming, and control. Mechatronics combines a physical mechanism, sensing, computation, and actuation into one working system. Follow the signal from the physical quantity to sensor output, analog conditioning, sampling, numerical processing, drive command, and mechanical response. A successful design considers the complete chain instead of optimizing each part independently.

## Theory

A sensor converts a physical quantity into a measurable signal. Its sensitivity is the change in output per change in input. Offset, gain error, nonlinearity, hysteresis, drift, resolution, and noise describe different imperfections. Calibration determines a relationship under stated conditions; it does not guarantee that the relationship holds indefinitely or outside the calibrated range.

An analog-to-digital converter samples a voltage and assigns a finite code. Sampling discretizes time; quantization discretizes amplitude. A large nominal bit count does not automatically mean accurate measurement because reference errors, front-end noise, input loading, and nonlinearity remain. The quantization conventions below use uniform bins and their midpoints; a real ADC's data sheet specifies transition levels and endpoint behavior.

Before sampling, an analog anti-alias filter limits unwanted high-frequency content. Once a high-frequency disturbance has aliased into the signal band, a subsequent digital low-pass filter generally cannot distinguish it from a real low-frequency signal. Sampling rate must also leave room for practical filter transition bands, timing jitter, and control delay.

Actuation converts an electrical, pneumatic, or hydraulic command into force, motion, or heat. A PWM driver switches power rapidly while adjusting duty ratio. The load's electrical and mechanical dynamics may average the switching, but peak current and switching losses still exist. A motor gearbox trades speed for torque while adding efficiency loss, backlash, compliance, and reflected inertia.

Embedded software must handle timing, units, communication failures, and limits as part of the physical design. The same numerical command can produce different real motion if supply voltage falls or a load jams. Use measured feedback when the required quantity cannot be inferred reliably from the command alone.

## Formula handbook

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

## Derivation

An ideal $N$-bit converter has $2^N$ possible codes. Dividing its voltage span by the number of bins gives $q$. If each bin is represented by its midpoint, the largest distance to that midpoint is $q/2$. Under a uniform error assumption, variance is

$$
\sigma_q^2=\frac1q\int_{-q/2}^{q/2}e^2de=\frac{q^2}{12}.
$$

The calculation explains why adding a bit halves ideal quantization step. It does not halve every real measurement error. For example, a fixed reference-voltage error scales all readings independently of bit count. This distinction is central when deciding whether a better ADC or a better sensor and reference will improve a system.

## Worked examples

**Example 1 — pressure measurement resolution.** A linear pressure sensor produces $0.5$ to $4.5\ \mathrm V$ for $0$ to $1000\ \mathrm{kPa}$. Its sensitivity is $0.004\ \mathrm{V/kPa}$. A 12-bit ADC spans $0$ to $5\ \mathrm V$, so $q=5/4096=0.001220703\ \mathrm V$. The pressure increment is $q/a=0.305176\ \mathrm{kPa}$, with ideal midpoint quantization bound $\pm0.152588\ \mathrm{kPa}$. At $2.5\ \mathrm V$, the inferred pressure is $(2.5-0.5)/0.004=500\ \mathrm{kPa}$. These are resolution figures, not an accuracy specification for the sensor assembly.

**Example 2 — geared motor.** A motor supplies $0.20\ \mathrm{N\,m}$ at $3000\ \mathrm{r/min}$ through a $20{:}1$ reducer with efficiency $0.80$. Output speed is $150\ \mathrm{r/min}$ and output torque is $0.80(20)(0.20)=3.20\ \mathrm{N\,m}$. Motor shaft power is $0.20[2\pi(3000/60)]=62.8319\ \mathrm W$; output power is $50.2655\ \mathrm W$. A load inertia of $0.040\ \mathrm{kg\,m^2}$ reflects as $0.040/20^2=0.000100\ \mathrm{kg\,m^2}$ in the ideal kinematic inertia relation. Add motor and gear inertia separately.

## Exercises

1. A 10-bit ADC spans $0$ to $3.3\ \mathrm V$. Find its ideal bin width.
2. A $12\ \mathrm V$ source supplies a $6\ \Omega$ heater by PWM at $D=0.25$. Find average voltage and average heating power.
3. An encoder provides 600 cycles per revolution and is decoded on four transitions per cycle. Find angular count increment in degrees.

## Solutions

1. $q=3.3/1024=0.00322266\ \mathrm V$, or $3.223\ \mathrm{mV}$.
2. Average voltage is $3\ \mathrm V$. Heating power is $D V_s^2/R=0.25(144)/6=6\ \mathrm W$. Squaring the average voltage would incorrectly give $1.5\ \mathrm W$.
3. $N_c=2400$ counts/revolution, so the increment is $360/2400=0.15^\circ$. Mechanical backlash and encoder mounting can dominate actual position uncertainty.

## Common mistakes

- Confusing resolution, repeatability, and accuracy.
- Using $2^N-1$ in a bin-width formula without stating an endpoint convention.
- Assuming PWM duty is directly proportional to motor speed under every load.
- Ignoring sensor settling time, communication latency, and sample timestamp.
- Choosing a fast controller without measuring actual loop execution time.

## Applications and limits

Mechatronics supports automated inspection, temperature regulation, positioning, and small robotic machines. A useful commissioning record includes wiring, signal ranges, calibration data, unit conversions, sample period, actuator limits, and observed failure behavior. The examples are component-level models. Real performance requires electrical noise control, thermal design, measured response, and mechanically safe limits.

## Further reading

- [Analog Devices — noise and distortion in data converters](https://www.analog.com/en/resources/technical-articles/2022/07/16/11/45/managing-noise-in-the-signal-chain-part-2-noise-and-distortion-in-data-converters.html): ADC quantization and practical noise context.
- [STMicroelectronics — Understanding and minimising ADC conversion errors](https://www.st.com/resource/en/application_note/an1636-understanding-and-minimising-adc-conversion-errors-stmicroelectronics.pdf): converter error mechanisms and practical design guidance.
- [University of Michigan CTMS](https://ctms.engin.umich.edu/CTMS/index.php?aux=Home): motor and sampled-control examples.
