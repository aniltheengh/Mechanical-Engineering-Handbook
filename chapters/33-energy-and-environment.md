# 33. Energy Systems and Environmental Accounting

## Learning map

Prerequisites: thermodynamics, fluid mechanics, heat transfer, electrical power, and engineering economics. Start with the service required, such as a volume of water pumped to a stated head, a comfortable occupied space, or a quantity of product. Then trace energy sources, conversions, losses, and environmental consequences. Comparing equipment on equal useful service prevents misleading conclusions from efficiency figures alone.

## Theory

Energy is conserved, but its usefulness for producing work depends on its form and surroundings. Electricity and shaft work can be converted extensively into other forms, while low-temperature heat has limited work potential. Efficiency measures useful output divided by input under a defined boundary. A heat pump can have a heating coefficient of performance above one because it transfers environmental heat in addition to consuming work; this does not violate energy conservation.

An energy system is a chain. Generation, conversion, transmission, storage, and end-use losses all influence the service delivered. Improving one device may have a smaller total benefit than expected if another part of the chain dominates losses. Conversely, reducing demand can avoid losses at several upstream stages. For pumps and fans, the actual operating point and control strategy can matter more than a nominal peak efficiency.

Renewable resources vary over time. A wind turbine's instantaneous power depends strongly on wind speed, but annual energy depends on the full speed distribution, turbine power curve, availability, and losses. Applying a cubic power relation to the annual mean wind speed generally does not produce annual mean power. Solar output depends on irradiance, module temperature, orientation, shading, and electrical losses. Capacity factor summarizes annual energy relative to continuous rated operation; it is not the same as conversion efficiency.

Environmental accounting requires a functional unit and system boundary. “Per kilowatt-hour delivered” differs from “per device manufactured” or “per year operated.” Include appropriate upstream material and energy impacts, operation, replacements, and end-of-life processes. An emission factor can depend on location, year, technology, and accounting purpose. An average grid factor and a marginal factor answer different questions; neither should be substituted without explanation.

Energy and carbon are related but not interchangeable. A lower-energy process may use a higher-emission fuel, while a lower-emission electricity supply may have different resource or land impacts. Water use, air pollutants, waste, biodiversity, and material depletion also matter. A single aggregate metric is useful only when its boundary and limitations remain visible.

## Formula handbook

Let $P$ be power (W), $E$ energy (J), $t$ time (s), and $\eta$ dimensionless efficiency. **Energy from variable power:**

$$
E=\int_0^T P(t)dt,\qquad 1\ \mathrm{kWh}=3.6\times10^6\ \mathrm J.
$$

**Conversion efficiency and simple sequential chain:**

$$
\eta=\frac{E_{\rm useful}}{E_{\rm input}},\qquad \eta_{\rm chain}=\prod_i\eta_i.
$$

The product assumes the output of one stage is the input of the next and no unaccounted parallel streams. **Wind kinetic power and extracted shaft power:**

$$
P_{\rm wind}=\tfrac12\rho A U^3,\qquad P_{\rm shaft}=C_P P_{\rm wind}.
$$

$\rho$ is air density ($\mathrm{kg/m^3}$), $A$ rotor area ($\mathrm{m^2}$), $U$ undisturbed wind speed (m/s), and $C_P$ power coefficient. The ideal unconfined actuator-disk limit is $C_P\le16/27$ under its assumptions. **Hydraulic power:**

$$
P_h=\rho gQH,\qquad P_{\rm electric}=\frac{P_h}{\eta_p\eta_m}.
$$

$Q$ is volumetric flow ($\mathrm{m^3/s}$), $H$ head (m), and pump and motor efficiencies refer to the operating point. **Approximate photovoltaic power at a stated condition:**

$$
P_{\rm PV}=G A\eta_{\rm PV}.
$$

$G$ is irradiance ($\mathrm{W/m^2}$); $\eta_{\rm PV}$ includes only explicitly stated losses. **Capacity factor:**

$$
CF=\frac{E_{\rm annual}}{P_{\rm rated}T_{\rm year}}.
$$

Use matching energy/time units. **Thermal work-potential upper bound for heat from a constant-temperature reservoir:**

$$
W_{\max}=Q\left(1-\frac{T_0}{T_h}\right),\qquad T_h>T_0.
$$

Temperatures are absolute kelvin. **Operational emissions accounting:**

$$
m_{\rm CO_2e}=\sum_i E_i\,EF_i.
$$

If $E_i$ is kWh and $EF_i$ is kg CO2e/kWh, the result is kg CO2e. **Inventory normalized by functional output:**

$$
I_{\rm unit}=\frac{I_{\rm materials}+I_{\rm manufacture}+I_{\rm operation}+I_{\rm end}}{N_{\rm functional\ units}}.
$$

All numerator terms need the same impact metric and allocation basis. **Discounted levelized energy cost:**

$$
\mathrm{LCOE}=\frac{\sum_{t=0}^n C_t/(1+i)^t}{\sum_{t=0}^n E_t/(1+i)^t}.
$$

State timing, included costs, and currency basis. This metric alone does not represent time-dependent energy value or grid integration cost.

## Derivation

During time $dt$, uniform wind carries a mass $dm=\rho A U\,dt$ through area $A$. Its kinetic energy is $dE=\frac12dm\,U^2$. Dividing by $dt$ gives $P_{\rm wind}=\frac12\rho A U^3$. The turbine cannot extract all of that power while maintaining steady flow through the rotor; deceleration changes the streamtube and downstream kinetic energy. The power coefficient represents the extracted fraction under a defined rotor model or measured operating condition. Electrical output requires additional drivetrain and generator efficiency factors unless they are already included in the stated coefficient.

## Worked examples

**Example 1 — wind output at one operating point.** Take $\rho=1.2\ \mathrm{kg/m^3}$, rotor area $A=10\ \mathrm{m^2}$, and uniform wind $U=8\ \mathrm{m/s}$. Available kinetic power is $0.5(1.2)(10)(8^3)=3072\ \mathrm W$. Assume aerodynamic power coefficient $C_P=0.40$ and drivetrain/generator efficiency $0.90$. Shaft power is $1228.8\ \mathrm W$, and electrical power is $1105.92\ \mathrm W$. These assumed values describe one operating point. Annual energy cannot be calculated from it without the time distribution and machine operating limits.

**Example 2 — pump energy and emissions.** Two alternatives provide the same measured hydraulic service. The first draws $10\ \mathrm{kW}$ and the second $8\ \mathrm{kW}$ for $4000\ \mathrm h/year$. Annual electrical saving is $(10-8)(4000)=8000\ \mathrm{kWh}=28.8\ \mathrm{GJ}$. With an explicitly hypothetical emission factor of $0.40\ \mathrm{kg\ CO_2e/kWh}$, avoided operational emissions are $3200\ \mathrm{kg\ CO_2e/year}$. If producing the replacement causes an assumed additional $1600\ \mathrm{kg\ CO_2e}$, a simple undiscounted carbon payback is $1600/3200=0.50$ years. This excludes changes in grid factors, performance, maintenance, and disposal.

## Exercises

1. A $2\ \mathrm{kW}$ device runs for three hours. Express its energy in kWh and MJ.
2. A $5\ \mathrm{kW}$ generator produces $8760\ \mathrm{kWh}$ in a 365-day year. Find capacity factor.
3. A collector receives $800\ \mathrm{W/m^2}$ over $2\ \mathrm{m^2}$ and delivers $960\ \mathrm W$ of useful heat. Find thermal efficiency at that condition.

## Solutions

1. Energy is $6\ \mathrm{kWh}$, or $6(3.6)=21.6\ \mathrm{MJ}$.
2. Rated annual energy is $5(8760)=43800\ \mathrm{kWh}$. Capacity factor is $8760/43800=0.20$, or $20\%$.
3. Incident power is $1600\ \mathrm W$. Efficiency is $960/1600=0.60$, or $60\%$. This does not specify performance at another ambient or fluid temperature.

## Common mistakes

- Treating kW as an energy unit or kWh as a power unit.
- Calling capacity factor an efficiency.
- Using one generic emissions factor without date, location, and accounting purpose.
- Comparing alternatives that deliver different amounts or qualities of useful service.
- Applying average wind speed to a cubic relation as if it gave average power.

## Applications and limits

Use these balances for plant audits, pumping systems, thermal retrofits, renewable-energy screening, and life-cycle comparisons. Measure power and duty where possible. Separate direct measurements, manufacturer data, modeled estimates, and hypothetical assumptions in reports. Environmental decisions require a broader assessment when impacts shift between stages or categories. The numerical examples teach calculation structure, not a site-specific sustainability claim.

## Further reading

- [U.S. Department of Energy — Small Wind Guidebook](https://www.energy.gov/cmei/systems/windexchange/small-wind-guidebook): resource, turbine, and system context.
- [National laboratory — comparative PV LCOE documentation](https://nrel.sitefinity.cloud/pv/lcoe-calculator/documentation): explicit cost and energy accounting definitions.
- [U.S. Department of Energy — life-cycle cost resources](https://www.energy.gov/cmei/femp/building-life-cycle-cost-programs): economic evaluation of energy and water projects.
