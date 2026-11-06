# 01 · Units, dimensions, and engineering estimates

## Learning map

Start here before using any formula in this handbook. You need arithmetic, powers, and elementary algebra. The goal is to translate a physical question into quantities with consistent units, estimate the answer before calculating, and attach a defensible statement of uncertainty. Continue to engineering mathematics and then statics or thermodynamics.

## Theory

A quantity is more than a number. A pipe diameter of 50 means nothing until a unit is supplied. The quantity equation describes physics independently of the selected units; a numerical equation may contain conversion factors tied to one unit convention. In this handbook, equations are quantity equations unless explicitly labelled otherwise. Convert all inputs into a consistent system before substitution.

The seven SI base quantities are time (second, s), length (metre, m), mass (kilogram, kg), electric current (ampere, A), thermodynamic temperature (kelvin, K), amount of substance (mole, mol), and luminous intensity (candela, cd). Force, energy, pressure, and power are derived quantities. A newton is kg m/s², a joule is N m, a pascal is N/m², and a watt is J/s. A torque and an energy have the same dimensions, but they are different physical quantities; reporting torque in N m preserves that distinction.

Mass is not weight. Mass expresses inertia, while weight is a gravitational force. The local acceleration $g$ varies; $9.81\ \mathrm{m/s^2}$ is an ordinary engineering approximation, not a universal exact constant. Density is mass per volume and specific weight is weight per volume. Similarly, pressure and stress have the same units but refer to different physical descriptions.

Dimensional consistency is necessary but insufficient. Both $mv^2$ and $mv^2/2$ have energy dimensions. Only the physical derivation determines the factor. An empirical correlation may also require dimensionless inputs, a specified geometry, and a limited experimental range. Never repair an inconsistent expression merely by inserting a numerical constant without understanding its units.

An estimate should expose the scale controlling the outcome. For lifting water, the important quantities are mass flow, height, gravity, and efficiency. Fine details about pipe roughness cannot rescue a calculation that uses litres per minute as cubic metres per second. Establish the dominant balance first, then refine the model.

Uncertainty describes imperfect knowledge of an input or result. Error is the difference from a reference value; its true value is often unknown. Standard uncertainty is expressed as a standard-deviation-equivalent quantity. Repeated measurements help estimate random variation, but do not automatically remove calibration bias. Correlated inputs require covariance terms; treating every measurement as independent can underestimate or overestimate uncertainty.

## Formula handbook

1. Weight: $W=mg$, with $W$ in N, $m$ in kg, and local $g$ in m/s².
2. Density: $\rho=m/V$ in kg/m³; specific weight $\gamma=\rho g$ in N/m³.
3. Pressure: $p=F_\perp/A$ in Pa for uniform normal force over area $A$ in m².
4. Absolute pressure: $p_{\mathrm{abs}}=p_{\mathrm{gauge}}+p_{\mathrm{ambient}}$. A vacuum gauge may use a different sign convention.
5. Absolute temperature: $T/\mathrm{K}=t/{}^\circ\mathrm{C}+273.15$. Temperature differences have the same numerical size in K and °C.
6. Rotational speed: $\omega=2\pi n/60$, where $n$ is the numerical speed in revolutions per minute and $\omega$ is in rad/s.
7. Shaft power: $P=\tau\omega$, where torque $\tau$ is in N m and $P$ in W.
8. Hydraulic power: $P_h=\rho gQH$, where $Q$ is volumetric flow in m³/s and $H$ is head in m. Input power is $P_{\mathrm{in}}=P_h/\eta$ for total efficiency $\eta$.
9. Relative deviation: $e_r=(x-x_{\mathrm{ref}})/x_{\mathrm{ref}}$ for nonzero reference; percent deviation is $100e_r$.
10. For a differentiable measurement model $y=f(x_1,\ldots,x_n)$, first-order uncertainty propagation is

$$
u_y^2\approx\sum_i\left(\frac{\partial f}{\partial x_i}\right)^2u_i^2+2\sum_{i<j}\frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j}\operatorname{cov}(x_i,x_j).
$$

The derivatives are evaluated at the reported estimates. Large uncertainties or strongly nonlinear models require more careful propagation.

11. For independent inputs in $y=C\prod_i x_i^{a_i}$, the small-uncertainty approximation is $(u_y/y)^2\approx\sum_i(a_i u_i/x_i)^2$.
12. Buckingham's dimensional theorem gives $n-r$ independent dimensionless groups when $n$ dimensional variables have a dimension matrix of rank $r$. A dimensionless group does not itself establish a causal law.

Useful exact conversions: $1\ \mathrm{L}=10^{-3}\ \mathrm{m^3}$, $1\ \mathrm{bar}=10^5\ \mathrm{Pa}$, $1\ \mathrm{MPa}=1\ \mathrm{N/mm^2}$, and $1\ \mathrm{kWh}=3.6\ \mathrm{MJ}$. Metric prefixes multiply the entire unit: $(1\ \mathrm{mm})^2=10^{-6}\ \mathrm{m^2}$.

## Derivation

Suppose drag $F$ depends on density $\rho$, speed $U$, diameter $D$, and dynamic viscosity $\mu$. Their dimensions are $MLT^{-2}$, $ML^{-3}$, $LT^{-1}$, $L$, and $ML^{-1}T^{-1}$. Five variables with three independent dimensions imply two dimensionless groups. Dividing force by $\rho U^2D^2$ removes all dimensions, while $\rho UD/\mu$ is already dimensionless. Therefore dimensional analysis permits

$$
\frac{F}{\rho U^2D^2}=\Phi\left(\frac{\rho UD}{\mu}\right).
$$

It does not determine the function $\Phi$. Surface roughness, compressibility, or free-surface effects add variables and groups if they matter physically. Omitting them at the start is a modelling assumption, not a mathematical consequence.

## Worked examples

### Example 1: Water-lifting power

A pump lifts water at 120 L/min through 18 m of total head. Use $\rho=998\ \mathrm{kg/m^3}$, $g=9.81\ \mathrm{m/s^2}$, and total efficiency 0.65. Convert the flow: $Q=120(10^{-3})/60=0.002\ \mathrm{m^3/s}$. Then $P_h=998(9.81)(0.002)(18)=352.45\ \mathrm{W}$ and $P_{\mathrm{in}}=542.24\ \mathrm{W}$. The efficiency correction must increase the required input power. This is a duty estimate, not a motor selection including start-up, service conditions, or operating margin.

### Example 2: Area uncertainty

A measured diameter is $d=20.00\ \mathrm{mm}$ with standard uncertainty $u_d=0.05\ \mathrm{mm}$. For $A=\pi d^2/4$, $A=314.159\ \mathrm{mm^2}$. The sensitivity is $dA/dd=\pi d/2$, so $u_A=(\pi20/2)(0.05)=1.571\ \mathrm{mm^2}$. Relative standard uncertainty is $2u_d/d=0.005=0.5\%$. Report about $314.2\ \mathrm{mm^2}$ with standard uncertainty $1.6\ \mathrm{mm^2}$, specifying the uncertainty meaning rather than silently calling it a guaranteed bound.

## Exercises

1. A shaft transmits 25 N m at 1440 rpm. Find power in kW.
2. A gauge reads 250 kPa and ambient pressure is 98 kPa. Find absolute pressure.
3. Density is obtained from independent measurements with relative standard uncertainties 1% in mass and 2% in volume. Estimate its relative standard uncertainty.

## Solutions

1. $\omega=2\pi(1440)/60=150.796\ \mathrm{rad/s}$ and $P=25\omega=3.770\ \mathrm{kW}$. Rpm cannot be substituted directly into $P=\tau\omega$.
2. $p_{\mathrm{abs}}=250+98=348\ \mathrm{kPa}$. The ambient datum must be stated.
3. Because $\rho=mV^{-1}$, $u_\rho/\rho=\sqrt{0.01^2+0.02^2}=0.02236$, or 2.24%. This result assumes independence and a suitable linear approximation.

## Common mistakes

Confusing kW with kWh, entering millimetres into an equation otherwise using metres, using Celsius in a temperature ratio, and mixing gauge and absolute pressure can each change an answer by orders of magnitude. Excess decimal places do not create measurement precision. A dimensionless number can still have a convention: the Darcy and Fanning friction factors differ by four.

## Applications and limits

Use a short calculation record: sketch the system, state the quantity sought, list input sources and units, write the physical model, substitute values, check the dimensions, estimate the scale, and record assumptions. Similarity arguments help plan experiments, but matching one dimensionless group does not guarantee full similarity. This chapter establishes calculation discipline for every later volume.

## Further reading

- [BIPM, SI Brochure](https://www.bipm.org/en/publications/si-brochure/) — official unit definitions and notation; the publisher page provides the current edition and updates.
- [NIST Technical Note 1297, uncertainty propagation](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty) — full treatment of sensitivity coefficients and covariance. The examples here are original.
