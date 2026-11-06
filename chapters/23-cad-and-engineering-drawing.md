# 23. CAD, engineering drawing, and tolerances

## Learning map

Prerequisites: geometry, manufacturing, statics, and metrology. Learn to communicate design intent through a parametric model, a functional datum scheme, dimensions, tolerances, material information, and revision control. CAD creates nominal geometry; an engineering definition also specifies acceptable variation and the conditions under which the part must assemble and function.

## Theory

A parametric model expresses relationships rather than merely storing a visible shape. Sketch constraints define orientation, size, and coincidence; features create or remove material. Stable modeling uses references that reflect function, such as an axis or mounting plane, and avoids unnecessary dependence on faces likely to disappear after an edit. Fully constrained does not mean well designed: a sketch can be mathematically complete yet encode the wrong design relationships.

Orthographic views project geometry onto mutually perpendicular planes. Section views expose internal features, while detail views enlarge local information. First-angle and third-angle projection arrange views differently, so the drawing must identify its convention. A perspective image helps recognition but generally does not supply a reliable basis for measurement.

Dimensions define size and location. Tolerances define the permitted variation and should follow function. Datum features provide the physical references used to establish a datum reference frame. Geometric tolerances describe form, orientation, location, and runout according to the chosen standard. Their symbols and modifiers have precise meanings; this chapter does not reproduce a standard or substitute a simplified equation for its rules.

An assembly can fail even when every individual dimension is within tolerance. A stack-up propagates component variation into a functional gap, alignment, or interference. Worst-case analysis checks all permitted extremes and supports guaranteed interchangeability under its assumptions. Statistical analysis can predict a distribution when input distributions, correlations, and process behavior are justified; it does not guarantee that every permitted part combination fits.

CAD geometry must also support manufacturing and inspection. Specify accessible surfaces, tool clearances, datum preparation, surface texture, threads, edge treatment, and material condition where functional. A STEP exchange file can transmit nominal geometry, but whether semantic product manufacturing information survives depends on the chosen format, exporter, importer, and workflow. Verify transferred units and critical geometry directly.

## Formula handbook

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

## Derivation

For a clearance fit, the tightest assembly combines the smallest permitted hole with the largest permitted shaft. Subtracting those limits produces minimum clearance. The loosest assembly combines the largest hole with the smallest shaft, giving maximum clearance. For a linear multi-part stack, each independent interval contributes its largest possible signed deviation in the unfavorable direction; adding absolute sensitivities gives the worst-case bound. Statistical root-sum-square combines variances under a different probabilistic model and must not be described as the same guarantee.

## Worked examples

### Example 1: Clearance-fit assessment

A hole may be 40.000–40.025 mm, while its shaft may be 39.980–39.990 mm. Minimum clearance is $40.000-39.990=0.010$ mm. Maximum clearance is $40.025-39.980=0.045$ mm. The assembly is always a clearance fit within these size limits. This does not establish free rotation: form error, temperature differences, coatings, contamination, and misalignment may consume functional clearance. A nominal diameter difference alone would miss the extreme combinations.

### Example 2: Bolt-circle layout

Place six equally spaced holes on a 100 mm diameter bolt circle centered at the origin, with the first hole at $30^\circ$. Radius is 50 mm and angular spacing is $360^\circ/6=60^\circ$. Coordinates in mm are $(43.3013,25)$, $(0,50)$, $(-43.3013,25)$, $(-43.3013,-25)$, $(0,-50)$, and $(43.3013,-25)$. Each point has radius 50 mm. Neighboring center spacing is $2(50)\sin30^\circ=50$ mm. These define nominal geometry; hole size, position tolerance, and datum references must be specified separately.

## Exercises

1. A functional gap is $G=A-B-C$, where nominal values are 100, 40, and 50 mm with symmetric tolerances ±0.2, ±0.1, and ±0.1 mm. Find nominal gap and worst-case interval.
2. A point $(20,0)$ mm is rotated $90^\circ$ counterclockwise about the origin. Find its new coordinates.
3. A taper changes diameter from 40 to 20 mm over 100 mm. Find half-angle and included angle.

## Solutions

1. Nominal gap is 10 mm. Worst-case half-width is $0.2+0.1+0.1=0.4$ mm, giving 9.6–10.4 mm.
2. The point becomes $(0,20)$ mm. A tiny numerical nonzero $x$ from floating-point cosine is not a geometric discrepancy.
3. $\alpha=\arctan[(40-20)/(2\times100)]=5.71059^\circ$. Included angle is $11.4212^\circ$.

## Common mistakes

- Duplicating dimensions so that later revisions create contradictory requirements.
- Using a model's visual appearance as proof of correct scale or units.
- Applying a general tolerance to a feature whose function requires a specific tolerance.
- Calling a statistical stack a guaranteed worst-case fit.
- Treating a simple coordinate position calculation as a complete GD&T inspection.

## Applications and limits

Use parametric CAD to express intended dependencies and drawings or model-based definitions to communicate acceptance requirements. Review assemblies through realistic motion and manufacturing states, not only their final nominal position. Preserve revision identifiers, material condition, reference standards, and inspection intent. For production, use the applicable adopted standard and project drawing rules; the elementary formulas here support reasoning but do not define those standards.

## Further reading

- [NIST: Fundamentals of Geometric Dimensioning and Tolerancing, Part II](https://www.nist.gov/publications/fundamentals-geometric-dimensioning-and-tolerancing-part-ii) — official educational presentation on engineering product definition.
- [MIT: FUNdaMentals of Design](https://meddevdesign.mit.edu/fundamentals-of-design/) — precision design and error-budget resources. Linked material is not copied into this chapter.
