# 12. Heat transfer

## Learning map

Prerequisites: energy balances, differential equations and basic fluid mechanics. Learn to identify conduction, convection and radiation paths, build thermal-resistance models, distinguish steady from transient behavior, and choose an appropriate length scale. Heat transfer converts a required heating or cooling duty into an area, temperature difference or time.

## Theory

Conduction transports energy through microscopic interactions within material. In a stationary solid, its rate is related to the temperature gradient and thermal conductivity. A high conductivity does not mean a body must be hot; it means a given gradient can support a larger heat flux. For anisotropic materials such as composites, conductivity can depend on direction and must be represented by a tensor when the direction matters.

Convection combines transport near a surface with fluid motion. The heat-transfer coefficient is a useful boundary relation, not an intrinsic material property like density. It depends on flow, geometry, fluid properties and thermal conditions. Forced convection uses externally driven flow; natural convection arises from buoyancy induced by density differences. A correlation is valid only for the stated geometry, boundary condition and dimensionless parameter ranges.

Thermal radiation is electromagnetic energy exchange. Every surface above absolute zero emits radiation, while net exchange also depends on what it sees and absorbs. Surface emissivity can vary with wavelength, temperature and finish. The simple gray-body-to-large-surroundings formula assumes a particular radiative environment. Two finite surfaces require view factors and, when reflections matter, a radiation-network treatment.

Steady state means no energy accumulation; it does not mean temperature is uniform. A plane wall can have a permanent temperature gradient carrying a constant heat rate. Resistances in series carry the same steady heat rate, while parallel paths share the same endpoint temperature difference. Thermal bridges and contact gaps can dominate a nominally well-insulated construction.

Transient problems also include storage. A lumped-capacitance model assumes the body is nearly uniform in temperature at every instant. Small size or high conductivity helps make this plausible. When internal gradients matter, solve the transient conduction equation or use appropriate analytical series solutions. A large external heat-transfer coefficient accelerates surface response but may make the lumped assumption worse.

## Formula handbook

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

## Derivation

For a lumped body with no internal heat generation and negligible radiation, energy conservation gives $mc_p,dT/dt=-hA_s(T-T_\infty)$. Divide by $(T-T_\infty)$ and integrate from $T_i$ at time zero:

$$
\ln\left(\frac{T-T_\infty}{T_i-T_\infty}\right)=-\frac{hA_s}{mc_p}t.
$$

Exponentiation gives the cooling law. The ratio tends to one at zero time and to zero as time tends to infinity, which are useful boundary checks. A common preliminary criterion is $Bi<0.1$, but its adequacy depends on required accuracy and the actual geometry. Adding radiation makes the governing equation nonlinear unless an appropriate linearized coefficient is justified.

## Worked examples

### Example 12-A: heat loss through a wall

A 10 m2 wall has thickness 0.15 m and conductivity 0.80 W/(m K). Indoor and outdoor air are 50 and 20 degrees Celsius. Convection coefficients are 8 and 20 W/(m2 K). Ignore radiation and thermal bridges. The total resistance is $1/(8\times10)+0.15/(0.8\times10)+1/(20\times10)=0.03625$ K/W. Heat loss is $30/0.03625=\mathbf{827.586\ W}$. Using only wall conduction would predict 1600 W and omit the finite surface temperature drops.

### Example 12-B: a small metal part cooling

A 0.020 kg part has $c_p=500$ J/(kg K), exposed area 0.010 m2 and $h=20$ W/(m2 K). Its initial temperature is 70 degrees Celsius and ambient is 20 degrees Celsius. With supplied conductivity 15 W/(m K) and density 7800 kg/m3, $L_c=(m/\rho)/A_s=0.0002564$ m and $Bi=0.000342$, supporting the lumped approximation. Time constant is **50.0 s**. After 300 s, $T=20+50e^{-6}=\mathbf{20.12394\ ^\circ C}$. This is a convection-only model with constant properties, not a measured cooldown curve.

## Exercises

1. A 0.010 m thick plate of area 0.50 m2 and conductivity 20 W/(m K) has a 30 K temperature difference. Find its steady conductive heat rate.
2. A body has $mc_p=200$ J/K and $hA=5$ W/K. How long does its excess temperature take to fall to 10% of its initial value?
3. A body has $h=100$ W/(m2 K), $L_c=0.020$ m and $k=0.20$ W/(m K). Calculate Biot number and assess a lumped model.

## Solutions

1. $\dot Q=kA\Delta T/L=20(0.5)(30)/0.01=30,000$ W. The temperature gradient is large because the plate is thin.
2. $\tau=200/5=40$ s. Solve $0.1=e^{-t/40}$ to obtain $t=40\ln10=92.10$ s.
3. $Bi=100(0.020)/0.20=10$. Internal gradients are likely important; a uniform-temperature assumption is not justified by the usual criterion.

## Common mistakes

Use Kelvin for fourth-power radiation terms. Distinguish heat rate from heat flux and conductivity from convection coefficient. Do not add parallel-path resistances as though they were in series. Use the area appropriate to each cylindrical surface. A convection correlation using fluid conductivity cannot accept solid conductivity. A thermal time constant is not the time to reach ambient exactly; ideal exponential cooling approaches ambient asymptotically.

## Applications and limits

Applications include insulation, electronics cooling, furnaces, casting, heat treatment and biological temperature control. First check energy balance and resistance dominance; then refine the part that controls uncertainty. Contact resistance, fouling, boiling, condensation and temperature-dependent properties may dominate simple conduction estimates. Finite-element thermal analysis still needs realistic boundary conditions and an energy-balance check.

## Further reading

- [MIT OCW: Intermediate Heat and Mass Transfer](https://ocw.mit.edu/courses/2-51-intermediate-heat-and-mass-transfer-fall-2008/) — advanced undergraduate course materials.
- [Lienhard and Lienhard: A Heat Transfer Textbook, sixth edition](https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/6/1810/files/2024/04/AHTTv600.pdf) — author-distributed full textbook PDF; consult its own license before redistribution.
