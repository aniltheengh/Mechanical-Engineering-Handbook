# 32. Engineering Economics

## Learning map

Prerequisites: algebra, geometric series, estimation, and uncertainty. Engineering economics compares alternatives that deliver a defined function over a stated study period. Learn to draw a cash-flow timeline, apply a consistent discount rate, and include installation, operation, maintenance, replacement, and disposal. These are educational calculations with hypothetical inputs; current quotations, taxes, financing, and local rules must be established for an actual investment.

## Theory

Money at different dates cannot be added directly when time value is relevant. Discounting converts future amounts to a common date using an assumed rate. The rate expresses the chosen economic basis; it is not a universal physical constant. A comparison should state currency, price date, timing convention, analysis period, and whether values are nominal or real.

Nominal cash flows include inflation. Real cash flows are expressed in constant purchasing-power terms. Use a nominal discount rate with nominal flows and a real discount rate with real flows. Mixing them silently can reverse an investment decision. Individual cost categories may also escalate differently from general inflation, especially energy, labor, and replacement parts.

Net present value compares discounted benefits with discounted costs. For mutually exclusive alternatives with equivalent required performance, compare consistent present worth or equivalent annual cost. An efficient machine can justify higher initial cost when operating savings are large enough, but the outcome depends on duty hours, energy price, maintenance, useful life, and the discount rate.

Simple payback is easy to communicate but ignores cash flows after payback and usually ignores time value. Internal rate of return is the rate that makes net present value zero. Cash flows with multiple sign changes can have multiple internal rates or no useful unique one. Incremental comparison and net present value are often clearer for mutually exclusive engineering alternatives.

Life-cycle costing extends the boundary beyond purchase price. Include engineering, site preparation, installation, commissioning, consumables, energy, maintenance, downtime, replacement, and end-of-life cost or salvage where relevant. Costs already incurred and unrecoverable are sunk; they should not be treated as avoidable future costs. Opportunity cost, however, can be real even without a new invoice.

Uncertainty deserves explicit sensitivity analysis. Test several plausible duty hours, service lives, and cost trajectories. A single precise net present value from uncertain assumptions can be less informative than a range and a break-even condition. NIST's life-cycle costing handbook gives a detailed public methodology; jurisdiction-specific assumptions should be obtained from the relevant current program.

## Formula handbook

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

## Derivation

A uniform end-of-year saving $A$ for $n$ years has present value $P=A[(1+i)^{-1}+(1+i)^{-2}+\cdots+(1+i)^{-n}]$. This is a geometric series with ratio $(1+i)^{-1}$. Summing it gives $P=A[1-(1+i)^{-n}]/i$. Inverting this factor gives the capital recovery factor. The derivation reveals the timing assumption: if payments occur at the beginning of each year, each is discounted one fewer period and the present value is multiplied by $(1+i)$. Payment timing is therefore part of the model, not an administrative detail.

## Worked examples

**Example 1 — hypothetical efficiency upgrade.** An upgrade costs $1{,}000{,}000$ yen now and saves $300{,}000$ yen at the end of each year for five years. Assume a real discount rate of $5\%$, constant real savings, and no salvage or other cost. The annuity factor is $[1-1.05^{-5}]/0.05=4.329477$. Present value of savings is $1{,}298{,}843$ yen, so NPV is $+298{,}843$ yen. Simple payback is $1{,}000{,}000/300{,}000=3.3333$ years. Positive NPV follows only for the stated hypothetical assumptions; changing service life or annual savings changes the result.

**Example 2 — equivalent annual equipment cost.** Equipment costs $2{,}000{,}000$ yen, incurs $100{,}000$ yen per year in operation, lasts ten years, and has $200{,}000$ yen terminal salvage. At $5\%$, CRF is $0.129504575$ and the sinking-fund factor is $0.079504575$. Equivalent annual cost is $2{,}000{,}000(0.129504575)+100{,}000-200{,}000(0.079504575)=343{,}108$ yen/year. An alternative should be compared on equal service, life-cycle boundary, and economic basis, not simply against its purchase price.

## Exercises

1. Find the present value of $100{,}000$ yen received in two years at $5\%$ per year.
2. A pump reduces input by $2\ \mathrm{kW}$ for $4000\ \mathrm h/year$. At an assumed price of $20$ yen/kWh, find annual energy and cost savings.
3. Two manufacturing options have fixed costs of $100{,}000$ and $300{,}000$ currency units, with variable costs $10$ and $6$ per part. Find break-even quantity.

## Solutions

1. $P=100000/1.05^2=90{,}702.95$ yen.
2. Energy saving is $8000\ \mathrm{kWh/year}$ and cost saving is $160{,}000$ yen/year. The price is a hypothetical input, not a current tariff claim.
3. $Q_{\rm BE}=(300000-100000)/(10-6)=50{,}000$ parts. Below that quantity option 1 has lower modeled total cost; above it option 2 does, assuming equal acceptable quality and no other differences.

## Common mistakes

- Mixing nominal cash flows with a real discount rate.
- Omitting maintenance, installation, or downtime because purchase prices are easier to obtain.
- Comparing alternatives with different capacity or useful life without adjustment.
- Treating payback as a complete profitability measure.
- Ignoring uncertainty while reporting results to the nearest currency unit.

## Applications and limits

Apply these methods to equipment replacement, energy projects, make-or-buy choices, maintenance policies, and production methods. Record quotations and measured duty as evidence separately from assumptions. For actual financial, tax, or procurement decisions, use current local requirements and qualified review. The calculations here explain time value and engineering tradeoffs; they do not predict investment returns.

## Further reading

- [NIST — Life Cycle Costing Manual for the Federal Energy Management Program](https://www.nist.gov/publications/life-cycle-costing-manual-federal-energy-management-program-0): detailed methodology and a specific published edition.
- [U.S. Department of Energy — Building Life Cycle Cost Programs](https://www.energy.gov/cmei/femp/building-life-cycle-cost-programs): tools, handbook links, and current program resources; program rates are not universal rates.
