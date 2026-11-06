# Manufacturing, metrology, and CAD

Mechanical Engineering Handbook · First edition · 2026-11-06

An original, AI-assisted educational reference. Maintained by aniltheengh. See [coverage](../COVERAGE.md), [validation](../VALIDATION.md), and [license](../LICENSE.md).

## Chapters

- [21. Manufacturing processes and production](../chapters/21-manufacturing.md)
- [22. Metrology, uncertainty, and quality](../chapters/22-metrology.md)
- [23. CAD, engineering drawing, and tolerances](../chapters/23-cad-and-engineering-drawing.md)

---

## 21. Manufacturing processes and production

### Learning map

Prerequisites: materials, mechanics, heat transfer, and basic economics. Compare machining, casting, forming, joining, molding, and additive manufacturing through physical mechanism, achievable geometry, quality, production rate, and cost. Learn to estimate a process before choosing equipment. A successful design includes an achievable manufacturing and inspection route.

### Theory

Machining removes material through controlled chip formation. Cutting speed affects temperature and tool wear; feed and depth of cut affect chip load, force, productivity, and surface geometry. Machine power, stiffness, chatter, workholding, chip evacuation, and tool accessibility constrain usable parameters. A catalog cutting speed is a starting point for a specified tool–material combination, not a universal setting.

Casting creates geometry by filling a mold and solidifying material. Shrinkage, feeding, gas entrapment, inclusions, and cooling gradients influence defects and microstructure. Risers should feed shrinkage as solidification proceeds; the thermal modulus $V/A$ helps reason about which regions cool more slowly. Pattern allowances and draft differ from final part dimensions and depend on the process and material.

Forming changes shape through plastic flow. Forging, rolling, extrusion, drawing, and sheet forming trade material utilization and production rate against tooling, load, friction, and ductility constraints. Volume is approximately conserved during plastic deformation of dense metals, while elastic recovery causes springback. Excessive local thinning or tensile strain can produce failure even when overall forming force is available.

Joining includes mechanical fastening, welding, brazing, soldering, and adhesive bonding. Fusion welding produces a heat-affected zone, residual stress, and possible distortion. Joint preparation, access, restraint, sequence, filler, and inspection requirements belong in the process plan. A heat-input estimate alone does not qualify a weld or predict all metallurgical effects.

Additive manufacturing creates parts in successive layers or deposited tracks. It can reduce tooling and enable complex internal geometry, but build orientation, supports, thermal history, porosity, anisotropy, surface finish, and postprocessing influence performance. Printed nominal geometry is not automatically equivalent to wrought material properties. Process selection should compare the complete route, including support removal, heat treatment, machining, and inspection.

### Formula handbook

**1. Turning cutting speed**, diameter $D$ in mm, spindle speed $n$ rpm, and speed $V_c$ m/min:

$$
V_c=\frac{\pi Dn}{1000}.
$$

**2. Turning feed speed and cutting time**, feed $f$ mm/rev and cutting travel $L_c$ mm:

$$
v_f=fn,\qquad t_c=\frac{L_c}{fn}.
$$

$v_f$ is mm/min and $t_c$ min; travel must include required approach and overrun.

**3. Approximate turning removal rate**, radial depth of cut $a_p$ mm:

$$
Q_v\approx1000V_cfa_p.
$$

$Q_v$ is mm³/min; this conventional relation treats surface speed as representative through the cut.

**4. Milling feed speed**, $z$ cutting teeth and feed per tooth $f_z$ mm/tooth:

$$
v_f=f_zzn.
$$

**5. Cutting power**, specific cutting energy $u_s$ J/m³ and removal rate in m³/s:

$$
P_c=u_sQ_v,\qquad P_{\mathrm{input}}=P_c/\eta.
$$

Specific energy varies with material, chip thickness, geometry, and condition.

**6. Taylor tool-life approximation**, under fixed tool, work material, feed, and depth conditions:

$$
V_cT^n=C_T.
$$

The empirical exponent $n$ here is not spindle speed; units of $C_T$ depend on chosen speed and time units.

**7. Idealized turning roughness**, feed $f$ and tool nose radius $r_e$ in matching length units:

$$
R_a\approx\frac{f^2}{32r_e}.
$$

This geometric estimate excludes built-up edge, vibration, wear, and material tearing.

**8. Chvorinov-type solidification estimate**:

$$
t_s=C_m\left(\frac VA\right)^n.
$$

$V$ is casting volume and $A$ cooling area; exponent is often approximated as 2 for a calibrated mold system. $C_m$ is process-specific and unit-dependent.

**9. Ideal true forming strain**, uniform compression from height $h_0$ to $h$:

$$
\epsilon=\ln(h_0/h),\qquad A_0h_0\approx Ah.
$$

**10. Instantaneous ideal homogeneous upsetting force**, current flow stress $\sigma_f(\epsilon)$ and current area $A$:

$$
F_{\mathrm{ideal}}(\epsilon)\approx\sigma_f(\epsilon)A(\epsilon).
$$

For a work-hardening material, evaluate the current flow stress and increasing area throughout the stroke to estimate the peak ideal load. The strain-averaged flow stress $\bar\sigma_f=(1/\epsilon)\int_0^\epsilon\sigma_f(\eta)\,d\eta$ is useful for plastic-work estimates. Substituting it into $\bar\sigma_f A$ gives only a rough representative load, not generally the instantaneous or peak force. Friction, barreling, and redundant deformation generally increase actual load.

**11. Net welding heat input per length**, voltage $U$, current $I$, travel speed $v$ m/s:

$$
H=\frac{\eta_wUI}{v}.
$$

$H$ is J/m; $\eta_w$ is the process-dependent thermal efficiency.

**12. Batch cost and break-even quantity**:

$$
C(N)=C_F+c_vN,\qquad N_* =\frac{C_{F,A}-C_{F,B}}{c_{v,B}-c_{v,A}}.
$$

Both alternatives must produce equivalent acceptable parts; include tooling, scrap, inspection, and postprocessing consistently.

### Derivation

For turning, the tool advances $f$ per revolution and the spindle completes $n$ revolutions per minute, so axial feed speed is $fn$. Cutting time follows from distance divided by speed. For a shallow radial cut, the chip-producing cross-section is approximately $fa_p$; multiplying by cutting speed in mm/min gives removal rate. Exact annular-volume removal differs slightly when depth is significant relative to diameter. This reasoning makes the approximation visible and helps prevent a factor-of-1000 error when combining metres and millimetres.

### Worked examples

#### Example 1: Turning-time estimate

Turn a nominal 50 mm diameter workpiece at $V_c=120$ m/min with feed 0.20 mm/rev and radial depth 2 mm. Required spindle speed is $n=1000(120)/(\pi50)=763.944$ rpm. Feed speed is 152.789 mm/min. For 100 mm cutting travel, time is $100/152.789=0.654498$ min, or 39.2699 s. Conventional removal-rate estimate is $1000(120)(0.20)(2)=48000$ mm³/min. This excludes setup, tool changes, acceleration, and approach not already included in the 100 mm travel.

#### Example 2: Process break-even

Route A requires 30000 currency units of tooling and costs 2 per accepted part; route B requires 5000 and costs 7 per accepted part. Set $30000+2N=5000+7N$, obtaining $N=5000$ accepted parts. Both routes cost 40000 at that quantity. At 1000 parts, A costs 32000 and B 12000, so B is cheaper. At 10000 parts, A costs 50000 and B 75000, so A is cheaper. Capacity and delivery constraints can still overturn a cost-only choice.

### Exercises

1. A four-flute milling tool runs at 2000 rpm with feed per tooth 0.05 mm. Find feed speed.
2. A casting's thermal modulus doubles while $C_m$ remains unchanged and $n=2$. How does estimated solidification time change?
3. A welding process uses 20 V, 150 A, efficiency 0.80, and speed 5 mm/s. Find net heat input in J/mm.

### Solutions

1. $v_f=0.05(4)(2000)=400$ mm/min.
2. Time increases by $2^2=4$. The conclusion assumes the same calibrated mold and thermal conditions.
3. Net thermal power is $0.8(20)(150)=2400$ W. Dividing by 5 mm/s gives 480 J/mm, equivalent to 480000 J/m.

### Common mistakes

- Using feed per tooth as feed per revolution.
- Mixing diameter and radius when specifying depth of cut.
- Comparing routes using raw parts for one route and accepted parts for another.
- Treating a printed or cast surface as a finished precision datum without inspection or machining.
- Assuming a simple weld heat-input calculation establishes joint quality.

### Applications and limits

Use these models for process screening, early cost estimates, and production planning. Confirm cutting parameters through tool and machine documentation and controlled trials. Manufacturing capability is a distribution, so tolerances should match a stable process and an inspection plan. Real economics include yield, changeovers, utilization, maintenance, lead time, and quality consequences rather than machining time alone.

### Further reading

- [MIT Mechanosynthesis Group: Manufacturing Processes](https://mechanosynthesis.mit.edu/education/manufacturing-processes-2-008/) — process families, variation, quality, and production systems.
- [MIT Open Learning: Fundamentals of Manufacturing Processes](https://openlearning.mit.edu/courses-programs/mitx-courses/fundamentals-manufacturing-processes) — official course description and access route. These are links, not reproductions of course materials.


---

## 22. Metrology, uncertainty, and quality

### Learning map

Prerequisites: units, statistics, geometry, and manufacturing. Define the measurand, construct a measurement model, identify uncertainty contributions, and report a result with its uncertainty. Then distinguish measurement-system capability from manufacturing-process capability. Learn dimensional measurement before applying the same reasoning to temperature, force, flow, pressure, and vibration.

### Theory

A measurement is a comparison that assigns a quantity value to a defined measurand. The measurand must be precise: diameter at which location, at what temperature, under what contact force, and using which definition of size? A result without these conditions can be ambiguous. Calibration establishes relationships to reference values with associated uncertainty; it does not make an instrument error-free.

Accuracy describes closeness to an appropriate reference, precision describes agreement among repeated results, and resolution is the smallest indicated increment. These concepts are not interchangeable. Repeatable readings can share a large bias. A display with many digits may have poor accuracy. Corrections remove estimated systematic effects; uncertainty remains because the correction and input quantities are imperfectly known.

Type A uncertainty evaluation uses statistical analysis of observations. Type B evaluation uses other evidence such as calibration certificates, specifications, physical knowledge, or prior data. These labels describe evaluation methods, not a simple random-versus-systematic division. Correlated input quantities require covariance terms. A common calibration error does not average away when the same instrument is read repeatedly.

Dimensional measurements are sensitive to temperature, alignment, cosine error, Abbe offset, contact deformation, surface texture, and fixturing. A datum establishes a reference for a geometric specification; a convenient best-fit coordinate system is not automatically the specified datum system. Inspection methods should implement the drawing's functional definition rather than measure a visually similar substitute.

Process capability compares a stable process distribution to specification limits. Control limits describe observed process variation, while specification limits describe requirements. A process can be statistically stable and still produce unacceptable parts. Capability indices assume the distribution and sampling model are appropriate; small samples, autocorrelation, mixed machines, and process shifts can make a single index misleading.

### Formula handbook

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

### Derivation

For small input deviations, a first-order Taylor expansion gives $\Delta y\approx\sum c_i\Delta x_i$. Square and take the expected value. Individual squared terms yield $c_i^2u_i^2$, while cross terms yield $2c_ic_j\operatorname{cov}(x_i,x_j)$. Independent inputs have zero covariance, producing root-sum-square combination. If two inputs share the same calibration bias, deleting the cross term can understate uncertainty. Strong nonlinearity may require higher-order treatment or numerical propagation.

### Worked examples

#### Example 1: Length uncertainty budget

Five independent readings in mm are 10.01, 10.00, 9.99, 10.02, and 9.98. Their mean is 10.000 mm and sample standard deviation is 0.0158114 mm, giving $u_A=0.00707107$ mm. Add independent calibration uncertainty $U_{cal}=0.008$ mm with certificate factor 2, so $u_{cal}=0.004$ mm. Treat resolution $q=0.01$ mm as an additional contribution not already represented in the repeatability term: $u_{res}=0.00288675$ mm. Then $u_c=\sqrt{0.00707107^2+0.004^2+0.00288675^2}=0.00862168$ mm and $U=2u_c=0.0172434$ mm. A concise report is $(10.000\pm0.017)$ mm with $k=2$, the stated model, and no claim of exact 95% coverage from this small sample. In a real budget, assess resolution double-counting explicitly.

#### Example 2: Capability and centering

A stable approximately normal process has specification limits 9.950 and 10.050 mm, mean 10.020 mm, and known process standard deviation 0.010 mm. $C_p=0.100/[6(0.010)]=1.6667$. Upper capability is $(10.050-10.020)/0.030=1.000$; lower capability is $(10.020-9.950)/0.030=2.3333$. Therefore $C_{pk}=1.000$. Recentering to 10.000 mm would improve $C_{pk}$ to 1.6667 without changing spread, provided the process remains stable.

### Exercises

1. A digital instrument has resolution 0.02 mm. Find standard uncertainty from uniform rounding alone.
2. An Abbe offset is 100 mm and angular error is 0.001 rad. Estimate the resulting length error.
3. Two independent standard uncertainties are 3 and 4 micrometres with unit sensitivity coefficients. Find combined and $k=2$ expanded uncertainty.

### Solutions

1. $u=0.02/\sqrt{12}=0.0057735$ mm. Resolution is an increment, so its half-width is 0.01 mm.
2. $e_A\approx100(0.001)=0.100$ mm. Reducing offset directly reduces this error source.
3. Combined uncertainty is $\sqrt{3^2+4^2}=5$ micrometres; expanded uncertainty is 10 micrometres. Correlation would change the first result.

### Common mistakes

- Reporting display resolution as total measurement uncertainty.
- Dividing a shared systematic calibration contribution by $\sqrt n$.
- Combining expanded uncertainties without first accounting for their coverage factors.
- Treating a capability index as proof of process stability.
- Ignoring the decision rule when measurement uncertainty overlaps a specification limit.

### Applications and limits

Use uncertainty budgets to identify which improvement matters: better calibration, alignment, environment, fixturing, or repeatability. For conformity decisions, agree on a decision rule and any guard band before judging marginal results. Traceability is a documented chain of calibrations with uncertainties, not simply ownership of a calibrated instrument. Measurement quality depends on the complete procedure and its execution.

### Further reading

- [NIST: Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297) — uncertainty evaluation and expression.
- [NIST: Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — measurement models and computational resources.
- [NIST: Fundamentals of Geometric Dimensioning and Tolerancing, Part II](https://www.nist.gov/publications/fundamentals-geometric-dimensioning-and-tolerancing-part-ii) — geometric product definition. These resources are linked, not reproduced.


---

## 23. CAD, engineering drawing, and tolerances

### Learning map

Prerequisites: geometry, manufacturing, statics, and metrology. Learn to communicate design intent through a parametric model, a functional datum scheme, dimensions, tolerances, material information, and revision control. CAD creates nominal geometry; an engineering definition also specifies acceptable variation and the conditions under which the part must assemble and function.

### Theory

A parametric model expresses relationships rather than merely storing a visible shape. Sketch constraints define orientation, size, and coincidence; features create or remove material. Stable modeling uses references that reflect function, such as an axis or mounting plane, and avoids unnecessary dependence on faces likely to disappear after an edit. Fully constrained does not mean well designed: a sketch can be mathematically complete yet encode the wrong design relationships.

Orthographic views project geometry onto mutually perpendicular planes. Section views expose internal features, while detail views enlarge local information. First-angle and third-angle projection arrange views differently, so the drawing must identify its convention. A perspective image helps recognition but generally does not supply a reliable basis for measurement.

Dimensions define size and location. Tolerances define the permitted variation and should follow function. Datum features provide the physical references used to establish a datum reference frame. Geometric tolerances describe form, orientation, location, and runout according to the chosen standard. Their symbols and modifiers have precise meanings; this chapter does not reproduce a standard or substitute a simplified equation for its rules.

An assembly can fail even when every individual dimension is within tolerance. A stack-up propagates component variation into a functional gap, alignment, or interference. Worst-case analysis checks all permitted extremes and supports guaranteed interchangeability under its assumptions. Statistical analysis can predict a distribution when input distributions, correlations, and process behavior are justified; it does not guarantee that every permitted part combination fits.

CAD geometry must also support manufacturing and inspection. Specify accessible surfaces, tool clearances, datum preparation, surface texture, threads, edge treatment, and material condition where functional. A STEP exchange file can transmit nominal geometry, but whether semantic product manufacturing information survives depends on the chosen format, exporter, importer, and workflow. Verify transferred units and critical geometry directly.

### Formula handbook

Use one stated length unit throughout each model and drawing. Formulas below describe geometry and elementary tolerances, not complete GD&T acceptance rules.

**1. Drawing scale**:

$$
S=\frac{L_{\mathrm{drawing}}}{L_{\mathrm{actual}}}.
$$

Written dimensions govern; never infer an unspecified production dimension by measuring a printed view.

**2. Homogeneous point transformation**:

$$
\begin{bmatrix}\mathbf p'\\1\end{bmatrix}=\begin{bmatrix}\mathbf R&\mathbf t\\\mathbf0^T&1\end{bmatrix}\begin{bmatrix}\mathbf p\\1\end{bmatrix}.
$$

$\mathbf R$ is a dimensionless rotation matrix and $\mathbf t$ a translation in the point's length unit.

**3. Planar rotation**:

$$
x'=x\cos\theta-y\sin\theta,\qquad y'=x\sin\theta+y\cos\theta.
$$

**4. Bolt-circle coordinates**, center $(x_c,y_c)$, radius $R$, $N$ holes:

$$
\theta_i=\theta_0+\frac{2\pi i}{N},\qquad x_i=x_c+R\cos\theta_i,\qquad y_i=y_c+R\sin\theta_i.
$$

**5. Arc length and chord**:

$$
s=R\theta,\qquad c=2R\sin(\theta/2).
$$

Use radians for $s=R\theta$.

**6. Conical taper**, large diameter $D$, small diameter $d$, length $L$:

$$
\tan\alpha=\frac{D-d}{2L}.
$$

$\alpha$ is the half-angle, not the included cone angle.

**7. Hole–shaft clearance limits**:

$$
C_{\min}=D_{h,\min}-D_{s,\max},\qquad C_{\max}=D_{h,\max}-D_{s,\min}.
$$

Negative clearance indicates interference for that combination.

**8. Linear dimension chain**, signed coefficients $a_i$:

$$
Y=\sum_i a_iX_i,\qquad T_{Y,\mathrm{worst}}=\sum_i|a_i|T_i.
$$

$T_i$ are symmetric half-width tolerances around nominal values.

**9. Independent statistical stack**, using standard deviations rather than arbitrary drawing tolerances:

$$
\sigma_Y=\sqrt{\sum_i a_i^2\sigma_i^2}.
$$

Add covariance terms if component dimensions are correlated.

**10. Coordinate-based diametral position deviation**, for a measured axis point relative to its basic location:

$$
p_{xy}=2\sqrt{(x-x_b)^2+(y-y_b)^2}.
$$

This simple two-dimensional calculation alone does not evaluate full axis orientation, datum establishment, material modifiers, or all requirements of a position tolerance.

**11. Approximate sheet bend allowance**:

$$
BA=\theta(R_i+K_bt).
$$

$R_i$ is inside bend radius, $t$ thickness, and $K_b$ a calibrated neutral-axis factor; angle is radians. Real bend tables depend on material and tooling.

**12. Uniform-density mass estimate**:

$$
m=\rho V,\qquad\mathbf r_G=\frac{\sum_i m_i\mathbf r_i}{\sum_i m_i}.
$$

Use actual material assignment, units, and modeled components; suppressed or simplified features can alter mass properties.

### Derivation

For a clearance fit, the tightest assembly combines the smallest permitted hole with the largest permitted shaft. Subtracting those limits produces minimum clearance. The loosest assembly combines the largest hole with the smallest shaft, giving maximum clearance. For a linear multi-part stack, each independent interval contributes its largest possible signed deviation in the unfavorable direction; adding absolute sensitivities gives the worst-case bound. Statistical root-sum-square combines variances under a different probabilistic model and must not be described as the same guarantee.

### Worked examples

#### Example 1: Clearance-fit assessment

A hole may be 40.000–40.025 mm, while its shaft may be 39.980–39.990 mm. Minimum clearance is $40.000-39.990=0.010$ mm. Maximum clearance is $40.025-39.980=0.045$ mm. The assembly is always a clearance fit within these size limits. This does not establish free rotation: form error, temperature differences, coatings, contamination, and misalignment may consume functional clearance. A nominal diameter difference alone would miss the extreme combinations.

#### Example 2: Bolt-circle layout

Place six equally spaced holes on a 100 mm diameter bolt circle centered at the origin, with the first hole at $30^\circ$. Radius is 50 mm and angular spacing is $360^\circ/6=60^\circ$. Coordinates in mm are $(43.3013,25)$, $(0,50)$, $(-43.3013,25)$, $(-43.3013,-25)$, $(0,-50)$, and $(43.3013,-25)$. Each point has radius 50 mm. Neighboring center spacing is $2(50)\sin30^\circ=50$ mm. These define nominal geometry; hole size, position tolerance, and datum references must be specified separately.

### Exercises

1. A functional gap is $G=A-B-C$, where nominal values are 100, 40, and 50 mm with symmetric tolerances ±0.2, ±0.1, and ±0.1 mm. Find nominal gap and worst-case interval.
2. A point $(20,0)$ mm is rotated $90^\circ$ counterclockwise about the origin. Find its new coordinates.
3. A taper changes diameter from 40 to 20 mm over 100 mm. Find half-angle and included angle.

### Solutions

1. Nominal gap is 10 mm. Worst-case half-width is $0.2+0.1+0.1=0.4$ mm, giving 9.6–10.4 mm.
2. The point becomes $(0,20)$ mm. A tiny numerical nonzero $x$ from floating-point cosine is not a geometric discrepancy.
3. $\alpha=\arctan[(40-20)/(2\times100)]=5.71059^\circ$. Included angle is $11.4212^\circ$.

### Common mistakes

- Duplicating dimensions so that later revisions create contradictory requirements.
- Using a model's visual appearance as proof of correct scale or units.
- Applying a general tolerance to a feature whose function requires a specific tolerance.
- Calling a statistical stack a guaranteed worst-case fit.
- Treating a simple coordinate position calculation as a complete GD&T inspection.

### Applications and limits

Use parametric CAD to express intended dependencies and drawings or model-based definitions to communicate acceptance requirements. Review assemblies through realistic motion and manufacturing states, not only their final nominal position. Preserve revision identifiers, material condition, reference standards, and inspection intent. For production, use the applicable adopted standard and project drawing rules; the elementary formulas here support reasoning but do not define those standards.

### Further reading

- [NIST: Fundamentals of Geometric Dimensioning and Tolerancing, Part II](https://www.nist.gov/publications/fundamentals-geometric-dimensioning-and-tolerancing-part-ii) — official educational presentation on engineering product definition.
- [MIT: FUNdaMentals of Design](https://meddevdesign.mit.edu/fundamentals-of-design/) — precision design and error-budget resources. Linked material is not copied into this chapter.
