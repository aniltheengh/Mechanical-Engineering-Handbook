# 38. Compressible flow

## Learning map

Prerequisites: [thermodynamics](08-thermodynamics.md), [fluid mechanics](10-fluid-mechanics.md), differential calculus and absolute-pressure measurement. Learn to distinguish static from stagnation conditions, connect Mach number with density change, calculate ideal nozzle flow, and treat a shock as an irreversible discontinuity. The central question is how a gas changes its density while accelerating, compressing or receiving energy. This chapter develops one-dimensional ideal-gas models before identifying the additional physics needed in real ducts and aerodynamic flows.

## Theory

Compressible-flow analysis allows density to change along a flow or with time. Mach number compares local fluid speed with local acoustic propagation speed. It measures how rapidly pressure information can travel relative to the gas. In a subsonic stream, small disturbances can propagate upstream as well as downstream. In a supersonic stream, their propagation relative to the ground is directed downstream within a limited region. The sound speed must be evaluated from the local thermodynamic state, rather than assigned one universal air value.

A small Mach number often supports an incompressible approximation when temperature changes are also small. It does not guarantee constant density in a strongly heated or cooled gas. Conversely, an ideal gas is not automatically incompressible: the ideal-gas equation explicitly relates density to pressure and temperature. The constant-specific-heat model below further assumes a calorically perfect gas. At high temperature, changes in heat capacity and composition invalidate some simple powers of Mach number.

Static properties describe the moving fluid locally. Stagnation properties describe a reference state reached by bringing that fluid to rest through an ideal adiabatic, reversible deceleration. Stagnation enthalpy is useful even when the actual flow contains irreversible regions. An adiabatic nozzle with no shaft work preserves stagnation enthalpy while converting static enthalpy into kinetic energy. It also preserves stagnation pressure only if its flow is isentropic. Across an adiabatic shock, stagnation temperature remains constant for a perfect gas, but stagnation pressure falls.

Nozzle geometry controls acceleration differently on the two sides of Mach one. A converging passage accelerates subsonic flow; a diverging passage accelerates supersonic flow under the stated one-dimensional isentropic assumptions. Thus a converging-diverging nozzle can accelerate a gas through a sonic throat and then to a supersonic exit. Geometry alone does not determine the realized branch: reservoir conditions and downstream pressure determine whether the passage stays subsonic, becomes choked, or contains shocks.

Choking is a maximum mass-flow condition for fixed throat area and upstream stagnation state. Reducing downstream pressure beyond the choking threshold does not keep increasing the ideal mass flow through that throat. It can still alter the downstream jet and shock structure. The critical-pressure ratio used for a simple converging nozzle is not a universal back-pressure criterion for every converging-diverging nozzle, valve, or long gas line.

A shock is a thin region of rapid compression. The conserved mass, momentum and total energy connect the states on its two sides, while entropy increases. A normal shock changes a supersonic upstream flow into a subsonic downstream flow. Static pressure, density and temperature rise, and velocity falls. An isentropic formula can relate static and stagnation properties on either side separately, but cannot equate stagnation pressures across the shock.

## Formula handbook

Use absolute pressure $p$ in Pa, temperature $T$ in K, density $\rho$ in kg/m3, gas-specific $R$ in J/(kg K), speed $V$ in m/s, area $A$ in m2 and mass flow $\dot m$ in kg/s. Subscript 0 denotes stagnation conditions; an asterisk denotes a sonic reference state. Unless stated otherwise, the gas is ideal with constant $\gamma=c_p/c_v$ and $c_p=\gamma R/(\gamma-1)$.

1. State, sound speed and Mach number:

$$
p=\rho RT,\qquad a=\sqrt{\gamma RT},\qquad M=V/a.
$$

2. Steady one-dimensional conservation of mass:

$$
\dot m=\rho VA.
$$

3. Adiabatic flow energy without shaft work or elevation change:

$$
h_0=h+\frac{V^2}{2},\qquad T_0=T+\frac{V^2}{2c_p}.
$$

4. Static-to-stagnation relations, with pressure and density referenced by isentropic deceleration:

$$
\frac{T_0}{T}=1+\frac{\gamma-1}{2}M^2,\qquad \frac{p_0}{p}=\left(\frac{T_0}{T}\right)^{\gamma/(\gamma-1)},\qquad \frac{\rho_0}{\rho}=\left(\frac{T_0}{T}\right)^{1/(\gamma-1)}.
$$

5. Area-velocity relation for smooth quasi-one-dimensional isentropic flow:

$$
\frac{dA}{A}=(M^2-1)\frac{dV}{V}.
$$

6. Area-Mach relation within one isentropic region:

$$
\frac{A}{A^*}=\frac1M\left[\frac2{\gamma+1}\left(1+\frac{\gamma-1}{2}M^2\right)\right]^{(\gamma+1)/[2(\gamma-1)]}.
$$

An area ratio greater than one has both a subsonic and a supersonic mathematical solution.

7. Mass-flow function:

$$
\dot m=\frac{Ap_0}{\sqrt{T_0}}\sqrt{\frac\gamma R}\,M\left(1+\frac{\gamma-1}{2}M^2\right)^{-(\gamma+1)/[2(\gamma-1)]}.
$$

8. Sonic temperature and pressure ratios:

$$
\frac{T^*}{T_0}=\frac2{\gamma+1},\qquad \frac{p^*}{p_0}=\left(\frac2{\gamma+1}\right)^{\gamma/(\gamma-1)}.
$$

9. Ideal choked mass flow, with sonic throat area $A^*$:

$$
\dot m^*=\frac{A^*p_0}{\sqrt{T_0}}\sqrt{\frac\gamma R}\left(\frac2{\gamma+1}\right)^{(\gamma+1)/[2(\gamma-1)]}.
$$

A measured discharge coefficient can modify this ideal result for a specified device; it must not be invented or transferred between unrelated geometries.

10. Normal-shock downstream Mach number, upstream $M_1>1$:

$$
M_2^2=\frac{1+\frac{\gamma-1}{2}M_1^2}{\gamma M_1^2-\frac{\gamma-1}{2}}.
$$

11. Normal-shock static-property ratios:

$$
\frac{p_2}{p_1}=1+\frac{2\gamma}{\gamma+1}(M_1^2-1),\qquad \frac{\rho_2}{\rho_1}=\frac{(\gamma+1)M_1^2}{2+(\gamma-1)M_1^2},\qquad \frac{T_2}{T_1}=\frac{p_2/p_1}{\rho_2/\rho_1}.
$$

12. Normal-shock stagnation-pressure ratio:

$$
\frac{p_{02}}{p_{01}}=\frac{p_2}{p_1}\left[\frac{1+\frac{\gamma-1}{2}M_2^2}{1+\frac{\gamma-1}{2}M_1^2}\right]^{\gamma/(\gamma-1)}.
$$

13. Entropy change for a perfect gas, and its shock-specific reduction:

$$
s_2-s_1=c_p\ln(T_2/T_1)-R\ln(p_2/p_1)=-R\ln(p_{02}/p_{01})>0.
$$

The last equality uses equal stagnation temperatures across an adiabatic normal shock.

14. Mach angle for infinitesimal disturbances in a uniform supersonic stream:

$$
\mu=\sin^{-1}(1/M).
$$

This is not the angle of an arbitrary finite-strength oblique shock.

## Derivation

Start with differential continuity: $d\rho/\rho+dV/V+dA/A=0$. For inviscid steady flow along the passage, momentum gives $dp+\rho V\,dV=0$. Along an isentrope, the acoustic definition is $dp=a^2d\rho$. Combining momentum with this relation gives $d\rho/\rho=-M^2dV/V$. Substitution into continuity yields $dA/A=(M^2-1)dV/V$. The sign reversal at Mach one follows from conservation and compressibility, not from a separate nozzle rule.

To locate maximum mass flow, hold $A,p_0,T_0$ fixed in formula 7 and differentiate its logarithm with respect to $M$. Apart from a positive denominator, the derivative is proportional to $1-M^2$. Flow therefore increases up to $M=1$ and decreases on the supersonic branch of the mathematical mass-flow function. The maximum is the choked value. This derivative result does not mean a simple converging nozzle can select the supersonic branch at its exit; the boundary-value problem still determines which state is attainable.

## Worked examples

### Example 1: a converging air nozzle

An ideal converging nozzle is supplied by a large reservoir at $p_0=300,000$ Pa absolute and $T_0=300$ K. Exit area is $1.00\times10^{-4}$ m2; back pressure is 100,000 Pa absolute. Use $R=287$ J/(kg K) and $\gamma=1.4$. The back-pressure ratio is 0.333333, below the critical ratio **0.528282**, so the exit is sonic in this model. The sonic static pressure is **158,484.5 Pa**, temperature is **250.000 K**, and speed is **316.938 m/s**. Formula 9 gives **0.0700068 kg/s**. Checking independently with $\rho^*=p^*/(RT^*)$ and $\rho^*a^*A^*$ reproduces that flow. The exit pressure exceeds ambient; further expansion occurs outside the nozzle. Setting exit static pressure equal to back pressure would contradict the choked internal solution.

### Example 2: a normal shock at Mach two

Air reaches a normal shock with $M_1=2.00$, $p_1=100,000$ Pa and $T_1=300$ K, using the same perfect-gas constants. The shock relations give **$M_2=0.577350$**, **$p_2/p_1=4.50000$**, and **$\rho_2/\rho_1=2.66667$**. Thus downstream pressure is **450,000 Pa** and temperature is **506.250 K**. Stagnation temperature is 540 K on both sides. Stagnation-pressure ratio is **0.720874**, and entropy rises by **93.9325 J/(kg K)**. This combination illustrates the distinction between static compression and loss of stagnation pressure. Independent checks of mass flux, momentum flux $p+\rho V^2$, and total enthalpy must agree across the shock.

## Exercises

1. Air has static temperature 300 K, static pressure 100,000 Pa and Mach number 0.50. With $\gamma=1.4$ and $R=287$ J/(kg K), find local speed, stagnation temperature and stagnation pressure.
2. Find the isentropic area ratio $A/A^*$ at Mach 2 for $\gamma=1.4$. Does that area ratio uniquely identify supersonic flow?
3. A simple ideal converging nozzle has reservoir pressure 150,000 Pa, reservoir temperature 300 K and back pressure 100,000 Pa. Determine whether it is choked and calculate exit Mach number and temperature. Use the same air model and an adequately large reservoir.

## Solutions

1. Sound speed is $\sqrt{1.4(287)(300)}=347.189$ m/s, giving **173.594 m/s**. The temperature multiplier is $1+0.2(0.5)^2=1.05$, so **$T_0=315.000$ K** and **$p_0=118,621.3$ Pa**. These pressures are absolute.
2. Substitution gives **$A/A^*=1.68750$**. A second, subsonic root also exists. Geometry and area ratio must be combined with boundary conditions and the presence or absence of shocks to identify the actual branch.
3. The imposed ratio is **0.666667**, above the critical value 0.528282, so the exit remains subsonic and its pressure matches back pressure in this ideal solution. Inverting formula 4 gives **$M_e=0.783659$** and **$T_e=267.183$ K**. Applying the choked mass-flow formula to this case without checking the ratio would be unjustified.

## Common mistakes

Use absolute pressure and Kelvin in every gas-state and stagnation relation. Do not carry the same stagnation pressure through a shock. Keep the local sound speed separate from fluid speed. A sonic reference area can change across an irreversible region, so one global $A^*$ is not automatically valid. “Adiabatic” does not mean “isentropic.” An increasing static pressure is compatible with a decreasing stagnation pressure when losses occur.

## Applications and limits

These models support early nozzle estimates, gas-turbine inlet reasoning and compressible CFD benchmarks. Long pipes with friction lead to Fanno-flow models; constant-area heating leads to Rayleigh-flow models. Both can produce choking without a geometric throat. Oblique shocks, expansion fans, boundary layers and real-gas effects require further development. The nozzle example does not establish valve capacity, pressure-relief sizing or a safe hardware operating envelope; those need the applicable device data and design methods.

## Further reading

- [NASA Glenn: Mass Flow Choking](https://www.grc.nasa.gov/www/k-12/airplane/mflchk.html) — derivation of the ideal mass-flow function and its sonic maximum.
- [NASA Glenn: Normal Shock Wave Equations](https://www.grc.nasa.gov/www/k-12/airplane/normal.html) — static and stagnation changes across a normal shock.
- [MIT OCW: Compressible Fluid Dynamics](https://ocw.mit.edu/courses/2-26-compressible-fluid-dynamics-spring-2004/) — full course materials extending to area change, friction, heat addition, waves and shocks.
