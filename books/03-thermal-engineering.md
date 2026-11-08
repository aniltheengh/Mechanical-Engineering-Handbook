# Thermodynamics and thermal engineering

Mechanical Engineering Handbook · Expanded edition · 2026-11-08

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [08. Thermodynamics](../chapters/08-thermodynamics.md)
- [09. Power cycles](../chapters/09-power-cycles.md)
- [12. Heat transfer](../chapters/12-heat-transfer.md)
- [13. Heat exchangers](../chapters/13-heat-exchangers.md)
- [15. Refrigeration and HVAC](../chapters/15-refrigeration-and-hvac.md)
- [16. Combustion and internal-combustion engines](../chapters/16-combustion-and-engines.md)

---

## 08. Thermodynamics

### Learning map

Prerequisites: SI units, algebra, integration and mechanical work. Learn to choose a system boundary, identify properties, apply energy and entropy balances, and distinguish an attainable process from a reversible limit. Continue to power cycles, refrigeration, combustion and heat transfer after this chapter. Thermodynamics answers how much energy a process needs and which direction it can proceed; heat transfer determines how quickly the thermal part occurs.

### Theory

A **closed system** contains a fixed mass. A **control volume** is a region through which mass may flow. An insulated tank, a compressor and a heat exchanger need different boundaries even when they contain the same substance. Choose the boundary before selecting an equation: otherwise shaft work can be counted twice or a mass-flow energy term omitted.

A property depends on the state, not the path used to reach it. Temperature, pressure, specific volume, internal energy, enthalpy and entropy are properties. Heat and work are transfers across a boundary and are not stored substances. A body stores energy, not heat. Equilibrium means no unresolved thermal, mechanical or chemical driving force remains within the chosen model. A quasi-equilibrium path can be represented by successive equilibrium states; it need not be reversible if friction remains.

An extensive property scales with system size; a specific property is per unit mass. Enthalpy combines internal energy and the pressure-volume contribution needed to move material into or out of a control volume. For an ideal gas, internal energy and enthalpy depend on temperature alone. This does not imply constant heat capacity. Constant $c_p$ and $c_v$ are additional approximations suitable only over an appropriate range.

For a pure substance in a two-phase liquid-vapor equilibrium region, pressure and temperature are linked by the saturation relation. Quality is vapor mass divided by total mass; it is meaningful only in that region. A temperature alone does not identify a superheated-vapor state. State tables require a sufficient pair of independent properties and a consistent reference convention.

The first law conserves energy. The second law constrains conversion: dissipating shaft work into thermal energy is easy, while converting heat from a single reservoir entirely into cyclic work is impossible. Entropy generation measures irreversibility; it does not measure an energy loss. Exergy measures useful-work potential relative to a specified environment. Mixing, throttling, friction and heat transfer across finite temperature differences destroy exergy while conserving energy.

### Formula handbook

Use heat $Q>0$ into a system and work $W>0$ done by it. Specific quantities are in J/kg, rates in W, mass in kg, pressure in Pa and absolute temperature in K.

1. Ideal-gas state equation, with gas-specific $R$ in J/(kg K):

$$
pV=mRT,\qquad pv=RT.
$$

2. Enthalpy and caloric changes for an ideal gas:

$$
h=u+pv,\qquad \Delta u=\int_{T_1}^{T_2}c_v(T)\,dT,\qquad \Delta h=\int_{T_1}^{T_2}c_p(T)\,dT.
$$

3. Ideal-gas heat-capacity relation and ratio:

$$
c_p-c_v=R,\qquad \gamma=c_p/c_v.
$$

4. Closed-system first law, including kinetic and potential energy:

$$
\Delta U+\Delta KE+\Delta PE=Q-W.
$$

5. Boundary work for a quasi-equilibrium simple compressible process:

$$
W_b=\int_{V_1}^{V_2}p\,dV.
$$

For a strongly irreversible expansion, use the appropriate external resisting pressure and a mechanically consistent boundary model, not an assumed equilibrium gas path.

6. Steady one-inlet, one-outlet energy balance, with $V_f$ denoting flow speed:

$$
\dot Q-\dot W_s=\dot m\left[h_2-h_1+\frac{V_{f,2}^2-V_{f,1}^2}{2}+g(z_2-z_1)\right].
$$

7. Closed-system entropy balance, boundary temperatures $T_b$:

$$
\Delta S=\int\frac{\delta Q}{T_b}+S_{gen},\qquad S_{gen}\geq0.
$$

8. Constant-heat-capacity ideal-gas entropy change:

$$
s_2-s_1=c_p\ln(T_2/T_1)-R\ln(p_2/p_1).
$$

9. Isentropic ideal-gas relation, constant $\gamma$:

$$
\frac{T_{2s}}{T_1}=\left(\frac{p_2}{p_1}\right)^{(\gamma-1)/\gamma}.
$$

10. Adiabatic compressor and turbine isentropic efficiencies:

$$
\eta_c=\frac{h_{2s}-h_1}{h_2-h_1},\qquad \eta_t=\frac{h_1-h_2}{h_1-h_{2s}}.
$$

11. Saturated mixture property, for $y=v,u,h,s$:

$$
y=y_f+x(y_g-y_f),\qquad 0\leq x\leq1.
$$

12. Exergy destruction for environmental temperature $T_0$:

$$
E_{D}=T_0S_{gen}.
$$

### Derivation

Derive the ideal-gas isentropic temperature relation instead of memorizing its exponent. For a simple compressible ideal gas, $Tds=dh-vdp$. Substitute $dh=c_p\,dT$ and $v=RT/p$, then divide by temperature:

$$
ds=c_p\frac{dT}{T}-R\frac{dp}{p}.
$$

For constant heat capacity and $ds=0$, integration gives $c_p\ln(T_2/T_1)=R\ln(p_2/p_1)$. Since $R/c_p=(\gamma-1)/\gamma$, exponentiation yields formula 9. Adiabatic alone is insufficient: an adiabatic real compressor produces entropy, so its temperature rise exceeds the isentropic rise for the same pressure ratio. For a throttling valve with negligible heat, shaft work and changes in speed or elevation, the first law instead gives $h_1=h_2$; throttling is not isentropic.

### Worked examples

#### Example 08-A: heating air in a rigid tank

A rigid sealed tank contains 2.00 kg of air heated from 300 to 380 K. Use $c_v=718$ J/(kg K), neglect changes in speed and height, and assume no electrical or shaft work crosses the boundary. Rigidity makes boundary work zero. Therefore $Q=\Delta U=mc_v\Delta T=2(718)(80)=114,880$ J, or **114.88 kJ**. The final-to-initial pressure ratio is $380/300=1.267$ under the ideal-gas model. Using $c_p$ would incorrectly include flow work that this boundary does not have.

#### Example 08-B: actual compressor power

Air enters an insulated compressor at 300 K and 100 kPa and leaves at 400 kPa. Let $\dot m=0.12$ kg/s, $c_p=1005$ J/(kg K), $\gamma=1.4$ and $\eta_c=0.80$. Neglect speed and elevation changes. First $T_{2s}=300(4)^{0.4/1.4}=445.798$ K. Then $T_2=300+(445.798-300)/0.80=482.248$ K. Shaft input is $\dot m c_p(T_2-T_1)=21,979.1$ W, or **21.979 kW**. The larger actual temperature rise is consistent with positive entropy generation. Motor electrical input would be larger still if motor efficiency were included.

### Exercises

1. A closed system receives 25 kJ of heat and performs 9 kJ of work. Its kinetic and potential energies remain fixed. Find its internal-energy change.
2. A hypothetical saturated mixture has $h_f=500$ and $h_g=2700$ kJ/kg. Find its enthalpy at quality 0.25. These are supplied exercise data, not a steam-table state.
3. A steady adiabatic turbine receives 0.5 kg/s with an actual enthalpy drop of 80 kJ/kg. Find shaft output and the isentropic drop when efficiency is 0.80.

### Solutions

1. $\Delta U=Q-W=25-9=16$ kJ. Positive means stored internal energy rises.
2. $h=500+0.25(2700-500)=1050$ kJ/kg. Quality weights phase mass, not phase volume.
3. $\dot W=0.5(80)=40$ kW. The isentropic drop is $80/0.80=100$ kJ/kg, larger than the actual useful drop.

### Common mistakes

Confusing absolute with gauge pressure corrupts gas laws. Mixing J/kg and kJ/kg causes factors of 1000 in power. Entropy can decrease within a system if sufficient entropy leaves with heat or mass; only generation must be nonnegative. A cyclic device has zero net change of every state property, not zero heat or work. Do not use quality for compressed liquid or superheated vapor.

### Applications and limits

Apply these balances to tanks, turbines, compressors, valves and thermal plants. Record assumptions before solving and test the sign and scale of the result afterwards. For real steam, refrigerants, high-pressure gases and wide temperature ranges, use a documented property model or tables. This chapter supplies the balance framework, not a substitute for a full property database or a design code.

### Further reading

- [MIT OCW: Thermal Energy](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/) — free course notes and problems for thermodynamic fundamentals and applications.
- [NIST Chemistry WebBook: fluid properties](https://webbook.nist.gov/chemistry/fluid/) — reference property data; select fluid, state, units and reference convention explicitly.
- [MIT OCW: Advanced Thermodynamics](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/pages/syllabus/) — a route into equilibrium and nonequilibrium theory after the fundamentals.


---

## 09. Power cycles

### Learning map

Prerequisites: the first and second laws, enthalpy, entropy and ideal-gas processes. Learn to label state points, compute component work and heat, distinguish thermal efficiency from output, and compare ideal reference cycles. This chapter covers Carnot, Otto, Diesel, Brayton and Rankine cycles and introduces regeneration, reheat and combined cycles.

### Theory

A thermodynamic cycle returns its working fluid to its initial state. Because stored energy returns to its initial value, net work equals net heat over a complete cycle. A heat engine receives energy at a higher temperature, produces work and rejects energy at a lower temperature. Its thermal efficiency describes the fraction of input heat converted to net work; it does not specify the amount of power or the physical size of the machine.

The Carnot cycle consists of two reversible isotherms and two reversible adiabats. It supplies an upper limit for a heat engine operating between two reservoirs, not a practical layout. If heating and cooling occur over changing temperatures, the highest temperature and lowest temperature give a bound but do not determine the actual efficiency. A proposed cycle must also satisfy positive net work and physically attainable component states.

Air-standard models replace reacting fuel-air mixtures with a fixed mass of ideal gas. Heat addition replaces combustion; heat rejection restores the original state. Cold-air-standard calculations additionally use constant heat capacities. The Otto model uses constant-volume heat addition and rejection; the Diesel model adds heat at constant pressure. Their efficiency formulas compare idealized cycles, not complete real engines with intake, exhaust, friction, incomplete combustion and cooling losses.

The Brayton cycle models a compressor, constant-pressure heater, turbine and constant-pressure cooler. In an open gas turbine, fresh air and exhaust replace the closed-loop cooler conceptually. A significant part of turbine work drives the compressor. Increasing pressure ratio can improve ideal efficiency while reducing net work beyond an optimum set by turbine-inlet temperature. These two objectives should not be confused.

The Rankine cycle uses liquid pumping, heating and vaporization, vapor expansion, and condensation. Pumping liquid requires much less work than compressing vapor over the same pressure rise because liquid specific volume is small. Real steam turbines face wetness and material-temperature constraints. Reheat reduces some expansion wetness and can improve work output; feedwater regeneration improves the average temperature of heat addition but changes steam flow through different turbine sections.

### Formula handbook

Use specific heat and work in J/kg, enthalpy in J/kg, temperature in K and power in W. Magnitudes $q_{in},q_{out},w_t,w_c,w_p$ below are positive unless stated otherwise.

1. Cycle energy and thermal efficiency:

$$
w_{net}=q_{in}-q_{out},\qquad \eta_{th}=w_{net}/q_{in}.
$$

2. Reversible two-reservoir limit:

$$
\eta_{Carnot}=1-T_L/T_H.
$$

3. Cold-air-standard Otto efficiency, compression ratio $r=V_{max}/V_{min}$:

$$
\eta_{Otto}=1-\frac{1}{r^{\gamma-1}}.
$$

4. Cold-air-standard Diesel efficiency, cutoff ratio $r_c=V_3/V_2$:

$$
\eta_{Diesel}=1-\frac{1}{r^{\gamma-1}}\frac{r_c^\gamma-1}{\gamma(r_c-1)}.
$$

5. Ideal Brayton efficiency, pressure ratio $r_p=p_2/p_1=p_3/p_4$:

$$
\eta_{Brayton}=1-r_p^{-(\gamma-1)/\gamma}.
$$

6. Ideal Brayton state temperatures, constant $\gamma$:

$$
T_2=T_1r_p^{(\gamma-1)/\gamma},\qquad T_4=T_3r_p^{-(\gamma-1)/\gamma}.
$$

7. Compressor and turbine specific work, constant $c_p$:

$$
w_c=c_p(T_2-T_1),\qquad w_t=c_p(T_3-T_4),\qquad w_{net}=w_t-w_c.
$$

8. Brayton heat input and back-work ratio:

$$
q_{in}=c_p(T_3-T_2),\qquad BWR=w_c/w_t.
$$

9. Ideal Brayton pressure ratio for maximum specific net work with fixed $T_1,T_3$:

$$
r_{p,opt}=\left(T_3/T_1\right)^{\gamma/[2(\gamma-1)]}.
$$

10. Rankine pump approximation for incompressible liquid, pump efficiency $\eta_p$:

$$
w_p\simeq v_f(p_2-p_1)/\eta_p.
$$

11. Rankine states: 1 condenser exit, 2 pump exit, 3 turbine inlet, 4 turbine exit:

$$
q_{in}=h_3-h_2,\quad q_{out}=h_4-h_1,\quad w_t=h_3-h_4,\quad \eta_{th}=\frac{w_t-w_p}{q_{in}}.
$$

12. Net power and fuel conversion:

$$
\dot W_{net}=\dot m w_{net},\qquad \eta_{fuel}=\frac{\dot W_{net}}{\dot m_f H_f}.
$$

$H_f$ is a specified higher or lower heating value in J/kg; never mix its basis between comparisons. Plant auxiliaries must be included for plant-net power.

### Derivation

For the ideal Brayton cycle, put $a=r_p^{(\gamma-1)/\gamma}$. The isentropic relations give $T_2=aT_1$ and $T_4=T_3/a$. Thus

$$
\frac{q_{out}}{q_{in}}=\frac{c_p(T_4-T_1)}{c_p(T_3-T_2)}=\frac{T_3/a-T_1}{T_3-aT_1}=\frac1a.
$$

This proves the efficiency formula under equal pressure ratios and constant heat capacity. For maximum work, differentiate $w_{net}/c_p=T_3-T_3/a-aT_1+T_1$ with respect to $a$. Setting $T_3/a^2-T_1=0$ gives $a=\sqrt{T_3/T_1}$. Increasing $a$ beyond this point still raises ideal efficiency but reduces specific output. Pressure losses and nonideal component efficiencies change both relations.

### Worked examples

#### Example 09-A: Otto reference efficiency

An ideal cold-air-standard Otto cycle has compression ratio 8.0 and $\gamma=1.4$. Its efficiency is $1-8^{-0.4}=0.564725$, or **56.47%**. If heat input is 800 kJ/kg per cycle, net work is $0.564725(800)=451.780$ kJ/kg. This is an ideal thermodynamic benchmark; it is not a predicted brake efficiency for a road engine.

#### Example 09-B: Brayton work and efficiency

An ideal Brayton cycle operates with $T_1=300$ K, $T_3=1200$ K, $r_p=6$, $c_p=1005$ J/(kg K), and $\gamma=1.4$. Compute $T_2=500.553$ K and $T_4=719.204$ K. Turbine work is **483.200 kJ/kg**; compressor work is **201.556 kJ/kg**. Net work is **281.644 kJ/kg**. Heat input is $1005(1200-500.553)=702.944$ kJ/kg, giving efficiency **40.066%**. Back-work ratio is approximately 0.417. At 2 kg/s, net power would be 563.287 kW before mechanical losses and auxiliaries.

### Exercises

1. Find the reversible heat-engine efficiency between reservoirs at 900 K and 300 K.
2. Use supplied hypothetical Rankine enthalpies $h_1=200$, $h_2=210$, $h_3=3200$, $h_4=2200$ kJ/kg. Find net work and efficiency.
3. A cycle takes 2 MW of heat and rejects 1.2 MW. Find net power and thermal efficiency. Would a 50 kW auxiliary load increase or decrease plant-net efficiency?

### Solutions

1. $1-300/900=0.6667$, or 66.67%. Actual operation between those reservoirs must not exceed this bound.
2. Turbine work is 1000 kJ/kg, pump work 10 kJ/kg and heat input 2990 kJ/kg. Net work is 990 kJ/kg and efficiency is $990/2990=33.11\%$. The supplied values teach bookkeeping and do not assert an actual steam state.
3. Net cycle output is 0.8 MW and efficiency is 40%. Subtracting auxiliaries gives 0.75 MW and plant-net efficiency 37.5% on the same heat-input basis.

### Common mistakes

Using Celsius in temperature ratios destroys the second-law bound. Ignoring compressor work greatly overestimates gas-turbine output. Comparing cycles at different peak temperatures, heat inputs or pressure limits without saying so gives misleading rankings. A steam quality calculated outside zero to one signals an incorrect region or assumed state. Boiler efficiency, cycle efficiency and overall fuel-to-electricity efficiency are different quantities.

### Applications and limits

Use cycle models for architecture comparisons and first estimates, then introduce pressure drops, variable heat capacities, measured component maps, cooling flows and real-fluid properties. Combined cycles recover gas-turbine exhaust heat in a steam bottoming cycle. A regenerator is useful only when the exhaust can heat the compressed stream across a feasible temperature difference. Economic, maintenance and emission constraints often determine the final design more strongly than ideal efficiency alone.

### Further reading

- [NASA Glenn: Brayton cycle](https://www.grc.nasa.gov/www/k-12/BGP/brayton.html) — introductory gas-turbine thermodynamic cycle explanation.
- [NASA Glenn: engine thermodynamic analysis](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/engine-thermodynamic-analysis/) — an ideal Otto-cycle development.
- [US Department of Energy: steam systems](https://www.energy.gov/cmei/ito/steam-systems) — practical steam-system publications and links; consult current project requirements separately.


---

## 12. Heat transfer

### Learning map

Prerequisites: energy balances, differential equations and basic fluid mechanics. Learn to identify conduction, convection and radiation paths, build thermal-resistance models, distinguish steady from transient behavior, and choose an appropriate length scale. Heat transfer converts a required heating or cooling duty into an area, temperature difference or time.

### Theory

Conduction transports energy through microscopic interactions within material. In a stationary solid, its rate is related to the temperature gradient and thermal conductivity. A high conductivity does not mean a body must be hot; it means a given gradient can support a larger heat flux. For anisotropic materials such as composites, conductivity can depend on direction and must be represented by a tensor when the direction matters.

Convection combines transport near a surface with fluid motion. The heat-transfer coefficient is a useful boundary relation, not an intrinsic material property like density. It depends on flow, geometry, fluid properties and thermal conditions. Forced convection uses externally driven flow; natural convection arises from buoyancy induced by density differences. A correlation is valid only for the stated geometry, boundary condition and dimensionless parameter ranges.

Thermal radiation is electromagnetic energy exchange. Every surface above absolute zero emits radiation, while net exchange also depends on what it sees and absorbs. Surface emissivity can vary with wavelength, temperature and finish. The simple gray-body-to-large-surroundings formula assumes a particular radiative environment. Two finite surfaces require view factors and, when reflections matter, a radiation-network treatment.

Steady state means no energy accumulation; it does not mean temperature is uniform. A plane wall can have a permanent temperature gradient carrying a constant heat rate. Resistances in series carry the same steady heat rate, while parallel paths share the same endpoint temperature difference. Thermal bridges and contact gaps can dominate a nominally well-insulated construction.

Transient problems also include storage. A lumped-capacitance model assumes the body is nearly uniform in temperature at every instant. Small size or high conductivity helps make this plausible. When internal gradients matter, solve the transient conduction equation or use appropriate analytical series solutions. A large external heat-transfer coefficient accelerates surface response but may make the lumped assumption worse.

### Formula handbook

Use heat rate $\dot Q$ in W, heat flux $q''$ in W/m2, conductivity $k$ in W/(m K), convection coefficient $h$ in W/(m2 K), and resistance in K/W.

1. Fourier's law in one direction:

$$
q_x''=-k\frac{dT}{dx}.
$$

2. Constant-conductivity plane-wall resistance:

$$
R_{wall}=\frac{L}{kA},\qquad \dot Q=\frac{T_1-T_2}{R_{wall}}.
$$

3. Cylindrical-wall resistance, length $L_z$:

$$
R_{cyl}=\frac{\ln(r_o/r_i)}{2\pi kL_z}.
$$

4. Convection relation and resistance:

$$
\dot Q=hA(T_s-T_\infty),\qquad R_{conv}=\frac1{hA}.
$$

5. Series thermal circuit without internal generation:

$$
\dot Q=\frac{T_{hot}-T_{cold}}{\sum R_i}.
$$

6. Small gray surface in large isothermal surroundings, temperatures in K:

$$
\dot Q_{rad}=\varepsilon\sigma A(T_s^4-T_{sur}^4),\qquad \sigma\simeq5.670374419\times10^{-8}\ \mathrm{W/(m^2K^4)}.
$$

7. Constant-property heat equation in a stationary solid:

$$
\rho c_p\frac{\partial T}{\partial t}=k\nabla^2T+\dot q'''.
$$

$\dot q'''$ is volumetric generation in W/m3.

8. Thermal diffusivity, Biot number and Fourier number:

$$
\alpha=\frac{k}{\rho c_p},\qquad Bi=\frac{hL_c}{k},\qquad Fo=\frac{\alpha t}{L_c^2}.
$$

For lumped analysis, $L_c=V/A_s$. Other analytical solutions can define their own characteristic length.

9. Lumped cooling under constant properties, $h$ and ambient temperature:

$$
\frac{T(t)-T_\infty}{T_i-T_\infty}=e^{-t/\tau},\qquad \tau=\frac{mc_p}{hA_s}.
$$

10. Convection dimensionless groups:

$$
Nu=\frac{hL}{k_f},\qquad Pr=\frac{\nu}{\alpha_f},\qquad Ra=\frac{g\beta|T_s-T_\infty|L^3}{\nu\alpha_f}.
$$

$k_f,\alpha_f$ are fluid properties; $\beta$ is volumetric thermal expansion coefficient in 1/K.

11. Straight uniform fin with an adiabatic tip and constant properties:

$$
m_f=\sqrt{\frac{hP}{kA_c}},\qquad \dot Q_f=\sqrt{hPkA_c}(T_b-T_\infty)\tanh(m_fL),\qquad \eta_f=\frac{\tanh(m_fL)}{m_fL}.
$$

$P$ is wetted perimeter, $A_c$ cross-sectional area and $L$ fin length.

12. Critical insulation radius for a long cylinder with constant external $h$:

$$
r_{crit}=k_{ins}/h.
$$

This limited model balances added conduction resistance against increased convecting area; it does not imply that insulation generally increases heat loss.

### Derivation

For a lumped body with no internal heat generation and negligible radiation, energy conservation gives $mc_p,dT/dt=-hA_s(T-T_\infty)$. Divide by $(T-T_\infty)$ and integrate from $T_i$ at time zero:

$$
\ln\left(\frac{T-T_\infty}{T_i-T_\infty}\right)=-\frac{hA_s}{mc_p}t.
$$

Exponentiation gives the cooling law. The ratio tends to one at zero time and to zero as time tends to infinity, which are useful boundary checks. A common preliminary criterion is $Bi<0.1$, but its adequacy depends on required accuracy and the actual geometry. Adding radiation makes the governing equation nonlinear unless an appropriate linearized coefficient is justified.

### Worked examples

#### Example 12-A: heat loss through a wall

A 10 m2 wall has thickness 0.15 m and conductivity 0.80 W/(m K). Indoor and outdoor air are 50 and 20 degrees Celsius. Convection coefficients are 8 and 20 W/(m2 K). Ignore radiation and thermal bridges. The total resistance is $1/(8\times10)+0.15/(0.8\times10)+1/(20\times10)=0.03625$ K/W. Heat loss is $30/0.03625=\mathbf{827.586\ W}$. Using only wall conduction would predict 1600 W and omit the finite surface temperature drops.

#### Example 12-B: a small metal part cooling

A 0.020 kg part has $c_p=500$ J/(kg K), exposed area 0.010 m2 and $h=20$ W/(m2 K). Its initial temperature is 70 degrees Celsius and ambient is 20 degrees Celsius. With supplied conductivity 15 W/(m K) and density 7800 kg/m3, $L_c=(m/\rho)/A_s=0.0002564$ m and $Bi=0.000342$, supporting the lumped approximation. Time constant is **50.0 s**. After 300 s, $T=20+50e^{-6}=\mathbf{20.12394\ ^\circ C}$. This is a convection-only model with constant properties, not a measured cooldown curve.

### Exercises

1. A 0.010 m thick plate of area 0.50 m2 and conductivity 20 W/(m K) has a 30 K temperature difference. Find its steady conductive heat rate.
2. A body has $mc_p=200$ J/K and $hA=5$ W/K. How long does its excess temperature take to fall to 10% of its initial value?
3. A body has $h=100$ W/(m2 K), $L_c=0.020$ m and $k=0.20$ W/(m K). Calculate Biot number and assess a lumped model.

### Solutions

1. $\dot Q=kA\Delta T/L=20(0.5)(30)/0.01=30,000$ W. The temperature gradient is large because the plate is thin.
2. $\tau=200/5=40$ s. Solve $0.1=e^{-t/40}$ to obtain $t=40\ln10=92.10$ s.
3. $Bi=100(0.020)/0.20=10$. Internal gradients are likely important; a uniform-temperature assumption is not justified by the usual criterion.

### Common mistakes

Use Kelvin for fourth-power radiation terms. Distinguish heat rate from heat flux and conductivity from convection coefficient. Do not add parallel-path resistances as though they were in series. Use the area appropriate to each cylindrical surface. A convection correlation using fluid conductivity cannot accept solid conductivity. A thermal time constant is not the time to reach ambient exactly; ideal exponential cooling approaches ambient asymptotically.

### Applications and limits

Applications include insulation, electronics cooling, furnaces, casting, heat treatment and biological temperature control. First check energy balance and resistance dominance; then refine the part that controls uncertainty. Contact resistance, fouling, boiling, condensation and temperature-dependent properties may dominate simple conduction estimates. Finite-element thermal analysis still needs realistic boundary conditions and an energy-balance check.

### Further reading

- [MIT OCW: Intermediate Heat and Mass Transfer](https://ocw.mit.edu/courses/2-51-intermediate-heat-and-mass-transfer-fall-2008/) — advanced undergraduate course materials.
- [Lienhard and Lienhard: A Heat Transfer Textbook, sixth edition](https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/6/1810/files/2024/04/AHTTv600.pdf) — author-distributed full textbook PDF; consult its own license before redistribution.


---

## 13. Heat exchangers

### Learning map

Prerequisites: thermodynamics, convection, conduction resistance and logarithms. Learn to close hot- and cold-side energy balances, use logarithmic mean temperature difference for known terminal temperatures, and use effectiveness-NTU when outlet temperatures are unknown. Treat thermal performance and pressure loss as coupled design questions.

### Theory

A recuperative heat exchanger transfers energy between streams separated by a wall. Double-pipe, shell-and-tube, plate and finned-tube designs differ in compactness, cleaning access, pressure capability and flow distribution. A regenerator stores heat temporarily in a matrix and transfers it to another stream at a later time; its analysis differs from a continuously separating wall.

For a well-insulated exchanger at steady state, heat lost by the hot stream equals heat gained by the cold stream. A mismatch in measured duties can reveal heat leakage, transient storage, inaccurate flow measurement or an inappropriate property estimate. Temperature changes alone do not determine duty: mass flow and heat capacity are also required. During phase change, use enthalpy change rather than forcing a constant-specific-heat expression through the two-phase region.

Parallel flow sends both streams in the same direction; counterflow sends them in opposite directions. Counterflow can maintain a more uniform temperature difference and can produce a cold outlet warmer than the hot outlet, because those outlets occur at opposite ends. A cold outlet cannot exceed the hot inlet in a passive two-stream exchanger under the usual assumptions. The temperature difference at every local contact must remain thermodynamically consistent.

The overall coefficient combines both convection resistances, the wall and fouling layers. Its numerical value depends on the chosen reference area. An inner-area coefficient and an outer-area coefficient for the same tube are not generally equal, although their products with their respective areas are. Fouling decreases conductance over time; adding area for fouling does not replace a cleaning and maintenance plan.

The LMTD method is convenient when inlet and outlet temperatures are known. Effectiveness-NTU is convenient when conductance and inlet conditions are known but outlets are not. Neither method removes the need for appropriate heat-transfer coefficients or arrangement assumptions. Multipass and crossflow configurations require their own correction or effectiveness relation. Flow maldistribution can make ideal arrangement formulas optimistic.

### Formula handbook

Use heat rate $\dot Q$ in W, $c_p$ in J/(kg K), capacity rates $C$ in W/K, overall coefficient $U$ in W/(m2 K), and area in m2.

1. Adiabatic steady exchanger balance without shaft work:

$$
\dot Q=\dot m_h(h_{h,in}-h_{h,out})=\dot m_c(h_{c,out}-h_{c,in}).
$$

2. Constant-$c_p$ single-phase form:

$$
\dot Q=C_h(T_{h,in}-T_{h,out})=C_c(T_{c,out}-T_{c,in}),\qquad C=\dot m c_p.
$$

3. Plane-wall resistance on one common area basis:

$$
\frac1U=\frac1{h_h}+R_{f,h}''+\frac{\delta}{k_w}+R_{f,c}''+\frac1{h_c}.
$$

$R_f''$ is fouling resistance in m2 K/W. Tubular walls require the appropriate area ratios and logarithmic conduction resistance.

4. LMTD heat-transfer relation:

$$
\dot Q=UA F\Delta T_{lm},\qquad \Delta T_{lm}=\frac{\Delta T_1-\Delta T_2}{\ln(\Delta T_1/\Delta T_2)}.
$$

$F=1$ for ideal single-pass parallel or counterflow; correction factors depend on other arrangements.

5. Counterflow terminal differences:

$$
\Delta T_1=T_{h,in}-T_{c,out},\qquad \Delta T_2=T_{h,out}-T_{c,in}.
$$

6. Parallel-flow terminal differences:

$$
\Delta T_1=T_{h,in}-T_{c,in},\qquad \Delta T_2=T_{h,out}-T_{c,out}.
$$

7. Capacity ratio and transfer units:

$$
C_{min}=\min(C_h,C_c),\quad C_r=C_{min}/C_{max},\quad NTU=UA/C_{min}.
$$

8. Maximum theoretical duty and effectiveness:

$$
\dot Q_{max}=C_{min}(T_{h,in}-T_{c,in}),\qquad \varepsilon=\dot Q/\dot Q_{max}.
$$

9. Ideal counterflow effectiveness for $C_r\ne1$:

$$
\varepsilon=\frac{1-e^{-NTU(1-C_r)}}{1-C_r e^{-NTU(1-C_r)}}.
$$

10. Counterflow equal-capacity limit:

$$
\varepsilon=\frac{NTU}{1+NTU}\qquad(C_r=1).
$$

11. Parallel-flow effectiveness:

$$
\varepsilon=\frac{1-e^{-NTU(1+C_r)}}{1+C_r}.
$$

12. One stream at approximately constant phase-change temperature:

$$
C_r\to0,\qquad \varepsilon=1-e^{-NTU}.
$$

13. Approximate pumping requirement for an incompressible stream:

$$
P_{pump}=\Delta p\,Q_v/\eta_p.
$$

$Q_v$ is volume flow, distinguished from thermal duty. Extra thermal area or tighter channels can increase this cost.

### Derivation

Consider parallel flow with constant heat capacities. Over a small area $dA$, $d\dot Q=U\Delta T,dA$. The hot stream cools by $dT_h=-d\dot Q/C_h$, while the cold stream warms by $dT_c=d\dot Q/C_c$. Therefore

$$
d(\Delta T)=-d\dot Q\left(\frac1{C_h}+\frac1{C_c}\right).
$$

Combining the relations and integrating yields a logarithmic variation in the local temperature difference. Substituting the total stream energy balances produces $\dot Q=UA\Delta T_{lm}$. The logarithmic mean, not the arithmetic mean, captures the progressive change in thermal driving force. If the two terminal differences are equal, the limiting LMTD equals that common difference; the apparent zero divided by zero is a removable mathematical limit.

### Worked examples

#### Example 13-A: required counterflow area

A counterflow exchanger transfers 100 kW. Hot fluid cools from 120 to 80 degrees Celsius; cold fluid warms from 30 to 40 degrees Celsius. The supplied overall coefficient is 500 W/(m2 K). Terminal differences are 80 and 50 K. Thus $\Delta T_{lm}=(80-50)/\ln(80/50)=63.8293$ K and $A=100000/(500\times63.8293)=\mathbf{3.13336\ m^2}$. The implied heat-capacity rates are 2500 and 10,000 W/K, so both stream balances support the specified 100 kW duty.

#### Example 13-B: unknown outlet temperatures

An ideal counterflow exchanger has $C_h=1000$ W/K, $C_c=2000$ W/K and $UA=2000$ W/K. Inlets are 100 and 20 degrees Celsius. Here $C_r=0.5$ and $NTU=2$. Effectiveness is **0.774600**, and duty is $0.774600(1000)(80)=\mathbf{61.9680\ kW}$. Hot outlet is $100-61968/1000=\mathbf{38.0320\ ^\circ C}$; cold outlet is $20+61968/2000=\mathbf{50.9840\ ^\circ C}$. Crossing of outlet temperatures is permissible in counterflow because the two outlets are at different ends.

### Exercises

1. Water flows at 0.50 kg/s with supplied $c_p=4200$ J/(kg K) and warms by 15 K. Find duty and heat-capacity rate.
2. An exchanger has equal terminal temperature differences of 25 K, $U=400$ W/(m2 K) and area 2 m2. Find duty for $F=1$.
3. A counterflow exchanger has $C_r=1$ and $NTU=3$. Find effectiveness. What is the corresponding parallel-flow effectiveness?

### Solutions

1. Capacity rate is $0.50(4200)=2100$ W/K and duty is $2100(15)=31,500$ W.
2. The equal-difference limit gives $\Delta T_{lm}=25$ K. Duty is $400(2)(25)=20,000$ W.
3. Counterflow gives $3/(1+3)=0.75$. Parallel flow gives $(1-e^{-6})/2=0.49876$. Different arrangements produce materially different outlet limits.

### Common mistakes

Do not pair the two inlets when calculating a counterflow terminal difference. Check the units and area basis of $U$. A negative local driving temperature under an assumed passive arrangement signals inconsistent temperature specifications. Do not use single-phase capacity-rate equations for a condensing stream without considering latent heat and pressure variation. Logarithmic means require a proper limit calculation when their inputs nearly match.

### Applications and limits

These methods support initial sizing of water heaters, oil coolers, condensers and process recuperators. Final selection also considers allowable pressure drops, fouling, corrosion, thermal expansion, vibration, cleaning access and pressure containment. A thermal duty calculation does not establish pressure-vessel compliance. Vendor rating software should be checked against independent stream balances and the applicable arrangement limits.

### Further reading

- [MIT OCW: Intermediate Heat and Mass Transfer](https://ocw.mit.edu/courses/2-51-intermediate-heat-and-mass-transfer-fall-2008/) — background for conduction, convection and exchanger analysis.
- [US DOE: Improving Steam System Performance](https://www.energy.gov/sites/default/files/2014/05/f15/steamsourcebook.pdf) — full practical sourcebook including heat recovery and steam-system equipment; published edition is identified in the document.


---

## 15. Refrigeration and HVAC

### Learning map

Prerequisites: thermodynamics, heat exchangers, fluid flow and elementary mixture concepts. Learn the vapor-compression cycle, distinguish cooling capacity from power input, calculate basic moist-air properties and separate sensible from latent loads. This chapter gives engineering fundamentals, not a building-code or refrigerant-handling procedure.

### Theory

A refrigerator uses work to move heat from a colder region to a warmer region. A heat pump uses the same physical process but values the delivered warm-side heat. Their coefficients of performance differ because the useful outputs differ. A COP above one is consistent with energy conservation: work drives heat transfer rather than creating all the delivered heat.

The basic vapor-compression cycle has an evaporator, compressor, condenser and expansion device. The evaporator absorbs the cooling load. The compressor raises refrigerant pressure and enthalpy. The condenser rejects both the absorbed cooling load and compressor work. The expansion valve drops pressure with approximately constant enthalpy; it does not perform useful shaft work. Its irreversibility distinguishes it from an ideal expansion turbine.

Saturated, superheated and subcooled states must be distinguished using a property model for the actual refrigerant. Superheat at the compressor inlet and subcooling at the expansion inlet influence capacity and protection, but their effects depend on where heat is gained or removed. Pressure losses, compressor efficiency, heat leakage and fan power all affect measured system performance. A refrigerant cannot be chosen from COP alone; working pressure, environmental constraints, compatibility and applicable rules also matter.

HVAC treats both temperature and moisture. Dry-bulb temperature describes the ordinary measured air temperature. Relative humidity compares water-vapor partial pressure with saturation pressure at that temperature. Humidity ratio is water-vapor mass per mass of dry air. Heating a fixed moist-air sample can reduce relative humidity without removing any water. Dehumidification requires moisture removal, for example by condensation or adsorption.

Dew point is the temperature at which the existing vapor partial pressure reaches saturation during cooling at roughly constant total pressure and composition. A cooling coil below dew point can condense water, creating a latent load in addition to sensible cooling. Ventilation and infiltration add outdoor-air loads; occupants, equipment, solar radiation and envelope conduction contribute other loads. A steady load estimate is not automatically a peak-load sizing result.

### Formula handbook

Refrigerant enthalpies may be in kJ/kg when mass flow is kg/s and resulting powers are kW. State 1 is evaporator outlet/compressor inlet, 2 compressor outlet, 3 condenser outlet and 4 expansion-valve outlet.

1. Vapor-compression specific cooling and compressor work:

$$
q_L=h_1-h_4,\qquad w_c=h_2-h_1.
$$

2. Throttling approximation, negligible heat, work and kinetic changes:

$$
h_4=h_3.
$$

3. Condenser duty and cycle energy balance:

$$
q_H=h_2-h_3=q_L+w_c.
$$

4. Refrigeration and heat-pump COP:

$$
COP_R=\frac{q_L}{w_c},\qquad COP_{HP}=\frac{q_H}{w_c}=COP_R+1.
$$

The last equality applies to the same defined cycle boundary; external auxiliaries can change system-level comparisons.

5. Reversible two-reservoir limits, all temperatures in K:

$$
COP_{R,rev}=\frac{T_L}{T_H-T_L},\qquad COP_{HP,rev}=\frac{T_H}{T_H-T_L}.
$$

6. Cooling rate and compressor power:

$$
\dot Q_L=\dot m_rq_L,\qquad P_c=\dot m_rw_c.
$$

7. Relative humidity, under the ideal-mixture approximation:

$$
\varphi=\frac{p_v}{p_{ws}(T)},\qquad 0\leq\varphi\leq1
$$

for ordinary unsaturated or saturated equilibrium air. Supersaturation requires separate treatment.

8. Humidity ratio:

$$
w=0.62198\frac{p_v}{p-p_v}.
$$

Pressures use the same units; $w$ is kg water per kg dry air.

9. Approximate moist-air enthalpy, $T_C$ in degrees Celsius:

$$
h_{ma}=1.006T_C+w(2501+1.86T_C)\quad\mathrm{kJ/kg_{dry\ air}}.
$$

This common moderate-temperature approximation uses a stated conventional reference and does not describe all high-temperature or high-pressure humid gases.

10. Dew-point relation:

$$
p_{ws}(T_{dp})=p_v.
$$

11. Coil load and condensate rate, ignoring condensate sensible-enthalpy correction in the load estimate:

$$
\dot Q_{coil}\simeq\dot m_{da}(h_{in}-h_{out}),\qquad \dot m_{cond}=\dot m_{da}(w_{in}-w_{out}).
$$

12. Adiabatic two-stream mixing without condensation:

$$
w_m=\frac{\dot m_{da,1}w_1+\dot m_{da,2}w_2}{\dot m_{da,1}+\dot m_{da,2}},\qquad h_m=\frac{\dot m_{da,1}h_1+\dot m_{da,2}h_2}{\dot m_{da,1}+\dot m_{da,2}}.
$$

13. Sensible load and sensible heat ratio:

$$
\dot Q_s\simeq\dot m c_p\Delta T,\qquad SHR=\frac{\dot Q_s}{\dot Q_s+\dot Q_l}.
$$

Keep dry-air and total-mixture mass bases consistent with the selected heat capacity.

### Derivation

For an ideal mixture at common temperature and volume, partial pressure is proportional to mole count. Thus $n_v/n_{da}=p_v/(p-p_v)$. Mass ratio equals mole ratio times molecular-mass ratio, so

$$
\frac{m_v}{m_{da}}=\frac{M_v}{M_{da}}\frac{p_v}{p-p_v}\simeq0.62198\frac{p_v}{p-p_v}.
$$

This explains why humidity ratio is not simply relative humidity expressed as a percentage. Relative humidity also depends on saturation pressure, which changes strongly with temperature. If air is heated without adding or removing water at approximately fixed total pressure, $w$ remains essentially fixed while saturation pressure rises and relative humidity falls.

### Worked examples

#### Example 15-A: prescribed refrigeration-cycle states

A teaching cycle has supplied enthalpies $h_1=400$, $h_2=440$, $h_3=250$ and $h_4=250$ kJ/kg with refrigerant flow 0.050 kg/s. These values illustrate balances and are not claimed as a particular refrigerant's measured states. Cooling capacity is $0.050(400-250)=\mathbf{7.50\ kW}$; compressor power is $0.050(440-400)=\mathbf{2.00\ kW}$. Therefore $COP_R=\mathbf{3.75}$. Condenser rejection is **9.50 kW**, which equals cooling load plus compressor work.

#### Example 15-B: moist-air properties

Air at 25 degrees Celsius and total pressure 101,325 Pa has water-vapor partial pressure 1500 Pa. Humidity ratio is $0.62198(1500)/(101325-1500)=\mathbf{0.00934606\ kg/kg_{da}}$, or 9.346 g/kg dry air. Its approximate enthalpy is $1.006(25)+0.00934606[2501+1.86(25)]=\mathbf{48.9591\ kJ/kg_{da}}$. Relative humidity would require the saturation pressure at 25 degrees Celsius; it cannot be obtained by treating 0.009346 as a percentage.

### Exercises

1. A refrigerator provides 12 kW cooling while consuming 3 kW compressor power. Find COP and condenser heat rejection for the defined cycle boundary.
2. A cooling coil processes 0.80 kg dry air/s and reduces humidity ratio from 0.014 to 0.009. Find condensate rate in kg/s and kg/h.
3. Find the reversible refrigerator COP between 270 and 300 K. Explain why increasing the hot-side temperature at fixed cold-side temperature reduces the limit.

### Solutions

1. $COP_R=12/3=4$ and condenser rejection is $12+3=15$ kW.
2. Condensate is $0.80(0.014-0.009)=0.004$ kg/s, or 14.4 kg/h. Verify that the leaving state is consistent with the coil temperature and saturation relation.
3. $COP=270/(300-270)=9$. Increasing $T_H$ increases the required temperature lift and the denominator, so more work is required per unit cooling in the reversible limit.

### Common mistakes

Cooling capacity is not electrical consumption. Relative humidity is not water mass fraction. A fan can change local comfort and evaporation without removing water from the room. Use absolute pressures in mixture equations and Kelvin in COP limits. Air enthalpy in psychrometrics is commonly per kg of dry air; multiplying by total moist-air mass flow without conversion introduces inconsistency.

### Applications and limits

These balances support heat pumps, cold rooms, air-handling units and process dehumidification. Detailed design needs weather and occupancy profiles, coil performance, part-load control, defrost and auxiliary power. Refrigerant handling, ventilation, pressure equipment and electrical work require the applicable current standards and qualified practice. The examples provide thermal bookkeeping, not equipment selection or installation approval.

### Further reading

- [ASHRAE: Psychrometrics chapter](https://handbook.ashrae.org/Handbooks/F17/IP/f17_ch01/f17_ch01_ip.aspx) — openly viewable reference discussion; this linked edition uses I-P units and is not the latest-edition compliance source.
- [PsychroLib: official project overview](https://github.com/psychrometrics/psychrolib/blob/master/docs/overview.md) — implementation notes for moist-air properties in SI and I-P units.
- [NIST fluid properties](https://webbook.nist.gov/chemistry/fluid/) — properties for supported working fluids; match the actual refrigerant and reference convention.


---

## 16. Combustion and internal-combustion engines

### Learning map

Prerequisites: chemical mole balances, ideal-gas mixtures, thermodynamics and rotating power. Learn to balance complete combustion, define fuel-air quantities, distinguish indicated and brake performance, and interpret simple engine metrics. Ideal cycles are treated separately in the power-cycle chapter; here the focus is reacting flow and actual performance bookkeeping.

### Theory

Combustion converts chemical energy through reactions between fuel and oxidizer. Stoichiometric oxidizer is the amount required for a specified complete-reaction model. Actual combustion depends on mixing, chemical kinetics, heat loss and residence time. A balanced overall equation satisfies atomic conservation but does not predict flame stability, ignition delay or the detailed pollutant concentrations.

For a hydrocarbon burning completely with sufficient oxygen, carbon forms carbon dioxide and hydrogen forms water. Air adds nitrogen and other species. A simple dry-air model treats nitrogen as an inert diluent, although nitrogen chemistry becomes important for emissions at high temperatures. Rich mixtures lack sufficient oxygen for complete conversion, so products can include carbon monoxide, hydrogen and unburned hydrocarbons. Even nominally lean combustion can have locally rich regions.

Heating value depends on the state of the products. The higher heating value includes condensation of the formed water to the specified reference state; the lower heating value leaves this water as vapor. Comparing engine efficiencies based on different heating values without correction is misleading. Fuel composition and reference conditions must accompany a precise heating-value claim.

An engine converts cylinder pressure into piston force, crankshaft torque and shaft power. Indicated work is obtained from the cylinder pressure-volume loop. Brake power is measured at the shaft after mechanical and accessory losses within the chosen boundary. Friction power is the difference under a consistently defined test. Mean effective pressure is a cycle-work-per-displacement metric, not the actual peak cylinder pressure.

Four-stroke engines complete a working cycle in two crankshaft revolutions; two-stroke engines have one cycle per revolution in the ideal counting model. This affects power formulas and volumetric-efficiency calculations. Volumetric efficiency compares inducted fresh charge with a reference-density volume based on displacement; its value depends on reference conditions and charge definition. Boosted engines can exceed unity on some reference bases.

### Formula handbook

Use mass flow in kg/s, heating value in J/kg, torque in N m, angular speed in rad/s, displacement in m3 and power in W unless otherwise specified.

1. Complete hydrocarbon reaction with oxygen, per mole fuel:

$$
\mathrm{C_xH_y}+\left(x+\frac y4\right)\mathrm{O_2}\rightarrow x\mathrm{CO_2}+\frac y2\mathrm{H_2O}.
$$

For a simplified molar dry-air model, append approximately 3.76 mol of nitrogen for each mole of oxygen on both sides.

2. Stoichiometric air-fuel mass ratio using oxygen mass fraction $Y_{O_2,air}$:

$$
AFR_{st}=\frac{m_{O_2,st}/m_f}{Y_{O_2,air}}.
$$

3. Excess-air ratio and equivalence ratio:

$$
\lambda=\frac{AFR}{AFR_{st}},\qquad \phi=\frac1\lambda,\qquad \%\text{ excess air}=100(\lambda-1).
$$

4. Fuel energy input and brake thermal efficiency:

$$
\dot E_f=\dot m_f H_f,\qquad \eta_b=\frac{P_b}{\dot m_fH_f}.
$$

5. Torque-speed power relation:

$$
P_b=\tau\omega=\tau\frac{2\pi N}{60}.
$$

$N$ is in rpm. Name the shaft at which torque is measured.

6. Brake-specific fuel consumption, using $P_b$ in kW:

$$
BSFC=\frac{3600\dot m_f}{P_b}\quad\mathrm{kg/kWh}.
$$

7. Total displacement for $n_c$ cylinders of bore $B$ and stroke $S$:

$$
V_d=n_c\frac{\pi B^2S}{4}.
$$

8. Mean effective pressure:

$$
MEP=\frac{W_{cycle}}{V_d},\qquad BMEP=\frac{4\pi\tau}{V_d}\quad\text{for a four-stroke engine}.
$$

For the analogous two-stroke expression, replace $4\pi$ with $2\pi$.

9. Four-stroke volumetric efficiency using the selected fresh-air reference density:

$$
\eta_v=\frac{\dot m_a}{\rho_{ref}V_d(N/120)}.
$$

10. Mean piston speed:

$$
\overline V_p=2S\frac{N}{60}.
$$

11. Mechanical efficiency on a consistent boundary:

$$
\eta_m=P_b/P_i,\qquad P_f=P_i-P_b.
$$

12. Steady adiabatic reacting-flow energy balance with negligible work, speed and elevation changes:

$$
\sum_{reactants}n_i\left(\bar h_{f,i}^{\circ}+\Delta\bar h_i\right)=\sum_{products}n_j\left(\bar h_{f,j}^{\circ}+\Delta\bar h_j\right).
$$

$\bar h_f^\circ$ is molar standard formation enthalpy and $\Delta\bar h$ is sensible enthalpy from that reference. Do not add a fuel heating value a second time if formation enthalpies already account for reaction energy.

13. Approximate constant-product, constant-heat-capacity flame-temperature rise:

$$
T_{ad}-T_{in}\simeq\frac{Q_{release}}{\sum_j n_j\bar c_{p,j}}.
$$

This simplified estimate neglects dissociation, temperature-dependent heat capacity and unequal reactant inlet temperatures.

### Derivation

For a four-stroke engine, the number of cycles per second is $N/120$ when $N$ is rpm. Brake power equals brake work per cycle times this frequency: $P_b=W_bN/120$. Since $BMEP=W_b/V_d$, power is $BMEP\,V_dN/120$. Equate this with torque power $2\pi\tau N/60$ and cancel speed to obtain

$$
BMEP=4\pi\tau/V_d.
$$

The factor of two between four-stroke and two-stroke forms follows from cycle frequency, not from an arbitrary efficiency correction. BMEP enables size-normalized torque comparison but says nothing by itself about peak stress, combustion pressure history or durability.

### Worked examples

#### Example 16-A: methane air requirement

Use the simplified reaction $\mathrm{CH_4+2O_2\rightarrow CO_2+2H_2O}$ with teaching molecular masses 16 kg/kmol for methane and 32 kg/kmol for oxygen. One kilogram of fuel requires 4 kg oxygen. With supplied dry-air oxygen mass fraction 0.232, $AFR_{st}=4/0.232=\mathbf{17.2414\ kg\ air/kg\ fuel}$. At 20% excess air, actual ratio is $1.20(17.2414)=\mathbf{20.6897}$ and equivalence ratio is $1/1.2=0.8333$. More precise molar masses or air composition slightly change the result.

#### Example 16-B: measured shaft performance

An engine develops torque 120 N m at 3000 rpm while consuming 0.0030 kg/s fuel of supplied lower heating value 43 MJ/kg. Brake power is $120(2\pi)(3000)/60=\mathbf{37.6991\ kW}$. Fuel power is 129 kW, so lower-heating-value brake efficiency is **29.2241%**. Brake-specific fuel consumption is $3600(0.0030)/37.6991=\mathbf{0.286479\ kg/kWh}$, or 286.479 g/kWh. If displacement is 0.0020 m3 and the engine is four-stroke, BMEP is approximately 754 kPa.

### Exercises

1. Find mean piston speed for stroke 0.090 m at 3000 rpm.
2. Fuel flow is 0.010 kg/s with heating value 42 MJ/kg. Find fuel power and brake power at efficiency 0.30.
3. Actual air-fuel ratio is 25 and stoichiometric ratio is 17.2 on the same mass basis. Find excess-air ratio and equivalence ratio; classify the overall mixture.

### Solutions

1. $\overline V_p=2(0.090)(3000/60)=9.0$ m/s. This is a cycle average of absolute piston travel speed, not peak piston speed.
2. Fuel power is $0.010(42\times10^6)=420,000$ W. Brake output is $0.30(420)=126$ kW.
3. $\lambda=25/17.2=1.45349$ and $\phi=17.2/25=0.688$. The overall mixture is lean, with about 45.35% excess air under the stated model.

### Common mistakes

Mole ratio and mass ratio are not interchangeable. Heating value is energy per fuel mass, not per mixture mass unless explicitly converted. Indicated and brake efficiencies need different power measurements. Use radians per second in torque power. A complete global reaction does not establish zero pollutant emissions. An air-standard efficiency from the Otto cycle is not a measured engine brake efficiency.

### Applications and limits

Use these relations to interpret engine test data, boiler fuel balances and early combustion-system energy estimates. Detailed combustion requires species chemistry, transport and radiation models or measurements. Knocking, ignition, flameholding, exhaust aftertreatment and heat rejection are important topics beyond this compact chapter. Fuel-system hardware and engine testing involve pressure, hot surfaces, moving parts and exhaust hazards; these calculations are educational analysis, not operating instructions.

### Further reading

- [NASA Glenn: engine thermodynamic analysis](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/engine-thermodynamic-analysis/) — the ideal thermodynamic model behind a reciprocating engine.
- [NIST Chemistry WebBook](https://webbook.nist.gov/chemistry/) — species thermochemistry and supporting property references.
- [MIT OCW: Thermal Energy](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/) — course materials including thermochemistry and energy conversion.
