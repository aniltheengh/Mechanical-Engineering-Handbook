# Fluid engineering and transport

Mechanical Engineering Handbook · Expanded edition · 2026-11-08

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [10. Fluid mechanics](../chapters/10-fluid-mechanics.md)
- [11. Pipe flow and pumps](../chapters/11-pipe-flow-and-pumps.md)
- [14. Turbomachinery](../chapters/14-turbomachinery.md)
- [17. Mass transfer](../chapters/17-mass-transfer.md)

---

## 10. Fluid mechanics

### Learning map

Prerequisites: vectors, Newton's laws, calculus and thermodynamic properties. Learn to distinguish hydrostatics from flow, choose a control volume, and apply conservation of mass, momentum and energy. Build confidence with idealized problems before introducing viscous resistance, turbulence or compressibility. Pipe systems and turbomachinery apply these same balances to particular geometries.

### Theory

A fluid deforms continuously under a sustained shear stress. Pressure is a normal compressive stress; viscosity relates shear stress to deformation rate. Density measures mass per volume and does not determine viscosity. Under the continuum model, properties are smooth fields over length scales large compared with molecular scales. This approximation can fail in very rarefied gases or microscopic passages.

A static fluid has no shear deformation rate, so its pressure gradient balances body forces. Pressure increases with depth in a gravitational field. The hydrostatic force on a submerged surface must be integrated because lower portions carry greater pressure. Buoyancy is the resulting upward force from the surrounding pressure field and equals the weight of displaced fluid, provided the usual hydrostatic assumptions apply.

Eulerian descriptions follow fields at fixed spatial points; Lagrangian descriptions follow fluid particles. A streamline is tangent to the instantaneous velocity field. In steady flow, streamlines and particle paths coincide. A control volume is useful when the desired result is a net force or mass flow. The momentum equation must include pressure forces, weight and support forces as well as momentum crossing the boundary.

Viscosity dissipates organized mechanical energy. For a Newtonian fluid, shear stress is proportional to strain rate, with dynamic viscosity as the proportionality coefficient. Water and air are often adequately Newtonian for ordinary engineering flow; slurries, polymer melts and some food products may not be. Turbulence produces fluctuating velocity and enhanced transport. It does not remove viscosity or eliminate the no-slip condition at an ordinary stationary wall.

Bernoulli's relation is a mechanical-energy statement for restrictive conditions. In its elementary form it connects points along one streamline in steady, incompressible, inviscid flow with gravity as the body force. Pumps, turbines, heat-driven density changes and significant viscous losses require a more general balance. The velocity in a control-volume energy equation may also require a kinetic-energy correction for a nonuniform profile.

### Formula handbook

Use density $\rho$ in kg/m3, speed $V$ in m/s, dynamic viscosity $\mu$ in Pa s, pressure $p$ in Pa, length in m and force in N.

1. Hydrostatics, upward coordinate $z$, constant density over depth $h$:

$$
\frac{dp}{dz}=-\rho g,\qquad p=p_0+\rho gh.
$$

2. Hydrostatic force on a plane area, measured against a uniform reference pressure:

$$
F=\rho g h_c A.
$$

Here $h_c$ is centroid depth. For a vertical plane, center-of-pressure depth is

$$
h_{cp}=h_c+\frac{I_G}{h_cA},
$$

where $I_G$ is the second moment of area about its horizontal centroidal axis.

3. Buoyant force in a uniform-density fluid:

$$
F_B=\rho g V_{disp}.
$$

4. Volume and mass flow for a section with mean normal speed:

$$
Q=AV,\qquad \dot m=\rho Q.
$$

5. Steady mass conservation:

$$
\sum\dot m_{in}=\sum\dot m_{out}.
$$

6. Steady vector momentum balance for uniform port profiles:

$$
\sum\mathbf F=\sum_{out}\dot m\mathbf V-\sum_{in}\dot m\mathbf V.
$$

7. Bernoulli relation under the assumptions given above:

$$
\frac{p}{\rho g}+\frac{V^2}{2g}+z=\text{constant along a streamline}.
$$

8. Newtonian simple-shear law and kinematic viscosity:

$$
\tau=\mu\frac{du}{dy},\qquad \nu=\mu/\rho.
$$

9. Incompressible Newtonian momentum equation, constant viscosity:

$$
\rho\left(\frac{\partial\mathbf u}{\partial t}+\mathbf u\cdot\nabla\mathbf u\right)=-\nabla p+\mu\nabla^2\mathbf u+\rho\mathbf g,\qquad \nabla\cdot\mathbf u=0.
$$

10. Reynolds, Mach and Froude numbers:

$$
Re=\frac{\rho VL}{\mu},\qquad Ma=\frac{V}{a},\qquad Fr=\frac{V}{\sqrt{gL}}.
$$

$L$ must match the geometry and comparison; $a$ is local sound speed.

11. Drag force, with declared reference area $A_{ref}$:

$$
F_D=\frac12\rho V^2 C_D A_{ref}.
$$

12. Surface-tension pressure jump for a spherical liquid droplet:

$$
\Delta p=2\sigma/R.
$$

Here $\sigma$ is surface tension in N/m. A thin soap bubble has two interfaces and a different factor.

### Derivation

Take a small static rectangular fluid element of horizontal area $A$ and height $dz$. The upward pressure force at the bottom is $pA$; the downward pressure force at the top is $(p+dp)A$. Its weight is $\rho gA,dz$. Force balance gives $pA-(p+dp)A-\rho gA,dz=0$, so $dp/dz=-\rho g$. For constant density, integrate to obtain the linear pressure-depth relation.

For a vertical plane area, integrate $dF=\rho gh,dA$. The first area moment gives $F=\rho gh_cA$. Equating moments about the free-surface line gives $Fh_{cp}=\rho g\int h^2dA$. Using the parallel-axis theorem yields the center-of-pressure formula. Its extra positive term explains why the resultant lies below the centroid for a surface with its upper side nearer the free surface.

### Worked examples

#### Example 10-A: force on a submerged gate

A vertical rectangular gate is 2 m wide and 3 m high; its top is 1 m below the water surface. Both free surface and dry side are at atmospheric pressure. Use $\rho=1000$ kg/m3 and $g=9.81$ m/s2. Area is 6 m2 and centroid depth is 2.5 m. Resultant net force is $1000(9.81)(2.5)(6)=\mathbf{147,150\ N}$. The centroidal second moment is $2(3^3)/12=4.5$ m4. Thus $h_{cp}=2.5+4.5/(2.5\times6)=\mathbf{2.80\ m}$. The gate hinges and supports must balance both this force and its moment.

#### Example 10-B: an ideal horizontal nozzle

Water flows at 0.010 m3/s through a horizontal nozzle contracting from 0.100 to 0.050 m diameter. Assume steady incompressible inviscid flow with uniform section speeds. Continuity gives $V_1=1.27324$ m/s and $V_2=5.09296$ m/s. Bernoulli gives $p_1-p_2=\rho(V_2^2-V_1^2)/2=\mathbf{12.159\ kPa}$. The pressure reduction supplies the kinetic-energy increase. A real nozzle needs additional pressure drop to overcome losses; outlet speed at the specified flow is still fixed by area.

### Exercises

1. What gauge pressure occurs 4 m below a water surface? Use $\rho=1000$ kg/m3 and $g=9.81$ m/s2.
2. A 0.020 m3 body is fully submerged in water. Find buoyancy with the same density and gravity. Does its own mass enter the buoyancy formula?
3. Oil with $\rho=850$ kg/m3 and $\mu=0.10$ Pa s flows at 0.50 m/s in a 0.020 m diameter pipe. Calculate Reynolds number.

### Solutions

1. $p_g=\rho gh=39,240$ Pa, or 39.24 kPa. Add the actual surface absolute pressure to obtain absolute pressure.
2. $F_B=1000(9.81)(0.020)=196.2$ N. Body mass determines its weight and resulting motion, not the surrounding fluid's buoyant force for this prescribed displacement.
3. $Re=850(0.50)(0.020)/0.10=85$. This is firmly in the laminar range for ordinary fully developed circular-pipe flow.

### Common mistakes

Pressure acting on an open control-volume face is a force and cannot be ignored in a momentum balance. Equal volume flow does not imply equal speed in different areas. Gauge pressure is convenient only when a consistent atmospheric reference cancels. Use area moments in m4 for hydrostatics, not mass moments of inertia in kg m2. A Reynolds threshold from pipe flow is not a universal threshold for every geometry.

### Applications and limits

These balances support tank, gate, nozzle, jet, duct, bearing and piping calculations. Before using a drag coefficient, match its reference area, Reynolds range, geometry and roughness. Before neglecting compressibility, assess density variation and Mach number; low speed alone does not eliminate density changes caused by strong heating. Free-surface, multiphase, cavitating and non-Newtonian flows require additional constitutive and interface models.

### Further reading

- [MIT: Fluid Mechanics graduate-area guide](https://ga3.mit.edu/fluid-mechanics/) — topic map linking conservation laws, viscous flow, scaling and compressibility.
- [MIT Open Learning: Advanced Fluid Mechanics fundamentals](https://openlearning.mit.edu/courses-programs/mitx-courses/advanced-fluid-mechanics-1-fundamentals) — course overview and route to structured study; platform access conditions may vary.
- [TU Delft: The Basics of Transport Phenomena](https://ocw.tudelft.nl/courses/basics-transport-phenomena/) — freely viewable momentum, heat and mass transport materials.


---

## 11. Pipe flow and pumps

### Learning map

Prerequisites: fluid properties, continuity, mechanical energy and dimensionless groups. Learn to assemble a system curve, calculate friction and fitting losses, locate a pump operating point and assess suction conditions. This chapter emphasizes liquid systems such as water-treatment circulation and transfer lines. Compressible-gas networks and two-phase flow need additional models.

### Theory

A pumping system includes reservoirs, pipes, fittings, control valves, equipment and the pump. The pump adds mechanical energy to the liquid. The system determines how much head is required at a given flow. Actual steady operation occurs where the pump head curve intersects the system head curve. A pump's catalog rated point is not automatically the installed operating point.

Static head arises from elevation and pressure differences between system boundaries. It is present even when flow tends toward zero. Dynamic losses generally grow with flow; for turbulent flow with approximately fixed friction factor, they scale roughly with flow squared. Enlarging a pipe can reduce lifetime energy demand because velocity and friction losses fall, although installation cost may increase.

Fully developed laminar flow in a circular pipe has a parabolic profile and a friction factor determined by Reynolds number alone. Turbulent friction depends on both Reynolds number and relative roughness. Entrance effects, disturbances, developing flow and corrosion can change the effective loss. Nominal pipe size is not the bore used in the equations; use the actual internal diameter associated with material, schedule and condition.

Fittings and valves dissipate energy by separation, mixing and recirculation. Their loss coefficient is referenced to a stated velocity and geometry. In a reducer, tee or valve assembly, identify which section defines that velocity. Summing coefficients blindly across different bores creates incorrect results. A throttling valve shifts the system curve; variable-speed control changes the pump curve. Each has a different efficiency consequence.

Cavitation begins when local pressure reaches the liquid vapor-pressure region. NPSH expresses suction energy above vapor pressure in units of liquid head. Available NPSH is a system quantity; required NPSH is a pump characteristic tied to a specified test criterion. Merely exceeding a catalog NPSH value may not provide a suitable operational margin. Temperature, site atmospheric pressure, suction losses and transient conditions matter.

### Formula handbook

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

### Derivation

For steady fully developed laminar flow in a circular pipe, the axial momentum equation reduces to a balance between pressure gradient and viscous shear. Integrating with no slip at radius $R$ yields

$$
u(r)=\frac{\Delta p}{4\mu L}(R^2-r^2).
$$

Area averaging gives $V=\Delta p R^2/(8\mu L)$, or $\Delta p=32\mu LV/D^2$. Compare this with Darcy-Weisbach pressure loss $\Delta p=f_D(L/D)\rho V^2/2$. Cancellation yields $f_D=64\mu/(\rho VD)=64/Re$. This derivation uses the **Darcy** friction factor. The Fanning friction factor is one-quarter of it; replacing one with the other without changing the governing equation creates a factor-of-four error.

### Worked examples

#### Example 11-A: water-transfer pump duty

Water flows at 0.010 m3/s through 80 m of 0.100 m internal-diameter pipe. Use $f_D=0.025$, total fitting coefficient 4, density 1000 kg/m3, and static lift 12 m between open reservoirs. Velocity is 1.27324 m/s. Combined loss is $[0.025(80/0.1)+4]V^2/(2g)=1.98304$ m. Required pump head is **13.9830 m**. At pump efficiency 0.70, shaft power is $1000(9.81)(0.010)(13.9830)/0.70=\mathbf{1.95962\ kW}$. Friction factor and efficiency are supplied assumptions; actual selection needs a manufacturer curve at this duty.

#### Example 11-B: suction head available

An open tank surface is 2.0 m above the pump centerline. Atmospheric pressure is 101,325 Pa; water vapor pressure is 2340 Pa; density is 998 kg/m3. Suction loss at operating flow is 1.5 m. With negligible tank-surface velocity, $NPSH_A=(101325-2340)/(998\times9.81)+2-1.5=\mathbf{10.6104\ m}$. Compare this system value with the pump's applicable suction criterion and chosen margin over the full operating range, rather than treating the number as a universal pass condition.

### Exercises

1. A laminar pipe flow has Reynolds number 800. Find Darcy and Fanning friction factors.
2. A pump delivers 0.020 m3/s at 15 m head with density 1000 kg/m3 and efficiency 0.75. Find hydraulic and shaft powers.
3. A fitting has $K=3$ at mean speed 2 m/s. Find its head loss. What happens if that speed doubles and $K$ remains unchanged?

### Solutions

1. $f_D=64/800=0.080$ and $f_F=f_D/4=0.020$.
2. $P_h=1000(9.81)(0.020)(15)=2943$ W. $P_s=2943/0.75=3924$ W.
3. $h=3(2^2)/(2\times9.81)=0.6116$ m. At 4 m/s it becomes 2.4465 m, four times greater.

### Common mistakes

Use actual bore, not nominal diameter. Distinguish pump shaft input from motor electrical input. Evaluate viscosity and vapor pressure at relevant temperature. Do not apply affinity laws to a fixed system as though its new flow were known without finding the new intersection. A pipe strength calculation, pressure class and pipe-support analysis are separate from the hydraulic loss calculation.

### Applications and limits

A practical study records normal, minimum and maximum flow; fluid properties; static boundaries; branch arrangements; and credible valve states. Series pumps approximately add head at common flow; parallel pumps approximately add flow at common head, subject to individual curves and controls. Long lines or rapid valve movements need transient analysis. Final pump procurement requires current manufacturer curves, materials, sealing, allowable operation range and project-specific engineering review.

### Further reading

- [US DOE: Pumps resources](https://betterbuildingssolutioncenter.energy.gov/better-plants/pumps) — practical sourcebook and system-efficiency resources.
- [NIST: thermophysical fluid properties](https://webbook.nist.gov/chemistry/fluid/) — density, viscosity and vapor-state data for supported fluids.
- [TU Delft: transport-phenomena course](https://ocw.tudelft.nl/courses/basics-transport-phenomena/) — deeper momentum-transport background.


---

## 14. Turbomachinery

### Learning map

Prerequisites: fluid momentum, energy balances, rotating mechanics and thermodynamics. Learn to draw velocity triangles, relate angular momentum to shaft torque, distinguish static from stagnation properties, and use similarity with stated limits. Pumps, fans, compressors and turbines share these principles even though their fluids, speeds and operating constraints differ.

### Theory

A turbomachine exchanges energy with a continuously flowing fluid through rotating blades. A pump, fan or compressor receives shaft work and transfers it to the fluid; a turbine extracts work. Stationary guide vanes can redirect flow and convert kinetic energy into pressure, but an ideal stationary row does not supply shaft work. Rotor and stator functions must be separated when interpreting a stage diagram.

Absolute velocity is measured in a fixed frame. Relative velocity is measured with the rotating blade, while blade speed is the local tangential speed of the rotor. Their vector relation creates a velocity triangle. The tangential, or whirl, component of absolute velocity determines angular momentum. A high outlet speed alone does not guarantee useful work transfer; its direction relative to the rotor matters.

Euler's turbomachinery equation comes from angular momentum, not from assuming a particular blade shape. Its ideal work represents the energy transferred through rotor torque. Actual usable head is smaller for a pump because of hydraulic loss. Mechanical losses, leakage and disk friction further affect shaft input and efficiency. A pump can satisfy an angular-momentum calculation while failing due to cavitation, unstable operation or excessive radial load.

Static enthalpy measures thermodynamic state without the stream's macroscopic kinetic energy. Stagnation enthalpy adds that kinetic energy. In an adiabatic stationary diffuser with no work, stagnation enthalpy remains approximately constant while static pressure can rise as speed decreases. Stagnation pressure can fall because of irreversibility even if stagnation enthalpy is unchanged. This distinction is essential in compressor and turbine stage calculations.

Similarity compares machines operating at similar dimensionless conditions. Affinity laws are especially useful for modest speed changes in a fixed incompressible machine when efficiency changes little. They are not universal laws for arbitrary impeller trimming, cavitation, large compressibility changes or changes in operating regime. A dimensionless specific speed helps describe machine family; dimensional catalog specific-speed values depend on unit conventions and cannot be compared blindly.

### Formula handbook

Let $C$ be absolute velocity, $W$ relative velocity, $U$ blade speed, $r$ radius, $\omega$ angular speed in rad/s, and $C_\theta$ absolute tangential velocity. Speeds are in m/s.

1. Velocity triangles:

$$
\mathbf C=\mathbf U+\mathbf W,\qquad U=\omega r.
$$

2. Rotation-rate conversion, $N$ in revolutions per minute:

$$
\omega=\frac{2\pi N}{60}.
$$

3. Torque applied by a rotor to the fluid, for steady uniform stations:

$$
\tau=\dot m(r_2C_{\theta2}-r_1C_{\theta1}).
$$

4. Euler specific work delivered to fluid:

$$
w_E=U_2C_{\theta2}-U_1C_{\theta1},\qquad P_E=\dot m w_E.
$$

5. Euler head and useful pump head with hydraulic efficiency $\eta_h$:

$$
H_E=w_E/g,\qquad H=\eta_hH_E.
$$

6. Incompressible hydraulic power and total pump efficiency:

$$
P_h=\rho gQH,\qquad \eta_p=P_h/P_{shaft}.
$$

7. Stagnation enthalpy and ideal-gas stagnation temperature with constant $c_p$:

$$
h_0=h+\frac{C^2}{2},\qquad T_0=T+\frac{C^2}{2c_p}.
$$

8. Adiabatic rotor energy balance neglecting elevation:

$$
h_{02}-h_{01}=w_E.
$$

For a turbine, useful extracted work has the opposite sign: $w_t=h_{01}-h_{02}$.

9. Total-to-total isentropic efficiencies:

$$
\eta_c=\frac{h_{02s}-h_{01}}{h_{02}-h_{01}},\qquad \eta_t=\frac{h_{01}-h_{02}}{h_{01}-h_{02s}}.
$$

10. One consistent set of incompressible similarity coefficients:

$$
\phi=\frac{Q}{\omega D^3},\qquad \psi=\frac{gH}{\omega^2D^2},\qquad \lambda=\frac{P}{\rho\omega^3D^5}.
$$

Reference diameter $D$ and power basis must be declared. Alternative conventions may include numerical constants.

11. Fixed-diameter affinity laws at similar conditions:

$$
Q\propto N,\qquad H\propto N^2,\qquad P\propto N^3.
$$

12. Dimensionless specific speed:

$$
\Omega_s=\frac{\omega\sqrt Q}{(gH)^{3/4}}.
$$

13. A common definition of compressor corrected quantities relative to reference conditions:

$$
\dot m_{corr}=\dot m\frac{\sqrt{T_{01}/T_{ref}}}{p_{01}/p_{ref}},\qquad N_{corr}=\frac{N}{\sqrt{T_{01}/T_{ref}}}.
$$

Map definitions vary; use the manufacturer's exact reference states and units.

### Derivation

Take a steady control volume around a rotor. The axial torque on the fluid equals the change in angular-momentum flow, $\tau=\dot m(r_2C_{\theta2}-r_1C_{\theta1})$. The power supplied by the rotating shaft is $P=\omega\tau$. Divide by mass flow and substitute $U_i=\omega r_i$ to obtain

$$
\frac{P}{\dot m}=U_2C_{\theta2}-U_1C_{\theta1}.
$$

The expression automatically handles inlet prewhirl when its sign is defined consistently. Assuming zero inlet whirl simplifies it to $w_E=U_2C_{\theta2}$, but that is a flow condition rather than a universal identity. In real finite-blade centrifugal impellers, outlet flow can deviate from the blade-based ideal triangle; slip and other losses require additional modeling or measured curves.

### Worked examples

#### Example 14-A: centrifugal pump rotor

A pump has $U_1=10$, $C_{\theta1}=2$, $U_2=30$ and $C_{\theta2}=18$ m/s. The stated whirl components are actual mean values used in the rotor balance. Euler work is $30(18)-10(2)=\mathbf{520\ J/kg}$ and Euler head is **53.0071 m**. With hydraulic efficiency 0.80, delivered head is **42.4057 m**. At water flow 0.050 m3/s and density 1000 kg/m3, rotor-to-fluid power is **26.0 kW** and useful hydraulic power is **20.8 kW**. Shaft input may exceed rotor-to-fluid power when mechanical losses are included.

#### Example 14-B: speed reduction

At a reference operating point, a fixed-impeller pump delivers 0.030 m3/s at 25 m head and consumes 4.0 kW. Estimate the homologous point at 80% speed, assuming similar efficiency and no regime change. Flow becomes $0.030(0.8)=\mathbf{0.0240\ m^3/s}$, head becomes $25(0.8)^2=\mathbf{16.0\ m}$ and power becomes $4000(0.8)^3=\mathbf{2.048\ kW}$. These values describe a corresponding pump-curve point. The installed system's new operating point still requires intersection with its system curve.

### Exercises

1. A rotor radius is 0.15 m and speed is 1800 rpm. Find angular and blade speeds.
2. An adiabatic compressor raises stagnation enthalpy by 60 kJ/kg at mass flow 0.30 kg/s. Find work input to the fluid.
3. A pump's hydraulic output is 12 kW and measured shaft input is 16 kW. Find total efficiency. If motor efficiency is 0.90, find electrical input.

### Solutions

1. $\omega=2\pi(1800)/60=188.496$ rad/s and $U=\omega r=28.2743$ m/s.
2. $P=\dot m\Delta h_0=0.30(60)=18$ kW, neglecting elevation and external heat transfer.
3. $\eta_p=12/16=0.75$. Motor input is $16/0.90=17.7778$ kW, so overall hydraulic-to-electric efficiency is 67.5%.

### Common mistakes

Do not substitute relative whirl for absolute whirl in Euler's equation. Mark positive rotation and velocity components on the sketch. Keep static and stagnation efficiencies distinct. Revolutions per minute cannot be used directly in $P=\tau\omega$. Affinity scaling does not prove that cavitation margin or vibration stays acceptable. A machine's total efficiency is not identical to its hydraulic efficiency.

### Applications and limits

Velocity triangles provide insight into pumps, fans, hydraulic turbines and gas-turbine stages. Compressor surge and choke, turbine cooling, Reynolds effects, blade stress and rotor dynamics require more detailed treatment. Use actual manufacturer maps for selection and determine the operating envelope, not only one nominal point. Structural integrity, overspeed protection and pressure containment are separate design obligations.

### Further reading

- [NASA Glenn: Brayton-cycle explanation](https://www.grc.nasa.gov/www/k-12/BGP/brayton.html) — the compressor and turbine in a system-level cycle.
- [US DOE: pump-system resources](https://betterbuildingssolutioncenter.energy.gov/better-plants/pumps) — practical pump performance and system efficiency.
- [MIT: fluid-mechanics subject guide](https://ga3.mit.edu/fluid-mechanics/) — angular momentum, control volumes and supporting fluid theory.


---

## 17. Mass transfer

### Learning map

Prerequisites: conservation laws, concentration units, fluid flow and differential equations. Learn to distinguish molecular diffusion from bulk transport, use film coefficients consistently, account for interfacial equilibrium and estimate transient approach to equilibrium. Applications include drying, membranes, gas absorption, corrosion control and water-treatment aeration.

### Theory

Mass transfer is transport of a chemical species relative to a chosen reference frame or through a chosen boundary. Molecular diffusion arises from molecular motion and chemical-potential differences. In simple dilute systems, concentration gradients can represent the driving force. Bulk advection transports species with the mixture velocity. Mixing can reduce concentration differences in the bulk while a thin near-interface region still controls the overall transfer rate.

A concentration must include its basis. Molar concentration is moles per volume; mass concentration is mass per volume; mole fraction and mass fraction are dimensionless but are not numerically identical unless the components have equal molecular masses. Gas concentrations also depend on pressure and temperature. A concentration reported in mg/L must be converted carefully before combining with SI diffusivity or flow quantities.

Diffusive flux is defined relative to a reference velocity, such as the molar-average or mass-average velocity. Total flux through a stationary surface includes bulk transport as well as diffusion. In equimolar counterdiffusion, the total molar flux can vanish while each species still diffuses in opposite directions. Evaporation through stagnant carrier gas creates a net molar flow, so the simplest linear Fick expression for total flux needs correction.

Film models replace a detailed concentration boundary layer by a transfer coefficient multiplying a bulk-to-interface concentration difference. The coefficient depends on flow and geometry; it is not solely a material property. At an interface, concentrations on the two sides generally differ according to equilibrium, even when chemical potentials match. Therefore an overall resistance must convert both sides to a common driving-force basis.

Diffusion, reaction and advection often compete. A reaction can maintain a low concentration and enhance uptake, or deplete a reactant before it reaches the desired location. A well-mixed tank model assumes the liquid bulk is uniform; it does not imply infinite transfer through bubble or wall boundary layers. The volumetric coefficient $k_La$ combines a liquid-side coefficient with interfacial area per liquid volume, making it useful for aeration and absorption models.

### Formula handbook

Use diffusivity $D_{AB}$ in m2/s, concentration $c_A$ in mol/m3, molar flux in mol/(m2 s), transfer coefficient $k_c$ in m/s, and time in s. Mass-concentration equations have analogous forms when the basis is used consistently.

1. Binary Fickian diffusive molar flux relative to the molar-average velocity, constant total concentration $c$:

$$
\mathbf J_A=-cD_{AB}\nabla y_A=-D_{AB}\nabla c_A.
$$

2. Total molar flux through a stationary plane:

$$
N_A=J_A+y_A(N_A+N_B).
$$

3. Steady one-dimensional diffusion through a slab, constant $D$ and equimolar counterdiffusion or no bulk transport:

$$
N_A=D_{AB}\frac{c_{A,1}-c_{A,2}}{L},\qquad \dot n_A=AN_A.
$$

4. Species balance with constant diffusivity, incompressible mixture and molar production rate $r_A$:

$$
\frac{\partial c_A}{\partial t}+\mathbf u\cdot\nabla c_A=D_{AB}\nabla^2c_A+r_A.
$$

5. Characteristic diffusion time:

$$
t_D\sim L^2/D_{AB}.
$$

This is an order-of-magnitude timescale; exact approach times depend on geometry and boundary conditions.

6. Film transfer law:

$$
N_A=k_c(c_{A,s}-c_{A,b}).
$$

Subscripts $s$ and $b$ denote interface and bulk; sign follows the chosen direction.

7. Sherwood, Schmidt and mass Peclet numbers:

$$
Sh=\frac{k_cL}{D_{AB}},\qquad Sc=\frac{\nu}{D_{AB}},\qquad Pe_m=\frac{VL}{D_{AB}}=Re\,Sc.
$$

8. First-order reaction-diffusion comparison, rate constant $k_r$ in 1/s:

$$
Da_D=\frac{k_rL^2}{D_{AB}}.
$$

9. Gas-liquid interfacial equilibrium in one specified concentration convention:

$$
c_{A,g}^{*}=m\,c_{A,l}.
$$

Here $m$ is the dimensionless gas-to-liquid concentration partition ratio for both concentrations in mol/m3. Other Henry-law conventions have different units and reciprocal forms.

10. Two-film overall coefficient on the gas concentration basis:

$$
N_A=K_g(c_{A,g,b}-m c_{A,l,b}),\qquad \frac1{K_g}=\frac1{k_g}+\frac{m}{k_l}.
$$

11. Well-mixed batch liquid with constant equilibrium concentration and no reaction:

$$
\frac{dC}{dt}=k_La(C^*-C),\qquad C(t)=C^*-(C^*-C_0)e^{-k_Lat}.
$$

$k_La$ is in 1/s; $C$ may be mass concentration if every term uses that basis.

12. Binary ideal-gas diffusion of A through stagnant B, constant pressure and temperature:

$$
N_A=\frac{D_{AB}c}{L}\ln\left(\frac{1-y_{A,2}}{1-y_{A,1}}\right),\qquad N_B=0.
$$

13. Simple solution-diffusion membrane model:

$$
N_A=\frac{\mathcal P_A}{L}(p_{A,1}-p_{A,2}),\qquad \mathcal P_A=D_AS_A.
$$

Solubility $S_A$ is mol/(m3 Pa), so permeability $\mathcal P_A$ is mol/(m s Pa). Actual membranes may show nonlinear sorption and coupled transport.

### Derivation

Derive the two-film overall resistance to make the concentration basis explicit. At steady transfer from gas to liquid, the same flux crosses each film:

$$
N_A=k_g(c_{g,b}-c_{g,i})=k_l(c_{l,i}-c_{l,b}).
$$

Interfacial equilibrium gives $c_{g,i}=m c_{l,i}$. Add the gas-film drop to $m$ times the liquid-film drop:

$$
c_{g,b}-m c_{l,b}=N_A\left(\frac1{k_g}+\frac{m}{k_l}\right).
$$

Comparison with the overall transfer law gives the resistance relation. A large gas-to-liquid partition ratio amplifies the liquid-film resistance on this gas concentration basis. Swapping to a pressure-based Henry constant without converting units would change the equation and produce a dimensional error.

### Worked examples

#### Example 17-A: diffusion across a stagnant layer

A dilute species diffuses through a 0.0020 m layer over area 0.10 m2. Use constant diffusivity $2.0\times10^{-9}$ m2/s and boundary concentrations 5.0 and 1.0 mol/m3. Assume steady one-dimensional diffusion, no reaction and no relevant bulk transport. Flux is $D\Delta c/L=\mathbf{4.0\times10^{-6}\ mol/(m^2s)}$. Transfer rate is **$4.0\times10^{-7}$ mol/s**, or **0.00144 mol/h**. Doubling thickness at the same boundary concentrations halves this steady rate; it also increases the diffusion timescale by a factor of four.

#### Example 17-B: dissolved-gas approach to equilibrium

A well-mixed 2.0 m3 liquid tank begins with dissolved-gas concentration zero. The maintained equilibrium concentration is 8.0 mg/L and the supplied $k_La$ is 0.030 s-1. Ignore reaction, outflow and variation of equilibrium conditions. After 100 s, $C=8[1-e^{-0.03(100)}]=\mathbf{7.60170\ mg/L}$. Since 1 mg/L equals 0.001 kg/m3, the tank then contains $2(0.00760170)=\mathbf{0.0152034\ kg}$ of dissolved gas. This is a transfer model with prescribed parameters, not an aerator performance prediction.

### Exercises

1. A 0.0010 m slab has diffusivity $10^{-9}$ m2/s and concentration difference 2.0 mol/m3. Find steady flux under the same assumptions as Example 17-A.
2. A film coefficient is $10^{-4}$ m/s, reference length 0.010 m and diffusivity $2\times10^{-9}$ m2/s. Find Sherwood number.
3. A batch tank begins at zero concentration and has constant $k_La=0.020$ s-1. Find the time to reach 90% of equilibrium concentration.

### Solutions

1. $N_A=10^{-9}(2)/0.001=2.0\times10^{-6}$ mol/(m2 s). Its diffusion timescale is approximately $L^2/D=1000$ s, so a steady approximation should be justified relative to the observation time.
2. $Sh=10^{-4}(0.010)/(2\times10^{-9})=500$. This dimensionless value compares the film coefficient with a diffusion scale; it is not an efficiency.
3. $0.9=1-e^{-0.020t}$ gives $t=-\ln(0.1)/0.020=115.129$ s.

### Common mistakes

Distinguish total flux from diffusive flux and specify the reference frame. Do not confuse mass fraction with molar concentration. A tabulated Henry constant must be used with its exact convention and temperature. Transfer coefficients depend on hydrodynamics and area definition. The gas-liquid interface can have unequal concentrations in the two phases while still satisfying equilibrium. Increasing agitation does not necessarily change equilibrium solubility, although it often changes the rate of approach.

### Applications and limits

These balances appear in drying, evaporation, humidification, membrane separation and oxygen transfer. Coupled heat and mass transfer can change surface temperature and thus the equilibrium driving force. Real aeration needs measured or justified $k_La$, oxygen demand, gas-phase depletion and water-quality corrections. Reactive absorption, multicomponent diffusion and porous media require additional constitutive relations beyond the binary dilute models introduced here.

### Further reading

- [TU Delft: Mass transfer introduction](https://ocw.tudelft.nl/course-lectures/mass-transfer-introduction/) — freely viewable transport course material.
- [TU Delft: The Basics of Transport Phenomena](https://ocw.tudelft.nl/courses/basics-transport-phenomena/) — connections among momentum, heat and mass transport.
- [MIT OCW: Intermediate Heat and Mass Transfer](https://ocw.mit.edu/courses/2-51-intermediate-heat-and-mass-transfer-fall-2008/) — deeper analytical treatment after the introductory balances.
