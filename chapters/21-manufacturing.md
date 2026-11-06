# 21. Manufacturing processes and production

## Learning map

Prerequisites: materials, mechanics, heat transfer, and basic economics. Compare machining, casting, forming, joining, molding, and additive manufacturing through physical mechanism, achievable geometry, quality, production rate, and cost. Learn to estimate a process before choosing equipment. A successful design includes an achievable manufacturing and inspection route.

## Theory

Machining removes material through controlled chip formation. Cutting speed affects temperature and tool wear; feed and depth of cut affect chip load, force, productivity, and surface geometry. Machine power, stiffness, chatter, workholding, chip evacuation, and tool accessibility constrain usable parameters. A catalog cutting speed is a starting point for a specified tool–material combination, not a universal setting.

Casting creates geometry by filling a mold and solidifying material. Shrinkage, feeding, gas entrapment, inclusions, and cooling gradients influence defects and microstructure. Risers should feed shrinkage as solidification proceeds; the thermal modulus $V/A$ helps reason about which regions cool more slowly. Pattern allowances and draft differ from final part dimensions and depend on the process and material.

Forming changes shape through plastic flow. Forging, rolling, extrusion, drawing, and sheet forming trade material utilization and production rate against tooling, load, friction, and ductility constraints. Volume is approximately conserved during plastic deformation of dense metals, while elastic recovery causes springback. Excessive local thinning or tensile strain can produce failure even when overall forming force is available.

Joining includes mechanical fastening, welding, brazing, soldering, and adhesive bonding. Fusion welding produces a heat-affected zone, residual stress, and possible distortion. Joint preparation, access, restraint, sequence, filler, and inspection requirements belong in the process plan. A heat-input estimate alone does not qualify a weld or predict all metallurgical effects.

Additive manufacturing creates parts in successive layers or deposited tracks. It can reduce tooling and enable complex internal geometry, but build orientation, supports, thermal history, porosity, anisotropy, surface finish, and postprocessing influence performance. Printed nominal geometry is not automatically equivalent to wrought material properties. Process selection should compare the complete route, including support removal, heat treatment, machining, and inspection.

## Formula handbook

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

## Derivation

For turning, the tool advances $f$ per revolution and the spindle completes $n$ revolutions per minute, so axial feed speed is $fn$. Cutting time follows from distance divided by speed. For a shallow radial cut, the chip-producing cross-section is approximately $fa_p$; multiplying by cutting speed in mm/min gives removal rate. Exact annular-volume removal differs slightly when depth is significant relative to diameter. This reasoning makes the approximation visible and helps prevent a factor-of-1000 error when combining metres and millimetres.

## Worked examples

### Example 1: Turning-time estimate

Turn a nominal 50 mm diameter workpiece at $V_c=120$ m/min with feed 0.20 mm/rev and radial depth 2 mm. Required spindle speed is $n=1000(120)/(\pi50)=763.944$ rpm. Feed speed is 152.789 mm/min. For 100 mm cutting travel, time is $100/152.789=0.654498$ min, or 39.2699 s. Conventional removal-rate estimate is $1000(120)(0.20)(2)=48000$ mm³/min. This excludes setup, tool changes, acceleration, and approach not already included in the 100 mm travel.

### Example 2: Process break-even

Route A requires 30000 currency units of tooling and costs 2 per accepted part; route B requires 5000 and costs 7 per accepted part. Set $30000+2N=5000+7N$, obtaining $N=5000$ accepted parts. Both routes cost 40000 at that quantity. At 1000 parts, A costs 32000 and B 12000, so B is cheaper. At 10000 parts, A costs 50000 and B 75000, so A is cheaper. Capacity and delivery constraints can still overturn a cost-only choice.

## Exercises

1. A four-flute milling tool runs at 2000 rpm with feed per tooth 0.05 mm. Find feed speed.
2. A casting's thermal modulus doubles while $C_m$ remains unchanged and $n=2$. How does estimated solidification time change?
3. A welding process uses 20 V, 150 A, efficiency 0.80, and speed 5 mm/s. Find net heat input in J/mm.

## Solutions

1. $v_f=0.05(4)(2000)=400$ mm/min.
2. Time increases by $2^2=4$. The conclusion assumes the same calibrated mold and thermal conditions.
3. Net thermal power is $0.8(20)(150)=2400$ W. Dividing by 5 mm/s gives 480 J/mm, equivalent to 480000 J/m.

## Common mistakes

- Using feed per tooth as feed per revolution.
- Mixing diameter and radius when specifying depth of cut.
- Comparing routes using raw parts for one route and accepted parts for another.
- Treating a printed or cast surface as a finished precision datum without inspection or machining.
- Assuming a simple weld heat-input calculation establishes joint quality.

## Applications and limits

Use these models for process screening, early cost estimates, and production planning. Confirm cutting parameters through tool and machine documentation and controlled trials. Manufacturing capability is a distribution, so tolerances should match a stable process and an inspection plan. Real economics include yield, changeovers, utilization, maintenance, lead time, and quality consequences rather than machining time alone.

## Further reading

- [MIT Mechanosynthesis Group: Manufacturing Processes](https://mechanosynthesis.mit.edu/education/manufacturing-processes-2-008/) — process families, variation, quality, and production systems.
- [MIT Open Learning: Fundamentals of Manufacturing Processes](https://openlearning.mit.edu/courses-programs/mitx-courses/fundamentals-manufacturing-processes) — official course description and access route. These are links, not reproductions of course materials.
