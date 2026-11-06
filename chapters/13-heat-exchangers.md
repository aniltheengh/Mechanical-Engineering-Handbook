# 13. Heat exchangers

## Learning map

Prerequisites: thermodynamics, convection, conduction resistance and logarithms. Learn to close hot- and cold-side energy balances, use logarithmic mean temperature difference for known terminal temperatures, and use effectiveness-NTU when outlet temperatures are unknown. Treat thermal performance and pressure loss as coupled design questions.

## Theory

A recuperative heat exchanger transfers energy between streams separated by a wall. Double-pipe, shell-and-tube, plate and finned-tube designs differ in compactness, cleaning access, pressure capability and flow distribution. A regenerator stores heat temporarily in a matrix and transfers it to another stream at a later time; its analysis differs from a continuously separating wall.

For a well-insulated exchanger at steady state, heat lost by the hot stream equals heat gained by the cold stream. A mismatch in measured duties can reveal heat leakage, transient storage, inaccurate flow measurement or an inappropriate property estimate. Temperature changes alone do not determine duty: mass flow and heat capacity are also required. During phase change, use enthalpy change rather than forcing a constant-specific-heat expression through the two-phase region.

Parallel flow sends both streams in the same direction; counterflow sends them in opposite directions. Counterflow can maintain a more uniform temperature difference and can produce a cold outlet warmer than the hot outlet, because those outlets occur at opposite ends. A cold outlet cannot exceed the hot inlet in a passive two-stream exchanger under the usual assumptions. The temperature difference at every local contact must remain thermodynamically consistent.

The overall coefficient combines both convection resistances, the wall and fouling layers. Its numerical value depends on the chosen reference area. An inner-area coefficient and an outer-area coefficient for the same tube are not generally equal, although their products with their respective areas are. Fouling decreases conductance over time; adding area for fouling does not replace a cleaning and maintenance plan.

The LMTD method is convenient when inlet and outlet temperatures are known. Effectiveness-NTU is convenient when conductance and inlet conditions are known but outlets are not. Neither method removes the need for appropriate heat-transfer coefficients or arrangement assumptions. Multipass and crossflow configurations require their own correction or effectiveness relation. Flow maldistribution can make ideal arrangement formulas optimistic.

## Formula handbook

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

## Derivation

Consider parallel flow with constant heat capacities. Over a small area $dA$, $d\dot Q=U\Delta T,dA$. The hot stream cools by $dT_h=-d\dot Q/C_h$, while the cold stream warms by $dT_c=d\dot Q/C_c$. Therefore

$$
d(\Delta T)=-d\dot Q\left(\frac1{C_h}+\frac1{C_c}\right).
$$

Combining the relations and integrating yields a logarithmic variation in the local temperature difference. Substituting the total stream energy balances produces $\dot Q=UA\Delta T_{lm}$. The logarithmic mean, not the arithmetic mean, captures the progressive change in thermal driving force. If the two terminal differences are equal, the limiting LMTD equals that common difference; the apparent zero divided by zero is a removable mathematical limit.

## Worked examples

### Example 13-A: required counterflow area

A counterflow exchanger transfers 100 kW. Hot fluid cools from 120 to 80 degrees Celsius; cold fluid warms from 30 to 40 degrees Celsius. The supplied overall coefficient is 500 W/(m2 K). Terminal differences are 80 and 50 K. Thus $\Delta T_{lm}=(80-50)/\ln(80/50)=63.8293$ K and $A=100000/(500\times63.8293)=\mathbf{3.13336\ m^2}$. The implied heat-capacity rates are 2500 and 10,000 W/K, so both stream balances support the specified 100 kW duty.

### Example 13-B: unknown outlet temperatures

An ideal counterflow exchanger has $C_h=1000$ W/K, $C_c=2000$ W/K and $UA=2000$ W/K. Inlets are 100 and 20 degrees Celsius. Here $C_r=0.5$ and $NTU=2$. Effectiveness is **0.774600**, and duty is $0.774600(1000)(80)=\mathbf{61.9680\ kW}$. Hot outlet is $100-61968/1000=\mathbf{38.0320\ ^\circ C}$; cold outlet is $20+61968/2000=\mathbf{50.9840\ ^\circ C}$. Crossing of outlet temperatures is permissible in counterflow because the two outlets are at different ends.

## Exercises

1. Water flows at 0.50 kg/s with supplied $c_p=4200$ J/(kg K) and warms by 15 K. Find duty and heat-capacity rate.
2. An exchanger has equal terminal temperature differences of 25 K, $U=400$ W/(m2 K) and area 2 m2. Find duty for $F=1$.
3. A counterflow exchanger has $C_r=1$ and $NTU=3$. Find effectiveness. What is the corresponding parallel-flow effectiveness?

## Solutions

1. Capacity rate is $0.50(4200)=2100$ W/K and duty is $2100(15)=31,500$ W.
2. The equal-difference limit gives $\Delta T_{lm}=25$ K. Duty is $400(2)(25)=20,000$ W.
3. Counterflow gives $3/(1+3)=0.75$. Parallel flow gives $(1-e^{-6})/2=0.49876$. Different arrangements produce materially different outlet limits.

## Common mistakes

Do not pair the two inlets when calculating a counterflow terminal difference. Check the units and area basis of $U$. A negative local driving temperature under an assumed passive arrangement signals inconsistent temperature specifications. Do not use single-phase capacity-rate equations for a condensing stream without considering latent heat and pressure variation. Logarithmic means require a proper limit calculation when their inputs nearly match.

## Applications and limits

These methods support initial sizing of water heaters, oil coolers, condensers and process recuperators. Final selection also considers allowable pressure drops, fouling, corrosion, thermal expansion, vibration, cleaning access and pressure containment. A thermal duty calculation does not establish pressure-vessel compliance. Vendor rating software should be checked against independent stream balances and the applicable arrangement limits.

## Further reading

- [MIT OCW: Intermediate Heat and Mass Transfer](https://ocw.mit.edu/courses/2-51-intermediate-heat-and-mass-transfer-fall-2008/) — background for conduction, convection and exchanger analysis.
- [US DOE: Improving Steam System Performance](https://www.energy.gov/sites/default/files/2014/05/f15/steamsourcebook.pdf) — full practical sourcebook including heat recovery and steam-system equipment; published edition is identified in the document.
