# 41. Welding Engineering

## Learning map

Prerequisites: materials science, heat transfer, manufacturing, stress analysis, and engineering drawings. Connect joining process, thermal cycle, metallurgy, geometry, loading, and inspection. Begin by distinguishing arc energy from heat transferred to the workpiece, and weld leg length from effective throat. The elementary calculations here estimate energy, geometry, and nominal stress. They do not qualify a procedure or establish a code-compliant weld size, fatigue life, or pressure boundary.

## Theory

Welding forms a joint through localized coalescence, with or without melting, pressure, or filler metal depending on the process. In common fusion welding, the weld pool solidifies while adjacent unmelted parent metal experiences a thermal cycle. That adjacent heat-affected zone, or HAZ, can undergo changes in grain structure, phases, hardness, toughness, and residual stress. A joint therefore contains more than a homogeneous block of deposited filler.

Process choice affects access, deposition, shielding, thermal input, defects, and automation. Gas tungsten arc welding uses a nonconsumable electrode and can add filler separately. Gas metal arc welding feeds a consumable wire. Shielded metal arc welding uses a coated consumable electrode, while submerged arc welding operates beneath granular flux. Laser and electron-beam processes concentrate energy differently; resistance and solid-state processes use other heat and pressure histories. A procedure valid for one process is not automatically transferable to another.

Heat input per unit length is one descriptor of a thermal cycle. The same nominal value can produce different temperature fields because plate thickness, joint geometry, travel speed, source distribution, preheat, and boundary heat losses differ. Faster cooling can promote hard microstructures in susceptible steels; excessively slow cooling can also impair desired properties in particular materials. Preheat and interpass control must therefore follow the material and procedure requirements. TWI explains why [increased heat input or preheat is not a universal remedy for hydrogen cracking](https://www.twi-global.com/technical-knowledge/faqs/faq-do-increased-preheat-and-heat-input-always-reduce-the-risk-of-hydrogen-cracking).

Hydrogen-assisted cracking depends on interacting material susceptibility, hydrogen, stress, and thermal history. Solidification cracking has a different mechanism associated with the final stages of freezing. Lack of fusion, incomplete penetration, porosity, undercut, and inclusions are also distinct discontinuities. Calling every imperfection a crack obscures its cause and the appropriate examination. Cleaning, fit-up, shielding, consumable handling, and repeatable parameters support quality, but acceptance requires the specified evaluation procedure.

Heating expands material locally; surrounding cooler material restrains that expansion. Plastic deformation and subsequent uneven contraction can leave distortion and residual stress after cooling. Clamping may reduce visible movement while increasing restraint, so zero visible distortion does not imply zero residual stress. TWI's [distortion explanation](https://www.twi-global.com/technical-knowledge/faqs/faq-what-causes-distortion) describes this thermal and mechanical interaction. A purely elastic expansion formula illustrates the strain scale; it cannot predict the final weld residual-stress field after melting, yielding, and phase transformation.

Joint design must provide a load path and fabrication access. Weld toes and roots introduce local stress concentrations. Cyclic performance depends on stress range, detail geometry, quality, environment, and the chosen fatigue assessment method. Simply selecting a stronger filler or enlarging a weld does not establish improved fatigue resistance at the governing location. Drawing symbols must distinguish leg and throat, weld side, length, pitch, contour, penetration requirements, and the applicable inspection basis.

## Formula handbook

Use current $I$ in A, voltage $U$ in V, travel speed $v$ in m/s, length $L$ in m, force $F$ in N, and stress in Pa unless a numerical unit conversion is explicitly stated.

**1. Electrical arc power:**

$$
P_{arc}=UI,\qquad \overline P_{arc}=\frac1T\int_0^T U(t)I(t)\,dt.
$$

For pulsed waveforms, the product of average voltage and average current need not equal average power.

**2. Arc energy per unit length, constant conditions:**

$$
E_{arc}=UI/v.
$$

The result is J/m. **3. Net heat transferred per length:**

$$
H=\eta_{th}UI/v.
$$

$\eta_{th}$ is the specified thermal efficiency fraction. A code or procedure may define its reporting convention differently; identify whether the reported quantity includes this factor.

**4. Explicit conversion with numerical travel speed $s$ in mm/min:**

$$
H_{\rm kJ/mm}=\frac{60\eta_{th}UI}{1000s}.
$$

**5. Arc-on time and transferred energy for a uniform run:**

$$
t_{arc}=L/v,\qquad Q_{net}=HL=\eta_{th}UI\,t_{arc}.
$$

Time is s and energy J; setup and interpass time are additional.

**6. Cooling interval and mean cooling rate:**

$$
t_{8/5}=t(T=500^\circ\mathrm C)-t(T=800^\circ\mathrm C),\qquad \overline{|\dot T|}=300/t_{8/5}.
$$

This defines a monotonic cooling segment in seconds, with rate K/s. It is a useful descriptor for some steel welds, not a universal metallurgical acceptance limit.

**7. Ideal equal-leg, flat-faced, right-angle fillet throat:**

$$
a=z\sin45^\circ=\frac z{\sqrt2}.
$$

$z$ is leg length and $a$ the theoretical root-to-face distance. This construction gives no extra penetration credit. Concavity, fit-up, fusion, and the governing design definition can change effective throat; see [TWI's throat-geometry discussion](https://www.twi-global.com/technical-knowledge/job-knowledge/design-part-2-091).

**8. Nominal throat area of several weld segments:**

$$
A_w=\sum_i a_iL_{e,i}.
$$

$L_{e,i}$ are effective lengths supplied by the model or governing design method, not automatically every visible millimetre of a bead.

**9. Centered direct loading, ideal uniform nominal shear:**

$$
\tau_{nom}=F/A_w.
$$

Load sharing assumes a symmetric or otherwise justified stiffness distribution. This equation excludes eccentric moment and local notch stresses.

**10. Elastic weld-line-group centroid and polar area moment:**

$$
\bar x=\frac{\int x\,a\,d\ell}{A_w},\qquad \bar y=\frac{\int y\,a\,d\ell}{A_w},\qquad J_w=\int(x^2+y^2)a\,d\ell.
$$

Coordinates in $J_w$ are measured from the group centroid. $J_w$ is in $\mathrm{m^4}$.

**11. Nominal in-plane moment loading in that line-group model:**

$$
M_z=Fe,\qquad \boldsymbol\tau_M=\frac{M_z}{J_w}(-y\mathbf e_x+x\mathbf e_y),\qquad \boldsymbol\tau=\frac{\mathbf F}{A_w}+\boldsymbol\tau_M.
$$

Here $e$ is a perpendicular eccentricity (m). Vector addition matters. This elastic nominal distribution is not a local three-dimensional throat stress or a code interaction rule.

**12. Ideal triangular fillet volume and mass:**

$$
A_f=z^2/2,\qquad V_f=A_fL,\qquad m_f=\rho V_f.
$$

$A_f$ is bead cross-sectional area, distinct from throat area $A_w$. The mass estimate excludes reinforcement, penetration, spatter, and dilution bookkeeping; it is not necessarily wire consumption.

**13. Constant-property thermal strain and free movement:**

$$
\varepsilon_{th}=\alpha\Delta T,\qquad \Delta L_{free}=\alpha L\Delta T.
$$

$\alpha$ is in K⁻¹. **14. Fully restrained, uniaxial elastic idealization:**

$$
\sigma_{th}=-E\alpha\Delta T.
$$

$E$ is modulus in Pa. The formula ceases to apply when yielding, creep, transformation, or restraint change becomes significant; it is not a weld residual-stress formula.

**15. Stress-range and generic power-law fatigue representation:**

$$
\Delta\sigma=\sigma_{max}-\sigma_{min},\qquad N(\Delta\sigma)^m=C.
$$

$N$ is cycles, and $C$ has the units required by the specified stress measure and fitted exponent $m$. Nominal, structural hot-spot, and notch-stress curves are not interchangeable. No fatigue class or allowable value is supplied here.

## Derivation

For constant power, a weld travels distance $dL=v\,dt$ while the arc supplies energy $dE=UI\,dt$. Dividing gives arc energy per length $UI/v$. Multiplication by thermal efficiency estimates the energy entering the workpiece. Integrating over a uniform run gives $Q_{net}=HL$, which must also equal net power times arc-on time. This equivalence is a useful independent unit check.

For an equal-leg flat fillet, the ideal cross-section is a right isosceles triangle. Its hypotenuse is $z\sqrt2$ and its area is $z^2/2$. Expressing that same area as half the hypotenuse times its perpendicular altitude gives $z^2/2=(z\sqrt2)a/2$, hence $a=z/\sqrt2$. The two-dimensional geometric result only identifies the nominal throat; sound fusion and usable effective length still need to be established.

## Worked examples

### Example 1: arc energy, net heat input, and run time

Assume steady $U=24$ V, $I=180$ A, thermal efficiency $0.80$, and travel speed $v=0.00500$ m/s, equivalent to 300 mm/min. Arc power is **4320 W** and net transferred power is **3456 W**. Arc energy is $4320/0.005=864000$ J/m, or **0.8640 kJ/mm**. Net heat input is **0.6912 kJ/mm**.

For a 0.300 m run, arc-on time is $0.300/0.005=\mathbf{60.0\ s}$. Net energy is $3456(60)=\mathbf{207.36\ kJ}$, also $0.6912(300)$ kJ. These values do not determine HAZ hardness or cooling time without material, thickness, geometry, preheat, and heat-loss information.

### Example 2: symmetric double-fillet nominal stress

Two identical longitudinal fillets transmit a centered 20.0 kN force parallel to their lengths. Assume equal stiffness, no eccentricity, flat faces, 6.00 mm legs, no penetration credit, and an already specified effective length of 100 mm per weld. Each theoretical throat is $6/\sqrt2=\mathbf{4.24264\ mm}$. Total throat area is $2(4.24264)(100)=\mathbf{848.528\ mm^2}$.

Uniform nominal shear is $20000/848.528=\mathbf{23.5702\ MPa}$. Each weld carries 10.0 kN, which reproduces the applied load when integrated over both throats. Ideal triangular bead volume is $2(6^2/2)(100)=3600\ \mathrm{mm^3}$; with supplied density $7850\ \mathrm{kg/m^3}$, ideal bead mass is **28.26 g**. The calculation supplies a nominal stress and geometric mass, not an allowable load or fatigue qualification.

## Exercises

1. At 22 V, 160 A, thermal efficiency 0.75, and travel speed 240 mm/min, calculate net heat input in kJ/mm.
2. Two symmetric longitudinal fillets each have 5 mm legs and 80 mm effective length. Under centered 12 kN loading parallel to the welds, find total throat area and nominal uniform shear.
3. A hypothetical uniform 0.500 m steel bar has $\alpha=12\times10^{-6}\ \mathrm{K^{-1}}$ and undergoes a 400 K temperature rise. Find free expansion. With $E=200$ GPa, find the fully restrained elastic stress prediction and explain why it cannot be asserted as an actual welding residual stress.

## Solutions

1. $H=60(0.75)(22)(160)/(1000\times240)=\mathbf{0.660\ kJ/mm}$. Omitting efficiency would instead report arc energy, 0.880 kJ/mm.
2. Throat is $5/\sqrt2=3.53553$ mm, total area is $2(3.53553)(80)=\mathbf{565.685\ mm^2}$, and shear is $12000/565.685=\mathbf{21.2132\ MPa}$. The stipulated symmetry and absence of eccentricity are essential.
3. Free expansion is $12\times10^{-6}(0.500)(400)=\mathbf{2.40\ mm}$. The ideal restrained stress is **−960 MPa**. This is an elastic-model result, not a credible universal material response: yielding and temperature-dependent properties can invalidate it. An actual weld also has nonuniform heating, cooling, melting, changing restraint, and metallurgical transformations.

## Common mistakes

Mixing mm/min with m/s creates large heat-input errors. A 6 mm leg is not a 6 mm throat. More convex reinforcement does not automatically add the assumed effective throat. Distinguish a procedure specification, its qualification evidence, and welder or operator qualification. Inspection can reveal relevant discontinuities but cannot by itself replace the required design and qualification evidence.

## Applications and limits

For a fabrication package, connect the drawing, joint preparation, material and filler identification, procedure, qualification records, fit-up, heat-treatment requirements, inspection plan, and acceptance criteria. Use the governing construction standard and its required edition. ASME's [official Section IX page](https://www.asme.org/codes-standards/find-codes-standards/bpvc-ix-bpvc-section-ix-welding-brazing-fusing-qualifications-%282%29) identifies its qualification subject matter; it does not make the elementary stress calculation here a complete structural or pressure design. No copyrighted qualification ranges, fatigue classes, or acceptance limits are reproduced.

## Further reading

- [TWI — hydrogen cracks in steels](https://www.twi-global.com/technical-knowledge/job-knowledge/defects-hydrogen-cracks-in-steels-identification-045): mechanisms and the distinction between arc energy and thermal heat input.
- [TWI — fillet throat geometry](https://www.twi-global.com/technical-knowledge/job-knowledge/design-part-2-091): leg, throat, face shape, and geometric interpretation.
- [TWI — causes of distortion](https://www.twi-global.com/technical-knowledge/faqs/faq-what-causes-distortion): thermal restraint, plasticity, and contraction.
- [ASME — BPVC Section IX](https://www.asme.org/codes-standards/find-codes-standards/bpvc-ix-bpvc-section-ix-welding-brazing-fusing-qualifications-%282%29): official publisher page; consult applicable project requirements for edition and scope. Links checked 2026-11-07.
