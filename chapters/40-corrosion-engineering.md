# 40. Corrosion Engineering

## Learning map

Prerequisites: materials science, elementary chemistry, electrical charge, and measurement uncertainty. Learn to identify a corrosion mechanism, define the exposed area and environment, and distinguish a thermodynamic driving force from a measured reaction rate. The calculations connect electrical charge to metal loss and metal loss to average thinning. Use them with inspection evidence; they do not determine allowable pressure, a safe inspection interval, or the remaining strength of a locally damaged component.

## Theory

Corrosion is material degradation through interaction with its environment. In aqueous metallic corrosion, an anodic reaction releases electrons as metal atoms enter an oxidized state, while a cathodic reaction consumes electrons. For iron dissolving as ferrous ions, the anodic reaction is $\mathrm{Fe\rightarrow Fe^{2+}+2e^-}$. A possible cathodic reaction in aerated near-neutral water is $\mathrm{O_2+2H_2O+4e^-\rightarrow4OH^-}$. Different environments support different reactions, and the eventual rust composition need not equal the initially dissolved ionic species.

Electronic conduction through the metal and ionic conduction through the electrolyte complete the circuit. A freely corroding isolated specimen can have zero externally measured net current while anodic and cathodic partial currents continue internally. Their charge rates balance at the corrosion potential. Therefore a zero ammeter reading is not evidence of zero corrosion. A corrosion current inferred from electrochemical measurements requires a valid interpretation of the reactions, geometry, and measurement method.

Thermodynamics describes the direction favored by a reaction and its equilibrium potential. Kinetics describes how quickly it proceeds. Polarization, passive films, dissolved-oxygen transport, solution resistance, and surface condition can change the rate. The Nernst equation adjusts an equilibrium potential for activities; it does not calculate corrosion current. A material can have a favorable oxidation driving force yet corrode slowly because a protective film limits reaction. Conversely, local film breakdown can concentrate attack into a small area.

Uniform corrosion removes material over much of the exposed surface, making average mass loss a useful thickness indicator. Pitting concentrates penetration in cavities, so a small total mass loss can coexist with a deep local defect. Crevices can create chemically distinct sheltered regions under gaskets, deposits, or overlaps. An average thinning rate cannot reconstruct the deepest pit or establish whether a remaining ligament is structurally acceptable. AMPP's descriptions of [uniform corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/uniform-corrosion) and [pitting](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/pitting-corrosion) support this mechanism distinction.

Galvanic interaction requires electrically connected materials and a shared conducting environment. The resulting potentials and currents depend on the actual environment and surface states, not only on a table of standard potentials. A small anodic area coupled to a larger cathodic area can experience concentrated anodic current. Area ratio alone does not supply a numerical corrosion rate because polarization and transport also change the total current. AMPP explains these coupling conditions in its [galvanic-corrosion overview](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/galvanic-corrosion).

Other mechanisms include erosion-corrosion, selective dissolution, intergranular attack, corrosion fatigue, stress-corrosion cracking, and hydrogen-related damage. Their distinction matters because replacing lost thickness may not address cracking or the chemical cause. Mitigation can involve materials selection, drainage and crevice reduction, coatings, electrical isolation, chemistry control, inhibitors, or designed cathodic protection. Selection depends on service and inspection evidence; a corrosion allowance is only one possible response to a characterized mechanism.

## Formula handbook

Use time $t$ in s, current $I$ in A, charge $q$ in C, exposed area $A_e$ in $\mathrm{m^2}$, density $\rho$ in $\mathrm{kg/m^3}$, and metal molar mass $M$ in kg/mol. $F\approx96485.33212\ \mathrm{C/mol}$ is the Faraday constant, $R=8.314462618\ \mathrm{J/(mol\,K)}$, and $z$ is the electron count per stated metal-oxidation reaction.

**1. Accumulated charge:**

$$
q=\int_0^t I(\tau)\,d\tau;\qquad q=It\quad\text{for constant current}.
$$

**2. Mean anodic current density:**

$$
i_a=I_a/A_e.
$$

Use the anodic partial current and its participating area, not an unexplained net external current.

**3. Faraday metal-loss relation:**

$$
\Delta m=\eta_F\frac{Mq}{zF}.
$$

$\eta_F$ is the fraction of the specified charge attributed to that dissolution reaction. Set it to one only when that assumption is justified. Alloy dissolution may need separate species and valence accounting.

**4. Average depth removed from one stated exposed surface area:**

$$
\bar d=\frac{\Delta m}{\rho A_e}.
$$

If both faces of a thin coupon are exposed, include both in $A_e$. Their individual penetration is different from the total reduction of plate thickness.

**5. Average measured thinning rate and conversion:**

$$
\bar c=\frac{\bar d}{t},\qquad c_{\rm mm/year}=\bar c_{\rm m/s}(1000)(365\times24\times3600).
$$

The “year” here is explicitly 365 days. Extrapolation assumes unchanged exposure and mechanism.

**6. Convenient coupon units, with cleaned metal mass loss:**

$$
c_{\rm mm/year}=\frac{87.6\,\Delta m_{\rm mg}}{\rho_{\rm g/cm^3}A_{\rm cm^2}t_{\rm h}}.
$$

This is a unit-conversion formula, not an alternative physical law. Cleaning must remove corrosion products without counting unrelated metal removal as service loss.

**7. Uniform electrochemical penetration rate:**

$$
\dot d=\eta_F\frac{M i_a}{zF\rho}.
$$

The result is m/s. Local current concentration invalidates interpreting this mean as maximum penetration.

**8. Reaction quotient and Nernst equation:**

$$
\mathcal Q=\prod_j a_j^{\nu_j},\qquad E_{\rm eq}=E^\circ-\frac{RT}{zF}\ln\mathcal Q.
$$

$a_j$ are dimensionless activities and $\nu_j$ are positive for products and negative for reactants. Use a consistently written reduction half-reaction or complete cell reaction. Pure solid phases have unit activity in their standard states. Potential is in V; half-cell potentials require a stated reference. The [IUPAC definition](https://goldbook.iupac.org/terms/view/09068/plain) specifies equilibrium and activities.

**9. At 298.15 K, base-ten form:**

$$
E_{\rm eq}=E^\circ-\frac{0.05915935\ \mathrm V}{z}\log_{10}\mathcal Q.
$$

The numerical coefficient changes with temperature. Concentration ratios replace activities only under an appropriate ideal or calibrated approximation.

**10. Complete-cell reaction free energy:**

$$
\Delta_rG=-zFE_{\rm cell}.
$$

This gives J per mole of reaction as written for a reversible cell potential. It does not give the heat generation of an operating corroding surface.

**11. Complete-cell equilibrium constant:**

$$
\ln K=\frac{zFE^\circ_{\rm cell}}{RT}.
$$

This follows at equilibrium, where $E_{\rm cell}=0$ and $\mathcal Q=K$.

**12. Simple uniform-loss projection:**

$$
t_w(\tau)=t_{w,0}-c\tau.
$$

Wall thicknesses $t_w,t_{w,0}$ and rate/time units must match. This kinematic estimate is not a pressure-design equation or fitness-for-service assessment.

**13. Descriptive pitting factor:**

$$
PF=d_{\max}/\bar d\qquad(\bar d>0).
$$

It describes inspected penetration relative to average loss over the stated area. It does not predict future pit growth.

## Derivation

One mole of metal atoms undergoing an oxidation that transfers $z$ electrons per atom transfers $zF$ coulombs. Charge $q$ therefore corresponds to $q/(zF)$ moles of that reaction. Multiplying by molar mass and the attributed charge fraction gives Faraday's mass relation. Dividing by density gives volume lost; dividing by exposed area gives mean penetration. Every step has a physical boundary: measured current must represent the reaction, mass must mean original metal removed, and exposed area must include all contributing surfaces.

For the practical coupon formula, a loss in milligrams becomes grams by multiplying by $10^{-3}$. Division by density in g/cm³ and area in cm² gives centimetres of penetration. Multiplying by 10 gives millimetres; multiplying a per-hour rate by 8760 gives a 365-day annual rate. The combined multiplier is $10^{-3}\times10\times8760=87.6$. This derivation explains why changing any stated unit without changing the factor gives an incorrect rate.

## Worked examples

### Example 1: charge, iron loss, and average thinning

Assume iron dissolves exclusively as $\mathrm{Fe^{2+}}$ with constant anodic current $I_a=0.00500$ A for 30 days, $\eta_F=1$, $M=0.055845$ kg/mol, $\rho=7870\ \mathrm{kg/m^3}$, and total participating area $A_e=0.0100\ \mathrm{m^2}$. The current is an assumed anodic dissolution current, not a direct open-circuit ammeter reading.

Time is $2{,}592{,}000$ s and charge is $12{,}960$ C. Mass loss is $0.055845(12960)/(2F)=0.003750576$ kg, or **3.75058 g**. Dividing by $7870(0.0100)$ gives average penetration **0.0476566 mm** over 30 days. A constant-rate annualization gives **0.579822 mm/year**. The current-density route, $i_a=0.500\ \mathrm{A/m^2}$ followed by Formula 7, gives the same result. Neither route supplies maximum pit depth or an acceptable operating pressure.

### Example 2: equilibrium potential of a stated cell reaction

For $\mathrm{Zn(s)+Cu^{2+}\rightarrow Zn^{2+}+Cu(s)}$, assume supplied standard cell potential $E^\circ=1.100$ V at 298.15 K. The electron count is two. Let the dimensionless ionic activities be $a_{\mathrm{Zn^{2+}}}=1.00$ and $a_{\mathrm{Cu^{2+}}}=0.0100$, with pure metals at unit activity. Then $\mathcal Q=100$ and $E=1.100-(0.05915935/2)\log_{10}(100)=\mathbf{1.04084\ V}$. The reaction free energy is $-2FE=\mathbf{-200.852\ kJ/mol}$ of reaction. The positive potential favors the written reaction under these assumptions, but no current, metal-loss rate, or galvanic service-life prediction follows without kinetic and circuit information.

## Exercises

1. A cleaned iron coupon loses 2.00 g over 60 days. Its total exposed area is $0.0250\ \mathrm{m^2}$ and density is $7870\ \mathrm{kg/m^3}$. Find average loss and its constant-rate annualization.
2. Convert $1.00\ \mathrm{\mu A/cm^2}$ to $\mathrm{A/m^2}$, then calculate uniform iron penetration in mm/year for $z=2$, $M=0.055845$ kg/mol, $\rho=7870\ \mathrm{kg/m^3}$, and unit charge efficiency.
3. At 298.15 K, a two-electron cell reaction's quotient increases tenfold while its standard potential remains fixed. Find the change in equilibrium cell potential.

## Solutions

1. Average depth is $0.002/[7870(0.025)]=1.01652\times10^{-5}$ m, or **0.0101652 mm**. Multiplying by $365/60$ gives **0.0618382 mm/year**. This assumes the 60-day exposure is representative of the projected period.
2. One square centimetre is $10^{-4}\ \mathrm{m^2}$, so the current density is **0.0100 A/m²**. Formula 7 gives $3.67721\times10^{-13}$ m/s, equivalent to **0.0115964 mm/year**. A missing area conversion would cause a factor-of-10,000 error.
3. $\Delta E=-(0.05915935/2)\log_{10}(10)=\mathbf{-0.0295797\ V}$, or **−29.5797 mV**. Increasing the quotient favors products less strongly for the reaction convention used.

## Common mistakes

Confusing electrode potential with corrosion rate, using net external current as the dissolution current, and overlooking oxidation valence are fundamental errors. Keep oxide mass separate from metal mass loss. Do not extrapolate average loss into a localized defect depth or reuse a seawater galvanic ranking for every water chemistry. A coating defect can change the participating areas; simply specifying a coating does not prove galvanic isolation or complete protection.

## Applications and limits

For plant piping, record material identity, temperature, fluid chemistry, aeration, deposits, wet/dry duty, electrical connections, and inspection locations before selecting a model. Compare repeated thickness maps, coupon data, and mechanism evidence rather than relying on one average. Inspection intervals, corrosion allowances, cathodic-protection settings, and pressure adequacy need applicable project requirements and specialist assessment. This chapter provides an educational calculation basis and deliberately supplies no universal acceptance thickness or protection potential.

## Further reading

- [IUPAC Gold Book — Nernst equation](https://goldbook.iupac.org/terms/view/09068/plain): primary definition, activities, and potential convention.
- [AMPP — Uniform corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/uniform-corrosion): mechanism and general thinning.
- [AMPP — Pitting corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/pitting-corrosion): localized attack and detection concerns.
- [AMPP — Galvanic corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/galvanic-corrosion): electrical coupling and environmental context. Links checked 2026-11-07; linked content is not reproduced as a standards document here.
