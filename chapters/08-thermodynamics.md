# 08. Thermodynamics

## Learning map

Prerequisites: SI units, algebra, integration and mechanical work. Learn to choose a system boundary, identify properties, apply energy and entropy balances, and distinguish an attainable process from a reversible limit. Continue to power cycles, refrigeration, combustion and heat transfer after this chapter. Thermodynamics answers how much energy a process needs and which direction it can proceed; heat transfer determines how quickly the thermal part occurs.

## Theory

A **closed system** contains a fixed mass. A **control volume** is a region through which mass may flow. An insulated tank, a compressor and a heat exchanger need different boundaries even when they contain the same substance. Choose the boundary before selecting an equation: otherwise shaft work can be counted twice or a mass-flow energy term omitted.

A property depends on the state, not the path used to reach it. Temperature, pressure, specific volume, internal energy, enthalpy and entropy are properties. Heat and work are transfers across a boundary and are not stored substances. A body stores energy, not heat. Equilibrium means no unresolved thermal, mechanical or chemical driving force remains within the chosen model. A quasi-equilibrium path can be represented by successive equilibrium states; it need not be reversible if friction remains.

An extensive property scales with system size; a specific property is per unit mass. Enthalpy combines internal energy and the pressure-volume contribution needed to move material into or out of a control volume. For an ideal gas, internal energy and enthalpy depend on temperature alone. This does not imply constant heat capacity. Constant $c_p$ and $c_v$ are additional approximations suitable only over an appropriate range.

For a pure substance in a two-phase liquid-vapor equilibrium region, pressure and temperature are linked by the saturation relation. Quality is vapor mass divided by total mass; it is meaningful only in that region. A temperature alone does not identify a superheated-vapor state. State tables require a sufficient pair of independent properties and a consistent reference convention.

The first law conserves energy. The second law constrains conversion: dissipating shaft work into thermal energy is easy, while converting heat from a single reservoir entirely into cyclic work is impossible. Entropy generation measures irreversibility; it does not measure an energy loss. Exergy measures useful-work potential relative to a specified environment. Mixing, throttling, friction and heat transfer across finite temperature differences destroy exergy while conserving energy.

## Formula handbook

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

## Derivation

Derive the ideal-gas isentropic temperature relation instead of memorizing its exponent. For a simple compressible ideal gas, $Tds=dh-vdp$. Substitute $dh=c_p,dT$ and $v=RT/p$, then divide by temperature:

$$
ds=c_p\frac{dT}{T}-R\frac{dp}{p}.
$$

For constant heat capacity and $ds=0$, integration gives $c_p\ln(T_2/T_1)=R\ln(p_2/p_1)$. Since $R/c_p=(\gamma-1)/\gamma$, exponentiation yields formula 9. Adiabatic alone is insufficient: an adiabatic real compressor produces entropy, so its temperature rise exceeds the isentropic rise for the same pressure ratio. For a throttling valve with negligible heat, shaft work and changes in speed or elevation, the first law instead gives $h_1=h_2$; throttling is not isentropic.

## Worked examples

### Example 08-A: heating air in a rigid tank

A rigid sealed tank contains 2.00 kg of air heated from 300 to 380 K. Use $c_v=718$ J/(kg K), neglect changes in speed and height, and assume no electrical or shaft work crosses the boundary. Rigidity makes boundary work zero. Therefore $Q=\Delta U=mc_v\Delta T=2(718)(80)=114,880$ J, or **114.88 kJ**. The final-to-initial pressure ratio is $380/300=1.267$ under the ideal-gas model. Using $c_p$ would incorrectly include flow work that this boundary does not have.

### Example 08-B: actual compressor power

Air enters an insulated compressor at 300 K and 100 kPa and leaves at 400 kPa. Let $\dot m=0.12$ kg/s, $c_p=1005$ J/(kg K), $\gamma=1.4$ and $\eta_c=0.80$. Neglect speed and elevation changes. First $T_{2s}=300(4)^{0.4/1.4}=445.798$ K. Then $T_2=300+(445.798-300)/0.80=482.248$ K. Shaft input is $\dot m c_p(T_2-T_1)=21,979.1$ W, or **21.979 kW**. The larger actual temperature rise is consistent with positive entropy generation. Motor electrical input would be larger still if motor efficiency were included.

## Exercises

1. A closed system receives 25 kJ of heat and performs 9 kJ of work. Its kinetic and potential energies remain fixed. Find its internal-energy change.
2. A hypothetical saturated mixture has $h_f=500$ and $h_g=2700$ kJ/kg. Find its enthalpy at quality 0.25. These are supplied exercise data, not a steam-table state.
3. A steady adiabatic turbine receives 0.5 kg/s with an actual enthalpy drop of 80 kJ/kg. Find shaft output and the isentropic drop when efficiency is 0.80.

## Solutions

1. $\Delta U=Q-W=25-9=16$ kJ. Positive means stored internal energy rises.
2. $h=500+0.25(2700-500)=1050$ kJ/kg. Quality weights phase mass, not phase volume.
3. $\dot W=0.5(80)=40$ kW. The isentropic drop is $80/0.80=100$ kJ/kg, larger than the actual useful drop.

## Common mistakes

Confusing absolute with gauge pressure corrupts gas laws. Mixing J/kg and kJ/kg causes factors of 1000 in power. Entropy can decrease within a system if sufficient entropy leaves with heat or mass; only generation must be nonnegative. A cyclic device has zero net change of every state property, not zero heat or work. Do not use quality for compressed liquid or superheated vapor.

## Applications and limits

Apply these balances to tanks, turbines, compressors, valves and thermal plants. Record assumptions before solving and test the sign and scale of the result afterwards. For real steam, refrigerants, high-pressure gases and wide temperature ranges, use a documented property model or tables. This chapter supplies the balance framework, not a substitute for a full property database or a design code.

## Further reading

- [MIT OCW: Thermal Energy](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/) — free course notes and problems for thermodynamic fundamentals and applications.
- [NIST Chemistry WebBook: fluid properties](https://webbook.nist.gov/chemistry/fluid/) — reference property data; select fluid, state, units and reference convention explicitly.
- [MIT OCW: Advanced Thermodynamics](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/pages/syllabus/) — a route into equilibrium and nonequilibrium theory after the fundamentals.
