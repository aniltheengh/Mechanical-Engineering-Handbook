# 16. Combustion and internal-combustion engines

## Learning map

Prerequisites: chemical mole balances, ideal-gas mixtures, thermodynamics and rotating power. Learn to balance complete combustion, define fuel-air quantities, distinguish indicated and brake performance, and interpret simple engine metrics. Ideal cycles are treated separately in the power-cycle chapter; here the focus is reacting flow and actual performance bookkeeping.

## Theory

Combustion converts chemical energy through reactions between fuel and oxidizer. Stoichiometric oxidizer is the amount required for a specified complete-reaction model. Actual combustion depends on mixing, chemical kinetics, heat loss and residence time. A balanced overall equation satisfies atomic conservation but does not predict flame stability, ignition delay or the detailed pollutant concentrations.

For a hydrocarbon burning completely with sufficient oxygen, carbon forms carbon dioxide and hydrogen forms water. Air adds nitrogen and other species. A simple dry-air model treats nitrogen as an inert diluent, although nitrogen chemistry becomes important for emissions at high temperatures. Rich mixtures lack sufficient oxygen for complete conversion, so products can include carbon monoxide, hydrogen and unburned hydrocarbons. Even nominally lean combustion can have locally rich regions.

Heating value depends on the state of the products. The higher heating value includes condensation of the formed water to the specified reference state; the lower heating value leaves this water as vapor. Comparing engine efficiencies based on different heating values without correction is misleading. Fuel composition and reference conditions must accompany a precise heating-value claim.

An engine converts cylinder pressure into piston force, crankshaft torque and shaft power. Indicated work is obtained from the cylinder pressure-volume loop. Brake power is measured at the shaft after mechanical and accessory losses within the chosen boundary. Friction power is the difference under a consistently defined test. Mean effective pressure is a cycle-work-per-displacement metric, not the actual peak cylinder pressure.

Four-stroke engines complete a working cycle in two crankshaft revolutions; two-stroke engines have one cycle per revolution in the ideal counting model. This affects power formulas and volumetric-efficiency calculations. Volumetric efficiency compares inducted fresh charge with a reference-density volume based on displacement; its value depends on reference conditions and charge definition. Boosted engines can exceed unity on some reference bases.

## Formula handbook

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

## Derivation

For a four-stroke engine, the number of cycles per second is $N/120$ when $N$ is rpm. Brake power equals brake work per cycle times this frequency: $P_b=W_bN/120$. Since $BMEP=W_b/V_d$, power is $BMEP\,V_dN/120$. Equate this with torque power $2\pi\tau N/60$ and cancel speed to obtain

$$
BMEP=4\pi\tau/V_d.
$$

The factor of two between four-stroke and two-stroke forms follows from cycle frequency, not from an arbitrary efficiency correction. BMEP enables size-normalized torque comparison but says nothing by itself about peak stress, combustion pressure history or durability.

## Worked examples

### Example 16-A: methane air requirement

Use the simplified reaction $\mathrm{CH_4+2O_2\rightarrow CO_2+2H_2O}$ with teaching molecular masses 16 kg/kmol for methane and 32 kg/kmol for oxygen. One kilogram of fuel requires 4 kg oxygen. With supplied dry-air oxygen mass fraction 0.232, $AFR_{st}=4/0.232=\mathbf{17.2414\ kg\ air/kg\ fuel}$. At 20% excess air, actual ratio is $1.20(17.2414)=\mathbf{20.6897}$ and equivalence ratio is $1/1.2=0.8333$. More precise molar masses or air composition slightly change the result.

### Example 16-B: measured shaft performance

An engine develops torque 120 N m at 3000 rpm while consuming 0.0030 kg/s fuel of supplied lower heating value 43 MJ/kg. Brake power is $120(2\pi)(3000)/60=\mathbf{37.6991\ kW}$. Fuel power is 129 kW, so lower-heating-value brake efficiency is **29.2241%**. Brake-specific fuel consumption is $3600(0.0030)/37.6991=\mathbf{0.286479\ kg/kWh}$, or 286.479 g/kWh. If displacement is 0.0020 m3 and the engine is four-stroke, BMEP is approximately 754 kPa.

## Exercises

1. Find mean piston speed for stroke 0.090 m at 3000 rpm.
2. Fuel flow is 0.010 kg/s with heating value 42 MJ/kg. Find fuel power and brake power at efficiency 0.30.
3. Actual air-fuel ratio is 25 and stoichiometric ratio is 17.2 on the same mass basis. Find excess-air ratio and equivalence ratio; classify the overall mixture.

## Solutions

1. $\overline V_p=2(0.090)(3000/60)=9.0$ m/s. This is a cycle average of absolute piston travel speed, not peak piston speed.
2. Fuel power is $0.010(42\times10^6)=420,000$ W. Brake output is $0.30(420)=126$ kW.
3. $\lambda=25/17.2=1.45349$ and $\phi=17.2/25=0.688$. The overall mixture is lean, with about 45.35% excess air under the stated model.

## Common mistakes

Mole ratio and mass ratio are not interchangeable. Heating value is energy per fuel mass, not per mixture mass unless explicitly converted. Indicated and brake efficiencies need different power measurements. Use radians per second in torque power. A complete global reaction does not establish zero pollutant emissions. An air-standard efficiency from the Otto cycle is not a measured engine brake efficiency.

## Applications and limits

Use these relations to interpret engine test data, boiler fuel balances and early combustion-system energy estimates. Detailed combustion requires species chemistry, transport and radiation models or measurements. Knocking, ignition, flameholding, exhaust aftertreatment and heat rejection are important topics beyond this compact chapter. Fuel-system hardware and engine testing involve pressure, hot surfaces, moving parts and exhaust hazards; these calculations are educational analysis, not operating instructions.

## Further reading

- [NASA Glenn: engine thermodynamic analysis](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/engine-thermodynamic-analysis/) — the ideal thermodynamic model behind a reciprocating engine.
- [NIST Chemistry WebBook](https://webbook.nist.gov/chemistry/) — species thermochemistry and supporting property references.
- [MIT OCW: Thermal Energy](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/) — course materials including thermochemistry and energy conversion.
