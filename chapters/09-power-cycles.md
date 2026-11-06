# 09. Power cycles

## Learning map

Prerequisites: the first and second laws, enthalpy, entropy and ideal-gas processes. Learn to label state points, compute component work and heat, distinguish thermal efficiency from output, and compare ideal reference cycles. This chapter covers Carnot, Otto, Diesel, Brayton and Rankine cycles and introduces regeneration, reheat and combined cycles.

## Theory

A thermodynamic cycle returns its working fluid to its initial state. Because stored energy returns to its initial value, net work equals net heat over a complete cycle. A heat engine receives energy at a higher temperature, produces work and rejects energy at a lower temperature. Its thermal efficiency describes the fraction of input heat converted to net work; it does not specify the amount of power or the physical size of the machine.

The Carnot cycle consists of two reversible isotherms and two reversible adiabats. It supplies an upper limit for a heat engine operating between two reservoirs, not a practical layout. If heating and cooling occur over changing temperatures, the highest temperature and lowest temperature give a bound but do not determine the actual efficiency. A proposed cycle must also satisfy positive net work and physically attainable component states.

Air-standard models replace reacting fuel-air mixtures with a fixed mass of ideal gas. Heat addition replaces combustion; heat rejection restores the original state. Cold-air-standard calculations additionally use constant heat capacities. The Otto model uses constant-volume heat addition and rejection; the Diesel model adds heat at constant pressure. Their efficiency formulas compare idealized cycles, not complete real engines with intake, exhaust, friction, incomplete combustion and cooling losses.

The Brayton cycle models a compressor, constant-pressure heater, turbine and constant-pressure cooler. In an open gas turbine, fresh air and exhaust replace the closed-loop cooler conceptually. A significant part of turbine work drives the compressor. Increasing pressure ratio can improve ideal efficiency while reducing net work beyond an optimum set by turbine-inlet temperature. These two objectives should not be confused.

The Rankine cycle uses liquid pumping, heating and vaporization, vapor expansion, and condensation. Pumping liquid requires much less work than compressing vapor over the same pressure rise because liquid specific volume is small. Real steam turbines face wetness and material-temperature constraints. Reheat reduces some expansion wetness and can improve work output; feedwater regeneration improves the average temperature of heat addition but changes steam flow through different turbine sections.

## Formula handbook

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

## Derivation

For the ideal Brayton cycle, put $a=r_p^{(\gamma-1)/\gamma}$. The isentropic relations give $T_2=aT_1$ and $T_4=T_3/a$. Thus

$$
\frac{q_{out}}{q_{in}}=\frac{c_p(T_4-T_1)}{c_p(T_3-T_2)}=\frac{T_3/a-T_1}{T_3-aT_1}=\frac1a.
$$

This proves the efficiency formula under equal pressure ratios and constant heat capacity. For maximum work, differentiate $w_{net}/c_p=T_3-T_3/a-aT_1+T_1$ with respect to $a$. Setting $T_3/a^2-T_1=0$ gives $a=\sqrt{T_3/T_1}$. Increasing $a$ beyond this point still raises ideal efficiency but reduces specific output. Pressure losses and nonideal component efficiencies change both relations.

## Worked examples

### Example 09-A: Otto reference efficiency

An ideal cold-air-standard Otto cycle has compression ratio 8.0 and $\gamma=1.4$. Its efficiency is $1-8^{-0.4}=0.564725$, or **56.47%**. If heat input is 800 kJ/kg per cycle, net work is $0.564725(800)=451.780$ kJ/kg. This is an ideal thermodynamic benchmark; it is not a predicted brake efficiency for a road engine.

### Example 09-B: Brayton work and efficiency

An ideal Brayton cycle operates with $T_1=300$ K, $T_3=1200$ K, $r_p=6$, $c_p=1005$ J/(kg K), and $\gamma=1.4$. Compute $T_2=500.553$ K and $T_4=719.204$ K. Turbine work is **483.200 kJ/kg**; compressor work is **201.556 kJ/kg**. Net work is **281.644 kJ/kg**. Heat input is $1005(1200-500.553)=702.944$ kJ/kg, giving efficiency **40.066%**. Back-work ratio is approximately 0.417. At 2 kg/s, net power would be 563.287 kW before mechanical losses and auxiliaries.

## Exercises

1. Find the reversible heat-engine efficiency between reservoirs at 900 K and 300 K.
2. Use supplied hypothetical Rankine enthalpies $h_1=200$, $h_2=210$, $h_3=3200$, $h_4=2200$ kJ/kg. Find net work and efficiency.
3. A cycle takes 2 MW of heat and rejects 1.2 MW. Find net power and thermal efficiency. Would a 50 kW auxiliary load increase or decrease plant-net efficiency?

## Solutions

1. $1-300/900=0.6667$, or 66.67%. Actual operation between those reservoirs must not exceed this bound.
2. Turbine work is 1000 kJ/kg, pump work 10 kJ/kg and heat input 2990 kJ/kg. Net work is 990 kJ/kg and efficiency is $990/2990=33.11\%$. The supplied values teach bookkeeping and do not assert an actual steam state.
3. Net cycle output is 0.8 MW and efficiency is 40%. Subtracting auxiliaries gives 0.75 MW and plant-net efficiency 37.5% on the same heat-input basis.

## Common mistakes

Using Celsius in temperature ratios destroys the second-law bound. Ignoring compressor work greatly overestimates gas-turbine output. Comparing cycles at different peak temperatures, heat inputs or pressure limits without saying so gives misleading rankings. A steam quality calculated outside zero to one signals an incorrect region or assumed state. Boiler efficiency, cycle efficiency and overall fuel-to-electricity efficiency are different quantities.

## Applications and limits

Use cycle models for architecture comparisons and first estimates, then introduce pressure drops, variable heat capacities, measured component maps, cooling flows and real-fluid properties. Combined cycles recover gas-turbine exhaust heat in a steam bottoming cycle. A regenerator is useful only when the exhaust can heat the compressed stream across a feasible temperature difference. Economic, maintenance and emission constraints often determine the final design more strongly than ideal efficiency alone.

## Further reading

- [NASA Glenn: Brayton cycle](https://www.grc.nasa.gov/www/k-12/BGP/brayton.html) — introductory gas-turbine thermodynamic cycle explanation.
- [NASA Glenn: engine thermodynamic analysis](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/engine-thermodynamic-analysis/) — an ideal Otto-cycle development.
- [US Department of Energy: steam systems](https://www.energy.gov/cmei/ito/steam-systems) — practical steam-system publications and links; consult current project requirements separately.
