# 44. Process Plant Engineering

## Learning map

Prerequisites: thermodynamics, fluid mechanics, heat transfer, instrumentation, and elementary differential equations. This chapter connects a process requirement to balances, drawings, equipment interfaces, controls, and an operating record. Follow a water-blending system from its stream table into a tank model and utility requirement. The aim is to understand what the plant must do and how its documents express that intent. Pressure design, relief sizing, hazardous-area classification, and construction-code compliance require separate work beyond these introductory models.

## Theory

A process basis states the required service and its conditions. Define capacity, product quality, feed composition and variability, utility availability, operating schedule, and the boundary between the project and existing facilities. Separate normal operation from startup, shutdown, cleaning, standby, and credible disturbances. A nominal flow alone cannot establish tank volume, pumping duty, heater capacity, or control behavior. Identify what is measured, specified, assumed, and still unknown before selecting equipment.

Process documents describe different aspects of the same system. A process flow diagram, or PFD, communicates major equipment and material and energy streams, normally supported by stream data. A piping and instrumentation diagram, or P&ID, describes functional equipment, piping, valves, instrumentation, and their connections using the project's conventions. A physical layout establishes space, elevation, access, routing, and interfaces. A P&ID is not a scale drawing, and a convincing 3D arrangement does not prove that its process or control logic works. [Northwestern's PFD teaching page](https://processdesign.mccormick.northwestern.edu/index.php/Process_flow_diagram) explains process-stream information; the [archived DOE drawing handbook](https://www.energy.gov/ehss/articles/doe-hdbk-10162-93) provides historical training in drawings and symbols rather than a current mandatory project standard.

Balances need a declared control volume and basis. Total mass is conserved for ordinary nonnuclear processes. Individual species may be generated or consumed by reaction, whereas an inert tracer is conserved if it neither reacts, adsorbs, evaporates, nor separates. Steady operation means the chosen inventories no longer change with time; it does not mean there is no material flowing. Recycles can create large internal flows while leaving the overall plant balance unchanged. Count only streams crossing the selected boundary.

Energy balances use a consistent enthalpy reference and include relevant heat and work. Temperature averaging is valid only for the stated property and mixing assumptions. Phase changes, chemical reactions, heat of mixing, heat loss, or appreciably different heat capacities can defeat a simple arithmetic average. For two streams of the same dilute liquid with constant equal heat capacity, the adiabatic outlet temperature is mass-flow weighted. The [University of Michigan energy-balance material](https://public.websites.umich.edu/~elements/7e/11chap/summary.html) develops the broader open-system balance.

Tank residence and mixing describe different behavior. Nominal hydraulic residence time is working liquid volume divided by throughput. Mixing time describes how rapidly spatial concentration differences are reduced. The ideal stirred-tank model assumes the outlet concentration equals the uniform tank concentration immediately; it does not calculate impeller performance. Real short circuits, dead regions, density stratification, or poor inlet placement can invalidate that assumption. [MIT's residence-time lecture](https://ocw.mit.edu/courses/10-37-chemical-and-biological-reaction-engineering-spring-2007/resources/lec10_03092007_w/) discusses nonideal mixing and tracer interpretation.

Piping and utilities are coupled to equipment. Flow through a branch depends on pressure boundaries, elevation, resistance, valve position, and the connected machine characteristic. A cooling-water flow requirement also needs inlet temperature, return conditions, available differential pressure, and water quality. Instrument air needs more than a pressure number: consumption, cleanliness, availability, and loss-of-air behavior affect actuators. State electrical loads and operating combinations before treating installed motor ratings as coincident plant demand.

Control design assigns each measured variable, manipulated variable, operating target, and limit. Level control may adjust an outlet while inlet ratio control maintains composition. Temperature control may adjust a utility valve, but saturation, transport delay, and sensor placement constrain the response. A transmitter tag does not specify its calibration range or an interlock's full logic. Record sequences and cause-and-effect behavior separately, including startup permissives, abnormal signals, manual modes, and restoration after interruption.

Maintainability belongs in the design basis. Operators need access to instruments and valves, removal paths for equipment, and means to drain, vent, clean, inspect, and isolate the relevant sections under approved procedures. A replaceable pump is not maintainable if its motor cannot be removed through the surrounding pipework. Equipment, line, instrument, and document identifiers should remain consistent across calculations, P&IDs, layout, specifications, and revision records. Changes to one interface can require changes to several documents.

## Formula handbook

Use inventory $M$ in kg, mass flow $\dot m$ in kg/s, volumetric flow $Q_v$ in $\mathrm{m^3/s}$, volume $V$ in $\mathrm{m^3}$, concentration $C$ in $\mathrm{kg/m^3}$, and time $t$ in s. Heat rate $\dot Q_h$ and shaft work rate $\dot W_s$ are in W; $\dot Q_h>0$ enters the system and $\dot W_s>0$ leaves as shaft work.

**1. Total mass inventory:**

$$
\frac{dM}{dt}=\sum_{in}\dot m_i-\sum_{out}\dot m_j.
$$

**2. Species inventory with mass fraction $w_k$:**

$$
\frac{d(Mw_k)}{dt}=\sum_{in}\dot m_iw_{k,i}-\sum_{out}\dot m_jw_{k,j}+\dot m_{k,gen}.
$$

$\dot m_{k,gen}$ is net generation in kg/s; it is zero for the conservative tracer used below.

**3. Steady open-system energy balance:**

$$
0=\dot Q_h-\dot W_s+\sum_{in}\dot m_i\left(h_i+\frac{u_i^2}{2}+gz_i\right)-\sum_{out}\dot m_j\left(h_j+\frac{u_j^2}{2}+gz_j\right).
$$

Specific enthalpy $h$ is J/kg, velocity $u$ m/s, and elevation $z$ m. Enthalpies must use one consistent reference and include required phase or reaction effects.

**4. Steady, nonreactive, adiabatic mixing with one outlet and constant equal $c_p$:**

$$
\dot m_o=\sum_i\dot m_i,\qquad T_o=\frac{\sum_i\dot m_iT_i}{\dot m_o}.
$$

Neglect kinetic, potential, and shaft-work effects and heat of mixing. A common Celsius reference is valid here because the common offset cancels through mass conservation.

**5. Conservative mass-fraction blending:**

$$
w_o=\frac{\sum_i\dot m_iw_i}{\dot m_o}.
$$

Do not substitute volume fractions without a density and mixing-volume model.

**6. Constant-density tank level, vertical constant area $A_T$:**

$$
A_T\frac{d\ell}{dt}=\sum Q_{v,in}-\sum Q_{v,out}.
$$

Level $\ell$ is m; variable-area vessels require $dV/d\ell$ instead of constant $A_T$.

**7. Nominal hydraulic residence time:**

$$
\tau=V/Q_v.
$$

Use working liquid volume and actual throughput. This is not a universal minimum contact time or impeller mixing time.

**8. Ideal constant-volume, constant-flow stirred tank with conservative solute:**

$$
V\frac{dC}{dt}=Q_v(C_{in}-C),\qquad C_{out}=C.
$$

**9. Constant inlet after a step, initial concentration $C_0$:**

$$
C(t)=C_{in}+(C_0-C_{in})e^{-t/\tau}.
$$

**10. Time to complete fraction $f$ of the initial-to-final change:**

$$
t_f=-\tau\ln(1-f),\qquad0<f<1.
$$

**11. Ideal stirred-tank residence-time probability density:**

$$
E(t)=\frac1\tau e^{-t/\tau},\qquad \int_0^\infty E(t)dt=1,\qquad \int_0^\infty tE(t)dt=\tau.
$$

$E(t)$ has units $\mathrm{s^{-1}}$. Individual fluid elements have different residence times.

**12. Pipe section and steady junction continuity:**

$$
u=\frac{4Q_v}{\pi D^2},\qquad \sum Q_{v,in}=\sum Q_{v,out}.
$$

The volumetric junction form assumes equal constant density. Head losses and pump characteristics must also be satisfied; continuity alone cannot determine every branch flow.

**13. Single-phase utility duty with constant heat capacity:**

$$
|\dot Q_h|=\dot m_u c_{p,u}|T_{u,out}-T_{u,in}|.
$$

$c_{p,u}$ is J/(kg K). Available temperature approach and exchanger conductance impose additional constraints.

**14. Ideal linear 4–20 mA scaling:**

$$
I_{\rm mA}=4+16\frac{x-x_L}{x_U-x_L}.
$$

$x_L,x_U$ are configured engineering-unit range limits. This mapping describes valid measurement span; out-of-range and fault behavior depend on the device and configuration.

## Derivation

Take a tank filled to constant working volume with a liquid whose density is effectively constant. Equal inlet and outlet volume flow preserves that volume. For a conservative solute, accumulation is $d(VC)/dt$, entering mass rate is $Q_vC_{in}$, and leaving rate is $Q_vC$ because ideal mixing makes outlet and bulk concentrations equal. Constant $V$ gives the differential equation above.

For constant inlet concentration, set $y=C-C_{in}$. The balance becomes $dy/dt=-y/\tau$. Integrating with $y(0)=C_0-C_{in}$ gives the exponential response. The initial value and long-time limit are recovered directly. With a clean initial tank and a step to $C_{in}$, cumulative solute discharged by time $t$ is

$$
m_{out}(t)=Q_vC_{in}\left[t-\tau(1-e^{-t/\tau})\right].
$$

Meanwhile inventory is $VC_{in}(1-e^{-t/\tau})$. Adding them gives $Q_vC_{in}t$, exactly the cumulative input. This integral balance checks the dynamic solution independently of a plotted curve. It also explains why one residence time does not replace all original liquid: the ideal step response has reached only $1-e^{-1}$ of its final change.

## Worked examples

### Example 1: water blending and downstream heating

Mix two dilute aqueous streams steadily. Stream 1 supplies 1.50 kg/s at 20°C with conservative tracer mass fraction 0.00100; stream 2 supplies 0.500 kg/s at 80°C with tracer fraction 0.00400. Assume identical constant $c_p=4180\ \mathrm{J/(kg\,K)}$, negligible heat of mixing, adiabatic blending, no phase change, and negligible work, speed, and elevation effects.

Total outlet flow is **2.00 kg/s**. The outlet temperature is $[1.5(20)+0.5(80)]/2=\mathbf{35.0^\circ C}$. Tracer flow is $1.5(0.001)+0.5(0.004)=0.00350$ kg/s; dividing by total flow gives **0.001750 kg/kg**, or **1750 mg/kg**. A consistent 0°C sensible-enthalpy reference gives inlet energy rates 125.4 and 167.2 kW, totaling **292.6 kW**, equal to $2(4180)(35)$ W at the outlet.

A separate downstream heater raising this blend to 60°C needs $2(4180)(60-35)=\mathbf{209.0\ kW}$ delivered to the liquid. This is thermal duty, not electrical or fuel input without the heater efficiency and losses. Changing the boundary to include the heater adds that energy stream to the balance.

### Example 2: a tracer step through a stirred tank

An ideal tank contains 1.20 m³ of initially tracer-free water. Constant inlet and outlet flows are 0.00200 m³/s. At $t=0$, inlet tracer concentration steps to 0.100 kg/m³, equivalent to 100 mg/L. Assume conservative solute, instant uniform mixing, constant volume, and no measurement delay.

Residence time is $\tau=1.20/0.00200=\mathbf{600\ s}$. After 600 s, outlet concentration is $0.100(1-e^{-1})=0.0632121\ \mathrm{kg/m^3}$, or **63.2121 mg/L**. Reaching 95% of the final change takes $-600\ln(0.05)=\mathbf{1797.44\ s}$, or **29.9573 min**.

By 600 s, input tracer mass is **0.120000 kg**. Tank inventory is $1.20(0.0632120559)=\mathbf{0.0758545\ kg}$, and integrated discharge is **0.0441455 kg**. Their sum closes the mass balance. These results characterize this ideal flow model; they do not prove real tank mixing, disinfection contact time, or sensor response.

## Exercises

1. Adiabatically blend 0.800 kg/s of water at 15°C with 1.20 kg/s at 65°C. With equal constant $c_p=4180\ \mathrm{J/(kg\,K)}$, find blend temperature and additional heat needed to reach 55°C.
2. A 2.00 m³ ideal stirred tank initially has tracer concentration 0.200 kg/m³. Clean water enters at 0.00500 m³/s with equal outflow. Find the time for concentration to fall to 10% of its initial value and tracer mass then remaining.
3. Cooling water removes 84.0 kW while warming by 8.00 K. Use $c_p=4200\ \mathrm{J/(kg\,K)}$ and density 1000 kg/m³. Find mass flow, volume flow, speed in a 50.0 mm internal-diameter pipe, and ideal transmitter output for a linear range of 0–5.00 L/s mapped to 4–20 mA.

## Solutions

1. Temperature is $[0.8(15)+1.2(65)]/2=\mathbf{45.0^\circ C}$. Heating duty is $2(4180)(55-45)=\mathbf{83.60\ kW}$. A simple average of inlet temperatures would be wrong because their mass flows differ.
2. Here $\tau=400$ s and $C/C_0=e^{-t/400}$. Thus $t=400\ln10=\mathbf{921.034\ s}$, or **15.3506 min**. Remaining concentration is 0.0200 kg/m³ and inventory is **0.0400 kg**. The discharged tracer accounts for the other 0.360 kg of initial inventory.
3. Mass flow is $84000/(4200\times8)=\mathbf{2.50\ kg/s}$ and volume flow **0.00250 m³/s**, or 2.50 L/s. Pipe speed is $4(0.00250)/(\pi0.05^2)=\mathbf{1.27324\ m/s}$. Half-span flow gives **12.0 mA**. Utility pressure, exchanger temperature approach, and instrumentation accuracy remain separate checks.

## Common mistakes

Confusing working volume with total tank capacity, residence time with mixing time, or mass fraction with mg/L changes the model. Do not equate a pressure transmitter range with allowable equipment pressure. A control valve's nominal diameter does not establish its installed flow characteristic. Flow arrows on a P&ID describe intended function; actual reverse-flow possibilities require analysis. Keep assumed steady balances separate from transient filling, draining, and startup behavior.

## Applications and limits

For a small water-treatment skid, prepare a process basis, stream table, balances, PFD, P&ID, equipment and line lists, utility schedule, instrument ranges, control narrative, layout, and verification record. Cross-check tag numbers and revisions before release. Compare measured flow, temperature, inventory, and response with predictions and measurement uncertainty. Record deviations and resolve their causes. The [integrated pumping capstone](../CAPSTONE.md) extends the interface discussion. These models neither select construction materials and pressure ratings nor replace qualified review, commissioning, or a documented operational procedure.

## Further reading

- [Northwestern process-design teaching — Process flow diagram](https://processdesign.mccormick.northwestern.edu/index.php/Process_flow_diagram): stream and equipment information on PFDs.
- [U.S. DOE — Engineering Symbology, Prints, and Drawings](https://www.energy.gov/ehss/articles/doe-hdbk-10162-93): archived training handbook and drawing interpretation; not a current mandatory design code.
- [University of Michigan — Steady-state energy balance](https://public.websites.umich.edu/~elements/7e/11chap/summary.html): open-system energy-balance development, including reactive extensions beyond this chapter.
- [MIT OpenCourseWare — Nonideal reactor mixing patterns](https://ocw.mit.edu/courses/10-37-chemical-and-biological-reaction-engineering-spring-2007/resources/lec10_03092007_w/): residence-time distributions and alternatives to ideal mixing. Primary-source links checked 2026-11-07.
