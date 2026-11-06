# Reliability, economics, energy, and systems

Mechanical Engineering Handbook · First edition · 2026-11-06

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [31. Reliability and Maintenance](../chapters/31-reliability-and-maintenance.md)
- [32. Engineering Economics](../chapters/32-engineering-economics.md)
- [33. Energy Systems and Environmental Accounting](../chapters/33-energy-and-environment.md)
- [35 · Systems engineering and integrated design](../chapters/35-systems-engineering.md)

---

## 31. Reliability and Maintenance

### Learning map

Prerequisites: probability, statistics, materials, fatigue, and machine operation. Reliability is the probability of performing a defined function for a stated duration under stated conditions. Availability concerns whether a repairable system is operating when required. Maintainability concerns the ability to restore function. These quantities answer different questions and should not be substituted for one another.

### Theory

A reliability statement needs a failure definition, mission duration, operating environment, and population. “The pump is reliable” has little quantitative meaning without specifying flow, head, leakage, duty, fluid, and what counts as failure. A survival model represents a distribution of possible failure times, not a fixed lifetime promised for every component.

The hazard rate is the instantaneous failure rate conditional on survival so far. It differs from the probability density because the surviving population shrinks with time. An exponential lifetime model has constant hazard and is useful only when that assumption is defensible. It does not represent wear-out simply because its mean time to failure is convenient. Weibull models allow increasing or decreasing hazard through a shape parameter, but selecting a flexible distribution does not replace collecting adequate data.

System architecture matters. A series system fails if any required component fails. A parallel redundant system succeeds if at least one of its paths succeeds, provided failures are independent and the architecture can actually use the surviving path. Common-cause failure, switching failures, shared power, shared cooling, and maintenance errors can invalidate a simple independence calculation. Redundancy must be analyzed as a system behavior.

Maintenance strategies include run-to-failure, age-based replacement, condition monitoring, and inspection. The best choice depends on failure consequences, detectability, deterioration behavior, spare availability, and intervention cost. Replacing a constant-hazard item at a fixed age does not automatically lower its subsequent hazard. Conversely, wear-out may justify scheduled replacement if the failure distribution and costs support it.

Failure data require careful treatment. A component still operating when a study ends provides a right-censored observation: its lifetime exceeds the recorded time. Discarding it biases analysis. Downtime, repair duration, waiting for spares, and scheduled maintenance should also be separated according to the metric's definition. The NIST reliability handbook discusses these statistical foundations and estimation methods in depth.

### Formula handbook

Let $T$ be time to failure, $t\ge0$ elapsed time, $F$ cumulative failure probability, $f$ probability density, and $R$ reliability.

$$
F(t)=P(T\le t),\qquad R(t)=1-F(t),\qquad f(t)=\frac{dF}{dt}=-\frac{dR}{dt}.
$$

Probabilities are dimensionless; $f$ has reciprocal-time units. **Hazard and cumulative hazard:**

$$
h(t)=\frac{f(t)}{R(t)},\qquad H(t)=\int_0^th(\tau)d\tau,\qquad R(t)=e^{-H(t)}.
$$

**Exponential constant-hazard model:**

$$
R(t)=e^{-\lambda t},\qquad f(t)=\lambda e^{-\lambda t},\qquad \mathrm{MTTF}=1/\lambda.
$$

$\lambda$ is in reciprocal hours if $t$ is in hours; units must match. **General nonnegative lifetime mean:**

$$
E[T]=\int_0^\infty R(t)\,dt.
$$

**Two-parameter Weibull model:**

$$
R(t)=e^{-(t/\eta)^\beta},\qquad h(t)=\frac\beta\eta\left(\frac t\eta\right)^{\beta-1}.
$$

$\eta>0$ is scale (time), $\beta>0$ dimensionless shape. **Independent series system:**

$$
R_s(t)=\prod_iR_i(t).
$$

**Independent active parallel system, success if any component works:**

$$
R_p(t)=1-\prod_i[1-R_i(t)].
$$

**Long-run inherent availability under a stationary alternating uptime/repair model:**

$$
A_i=\frac{\mathrm{MTBF}}{\mathrm{MTBF}+\mathrm{MTTR}}.
$$

Here MTBF denotes mean operating time between failures, and MTTR mean corrective repair time. Logistics or administrative delays require an operational availability definition. **Observed uptime fraction:**

$$
A_{\rm observed}=\frac{t_{\rm up}}{t_{\rm up}+t_{\rm down}}.
$$

**Independent repeated Bernoulli trials:**

$$
P(K=k)=\binom nkp^k(1-p)^{n-k}.
$$

This describes counts under the trial assumptions; it is not directly a life-distribution model. **Expected failure consequence for mutually exclusive outcomes:**

$$
E[C]=\sum_i p_iC_i.
$$

Expected cost does not capture every safety or operational requirement.

### Derivation

From $h(t)=f(t)/R(t)$ and $f(t)=-dR/dt$, obtain $dR/dt=-h(t)R(t)$. Separate variables: $dR/R=-h(t)dt$. Integrating from zero with $R(0)=1$ gives $\ln R(t)=-\int_0^th(\tau)d\tau$. Exponentiating yields the survival-hazard relation. For constant $h=\lambda$, this becomes $R=e^{-\lambda t}$, and integration gives $E[T]=1/\lambda$. The model's memoryless property follows from $P(T>s+t\mid T>s)=R(s+t)/R(s)=e^{-\lambda t}$. Surviving longer does not improve or worsen its conditional remaining lifetime under this particular model.

### Worked examples

**Example 1 — mission reliability.** Assume a component has a constant hazard with MTTF $5000\ \mathrm h$. Then $\lambda=0.0002\ \mathrm{h^{-1}}$. For a $1000\ \mathrm h$ mission, reliability is $e^{-0.2}=0.818731$. Two independent such components, both required, have reliability $e^{-0.4}=0.670320$. The system's probability of completing the mission is about $67.0\%$ under these assumptions, despite each mean lifetime being much longer than the mission. MTTF is a mean, not a guarantee.

**Example 2 — redundancy and repair.** Two independent active channels have mission reliabilities $0.90$ and $0.80$. Their parallel reliability is $1-(0.10)(0.20)=0.98$; if both were required, it would instead be $0.72$. Separately, suppose a repairable unit averages $500\ \mathrm h$ operating time and $5\ \mathrm h$ corrective repair time. Its inherent availability is $500/505=0.990099$, or $99.0099\%$. This availability does not mean a $500\ \mathrm h$ uninterrupted mission has $99\%$ reliability; interruptions and restoration answer a different question.

### Exercises

1. Find exponential-model reliability at $200\ \mathrm h$ for $\lambda=0.001\ \mathrm{h^{-1}}$.
2. For a Weibull shape $\beta=2$, does hazard rise, fall, or remain constant with age?
3. A plant logs $900\ \mathrm h$ operating and $100\ \mathrm h$ down. Find observed availability. Can this alone determine the failure-time distribution?

### Solutions

1. $R=e^{-0.2}=0.818731$.
2. $h(t)=2t/\eta^2$, so hazard rises linearly with age. This is compatible with a wear-out trend within the fitted model.
3. Availability is $900/(900+100)=0.90$. The aggregate totals do not identify the number, timing, or causes of failures, so they cannot determine a lifetime distribution.

### Common mistakes

- Calling MTTF the guaranteed service life.
- Multiplying reliabilities while ignoring common-cause failures.
- Using “MTBF” without stating whether downtime is included.
- Fitting only failed units and discarding censored survivors.
- Treating a failure-mode ranking number as a calibrated probability.

### Applications and limits

Use reliability models to plan tests, spares, redundancy, and maintenance, while recording the evidence behind model parameters. Failure-mode analysis helps identify mechanisms and effects; numerical life models quantify only mechanisms represented by their data and assumptions. Low-probability high-consequence events may require constraints beyond minimum expected cost. The worked values are illustrative, not equipment reliability claims.

### Further reading

- [NIST/SEMATECH — Reliability handbook](https://www.itl.nist.gov/div898/handbook/apr/apr.htm): lifetime distributions, censored data, and reliability analysis.
- [NIST — Exponential lifetime model](https://itl.nist.gov/div898/handbook/apr/section1/apr161.htm): constant-hazard formulas and use conditions.


---

## 32. Engineering Economics

### Learning map

Prerequisites: algebra, geometric series, estimation, and uncertainty. Engineering economics compares alternatives that deliver a defined function over a stated study period. Learn to draw a cash-flow timeline, apply a consistent discount rate, and include installation, operation, maintenance, replacement, and disposal. These are educational calculations with hypothetical inputs; current quotations, taxes, financing, and local rules must be established for an actual investment.

### Theory

Money at different dates cannot be added directly when time value is relevant. Discounting converts future amounts to a common date using an assumed rate. The rate expresses the chosen economic basis; it is not a universal physical constant. A comparison should state currency, price date, timing convention, analysis period, and whether values are nominal or real.

Nominal cash flows include inflation. Real cash flows are expressed in constant purchasing-power terms. Use a nominal discount rate with nominal flows and a real discount rate with real flows. Mixing them silently can reverse an investment decision. Individual cost categories may also escalate differently from general inflation, especially energy, labor, and replacement parts.

Net present value compares discounted benefits with discounted costs. For mutually exclusive alternatives with equivalent required performance, compare consistent present worth or equivalent annual cost. An efficient machine can justify higher initial cost when operating savings are large enough, but the outcome depends on duty hours, energy price, maintenance, useful life, and the discount rate.

Simple payback is easy to communicate but ignores cash flows after payback and usually ignores time value. Internal rate of return is the rate that makes net present value zero. Cash flows with multiple sign changes can have multiple internal rates or no useful unique one. Incremental comparison and net present value are often clearer for mutually exclusive engineering alternatives.

Life-cycle costing extends the boundary beyond purchase price. Include engineering, site preparation, installation, commissioning, consumables, energy, maintenance, downtime, replacement, and end-of-life cost or salvage where relevant. Costs already incurred and unrecoverable are sunk; they should not be treated as avoidable future costs. Opportunity cost, however, can be real even without a new invoice.

Uncertainty deserves explicit sensitivity analysis. Test several plausible duty hours, service lives, and cost trajectories. A single precise net present value from uncertain assumptions can be less informative than a range and a break-even condition. NIST's life-cycle costing handbook gives a detailed public methodology; jurisdiction-specific assumptions should be obtained from the relevant current program.

### Formula handbook

Let $P$ be present value, $F$ future value, $A$ uniform end-of-period amount, $i$ effective discount rate per period, and $n$ number of periods. Currency units are arbitrary but must be consistent.

**Single amount:**

$$
F=P(1+i)^n,\qquad P=\frac F{(1+i)^n}.
$$

**Uniform series present worth, $i\ne0$:**

$$
P=A\frac{1-(1+i)^{-n}}i.
$$

**Capital recovery factor and annual equivalent:**

$$
\mathrm{CRF}=\frac{i(1+i)^n}{(1+i)^n-1},\qquad A=P\,\mathrm{CRF}.
$$

**Sinking-fund factor:**

$$
A=F\frac i{(1+i)^n-1}.
$$

At $i=0$, use limiting values $P=nA$ and $A=P/n$, avoiding division by zero. **Net present value:**

$$
\mathrm{NPV}=\sum_{t=0}^{n}\frac{CF_t}{(1+i)^t}.
$$

Positive $CF_t$ is net receipt; an initial investment is usually negative. **Equivalent annual cost with initial cost $C_0$, annual operating cost $C_a$, and terminal salvage $S$:**

$$
\mathrm{EAC}=C_0\mathrm{CRF}+C_a-S\frac i{(1+i)^n-1}.
$$

**Nominal-real rate consistency with general inflation $f$:**

$$
1+i_{\rm nominal}=(1+i_{\rm real})(1+f).
$$

**Simple payback for constant positive annual net savings $B$:**

$$
t_{\rm payback}=C_0/B.
$$

**Annual electrical energy and cost:**

$$
E_{\rm annual}=P_{\rm kW}h_{\rm annual},\qquad C_E=E_{\rm annual}c_E.
$$

$E$ is in kWh, $h$ hours/year, and $c_E$ currency/kWh. **Break-even production quantity:**

$$
Q_{\rm BE}=\frac{C_{F,2}-C_{F,1}}{c_{V,1}-c_{V,2}}.
$$

Fixed costs $C_F$ and variable costs $c_V$ must refer to the same period and output basis; the denominator must be nonzero. **Internal rate of return:**

$$
0=\sum_{t=0}^n\frac{CF_t}{(1+i_{\rm IRR})^t}.
$$

Finding a root does not guarantee it is unique or the correct comparison metric.

### Derivation

A uniform end-of-year saving $A$ for $n$ years has present value $P=A[(1+i)^{-1}+(1+i)^{-2}+\cdots+(1+i)^{-n}]$. This is a geometric series with ratio $(1+i)^{-1}$. Summing it gives $P=A[1-(1+i)^{-n}]/i$. Inverting this factor gives the capital recovery factor. The derivation reveals the timing assumption: if payments occur at the beginning of each year, each is discounted one fewer period and the present value is multiplied by $(1+i)$. Payment timing is therefore part of the model, not an administrative detail.

### Worked examples

**Example 1 — hypothetical efficiency upgrade.** An upgrade costs $1{,}000{,}000$ yen now and saves $300{,}000$ yen at the end of each year for five years. Assume a real discount rate of $5\%$, constant real savings, and no salvage or other cost. The annuity factor is $[1-1.05^{-5}]/0.05=4.329477$. Present value of savings is $1{,}298{,}843$ yen, so NPV is $+298{,}843$ yen. Simple payback is $1{,}000{,}000/300{,}000=3.3333$ years. Positive NPV follows only for the stated hypothetical assumptions; changing service life or annual savings changes the result.

**Example 2 — equivalent annual equipment cost.** Equipment costs $2{,}000{,}000$ yen, incurs $100{,}000$ yen per year in operation, lasts ten years, and has $200{,}000$ yen terminal salvage. At $5\%$, CRF is $0.129504575$ and the sinking-fund factor is $0.079504575$. Equivalent annual cost is $2{,}000{,}000(0.129504575)+100{,}000-200{,}000(0.079504575)=343{,}108$ yen/year. An alternative should be compared on equal service, life-cycle boundary, and economic basis, not simply against its purchase price.

### Exercises

1. Find the present value of $100{,}000$ yen received in two years at $5\%$ per year.
2. A pump reduces input by $2\ \mathrm{kW}$ for $4000\ \mathrm h/year$. At an assumed price of $20$ yen/kWh, find annual energy and cost savings.
3. Two manufacturing options have fixed costs of $100{,}000$ and $300{,}000$ currency units, with variable costs $10$ and $6$ per part. Find break-even quantity.

### Solutions

1. $P=100000/1.05^2=90{,}702.95$ yen.
2. Energy saving is $8000\ \mathrm{kWh/year}$ and cost saving is $160{,}000$ yen/year. The price is a hypothetical input, not a current tariff claim.
3. $Q_{\rm BE}=(300000-100000)/(10-6)=50{,}000$ parts. Below that quantity option 1 has lower modeled total cost; above it option 2 does, assuming equal acceptable quality and no other differences.

### Common mistakes

- Mixing nominal cash flows with a real discount rate.
- Omitting maintenance, installation, or downtime because purchase prices are easier to obtain.
- Comparing alternatives with different capacity or useful life without adjustment.
- Treating payback as a complete profitability measure.
- Ignoring uncertainty while reporting results to the nearest currency unit.

### Applications and limits

Apply these methods to equipment replacement, energy projects, make-or-buy choices, maintenance policies, and production methods. Record quotations and measured duty as evidence separately from assumptions. For actual financial, tax, or procurement decisions, use current local requirements and qualified review. The calculations here explain time value and engineering tradeoffs; they do not predict investment returns.

### Further reading

- [NIST — Life Cycle Costing Manual for the Federal Energy Management Program](https://www.nist.gov/publications/life-cycle-costing-manual-federal-energy-management-program-0): detailed methodology and a specific published edition.
- [U.S. Department of Energy — Building Life Cycle Cost Programs](https://www.energy.gov/cmei/femp/building-life-cycle-cost-programs): tools, handbook links, and current program resources; program rates are not universal rates.


---

## 33. Energy Systems and Environmental Accounting

### Learning map

Prerequisites: thermodynamics, fluid mechanics, heat transfer, electrical power, and engineering economics. Start with the service required, such as a volume of water pumped to a stated head, a comfortable occupied space, or a quantity of product. Then trace energy sources, conversions, losses, and environmental consequences. Comparing equipment on equal useful service prevents misleading conclusions from efficiency figures alone.

### Theory

Energy is conserved, but its usefulness for producing work depends on its form and surroundings. Electricity and shaft work can be converted extensively into other forms, while low-temperature heat has limited work potential. Efficiency measures useful output divided by input under a defined boundary. A heat pump can have a heating coefficient of performance above one because it transfers environmental heat in addition to consuming work; this does not violate energy conservation.

An energy system is a chain. Generation, conversion, transmission, storage, and end-use losses all influence the service delivered. Improving one device may have a smaller total benefit than expected if another part of the chain dominates losses. Conversely, reducing demand can avoid losses at several upstream stages. For pumps and fans, the actual operating point and control strategy can matter more than a nominal peak efficiency.

Renewable resources vary over time. A wind turbine's instantaneous power depends strongly on wind speed, but annual energy depends on the full speed distribution, turbine power curve, availability, and losses. Applying a cubic power relation to the annual mean wind speed generally does not produce annual mean power. Solar output depends on irradiance, module temperature, orientation, shading, and electrical losses. Capacity factor summarizes annual energy relative to continuous rated operation; it is not the same as conversion efficiency.

Environmental accounting requires a functional unit and system boundary. “Per kilowatt-hour delivered” differs from “per device manufactured” or “per year operated.” Include appropriate upstream material and energy impacts, operation, replacements, and end-of-life processes. An emission factor can depend on location, year, technology, and accounting purpose. An average grid factor and a marginal factor answer different questions; neither should be substituted without explanation.

Energy and carbon are related but not interchangeable. A lower-energy process may use a higher-emission fuel, while a lower-emission electricity supply may have different resource or land impacts. Water use, air pollutants, waste, biodiversity, and material depletion also matter. A single aggregate metric is useful only when its boundary and limitations remain visible.

### Formula handbook

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

### Derivation

During time $dt$, uniform wind carries a mass $dm=\rho A U\,dt$ through area $A$. Its kinetic energy is $dE=\frac12dm\,U^2$. Dividing by $dt$ gives $P_{\rm wind}=\frac12\rho A U^3$. The turbine cannot extract all of that power while maintaining steady flow through the rotor; deceleration changes the streamtube and downstream kinetic energy. The power coefficient represents the extracted fraction under a defined rotor model or measured operating condition. Electrical output requires additional drivetrain and generator efficiency factors unless they are already included in the stated coefficient.

### Worked examples

**Example 1 — wind output at one operating point.** Take $\rho=1.2\ \mathrm{kg/m^3}$, rotor area $A=10\ \mathrm{m^2}$, and uniform wind $U=8\ \mathrm{m/s}$. Available kinetic power is $0.5(1.2)(10)(8^3)=3072\ \mathrm W$. Assume aerodynamic power coefficient $C_P=0.40$ and drivetrain/generator efficiency $0.90$. Shaft power is $1228.8\ \mathrm W$, and electrical power is $1105.92\ \mathrm W$. These assumed values describe one operating point. Annual energy cannot be calculated from it without the time distribution and machine operating limits.

**Example 2 — pump energy and emissions.** Two alternatives provide the same measured hydraulic service. The first draws $10\ \mathrm{kW}$ and the second $8\ \mathrm{kW}$ for $4000\ \mathrm h/year$. Annual electrical saving is $(10-8)(4000)=8000\ \mathrm{kWh}=28.8\ \mathrm{GJ}$. With an explicitly hypothetical emission factor of $0.40\ \mathrm{kg\ CO_2e/kWh}$, avoided operational emissions are $3200\ \mathrm{kg\ CO_2e/year}$. If producing the replacement causes an assumed additional $1600\ \mathrm{kg\ CO_2e}$, a simple undiscounted carbon payback is $1600/3200=0.50$ years. This excludes changes in grid factors, performance, maintenance, and disposal.

### Exercises

1. A $2\ \mathrm{kW}$ device runs for three hours. Express its energy in kWh and MJ.
2. A $5\ \mathrm{kW}$ generator produces $8760\ \mathrm{kWh}$ in a 365-day year. Find capacity factor.
3. A collector receives $800\ \mathrm{W/m^2}$ over $2\ \mathrm{m^2}$ and delivers $960\ \mathrm W$ of useful heat. Find thermal efficiency at that condition.

### Solutions

1. Energy is $6\ \mathrm{kWh}$, or $6(3.6)=21.6\ \mathrm{MJ}$.
2. Rated annual energy is $5(8760)=43800\ \mathrm{kWh}$. Capacity factor is $8760/43800=0.20$, or $20\%$.
3. Incident power is $1600\ \mathrm W$. Efficiency is $960/1600=0.60$, or $60\%$. This does not specify performance at another ambient or fluid temperature.

### Common mistakes

- Treating kW as an energy unit or kWh as a power unit.
- Calling capacity factor an efficiency.
- Using one generic emissions factor without date, location, and accounting purpose.
- Comparing alternatives that deliver different amounts or qualities of useful service.
- Applying average wind speed to a cubic relation as if it gave average power.

### Applications and limits

Use these balances for plant audits, pumping systems, thermal retrofits, renewable-energy screening, and life-cycle comparisons. Measure power and duty where possible. Separate direct measurements, manufacturer data, modeled estimates, and hypothetical assumptions in reports. Environmental decisions require a broader assessment when impacts shift between stages or categories. The numerical examples teach calculation structure, not a site-specific sustainability claim.

### Further reading

- [U.S. Department of Energy — Small Wind Guidebook](https://www.energy.gov/cmei/systems/windexchange/small-wind-guidebook): resource, turbine, and system context.
- [National laboratory — comparative PV LCOE documentation](https://nrel.sitefinity.cloud/pv/lcoe-calculator/documentation): explicit cost and energy accounting definitions.
- [U.S. Department of Energy — life-cycle cost resources](https://www.energy.gov/cmei/femp/building-life-cycle-cost-programs): economic evaluation of energy and water projects.


---

## 35 · Systems engineering and integrated design

### Learning map

This chapter combines the preceding subjects into a traceable engineering process. Prerequisites are basic mechanics, fluid and thermal balances, reliability, and economics. The aim is to turn a need into requirements, architecture, analyses, tests, and an operating system whose interfaces and limitations are understood.

### Theory

A system is a set of interacting elements considered within a defined boundary and environment. The same pump may be a component in a water-treatment plant and a system when analysing its motor, impeller, bearings, seals, and controller. Choosing the boundary determines which flows and interactions must be modelled explicitly. System performance is not generally the sum of isolated component ratings.

A stakeholder need expresses the desired outcome. A requirement converts part of that outcome into a testable constraint under stated conditions. “The skid shall be efficient” cannot be verified without a metric and operating condition. “At 0.003 m³/s and 20 m total head, measured electrical input shall not exceed 1.2 kW under the stated water temperature and supply conditions” can be tested, although the value must first be justified.

Architecture assigns functions to elements and defines interfaces. A mechanical interface includes loads, alignment, dimensions, tolerances, support, and access. A fluid interface includes flow, pressure, temperature, composition, cleanliness, and allowable transients. An electrical interface includes voltage, current, grounding, isolation, and protection. A control interface includes signals, timing, units, failure states, and authority. Most integration problems occur at these boundaries rather than inside a single discipline's idealized calculation.

Verification establishes whether a specified requirement has been met through test, analysis, inspection, or demonstration. Validation establishes whether the delivered system meets its intended use in the relevant environment. A correctly built pump skid may still fail to meet the user's operational need if maintenance is impractical or the expected water contains unmodelled solids. Both questions should influence planning before fabrication.

Budgets allocate limited resources such as mass, power, heat rejection, cost, and time. A margin is a quantified allowance under a stated convention, not a vague feeling of safety. Risk combines uncertain outcomes with consequences, but multiplying ordinal labels such as “low, medium, high” does not create a calibrated probability. Fault analysis should distinguish independent failures, shared causes, and failure propagation.

Configuration control records which requirements, drawings, code, models, and parts belong to a particular version. An accurate calculation attached to an obsolete drawing is not usable evidence. Traceability connects each requirement to its source, implementing element, analysis, and verification evidence. This can be maintained with a simple table for a small project; complexity should support decisions rather than conceal them.

### Formula handbook

1. A conserved quantity satisfies accumulation = inflow − outflow + generation − consumption. Mass has no generation term in ordinary non-nuclear equipment balances.
2. A scalar resource budget is $B_{\mathrm{total}}=\sum_iB_i+B_{\mathrm{shared}}$, provided items do not overlap.
3. Under the convention used here, capacity margin is $m=(C-D)/D$, where capacity $C$ and demand $D>0$ have matching units. Another project may divide by capacity; always state the convention.
4. For a multiplicative chain, total efficiency is $\eta_{\mathrm{total}}=\prod_i\eta_i$, if each stage's useful output is the next stage's input.
5. Steady pump electrical demand is $P_e=\rho gQH/(\eta_p\eta_m\eta_d)$, with pump, motor, and drive efficiencies stated separately.
6. An illustrative system curve is $H_s(Q)=H_0+kQ^2$, with $k$ in s²/m⁵ when $Q$ is in m³/s and head in m. It assumes a compatible fixed configuration and approximately quadratic losses.
7. The operating point satisfies $H_p(Q)=H_s(Q)$. A root must lie within physically permissible pump and system ranges.
8. Local sensitivity: $\Delta y\approx\sum_i(\partial f/\partial x_i)\Delta x_i$ for small perturbations to $y=f(\mathbf x)$.
9. Independent series reliability: $R_{\mathrm{sys}}=\prod_iR_i$ for elements all required to succeed over the same mission.
10. Independent parallel success: $R_{\mathrm{sys}}=1-\prod_i(1-R_i)$ only when any one element suffices and switching/supporting functions are properly accounted for.
11. Expected monetary loss is $E[L]=\sum_i p_iL_i$ for mutually exclusive scenarios covering the modelled outcomes, with calibrated probabilities $p_i$ and losses in a common currency/date basis.
12. For a finish-to-start activity network without resource constraints, earliest finish is $EF_i=\max_{j\in\mathrm{pred}(i)}EF_j+d_i$. Start activities use earliest start zero. Duration $d_i$ and finish times use the same time unit.

These equations assist decisions; none replaces the judgement needed to define requirements, identify credible failure modes, or decide whether evidence is sufficient.

### Derivation

Suppose pump head is approximated by $H_p=a-bQ^2$, with positive constants over a limited operating interval, and the system head is $H_s=H_0+kQ^2$. Equal head at a steady operating point gives $a-H_0=(b+k)Q^2$. Therefore

$$
Q=\sqrt{\frac{a-H_0}{b+k}}
$$

for a positive-flow solution when $a>H_0$ and $b+k>0$. If $a\leq H_0$, this approximation gives no positive delivery against the static head. Adding a valve increases $k$ and lowers the flow for an unchanged pump curve. Changing pump speed shifts the pump curve, so the same algebra must be repeated with the new characteristic. This illustrates why a component nameplate cannot determine the integrated operating condition by itself.

### Worked examples

#### Example 1: Pump and system interaction

Let $H_p=30-200000Q^2$ m and $H_s=10+300000Q^2$ m, with $Q$ in m³/s. Equating gives $Q^2=20/500000=4\times10^{-5}$, so $Q=0.00632456\ \mathrm{m^3/s}$, or 6.325 L/s. Either curve gives $H=22$ m. With water density 1000 kg/m³, $g=9.81$ m/s², and total efficiency 0.70, electrical power is $P=1000(9.81)(0.00632456)(22)/0.70=1.950\ \mathrm{kW}$. The assumed curves say nothing about NPSH, allowable operating range, solids, or transient pressures; those are separate interface checks.

#### Example 2: A schedule dependency

Activity A, requirements, takes 2 days. B, layout, takes 3 days after A. C, procurement definition, takes 4 days after A. D, integration review, takes 2 days after both B and C. Earliest finish times are A = 2, B = 5, C = 6, and D = $\max(5,6)+2=8$ days. Path A–C–D is critical at 8 days; A–B–D is 7 days. Shortening B by one day alone does not shorten project completion. Resource competition or calendar restrictions would require a more detailed schedule.

### Exercises

1. A motor is 90% efficient and a pump is 70% efficient. What electrical input supports 1 kW of hydraulic output, neglecting other losses?
2. Demand is 80 kg and capacity is 100 kg. Compute capacity margin using this chapter's definition.
3. Two independent required components have mission reliabilities 0.98 and 0.99. Compute series reliability and explain one reason the model might fail.

### Solutions

1. Total efficiency is $0.90(0.70)=0.63$. Required input is $1/0.63=1.587$ kW. Adding efficiencies would have no physical meaning.
2. $m=(100-80)/80=0.25$, or 25%. Relative unused capacity would instead be 20%; state the denominator to avoid ambiguity.
3. $R=0.98(0.99)=0.9702$. A shared power supply, common contamination, or common environmental overload could violate independence and change the result.

### Common mistakes

Optimizing one component while ignoring its interfaces can worsen system performance. Adding several margins without tracking their purpose can create an oversized design; removing them without evidence can erase necessary allowances. Do not equate a completed checklist with validation or treat an untested model as an acceptance test. Requirements should specify conditions, thresholds, and verification methods before results are known.

### Applications and limits

For a small water skid, maintain a requirements table, P&ID, layout, calculation sheet, component list, interface list, operating sequence, failure response, and verification record. Review them as one configuration. The integrated capstone in this repository applies this process to a hypothetical pumping system. Its educational values are deliberately stated so they cannot be mistaken for an approved construction design.

### Further reading

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — publisher-hosted handbook and process guidance.
- [MIT OCW, Design of Electromechanical Robotic Systems](https://ocw.mit.edu/courses/2-017j-design-of-electromechanical-robotic-systems-fall-2009/) — a project course connecting electromechanical architecture, analysis, and implementation, with an open textbook on design for uncertainty.
