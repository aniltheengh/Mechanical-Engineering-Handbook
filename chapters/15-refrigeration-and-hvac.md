# 15. Refrigeration and HVAC

## Learning map

Prerequisites: thermodynamics, heat exchangers, fluid flow and elementary mixture concepts. Learn the vapor-compression cycle, distinguish cooling capacity from power input, calculate basic moist-air properties and separate sensible from latent loads. This chapter gives engineering fundamentals, not a building-code or refrigerant-handling procedure.

## Theory

A refrigerator uses work to move heat from a colder region to a warmer region. A heat pump uses the same physical process but values the delivered warm-side heat. Their coefficients of performance differ because the useful outputs differ. A COP above one is consistent with energy conservation: work drives heat transfer rather than creating all the delivered heat.

The basic vapor-compression cycle has an evaporator, compressor, condenser and expansion device. The evaporator absorbs the cooling load. The compressor raises refrigerant pressure and enthalpy. The condenser rejects both the absorbed cooling load and compressor work. The expansion valve drops pressure with approximately constant enthalpy; it does not perform useful shaft work. Its irreversibility distinguishes it from an ideal expansion turbine.

Saturated, superheated and subcooled states must be distinguished using a property model for the actual refrigerant. Superheat at the compressor inlet and subcooling at the expansion inlet influence capacity and protection, but their effects depend on where heat is gained or removed. Pressure losses, compressor efficiency, heat leakage and fan power all affect measured system performance. A refrigerant cannot be chosen from COP alone; working pressure, environmental constraints, compatibility and applicable rules also matter.

HVAC treats both temperature and moisture. Dry-bulb temperature describes the ordinary measured air temperature. Relative humidity compares water-vapor partial pressure with saturation pressure at that temperature. Humidity ratio is water-vapor mass per mass of dry air. Heating a fixed moist-air sample can reduce relative humidity without removing any water. Dehumidification requires moisture removal, for example by condensation or adsorption.

Dew point is the temperature at which the existing vapor partial pressure reaches saturation during cooling at roughly constant total pressure and composition. A cooling coil below dew point can condense water, creating a latent load in addition to sensible cooling. Ventilation and infiltration add outdoor-air loads; occupants, equipment, solar radiation and envelope conduction contribute other loads. A steady load estimate is not automatically a peak-load sizing result.

## Formula handbook

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

## Derivation

For an ideal mixture at common temperature and volume, partial pressure is proportional to mole count. Thus $n_v/n_{da}=p_v/(p-p_v)$. Mass ratio equals mole ratio times molecular-mass ratio, so

$$
\frac{m_v}{m_{da}}=\frac{M_v}{M_{da}}\frac{p_v}{p-p_v}\simeq0.62198\frac{p_v}{p-p_v}.
$$

This explains why humidity ratio is not simply relative humidity expressed as a percentage. Relative humidity also depends on saturation pressure, which changes strongly with temperature. If air is heated without adding or removing water at approximately fixed total pressure, $w$ remains essentially fixed while saturation pressure rises and relative humidity falls.

## Worked examples

### Example 15-A: prescribed refrigeration-cycle states

A teaching cycle has supplied enthalpies $h_1=400$, $h_2=440$, $h_3=250$ and $h_4=250$ kJ/kg with refrigerant flow 0.050 kg/s. These values illustrate balances and are not claimed as a particular refrigerant's measured states. Cooling capacity is $0.050(400-250)=\mathbf{7.50\ kW}$; compressor power is $0.050(440-400)=\mathbf{2.00\ kW}$. Therefore $COP_R=\mathbf{3.75}$. Condenser rejection is **9.50 kW**, which equals cooling load plus compressor work.

### Example 15-B: moist-air properties

Air at 25 degrees Celsius and total pressure 101,325 Pa has water-vapor partial pressure 1500 Pa. Humidity ratio is $0.62198(1500)/(101325-1500)=\mathbf{0.00934606\ kg/kg_{da}}$, or 9.346 g/kg dry air. Its approximate enthalpy is $1.006(25)+0.00934606[2501+1.86(25)]=\mathbf{48.9591\ kJ/kg_{da}}$. Relative humidity would require the saturation pressure at 25 degrees Celsius; it cannot be obtained by treating 0.009346 as a percentage.

## Exercises

1. A refrigerator provides 12 kW cooling while consuming 3 kW compressor power. Find COP and condenser heat rejection for the defined cycle boundary.
2. A cooling coil processes 0.80 kg dry air/s and reduces humidity ratio from 0.014 to 0.009. Find condensate rate in kg/s and kg/h.
3. Find the reversible refrigerator COP between 270 and 300 K. Explain why increasing the hot-side temperature at fixed cold-side temperature reduces the limit.

## Solutions

1. $COP_R=12/3=4$ and condenser rejection is $12+3=15$ kW.
2. Condensate is $0.80(0.014-0.009)=0.004$ kg/s, or 14.4 kg/h. Verify that the leaving state is consistent with the coil temperature and saturation relation.
3. $COP=270/(300-270)=9$. Increasing $T_H$ increases the required temperature lift and the denominator, so more work is required per unit cooling in the reversible limit.

## Common mistakes

Cooling capacity is not electrical consumption. Relative humidity is not water mass fraction. A fan can change local comfort and evaporation without removing water from the room. Use absolute pressures in mixture equations and Kelvin in COP limits. Air enthalpy in psychrometrics is commonly per kg of dry air; multiplying by total moist-air mass flow without conversion introduces inconsistency.

## Applications and limits

These balances support heat pumps, cold rooms, air-handling units and process dehumidification. Detailed design needs weather and occupancy profiles, coil performance, part-load control, defrost and auxiliary power. Refrigerant handling, ventilation, pressure equipment and electrical work require the applicable current standards and qualified practice. The examples provide thermal bookkeeping, not equipment selection or installation approval.

## Further reading

- [ASHRAE: Psychrometrics chapter](https://handbook.ashrae.org/Handbooks/F17/IP/f17_ch01/f17_ch01_ip.aspx) — openly viewable reference discussion; this linked edition uses I-P units and is not the latest-edition compliance source.
- [PsychroLib: official project overview](https://github.com/psychrometrics/psychrolib/blob/master/docs/overview.md) — implementation notes for moist-air properties in SI and I-P units.
- [NIST fluid properties](https://webbook.nist.gov/chemistry/fluid/) — properties for supported working fluids; match the actual refrigerant and reference convention.
