# 14. Turbomachinery

## Learning map

Prerequisites: fluid momentum, energy balances, rotating mechanics and thermodynamics. Learn to draw velocity triangles, relate angular momentum to shaft torque, distinguish static from stagnation properties, and use similarity with stated limits. Pumps, fans, compressors and turbines share these principles even though their fluids, speeds and operating constraints differ.

## Theory

A turbomachine exchanges energy with a continuously flowing fluid through rotating blades. A pump, fan or compressor receives shaft work and transfers it to the fluid; a turbine extracts work. Stationary guide vanes can redirect flow and convert kinetic energy into pressure, but an ideal stationary row does not supply shaft work. Rotor and stator functions must be separated when interpreting a stage diagram.

Absolute velocity is measured in a fixed frame. Relative velocity is measured with the rotating blade, while blade speed is the local tangential speed of the rotor. Their vector relation creates a velocity triangle. The tangential, or whirl, component of absolute velocity determines angular momentum. A high outlet speed alone does not guarantee useful work transfer; its direction relative to the rotor matters.

Euler's turbomachinery equation comes from angular momentum, not from assuming a particular blade shape. Its ideal work represents the energy transferred through rotor torque. Actual usable head is smaller for a pump because of hydraulic loss. Mechanical losses, leakage and disk friction further affect shaft input and efficiency. A pump can satisfy an angular-momentum calculation while failing due to cavitation, unstable operation or excessive radial load.

Static enthalpy measures thermodynamic state without the stream's macroscopic kinetic energy. Stagnation enthalpy adds that kinetic energy. In an adiabatic stationary diffuser with no work, stagnation enthalpy remains approximately constant while static pressure can rise as speed decreases. Stagnation pressure can fall because of irreversibility even if stagnation enthalpy is unchanged. This distinction is essential in compressor and turbine stage calculations.

Similarity compares machines operating at similar dimensionless conditions. Affinity laws are especially useful for modest speed changes in a fixed incompressible machine when efficiency changes little. They are not universal laws for arbitrary impeller trimming, cavitation, large compressibility changes or changes in operating regime. A dimensionless specific speed helps describe machine family; dimensional catalog specific-speed values depend on unit conventions and cannot be compared blindly.

## Formula handbook

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

## Derivation

Take a steady control volume around a rotor. The axial torque on the fluid equals the change in angular-momentum flow, $\tau=\dot m(r_2C_{\theta2}-r_1C_{\theta1})$. The power supplied by the rotating shaft is $P=\omega\tau$. Divide by mass flow and substitute $U_i=\omega r_i$ to obtain

$$
\frac{P}{\dot m}=U_2C_{\theta2}-U_1C_{\theta1}.
$$

The expression automatically handles inlet prewhirl when its sign is defined consistently. Assuming zero inlet whirl simplifies it to $w_E=U_2C_{\theta2}$, but that is a flow condition rather than a universal identity. In real finite-blade centrifugal impellers, outlet flow can deviate from the blade-based ideal triangle; slip and other losses require additional modeling or measured curves.

## Worked examples

### Example 14-A: centrifugal pump rotor

A pump has $U_1=10$, $C_{\theta1}=2$, $U_2=30$ and $C_{\theta2}=18$ m/s. The stated whirl components are actual mean values used in the rotor balance. Euler work is $30(18)-10(2)=\mathbf{520\ J/kg}$ and Euler head is **53.0071 m**. With hydraulic efficiency 0.80, delivered head is **42.4057 m**. At water flow 0.050 m3/s and density 1000 kg/m3, rotor-to-fluid power is **26.0 kW** and useful hydraulic power is **20.8 kW**. Shaft input may exceed rotor-to-fluid power when mechanical losses are included.

### Example 14-B: speed reduction

At a reference operating point, a fixed-impeller pump delivers 0.030 m3/s at 25 m head and consumes 4.0 kW. Estimate the homologous point at 80% speed, assuming similar efficiency and no regime change. Flow becomes $0.030(0.8)=\mathbf{0.0240\ m^3/s}$, head becomes $25(0.8)^2=\mathbf{16.0\ m}$ and power becomes $4000(0.8)^3=\mathbf{2.048\ kW}$. These values describe a corresponding pump-curve point. The installed system's new operating point still requires intersection with its system curve.

## Exercises

1. A rotor radius is 0.15 m and speed is 1800 rpm. Find angular and blade speeds.
2. An adiabatic compressor raises stagnation enthalpy by 60 kJ/kg at mass flow 0.30 kg/s. Find work input to the fluid.
3. A pump's hydraulic output is 12 kW and measured shaft input is 16 kW. Find total efficiency. If motor efficiency is 0.90, find electrical input.

## Solutions

1. $\omega=2\pi(1800)/60=188.496$ rad/s and $U=\omega r=28.2743$ m/s.
2. $P=\dot m\Delta h_0=0.30(60)=18$ kW, neglecting elevation and external heat transfer.
3. $\eta_p=12/16=0.75$. Motor input is $16/0.90=17.7778$ kW, so overall hydraulic-to-electric efficiency is 67.5%.

## Common mistakes

Do not substitute relative whirl for absolute whirl in Euler's equation. Mark positive rotation and velocity components on the sketch. Keep static and stagnation efficiencies distinct. Revolutions per minute cannot be used directly in $P=\tau\omega$. Affinity scaling does not prove that cavitation margin or vibration stays acceptable. A machine's total efficiency is not identical to its hydraulic efficiency.

## Applications and limits

Velocity triangles provide insight into pumps, fans, hydraulic turbines and gas-turbine stages. Compressor surge and choke, turbine cooling, Reynolds effects, blade stress and rotor dynamics require more detailed treatment. Use actual manufacturer maps for selection and determine the operating envelope, not only one nominal point. Structural integrity, overspeed protection and pressure containment are separate design obligations.

## Further reading

- [NASA Glenn: Brayton-cycle explanation](https://www.grc.nasa.gov/www/k-12/BGP/brayton.html) — the compressor and turbine in a system-level cycle.
- [US DOE: pump-system resources](https://betterbuildingssolutioncenter.energy.gov/better-plants/pumps) — practical pump performance and system efficiency.
- [MIT: fluid-mechanics subject guide](https://ga3.mit.edu/fluid-mechanics/) — angular momentum, control volumes and supporting fluid theory.
