# 39. Engineering acoustics

## Learning map

Prerequisites: [vibrations](20-vibrations.md), elementary waves, logarithms and fluid properties. Learn to distinguish source sound power from receiver sound pressure, convert between pressure and intensity under appropriate assumptions, add independent sound contributions, and analyze basic reflection and duct resonance. The aim is to build a defensible first acoustic model for mechanical equipment before using detailed measurements or numerical acoustics.

## Theory

Sound in a fluid is a traveling disturbance of pressure, density and particle velocity. The fluid particles oscillate about their mean positions while the disturbance propagates through the medium. Particle velocity is therefore different from sound speed. A small particle motion can accompany a wave traveling hundreds of meters per second. Linear acoustics assumes the disturbances are sufficiently small that products of perturbations can be neglected.

Acoustic pressure is the fluctuating part of total pressure, not the atmospheric or static pressure itself. A sinusoidal pressure has zero mean but nonzero mean square, so its root-mean-square value measures amplitude for many energy calculations. Peak, peak-to-peak and rms values are different conventions. For random sound, rms must be associated with a measurement bandwidth and averaging interval; there need not be a single meaningful sinusoidal peak factor.

Sound pressure level describes pressure at a particular position. Sound power describes the rate of acoustic energy emitted by a source across an enclosing surface. The same source can produce different pressure levels at different distances or in different rooms. Reflections, directionality and absorption influence the received field. Comparing an equipment sound-power declaration directly with a microphone sound-pressure reading confuses two physical quantities, even though both are expressed in decibels.

A decibel is a logarithm of a dimensionless ratio. A level is incomplete without its reference and physical quantity. This chapter uses 20 micropascals for airborne sound pressure, $10^{-12}$ W/m2 for intensity and $10^{-12}$ W for power. These references do not make pressure level and intensity level universally identical. A-weighting and other filters modify the spectral contribution before reporting a level; unweighted calculations here must not be relabeled as dBA.

In a traveling plane wave, pressure and particle velocity are in phase and their ratio is the characteristic impedance. In a standing wave, incident and reflected components interfere. High rms pressure can exist where net average energy flow is small or zero. Thus a microphone pressure measurement alone does not generally determine intensity in a reactive near field or strongly reflecting space.

Independent sound sources combine through mean-square pressure when their cross-correlation averages to zero. Their decibel values do not add arithmetically. Coherent tones require phase-sensitive addition instead: two equal in-phase pressures double the pressure, whereas two equal incoherent sources double the mean-square pressure. This distinction matters when comparing rotating-machine tones with broadband background noise.

## Formula handbook

Let $p'$ be acoustic pressure in Pa, $u'$ particle velocity in m/s, $\rho_0$ mean density in kg/m3, $c$ sound speed in m/s and $W_a$ acoustic power in W. These equations assume linear acoustics unless specified otherwise.

1. Small pressure perturbation and sound speed:

$$
p_{total}=p_0+p',\qquad c=\sqrt{K_s/\rho_0}=\sqrt{\gamma RT}\quad\text{for a perfect gas}.
$$

$K_s$ is the isentropic bulk modulus in Pa. The gas formula uses absolute temperature in K.

2. Homogeneous lossless wave equation with no mean flow:

$$
\nabla^2p'-\frac1{c^2}\frac{\partial^2p'}{\partial t^2}=0.
$$

3. Sinusoidal wave, rms amplitude and wavelength:

$$
p'=\hat p\cos(\omega t-kx+\theta),\qquad p_{rms}=\frac{\hat p}{\sqrt2},\qquad \lambda=\frac cf,\qquad k=\frac{2\pi}{\lambda}.
$$

$\omega=2\pi f$ in rad/s; $f$ is frequency in Hz. The rms conversion applies to a sinusoid.

4. Specific acoustic impedance and progressive plane-wave impedance:

$$
Z=\frac{\tilde p}{\tilde u},\qquad Z_0=\rho_0c.
$$

Tildes denote complex amplitudes; impedance has units Pa s/m. General $Z$ can be complex, while $Z_0$ here is real and positive for a wave traveling in the positive direction.

5. Time-averaged intensity and its plane-wave reduction:

$$
I=\langle p'u'\rangle=p_{rms}u_{rms}\cos\phi,\qquad I=\frac{p_{rms}^2}{\rho_0c}\quad\text{for a progressive plane wave}.
$$

$\phi$ is pressure-velocity phase difference for single-frequency harmonic quantities. For a general broadband signal, use the time average or a suitable cross-spectral calculation rather than assigning one phase angle to all frequencies. Intensity is directional and measured in W/m2.

6. Airborne sound-pressure level:

$$
L_p=20\log_{10}\left(\frac{p_{rms}}{p_{ref}}\right),\qquad p_{ref}=20\times10^{-6}\ \mathrm{Pa}.
$$

7. Intensity and sound-power levels, for positive scalar magnitudes:

$$
L_I=10\log_{10}(I/I_{ref}),\quad I_{ref}=10^{-12}\ \mathrm{W/m^2},\qquad L_W=10\log_{10}(W_a/W_{ref}),\quad W_{ref}=10^{-12}\ \mathrm W.
$$

8. Ideal free-field intensity from a compact source:

$$
I(r)=\frac{Q_dW_a}{4\pi r^2}.
$$

$Q_d$ is a dimensionless directivity factor in the observation direction; $Q_d=1$ for an omnidirectional source. The model excludes reflections and atmospheric attenuation.

9. Pressure-level change in the same free-field far-field direction:

$$
L_p(r_2)-L_p(r_1)=-20\log_{10}(r_2/r_1).
$$

10. Addition of mutually incoherent pressure levels with the same reference and bandwidth:

$$
L_{p,total}=10\log_{10}\left(\sum_i10^{L_{p,i}/10}\right).
$$

11. Coherent pressure addition instead uses complex amplitudes:

$$
\tilde p_{total}=\sum_i\tilde p_i.
$$

Two equal in-phase sinusoidal pressures increase level by $20\log_{10}2=6.0206$ dB; two equal incoherent sources increase it by $10\log_{10}2=3.0103$ dB.

12. Normal-incidence pressure reflection at a boundary between two lossless fluid half-spaces:

$$
r_p=\frac{Z_2-Z_1}{Z_2+Z_1},\qquad t_p=\frac{2Z_2}{Z_2+Z_1}.
$$

$r_p$ and $t_p$ relate reflected and transmitted pressure amplitudes to incident pressure. They are not power fractions.

13. Corresponding energy fractions for real positive impedances:

$$
\mathcal R=r_p^2,\qquad \tau=\frac{Z_1}{Z_2}t_p^2=\frac{4Z_1Z_2}{(Z_1+Z_2)^2},\qquad \mathcal R+\tau=1.
$$

14. Transmission loss and absorption bookkeeping:

$$
TL=10\log_{10}(W_{incident}/W_{transmitted})=-10\log_{10}\tau,\qquad \alpha=1-\mathcal R-\tau.
$$

The absorption relation is for a passive boundary with all reflected and transmitted channels accounted for. Absorption and transmission loss measure different outcomes.

15. Ideal longitudinal duct resonances, neglecting end corrections and losses:

$$
f_n=\frac{nc}{2L}\quad\text{open-open},\qquad f_n=\frac{(2n-1)c}{4L}\quad\text{closed-open},\qquad n=1,2,3,\ldots
$$

An ideal open end is a pressure node; an ideal rigid closed end is a particle-velocity node.

## Derivation

Linearized one-dimensional momentum gives $\rho_0\partial u'/\partial t=-\partial p'/\partial x$. Linearized continuity gives $\partial\rho'/\partial t=-\rho_0\partial u'/\partial x$. For a small isentropic disturbance, $p'=c^2\rho'$. Differentiate the pressure relation in time and substitute continuity and momentum to obtain $\partial^2p'/\partial t^2=c^2\partial^2p'/\partial x^2$. This derivation makes the uniform medium, small disturbance and negligible mean-flow assumptions explicit.

The incoherent addition rule follows from $p_{total}=p_1+p_2$. Squaring and averaging gives $\langle p_{total}^2\rangle=\langle p_1^2\rangle+\langle p_2^2\rangle+2\langle p_1p_2\rangle$. Only when the cross term vanishes do mean squares add. Applying the pressure-level definition then gives formula 10. For coherent tones, the cross term depends on relative phase and cannot be discarded merely because two physical machines are present.

## Worked examples

### Example 1: pressure, motion and energy in a plane wave

A 1000 Hz progressive plane wave in air has rms pressure 0.200 Pa. Take $\rho_0=1.20$ kg/m3 and $c=343$ m/s as supplied properties. Pressure level is $20\log_{10}[0.200/(20\times10^{-6})]=\mathbf{80.0000\ dB}$ re 20 micropascals. Characteristic impedance is **411.600 Pa s/m**. Intensity is **$9.71817\times10^{-5}$ W/m2**, particle-velocity rms is **$4.85909\times10^{-4}$ m/s**, and wavelength is **0.343000 m**. The pressure peak is **0.282843 Pa**. The intensity result assumes a progressive wave; inserting the same rms pressure from an arbitrary standing-wave measurement would not justify it.

### Example 2: two sources and increased distance

Two compact, mutually incoherent sources each produce 80.0 dB sound pressure at a 1.0 m reference distance in the observation direction. Treat their separation as negligible for the propagation estimate and assume both the reference and receiver positions are in a free-field far field. Combined level at 1 m is $80+10\log_{10}2=\mathbf{83.0103\ dB}$. At 5.0 m the geometric reduction is $20\log_{10}5=\mathbf{13.9794\ dB}$, giving **69.0309 dB**. Independently, each source's mean-square pressure falls by a factor 25, and the combined rms pressure becomes **0.0565685 Pa**. That pressure reproduces the final level. A reflecting plant room or coherent tonal sources would require a different model.

## Exercises

1. A sinusoidal airborne sound has peak pressure 0.200 Pa. Find rms pressure and sound-pressure level using 20 micropascals as reference. Compare with Example 1, where 0.200 Pa was rms.
2. A normally incident plane wave meets a lossless interface with $Z_1=400$ and $Z_2=1600$ Pa s/m. Find pressure reflection coefficient, reflected power fraction, transmitted power fraction and transmission loss.
3. A 0.500 m duct has an ideal rigid closed end and an ideal open end. With $c=343$ m/s, find its first two longitudinal resonances. Find the fundamental if both ends are instead open, neglecting end correction.

## Solutions

1. Rms pressure is $0.200/\sqrt2=\mathbf{0.141421\ Pa}$ and level is **76.9897 dB**. Confusing the specified peak value with rms would overstate this sinusoid's pressure level by 3.0103 dB.
2. $r_p=(1600-400)/(1600+400)=\mathbf{0.600000}$. Thus **$\mathcal R=0.360000$**, **$\tau=0.640000$** and **$TL=1.93820$ dB**. The pressure transmission coefficient is 1.6, but its square is not the transmitted energy fraction; the impedance ratio is also needed. Reflected and transmitted fractions sum to one.
3. Closed-open resonances begin at **171.500 Hz** and **514.500 Hz**, the fundamental and third harmonic. The open-open fundamental is **343.000 Hz**. Real end radiation and geometry shift these ideal frequencies; pressure and displacement nodes must not be interchanged.

## Common mistakes

Do not add decibel numbers directly or use the factor 20 for a power ratio. Declare rms or peak and the pressure reference. A negative level is possible for a positive quantity below its reference; it does not mean negative acoustic energy. Distinguish acoustic pressure from static pressure and source power from receiver level. A highly absorbing finish can reduce reverberation without providing the transmission loss of a sealed barrier. Leaks and structural transmission can dominate an enclosure.

## Applications and limits

Apply these models to fan and pump noise, duct tones, acoustic sensors and preliminary enclosure reasoning. Begin with source, transmission path and receiver, then identify whether direct sound, reflected sound or structural vibration dominates. Measurements need stated location, bandwidth, weighting, calibration and operating condition. This chapter supplies no occupational exposure limits or compliance conclusions. Flow-generated noise, nonlinear shocks, porous absorbers, room modes and structural-acoustic coupling require models beyond the elementary equations here.

## Further reading

- [MIT OCW: The Quantification of Sound and the Wave Equation](https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/c45734e2684a8592c0600120a0b6584c_lec_1_2004.pdf) — pressure, particle velocity, impedance and acoustic fundamentals.
- [OpenStax: Sound Intensity](https://openstax.org/books/university-physics-volume-1/pages/17-3-sound-intensity) — energy transport, intensity and logarithmic levels in an openly published physics textbook.
- [TU Delft: Fundamentals of Acoustics](https://www.ocw.tudelft.nl/wp-content/uploads/Lecture_2_-_Fundamentals_on_acoustics.pdf) — wave propagation, reflection and transmission lecture materials.
- [OpenStax: Normal Modes of a Standing Sound Wave](https://openstax.org/books/university-physics-volume-1/pages/17-4-normal-modes-of-a-standing-sound-wave) — interference and ideal air-column resonances.
