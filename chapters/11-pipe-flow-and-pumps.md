# 11. Pipe flow and pumps

## Learning map

Prerequisites: fluid properties, continuity, mechanical energy and dimensionless groups. Learn to assemble a system curve, calculate friction and fitting losses, locate a pump operating point and assess suction conditions. This chapter emphasizes liquid systems such as water-treatment circulation and transfer lines. Compressible-gas networks and two-phase flow need additional models.

## Theory

A pumping system includes reservoirs, pipes, fittings, control valves, equipment and the pump. The pump adds mechanical energy to the liquid. The system determines how much head is required at a given flow. Actual steady operation occurs where the pump head curve intersects the system head curve. A pump's catalog rated point is not automatically the installed operating point.

Static head arises from elevation and pressure differences between system boundaries. It is present even when flow tends toward zero. Dynamic losses generally grow with flow; for turbulent flow with approximately fixed friction factor, they scale roughly with flow squared. Enlarging a pipe can reduce lifetime energy demand because velocity and friction losses fall, although installation cost may increase.

Fully developed laminar flow in a circular pipe has a parabolic profile and a friction factor determined by Reynolds number alone. Turbulent friction depends on both Reynolds number and relative roughness. Entrance effects, disturbances, developing flow and corrosion can change the effective loss. Nominal pipe size is not the bore used in the equations; use the actual internal diameter associated with material, schedule and condition.

Fittings and valves dissipate energy by separation, mixing and recirculation. Their loss coefficient is referenced to a stated velocity and geometry. In a reducer, tee or valve assembly, identify which section defines that velocity. Summing coefficients blindly across different bores creates incorrect results. A throttling valve shifts the system curve; variable-speed control changes the pump curve. Each has a different efficiency consequence.

Cavitation begins when local pressure reaches the liquid vapor-pressure region. NPSH expresses suction energy above vapor pressure in units of liquid head. Available NPSH is a system quantity; required NPSH is a pump characteristic tied to a specified test criterion. Merely exceeding a catalog NPSH value may not provide a suitable operational margin. Temperature, site atmospheric pressure, suction losses and transient conditions matter.

## Formula handbook

Use $Q$ in m3/s, pipe diameter $D$ and head in m, $p$ in Pa, $\rho$ in kg/m3 and $\mu$ in Pa s. $g=9.81$ m/s2 is used in examples.

1. Mean pipe speed and Reynolds number:

$$
V=\frac{4Q}{\pi D^2},\qquad Re=\frac{\rho VD}{\mu}.
$$

2. Darcy-Weisbach straight-pipe head loss:

$$
h_f=f_D\frac{L}{D}\frac{V^2}{2g}.
$$

3. Fully developed laminar circular-pipe friction factor:

$$
f_D=\frac{64}{Re}.
$$

4. Colebrook equation for ordinary turbulent pipe flow:

$$
\frac1{\sqrt{f_D}}=-2\log_{10}\left(\frac{\epsilon/D}{3.7}+\frac{2.51}{Re\sqrt{f_D}}\right).
$$

$\epsilon$ is effective roughness. Transitional flow needs special attention rather than uncritical interpolation.

5. Local fitting losses, with each $V_i$ matching its coefficient:

$$
h_m=\sum_i K_i\frac{V_i^2}{2g}.
$$

6. Energy balance between boundary sections, no turbine:

$$
H_p=\frac{p_2-p_1}{\rho g}+z_2-z_1+\frac{\alpha_2V_2^2-\alpha_1V_1^2}{2g}+h_f+h_m.
$$

$\alpha$ is the kinetic-energy correction; reservoir surface velocities are often negligible.

7. Hydraulic, shaft and electrical powers:

$$
P_h=\rho gQH_p,\qquad P_s=P_h/\eta_p,\qquad P_e=P_s/\eta_m.
$$

8. Approximate turbulent system curve for fixed geometry:

$$
H_{sys}=H_{static}+CQ^2.
$$

$C$ has units s2/m5 and includes the assumed loss behavior.

9. Available NPSH at pump suction flange, with its elevation datum:

$$
NPSH_A=\frac{p_{s,abs}}{\rho g}+\frac{V_s^2}{2g}-\frac{p_v}{\rho g}.
$$

10. For an open suction reservoir with negligible surface speed:

$$
NPSH_A=\frac{p_{atm}-p_v}{\rho g}+z_{surface}-z_{pump}-h_{L,suction}.
$$

11. Same impeller, approximately homologous speed changes:

$$
\frac{Q_2}{Q_1}=\frac{N_2}{N_1},\qquad \frac{H_2}{H_1}=\left(\frac{N_2}{N_1}\right)^2,\qquad \frac{P_2}{P_1}\simeq\left(\frac{N_2}{N_1}\right)^3.
$$

12. Rapid liquid velocity change, ideal Joukowsky pressure rise:

$$
\Delta p=\rho a\Delta V.
$$

$a$ is the coupled liquid-pipe wave speed, not automatically the free-liquid sound speed. The relation describes a rapid event before reflection details are resolved.

## Derivation

For steady fully developed laminar flow in a circular pipe, the axial momentum equation reduces to a balance between pressure gradient and viscous shear. Integrating with no slip at radius $R$ yields

$$
u(r)=\frac{\Delta p}{4\mu L}(R^2-r^2).
$$

Area averaging gives $V=\Delta p R^2/(8\mu L)$, or $\Delta p=32\mu LV/D^2$. Compare this with Darcy-Weisbach pressure loss $\Delta p=f_D(L/D)\rho V^2/2$. Cancellation yields $f_D=64\mu/(\rho VD)=64/Re$. This derivation uses the **Darcy** friction factor. The Fanning friction factor is one-quarter of it; replacing one with the other without changing the governing equation creates a factor-of-four error.

## Worked examples

### Example 11-A: water-transfer pump duty

Water flows at 0.010 m3/s through 80 m of 0.100 m internal-diameter pipe. Use $f_D=0.025$, total fitting coefficient 4, density 1000 kg/m3, and static lift 12 m between open reservoirs. Velocity is 1.27324 m/s. Combined loss is $[0.025(80/0.1)+4]V^2/(2g)=1.98304$ m. Required pump head is **13.9830 m**. At pump efficiency 0.70, shaft power is $1000(9.81)(0.010)(13.9830)/0.70=\mathbf{1.95962\ kW}$. Friction factor and efficiency are supplied assumptions; actual selection needs a manufacturer curve at this duty.

### Example 11-B: suction head available

An open tank surface is 2.0 m above the pump centerline. Atmospheric pressure is 101,325 Pa; water vapor pressure is 2340 Pa; density is 998 kg/m3. Suction loss at operating flow is 1.5 m. With negligible tank-surface velocity, $NPSH_A=(101325-2340)/(998\times9.81)+2-1.5=\mathbf{10.6104\ m}$. Compare this system value with the pump's applicable suction criterion and chosen margin over the full operating range, rather than treating the number as a universal pass condition.

## Exercises

1. A laminar pipe flow has Reynolds number 800. Find Darcy and Fanning friction factors.
2. A pump delivers 0.020 m3/s at 15 m head with density 1000 kg/m3 and efficiency 0.75. Find hydraulic and shaft powers.
3. A fitting has $K=3$ at mean speed 2 m/s. Find its head loss. What happens if that speed doubles and $K$ remains unchanged?

## Solutions

1. $f_D=64/800=0.080$ and $f_F=f_D/4=0.020$.
2. $P_h=1000(9.81)(0.020)(15)=2943$ W. $P_s=2943/0.75=3924$ W.
3. $h=3(2^2)/(2\times9.81)=0.6116$ m. At 4 m/s it becomes 2.4465 m, four times greater.

## Common mistakes

Use actual bore, not nominal diameter. Distinguish pump shaft input from motor electrical input. Evaluate viscosity and vapor pressure at relevant temperature. Do not apply affinity laws to a fixed system as though its new flow were known without finding the new intersection. A pipe strength calculation, pressure class and pipe-support analysis are separate from the hydraulic loss calculation.

## Applications and limits

A practical study records normal, minimum and maximum flow; fluid properties; static boundaries; branch arrangements; and credible valve states. Series pumps approximately add head at common flow; parallel pumps approximately add flow at common head, subject to individual curves and controls. Long lines or rapid valve movements need transient analysis. Final pump procurement requires current manufacturer curves, materials, sealing, allowable operation range and project-specific engineering review.

## Further reading

- [US DOE: Pumps resources](https://betterbuildingssolutioncenter.energy.gov/better-plants/pumps) — practical sourcebook and system-efficiency resources.
- [NIST: thermophysical fluid properties](https://webbook.nist.gov/chemistry/fluid/) — density, viscosity and vapor-state data for supported fluids.
- [TU Delft: transport-phenomena course](https://ocw.tudelft.nl/courses/basics-transport-phenomena/) — deeper momentum-transport background.
