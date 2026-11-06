# 31. Reliability and Maintenance

## Learning map

Prerequisites: probability, statistics, materials, fatigue, and machine operation. Reliability is the probability of performing a defined function for a stated duration under stated conditions. Availability concerns whether a repairable system is operating when required. Maintainability concerns the ability to restore function. These quantities answer different questions and should not be substituted for one another.

## Theory

A reliability statement needs a failure definition, mission duration, operating environment, and population. “The pump is reliable” has little quantitative meaning without specifying flow, head, leakage, duty, fluid, and what counts as failure. A survival model represents a distribution of possible failure times, not a fixed lifetime promised for every component.

The hazard rate is the instantaneous failure rate conditional on survival so far. It differs from the probability density because the surviving population shrinks with time. An exponential lifetime model has constant hazard and is useful only when that assumption is defensible. It does not represent wear-out simply because its mean time to failure is convenient. Weibull models allow increasing or decreasing hazard through a shape parameter, but selecting a flexible distribution does not replace collecting adequate data.

System architecture matters. A series system fails if any required component fails. A parallel redundant system succeeds if at least one of its paths succeeds, provided failures are independent and the architecture can actually use the surviving path. Common-cause failure, switching failures, shared power, shared cooling, and maintenance errors can invalidate a simple independence calculation. Redundancy must be analyzed as a system behavior.

Maintenance strategies include run-to-failure, age-based replacement, condition monitoring, and inspection. The best choice depends on failure consequences, detectability, deterioration behavior, spare availability, and intervention cost. Replacing a constant-hazard item at a fixed age does not automatically lower its subsequent hazard. Conversely, wear-out may justify scheduled replacement if the failure distribution and costs support it.

Failure data require careful treatment. A component still operating when a study ends provides a right-censored observation: its lifetime exceeds the recorded time. Discarding it biases analysis. Downtime, repair duration, waiting for spares, and scheduled maintenance should also be separated according to the metric's definition. The NIST reliability handbook discusses these statistical foundations and estimation methods in depth.

## Formula handbook

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

## Derivation

From $h(t)=f(t)/R(t)$ and $f(t)=-dR/dt$, obtain $dR/dt=-h(t)R(t)$. Separate variables: $dR/R=-h(t)dt$. Integrating from zero with $R(0)=1$ gives $\ln R(t)=-\int_0^th(\tau)d\tau$. Exponentiating yields the survival-hazard relation. For constant $h=\lambda$, this becomes $R=e^{-\lambda t}$, and integration gives $E[T]=1/\lambda$. The model's memoryless property follows from $P(T>s+t\mid T>s)=R(s+t)/R(s)=e^{-\lambda t}$. Surviving longer does not improve or worsen its conditional remaining lifetime under this particular model.

## Worked examples

**Example 1 — mission reliability.** Assume a component has a constant hazard with MTTF $5000\ \mathrm h$. Then $\lambda=0.0002\ \mathrm{h^{-1}}$. For a $1000\ \mathrm h$ mission, reliability is $e^{-0.2}=0.818731$. Two independent such components, both required, have reliability $e^{-0.4}=0.670320$. The system's probability of completing the mission is about $67.0\%$ under these assumptions, despite each mean lifetime being much longer than the mission. MTTF is a mean, not a guarantee.

**Example 2 — redundancy and repair.** Two independent active channels have mission reliabilities $0.90$ and $0.80$. Their parallel reliability is $1-(0.10)(0.20)=0.98$; if both were required, it would instead be $0.72$. Separately, suppose a repairable unit averages $500\ \mathrm h$ operating time and $5\ \mathrm h$ corrective repair time. Its inherent availability is $500/505=0.990099$, or $99.0099\%$. This availability does not mean a $500\ \mathrm h$ uninterrupted mission has $99\%$ reliability; interruptions and restoration answer a different question.

## Exercises

1. Find exponential-model reliability at $200\ \mathrm h$ for $\lambda=0.001\ \mathrm{h^{-1}}$.
2. For a Weibull shape $\beta=2$, does hazard rise, fall, or remain constant with age?
3. A plant logs $900\ \mathrm h$ operating and $100\ \mathrm h$ down. Find observed availability. Can this alone determine the failure-time distribution?

## Solutions

1. $R=e^{-0.2}=0.818731$.
2. $h(t)=2t/\eta^2$, so hazard rises linearly with age. This is compatible with a wear-out trend within the fitted model.
3. Availability is $900/(900+100)=0.90$. The aggregate totals do not identify the number, timing, or causes of failures, so they cannot determine a lifetime distribution.

## Common mistakes

- Calling MTTF the guaranteed service life.
- Multiplying reliabilities while ignoring common-cause failures.
- Using “MTBF” without stating whether downtime is included.
- Fitting only failed units and discarding censored survivors.
- Treating a failure-mode ranking number as a calibrated probability.

## Applications and limits

Use reliability models to plan tests, spares, redundancy, and maintenance, while recording the evidence behind model parameters. Failure-mode analysis helps identify mechanisms and effects; numerical life models quantify only mechanisms represented by their data and assumptions. Low-probability high-consequence events may require constraints beyond minimum expected cost. The worked values are illustrative, not equipment reliability claims.

## Further reading

- [NIST/SEMATECH — Reliability handbook](https://www.itl.nist.gov/div898/handbook/apr/apr.htm): lifetime distributions, censored data, and reliability analysis.
- [NIST — Exponential lifetime model](https://itl.nist.gov/div898/handbook/apr/section1/apr161.htm): constant-hazard formulas and use conditions.
