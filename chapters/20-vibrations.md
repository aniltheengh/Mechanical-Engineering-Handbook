# 20. Mechanical vibrations

## Learning map

Prerequisites: dynamics, differential equations, complex numbers, and elementary matrix algebra. Begin with a single-degree-of-freedom mass–spring–damper, then study forced response, isolation, rotating imbalance, and multiple modes. Distinguish excitation frequency, natural frequency, and observed response frequency. The aim is to predict motion, transmitted loads, and resonance sensitivity rather than merely calculate one natural frequency.

## Theory

Vibration exchanges kinetic and potential energy. A mass stores kinetic energy, a spring stores strain energy, and a damper dissipates energy. Linear viscous damping assumes force proportional to relative velocity; it is an approximation for many real mechanisms. Coulomb friction, material hysteresis, backlash, and fluid drag can produce qualitatively different behavior.

The free response depends on initial displacement and velocity. An underdamped system oscillates with a decaying envelope; a critically damped system returns without oscillation in the ideal model; an overdamped system also does not oscillate but contains two real decay rates. A constant gravity load shifts the equilibrium position and does not change the natural frequency of an ideal linear vertical spring.

Forced response contains a transient plus a steady response. Near resonance, small damping can permit large amplitude. The maximum displacement-response frequency is not exactly the undamped natural frequency when damping is present. Resonance is a relationship among forcing, modal properties, and damping, not a universal condition that every spinning machine automatically reaches at one specific speed.

Isolation means reducing transmission between a vibrating source and its support. A soft mount can reduce high-frequency force transmission yet amplify motion during passage through resonance. Damping reduces the resonant peak but can increase high-frequency force transmission for the basic viscous isolator. Travel, stability, static deflection, startup, and shutdown therefore belong in an isolation design.

Real structures have multiple modes. Each mode has a shape and natural frequency, and forcing couples to it according to spatial distribution. A sensor at a modal node may miss a mode. A frequency spectrum is evidence of response, not by itself a diagnosis of the cause; speed tracking, phase, operating conditions, and a physical model help distinguish imbalance, misalignment, looseness, and structural resonance.

## Formula handbook

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

## Derivation

Represent harmonic force and displacement by the real parts of $F_0e^{i\omega t}$ and $\hat Xe^{i\omega t}$. Substitution into the equation of motion gives $(k-m\omega^2+ic\omega)\hat X=F_0$. Taking magnitude gives the amplitude formula, while the complex argument gives phase lag. At low frequency, stiffness dominates and $X\approx F_0/k$. At high frequency, inertia dominates and $X\approx F_0/(m\omega^2)$ for constant forcing amplitude. Rotating imbalance has forcing amplitude proportional to $\omega^2$, so that last displacement trend changes.

## Worked examples

### Example 1: Free decay

Take $m=2$ kg, $k=800$ N/m, and $c=8$ N s/m. The undamped natural frequency is 20 rad/s, or 3.18310 Hz. Critical damping is 80 N s/m, so $\zeta=0.10$. The damped frequency is $20\sqrt{0.99}=19.89975$ rad/s. After one second the exponential envelope is $e^{-0.1(20)(1)}=0.135335$ times its initial envelope value. This envelope ratio is not generally the ratio of the actual displacements at arbitrary times because the cosine and sine also change.

### Example 2: Harmonic displacement

Apply $F(t)=10\cos(10t)$ N to the same oscillator. Frequency ratio is 0.5 and static displacement amplitude is $10/800=0.0125$ m. Dynamic stiffness magnitude is $\sqrt{(800-2\times10^2)^2+(8\times10)^2}=605.310$ N/m. Thus steady displacement amplitude is 0.0165205 m, or 16.5205 mm. Phase lag is $\operatorname{atan2}(80,600)=0.132552$ rad, or $7.59464^\circ$. The total response still depends on initial conditions until the transient decays.

## Exercises

1. How does natural frequency change if mass increases by a factor of four while stiffness remains fixed?
2. An undamped 5 kg mass is attached to a 2000 N/m spring. Find natural frequency in rad/s and Hz.
3. A viscously damped isolator operates at $r=3$ and $\zeta=0.10$. Calculate force transmissibility.

## Solutions

1. Since $\omega_n\propto m^{-1/2}$, frequency halves.
2. $\omega_n=\sqrt{2000/5}=20$ rad/s and $f_n=20/(2\pi)=3.18310$ Hz.
3. $T_F=\sqrt{1+0.6^2}/\sqrt{(1-9)^2+0.6^2}=0.145365$. Transmitted harmonic force is about 14.5% of excitation amplitude under the stated model.

## Common mistakes

- Mixing Hz with rad/s in mass and stiffness formulas.
- Using peak-to-peak displacement where an amplitude is required.
- Assuming a large resonant response proves the forcing itself is large.
- Applying the constant-force resonance formula to a speed-dependent imbalance force without adjustment.
- Ignoring mounting travel and startup resonance when selecting soft isolators.

## Applications and limits

Use vibration models for machine mounts, rotating equipment, structures, instruments, and condition monitoring. Linear models are local approximations around an operating point. Contact loss, large motion, nonlinear springs, and dry friction require extended models. Measure damping when it materially controls the prediction; it is often more uncertain than mass or stiffness. Validate mode shapes and response levels as well as natural frequencies.

## Further reading

- [MIT OCW: Engineering Dynamics](https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/) — single- and multiple-DOF vibration modules.
- [MIT OCW: Elements of Mechanical Design](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/) — stiffness, machine integration, and dynamic performance. External materials are linked rather than reproduced.
