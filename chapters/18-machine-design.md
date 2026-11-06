# 18. Machine elements and mechanical design

## Learning map

Prerequisites: statics, dynamics, strength of materials, materials science, and manufacturing. Follow power from actuator to load, calculate forces at every interface, and check each component for strength, stiffness, life, fit, and serviceability. This chapter covers shafts, gears, rolling bearings, bolts, springs, and fatigue screening. Detailed product selection requires the relevant manufacturer's data and applicable design standards.

## Theory

A machine is a load path and a motion path. A gearbox changes torque and speed, while shafts, keys, splines, bearings, housings, and fasteners transmit the resulting loads. Power balance alone does not determine bearing forces: tooth pressure angle, shaft spacing, overhangs, and external loads determine reactions. Deflection can spoil alignment even when nominal stresses are low.

Gear ratio sets ideal kinematic relations. Real gears also require tooth-root fatigue, contact fatigue, scuffing, lubrication, backlash, and manufacturing accuracy checks. A pitch-circle force calculation is an input to those checks. Bearing dynamic rating life is a statistical fatigue measure under specified assumptions; it is not a promise that every bearing lasts that long. Contamination, poor lubrication, excessive preload, installation damage, or electrical erosion may cause earlier failure.

A preloaded bolted joint initially compresses the clamped members. An external separating load increases bolt tension and reduces member compression according to their stiffnesses. While contact remains, the bolt does not generally receive the entire external load increment. Once the joint separates, that model changes. Torque tightening is sensitive to friction, so a single torque coefficient is a rough preload estimate rather than a universal law.

Helical compression springs store energy largely through torsion of their wire. Curvature increases local stress, requiring a correction such as the Wahl factor for the stated spring geometry. Active coil count differs from total coils, and coil bind, buckling, surge, end seating, and fatigue may govern. Fatigue assessment separates mean and alternating stress and uses experimentally supported material and surface data.

## Formula handbook

**1. Rotary power**, with torque $T$ in N m and speed $n$ in rpm:

$$
P=T\omega,\qquad\omega=\frac{2\pi n}{60}.
$$

**2. External gear-pair ratio**, using magnitudes and tooth counts $z$:

$$
i=\frac{z_2}{z_1}=\frac{n_1}{n_2},\qquad T_2=\eta i T_1.
$$

Two external gears reverse rotational direction; $\eta$ is mesh efficiency.

**3. Spur-gear dimensions and loads**, module $m_g$ in m and pressure angle $\phi$:

$$
d=m_gz,\qquad F_t=\frac{2T}{d},\qquad F_r=F_t\tan\phi.
$$

**4. Solid shaft stresses**, nominal bending moment $M$ and torque $T$:

$$
\sigma_b=\frac{32M}{\pi d^3},\qquad\tau_t=\frac{16T}{\pi d^3}.
$$

Apply appropriate stress-concentration and fatigue effects separately.

**5. Basic rolling-bearing rating life**, with dynamic rating $C$ and equivalent dynamic load $P_b$ in the same force units:

$$
L_{10}=\left(\frac{C}{P_b}\right)^p,\qquad L_{10h}=\frac{10^6}{60n}L_{10}.
$$

$L_{10}$ is in millions of revolutions, corresponding to 90% population survival under the model; $p=3$ for ball bearings and $10/3$ for rollers. SKF provides the model and its applicability qualifications in its [rolling-bearing catalog](https://www.skf.com/binaries/pub12/Images/0901d196802809de-Rolling-bearings---17000_1-EN_tcm_12-121486.pdf).

**6. Joint load-sharing factor**, bolt stiffness $k_b$ and member stiffness $k_m$:

$$
C_j=\frac{k_b}{k_b+k_m},\qquad F_b=F_i+C_jF_e,\qquad F_c=F_i-(1-C_j)F_e.
$$

$F_i$ is preload, $F_e$ external separating force, and $F_c$ remaining clamp force; valid while contact persists and stiffnesses remain linear.

**7. Approximate tightening torque**:

$$
T_{\mathrm{tighten}}\approx K_T F_i d.
$$

$K_T$ is an empirical nut factor sensitive to thread and bearing friction.

**8. Close-coiled round-wire compression-spring rate**:

$$
k_s=\frac{Gd_w^4}{8D^3N_a},\qquad\delta=F/k_s.
$$

$D$ is mean coil diameter, $d_w$ wire diameter, and $N_a$ active turns. Use m and Pa for $k_s$ in N/m.

**9. Spring stress correction**, spring index $C_s=D/d_w$:

$$
K_w=\frac{4C_s-1}{4C_s-4}+\frac{0.615}{C_s},\qquad\tau_{\max}=K_w\frac{8FD}{\pi d_w^3}.
$$

This conventional expression assumes ordinary close-coiled spring geometry, not arbitrary curved wire.

**10. Mean and alternating stress**:

$$
\sigma_m=\frac{\sigma_{\max}+\sigma_{\min}}2,\qquad\sigma_a=\frac{\sigma_{\max}-\sigma_{\min}}2.
$$

**11. Modified Goodman screening**, tensile mean stress and corrected endurance strength $S_e$:

$$
\frac{\sigma_a}{S_e}+\frac{\sigma_m}{S_{ut}}\le\frac1{n_f}.
$$

$S_{ut}$ is ultimate strength and $n_f$ a chosen fatigue design factor. This linear approximation is not universal, particularly for compressive mean stresses or materials without an endurance limit.

**12. Linear cumulative damage estimate**:

$$
D_f=\sum_i\frac{n_i}{N_i}.
$$

Miner's estimate uses cycles experienced $n_i$ and corresponding constant-amplitude lives $N_i$; order effects and interactions are excluded.

## Derivation

For an ideal gear pair, equal pitch-line speed gives $\omega_1r_1=\omega_2r_2$. Equal tangential force gives $T_1/r_1=T_2/r_2$. Combining these equations shows that torque multiplies by the same ratio by which speed decreases, leaving power unchanged. Real loss changes torque through $\eta$, but it does not change the geometric speed ratio when teeth remain engaged without slip. This separates kinematic constraints from energy efficiency.

## Worked examples

### Example 1: Gear reduction

A 5 kW motor runs at 1500 rpm and drives a 20-tooth pinion meshing with a 60-tooth gear. Pinion pitch diameter is 0.060 m. Input torque is $5000/[2\pi(1500)/60]=31.831$ N m. The ratio is 3, output speed is 500 rpm, and ideal output torque is 95.493 N m. Tangential tooth force is $2(31.831)/0.060=1061.03$ N. For a specified $20^\circ$ pressure angle, radial force is 386.18 N. Actual tooth capacity is not established by these forces alone.

### Example 2: Ball-bearing basic life

A ball bearing has $C=20$ kN, equivalent dynamic load $P_b=5$ kN, and speed 1200 rpm. Basic life is $(20/5)^3=64$ million revolutions. Hour conversion gives $64\times10^6/[60(1200)]=888.89$ h. Halving load would increase this model's life by a factor of eight. Actual selection must also assess static load, minimum load, speed, lubrication, contamination, mounting, and duty-cycle variation.

## Exercises

1. A joint has preload 20 kN and stiffness fraction $C_j=0.20$. A 10 kN separating force is applied. Find bolt tension and remaining clamp force.
2. Stress cycles between 20 and 100 MPa. Find mean and alternating components.
3. An ideal 4:1 speed reduction receives 8 N m at 1200 rpm. Find output speed and torque.

## Solutions

1. Bolt tension is $20+0.2(10)=22$ kN. Clamp force is $20-0.8(10)=12$ kN, still positive, so the contact assumption remains possible.
2. Mean stress is 60 MPa and alternating stress 40 MPa. The stress ratio is $20/100=0.20$.
3. Output speed is 300 rpm and torque is 32 N m. Both sides transmit approximately 1005.31 W in the ideal model.

## Common mistakes

- Treating catalog dynamic load rating as the maximum allowable static load.
- Selecting bearings using shaft torque instead of bearing reaction forces.
- Using a gear ratio to multiply both speed and torque.
- Ignoring joint separation when applying bolt load sharing.
- Calling a nominal fatigue stress acceptable without accounting for surface, size, notch, temperature, and reliability effects.

## Applications and limits

Use these relations to size a first design, identify dominant loads, and choose candidate components. Then close the loop through tolerances, alignment, lubrication, assembly, maintenance, and testing. Review the manufacturer's current calculation method for the actual part family. A complete machine-element design includes failure modes and lifecycle evidence beyond a single stress or life equation.

## Further reading

- [MIT OCW: Elements of Mechanical Design](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/) — machine-element modeling, integration, and projects.
- [MIT: FUNdaMentals of Design](https://meddevdesign.mit.edu/fundamentals-of-design/) — linked lectures and design spreadsheets.
- [SKF: Rolling Bearings catalog](https://www.skf.com/binaries/pub12/Images/0901d196802809de-Rolling-bearings---17000_1-EN_tcm_12-121486.pdf) — manufacturer definitions and selection limitations. Linked material is not reproduced.
