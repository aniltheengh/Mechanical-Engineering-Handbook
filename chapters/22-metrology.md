# 22. Metrology, uncertainty, and quality

## Learning map

Prerequisites: units, statistics, geometry, and manufacturing. Define the measurand, construct a measurement model, identify uncertainty contributions, and report a result with its uncertainty. Then distinguish measurement-system capability from manufacturing-process capability. Learn dimensional measurement before applying the same reasoning to temperature, force, flow, pressure, and vibration.

## Theory

A measurement is a comparison that assigns a quantity value to a defined measurand. The measurand must be precise: diameter at which location, at what temperature, under what contact force, and using which definition of size? A result without these conditions can be ambiguous. Calibration establishes relationships to reference values with associated uncertainty; it does not make an instrument error-free.

Accuracy describes closeness to an appropriate reference, precision describes agreement among repeated results, and resolution is the smallest indicated increment. These concepts are not interchangeable. Repeatable readings can share a large bias. A display with many digits may have poor accuracy. Corrections remove estimated systematic effects; uncertainty remains because the correction and input quantities are imperfectly known.

Type A uncertainty evaluation uses statistical analysis of observations. Type B evaluation uses other evidence such as calibration certificates, specifications, physical knowledge, or prior data. These labels describe evaluation methods, not a simple random-versus-systematic division. Correlated input quantities require covariance terms. A common calibration error does not average away when the same instrument is read repeatedly.

Dimensional measurements are sensitive to temperature, alignment, cosine error, Abbe offset, contact deformation, surface texture, and fixturing. A datum establishes a reference for a geometric specification; a convenient best-fit coordinate system is not automatically the specified datum system. Inspection methods should implement the drawing's functional definition rather than measure a visually similar substitute.

Process capability compares a stable process distribution to specification limits. Control limits describe observed process variation, while specification limits describe requirements. A process can be statistically stable and still produce unacceptable parts. Capability indices assume the distribution and sampling model are appropriate; small samples, autocorrelation, mixed machines, and process shifts can make a single index misleading.

## Formula handbook

**1. Sample mean and sample standard deviation**, $n>1$ observations:

$$
\bar x=\frac1n\sum x_i,\qquad s=\sqrt{\frac{\sum(x_i-\bar x)^2}{n-1}}.
$$

**2. Standard uncertainty of an independent-observation mean**:

$$
u_A(\bar x)=\frac{s}{\sqrt n}.
$$

Autocorrelated readings require a different effective information model.

**3. Rectangular distribution**, half-width $a$ around its center:

$$
u=a/\sqrt3.
$$

**4. Digital rounding resolution**, increment $q$ and uniform rounding error:

$$
u_{\mathrm{res}}=q/\sqrt{12}.
$$

**5. Linearized combined uncertainty**, $y=f(x_1,\ldots,x_n)$:

$$
u_c^2(y)=\sum_i c_i^2u^2(x_i)+2\sum_{i<j}c_ic_j\operatorname{cov}(x_i,x_j),\qquad c_i=\frac{\partial f}{\partial x_i}.
$$

Sensitivity coefficients carry the units needed to convert each input contribution into output units.

**6. Expanded uncertainty**:

$$
U=ku_c.
$$

Coverage factor $k$ is not automatically 2; distribution, effective degrees of freedom, and desired coverage matter. NIST explains the evaluation and reporting framework in [Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297).

**7. First-order thermal length correction**, constant expansion coefficient $\alpha_T$:

$$
L(T)\approx L(T_0)[1+\alpha_T(T-T_0)].
$$

**8. Abbe offset error**, offset $h$ and small angular error $\theta$:

$$
e_A=h\tan\theta\approx h\theta.
$$

Use radians in the small-angle approximation.

**9. Cosine projection error**, projected length $L_m=L\cos\theta$:

$$
e_C=L_m-L=L(\cos\theta-1)\approx-\tfrac12L\theta^2.
$$

**10. Process potential capability**, normal stable distribution with standard deviation $\sigma$:

$$
C_p=\frac{USL-LSL}{6\sigma}.
$$

**11. Centering-sensitive capability**:

$$
C_{pk}=\min\left(\frac{USL-\mu}{3\sigma},\frac{\mu-LSL}{3\sigma}\right).
$$

**12. Arithmetic mean roughness**, over the defined evaluation length after the required filtering:

$$
R_a=\frac1L\int_0^L|z(x)|\,dx.
$$

Roughness depends on measurement direction, filtering, and evaluation conventions; a single number does not describe all surface functionality.

## Derivation

For small input deviations, a first-order Taylor expansion gives $\Delta y\approx\sum c_i\Delta x_i$. Square and take the expected value. Individual squared terms yield $c_i^2u_i^2$, while cross terms yield $2c_ic_j\operatorname{cov}(x_i,x_j)$. Independent inputs have zero covariance, producing root-sum-square combination. If two inputs share the same calibration bias, deleting the cross term can understate uncertainty. Strong nonlinearity may require higher-order treatment or numerical propagation.

## Worked examples

### Example 1: Length uncertainty budget

Five independent readings in mm are 10.01, 10.00, 9.99, 10.02, and 9.98. Their mean is 10.000 mm and sample standard deviation is 0.0158114 mm, giving $u_A=0.00707107$ mm. Add independent calibration uncertainty $U_{cal}=0.008$ mm with certificate factor 2, so $u_{cal}=0.004$ mm. Treat resolution $q=0.01$ mm as an additional contribution not already represented in the repeatability term: $u_{res}=0.00288675$ mm. Then $u_c=\sqrt{0.00707107^2+0.004^2+0.00288675^2}=0.00862168$ mm and $U=2u_c=0.0172434$ mm. A concise report is $(10.000\pm0.017)$ mm with $k=2$, the stated model, and no claim of exact 95% coverage from this small sample. In a real budget, assess resolution double-counting explicitly.

### Example 2: Capability and centering

A stable approximately normal process has specification limits 9.950 and 10.050 mm, mean 10.020 mm, and known process standard deviation 0.010 mm. $C_p=0.100/[6(0.010)]=1.6667$. Upper capability is $(10.050-10.020)/0.030=1.000$; lower capability is $(10.020-9.950)/0.030=2.3333$. Therefore $C_{pk}=1.000$. Recentering to 10.000 mm would improve $C_{pk}$ to 1.6667 without changing spread, provided the process remains stable.

## Exercises

1. A digital instrument has resolution 0.02 mm. Find standard uncertainty from uniform rounding alone.
2. An Abbe offset is 100 mm and angular error is 0.001 rad. Estimate the resulting length error.
3. Two independent standard uncertainties are 3 and 4 micrometres with unit sensitivity coefficients. Find combined and $k=2$ expanded uncertainty.

## Solutions

1. $u=0.02/\sqrt{12}=0.0057735$ mm. Resolution is an increment, so its half-width is 0.01 mm.
2. $e_A\approx100(0.001)=0.100$ mm. Reducing offset directly reduces this error source.
3. Combined uncertainty is $\sqrt{3^2+4^2}=5$ micrometres; expanded uncertainty is 10 micrometres. Correlation would change the first result.

## Common mistakes

- Reporting display resolution as total measurement uncertainty.
- Dividing a shared systematic calibration contribution by $\sqrt n$.
- Combining expanded uncertainties without first accounting for their coverage factors.
- Treating a capability index as proof of process stability.
- Ignoring the decision rule when measurement uncertainty overlaps a specification limit.

## Applications and limits

Use uncertainty budgets to identify which improvement matters: better calibration, alignment, environment, fixturing, or repeatability. For conformity decisions, agree on a decision rule and any guard band before judging marginal results. Traceability is a documented chain of calibrations with uncertainties, not simply ownership of a calibrated instrument. Measurement quality depends on the complete procedure and its execution.

## Further reading

- [NIST: Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297) — uncertainty evaluation and expression.
- [NIST: Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — measurement models and computational resources.
- [NIST: Fundamentals of Geometric Dimensioning and Tolerancing, Part II](https://www.nist.gov/publications/fundamentals-geometric-dimensioning-and-tolerancing-part-ii) — geometric product definition. These resources are linked, not reproduced.
