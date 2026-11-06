# 37 · Composite materials and laminated plates

## Learning map

Prerequisites are elasticity, stress and strain, matrix algebra, and material behaviour. Study chapters 06–07 before this chapter and use chapter 24 for later finite-element applications. The objective is to distinguish constituent properties, lamina response, laminate response, and failure. Two elementary calculations connect a material mixture to an orthotropic ply and a symmetric laminate. They are stiffness models, not a complete composite design procedure.

## Theory

A composite combines distinguishable constituents to obtain a useful combination of properties. A fibre-reinforced polymer uses relatively stiff fibres to carry much of the longitudinal load and a matrix to support, separate, and transfer load between them. The interface is crucial: broken adhesion, porosity, fibre waviness, moisture, and processing defects can change performance substantially. Constituent strength values alone cannot establish the manufactured part's strength.

A unidirectional lamina is a thin layer with a preferred fibre direction, labelled 1. Direction 2 lies transverse to the fibres in the layer. The layer is often treated as orthotropic: its material axes have different elastic responses with specified symmetry. A laminate stacks layers at different angles and positions. The laminate's global axes differ from each layer's local material axes, so stresses and strains must be transformed consistently.

The longitudinal rule of mixtures assumes equal axial strain in continuous, well-bonded constituents. Its transverse counterpart under an equal-stress assumption is a series idealization. These models are useful estimates and teaching bounds for the stated scalar arrangements; they are not exact general transverse-property predictions for a real microstructure. Voids, packing, constituent Poisson effects, and interfaces can matter. Measured lamina data are preferable for detailed analysis.

Classical laminate theory assumes thin layers, small deformation, in-plane elastic response, perfect bonding, and a linear variation of in-plane strain through thickness. Normals to the midplane remain straight and normal in the classical thin-plate kinematics. Transverse shear deformation is neglected. This can be inadequate for thick laminates, sandwich structures with compliant cores, local joints, impact, or delamination. Interlaminar stresses near free edges require more than the elementary in-plane model.

Three stiffness matrices organize the laminate response. A maps midplane strain to membrane force resultants; D maps curvature to moment resultants; B couples extension and bending. A laminate symmetric about its midplane has B equal to zero under this constitutive model. Balanced angle pairs can remove some extension–shear coupling, but balanced and symmetric are different properties. Neither automatically makes a laminate isotropic in bending or guarantees every coupling term vanishes.

Composite failure can involve fibre tension, fibre compression, matrix cracking, shear failure, interface damage, and delamination. The maximum-stress criterion is a simple componentwise screening approach, while interactive criteria use combinations of stresses. A first-ply-failure prediction does not automatically equal final collapse; redistribution and progressive damage require an appropriate model and evidence. Allowables must match direction, sign, condition, and statistical/design basis.

## Formula handbook

Use constituent volume fractions $V_f,V_m$, densities $\rho_f,\rho_m$ in kg/m³, and elastic moduli in Pa. The subscript f denotes fibre and m denotes matrix; the symbol $m$ elsewhere may mean mass, so read local definitions.

1. With no void fraction, $V_f+V_m=1$ and $\rho_c=V_f\rho_f+V_m\rho_m$. Void-containing mixtures require another constituent fraction and an appropriate density model.
2. Equal longitudinal strain gives $E_L=V_fE_f+V_mE_m$ for the simple continuous parallel model.
3. The equal-stress transverse series model gives $1/E_T=V_f/E_f+V_m/E_m$.
4. Under equal axial strain $\epsilon$, constituent stresses are $\sigma_f=E_f\epsilon$, $\sigma_m=E_m\epsilon$, and macroscopic stress is $\sigma_c=V_f\sigma_f+V_m\sigma_m$.
5. Orthotropic reciprocity requires $\nu_{12}/E_1=\nu_{21}/E_2$. Here $\nu_{12}=-\epsilon_2/\epsilon_1$ under uniaxial stress in direction 1, and the reverse ratio defines $\nu_{21}$.
6. The lamina plane-stress compliance relation is

$$
\begin{bmatrix}\epsilon_1\\\epsilon_2\\\gamma_{12}\end{bmatrix}
=\begin{bmatrix}1/E_1&-\nu_{21}/E_2&0\\-\nu_{12}/E_1&1/E_2&0\\0&0&1/G_{12}\end{bmatrix}
\begin{bmatrix}\sigma_1\\\sigma_2\\\tau_{12}\end{bmatrix}.
$$

Engineering shear strain $\gamma_{12}$ is twice the tensor shear strain; use that convention consistently in transformations.
7. Let $d=1-\nu_{12}\nu_{21}$. The reduced stiffness terms are $Q_{11}=E_1/d$, $Q_{22}=E_2/d$, $Q_{12}=\nu_{12}E_2/d$, and $Q_{66}=G_{12}$. They have units Pa, with $\boldsymbol\sigma=\mathbf Q\boldsymbol\epsilon$.
8. In global axes, $\boldsymbol\sigma_{xy}=\overline{\mathbf Q}\boldsymbol\epsilon_{xy}$. At 90 degrees, $\overline Q_{11}=Q_{22}$, $\overline Q_{22}=Q_{11}$, $\overline Q_{12}=Q_{12}$, and $\overline Q_{66}=Q_{66}$; the 16 and 26 terms vanish for a specially orthotropic ply at 0 or 90 degrees.
9. With the convention $\boldsymbol\epsilon(z)=\boldsymbol\epsilon^0+z\boldsymbol\kappa$, layer boundaries $z_k$ measured from the midplane give

$$
\mathbf A=\sum_k\overline{\mathbf Q}_k(z_k-z_{k-1}),\quad
\mathbf B=\frac12\sum_k\overline{\mathbf Q}_k(z_k^2-z_{k-1}^2),\quad
\mathbf D=\frac13\sum_k\overline{\mathbf Q}_k(z_k^3-z_{k-1}^3).
$$

The units are N/m, N, and N m respectively.
10. Without thermal or other initial strains,

$$
\begin{bmatrix}\mathbf N\\\mathbf M\end{bmatrix}
=\begin{bmatrix}\mathbf A&\mathbf B\\\mathbf B&\mathbf D\end{bmatrix}
\begin{bmatrix}\boldsymbol\epsilon^0\\\boldsymbol\kappa\end{bmatrix}.
$$

Membrane resultant $\mathbf N$ is force per width in N/m, moment resultant $\mathbf M$ is moment per width in N, and curvature is in m⁻¹. The bending sign follows the chosen $z$ and curvature convention.
11. Layer stress recovery is $\boldsymbol\sigma_k(z)=\overline{\mathbf Q}_k[\boldsymbol\epsilon^0+z\boldsymbol\kappa-\overline{\boldsymbol\alpha}_k\Delta T]$ when a compatible thermal expansion vector is included. Moisture and other initial strains need additional terms.
12. Simple maximum-stress screening compares local $\sigma_1,\sigma_2,\tau_{12}$ with the corresponding tensile/compressive and shear allowables. For example, $-X_c\leq\sigma_1\leq X_t$ and $|\tau_{12}|\leq S$; the transverse pair uses $Y_t,Y_c$. This separate-component model omits interactions and delamination.

## Derivation

Consider a symmetric laminate with no thermal strain and only applied membrane loads. Identical material at equal positive and negative distances from the midplane makes the integral of $z\overline{\mathbf Q}$ cancel, giving $\mathbf B=0$. If no bending moments act and $\mathbf D$ is nonsingular, curvature is zero. All plies then have the same global in-plane strain, but their stresses differ because their transformed stiffness matrices differ. Integrating those stresses gives $\mathbf N=\mathbf A\boldsymbol\epsilon^0$.

For a cross-ply laminate with equal 0- and 90-degree thicknesses, $A_{16}=A_{26}=0$ and $A_{11}=A_{22}$. Under $N_x$ alone, solving the two coupled normal equations gives $\epsilon_x=N_xA_{11}/(A_{11}^2-A_{12}^2)$ and $\epsilon_y=-N_xA_{12}/(A_{11}^2-A_{12}^2)$. Setting transverse strain to zero would impose an extra constraint and would represent a different boundary condition.

## Worked examples

### Example 1: a constituent stiffness estimate

Use hypothetical continuous fibres with $E_f=230$ GPa, matrix modulus $E_m=3.5$ GPa, and $V_f=0.60$. The parallel estimate is **$E_L=139.400$ GPa**. The series estimate is **$E_T=8.554729$ GPa**. With fibre and matrix densities 1800 and 1200 kg/m³, density is **1560 kg/m³**. Under a common axial strain 0.001, fibre stress is **230 MPa**, matrix stress **3.5 MPa**, and average stress **139.4 MPa**. The fibre share of total axial force is **0.989957**, about 99.0%, under the parallel assumptions. These values illustrate stiffness and load sharing; they do not predict failure strength or exact transverse response.

### Example 2: a symmetric cross-ply membrane

Four identical 0.125 mm plies form $[0/90/90/0]$, for total thickness 0.500 mm. Use measured-or-supplied lamina inputs $E_1=135$ GPa, $E_2=10$ GPa, $G_{12}=5$ GPa, and $\nu_{12}=0.30$. Here they are hypothetical teaching inputs. Reciprocity gives $\nu_{21}=0.0222222$. The reduced stiffnesses are $Q_{11}=135.9060$, $Q_{22}=10.06711$, $Q_{12}=3.020134$, and $Q_{66}=5.00000$ GPa.

Integration gives **$A_{11}=A_{22}=36.49329$ MN/m**, **$A_{12}=1.510067$ MN/m**, **$A_{66}=2.500000$ MN/m**, and $\mathbf B=0$. Apply $N_x=50,000$ N/m with $N_y=N_{xy}=0$ and no moments. Midplane strains are **$\epsilon_x=0.001372465$**, **$\epsilon_y=-0.00005679165$**, and zero engineering shear. A 0-degree ply has local stresses **186.3548 MPa** and **3.573300 MPa**; a 90-degree ply has local stresses **−3.573300 MPa** and **13.64524 MPa** in its own 1 and 2 directions. Transforming back and integrating recovers the applied 50,000 N/m and zero transverse resultant. No strength conclusion is possible without appropriate allowables and failure models.

## Exercises

1. For $E_1=140$ GPa, $E_2=10$ GPa and $\nu_{12}=0.28$, find $\nu_{21}$. Explain why setting both Poisson ratios equal is inconsistent here.
2. All ply thicknesses in Example 2 are doubled while the stacking sequence and material properties remain unchanged. How do A, B, and D scale? What happens to strain under the same pure membrane load?
3. Under the same 0.001 axial strain as Example 1, reduce fibre fraction to 0.40. Find the parallel modulus, density, and average stress using the same constituent data.

## Solutions

1. Reciprocity gives $\nu_{21}=0.28(10/140)=\mathbf{0.0200}$. Equal ratios would violate the symmetric compliance relation when the moduli differ.
2. A doubles, D increases by a factor **8**, and B remains **zero** because symmetry is preserved. The same membrane load produces **half the strain**. This scaling assumes every through-thickness coordinate doubles about the same midplane; it is not an arbitrary addition of one new ply.
3. $E_L=0.4(230)+0.6(3.5)=\mathbf{94.100\ GPa}$, density is **1440 kg/m³**, and average stress is **94.100 MPa**. Constituent stresses under prescribed equal strain remain unchanged; their area fractions and total load change.

## Common mistakes

Using isotropic relations to infer $G_{12}$ from $E_1$ and $\nu_{12}$ is generally invalid. A laminate-average stress cannot replace local ply stresses in a directional criterion. Mixing tensor shear and engineering shear introduces factors of two. Symmetric, balanced, and quasi-isotropic describe different properties. An apparently stiff laminate may still be weak at a bolt hole, a free edge, an impact site, or an interface.

## Applications and limits

Use laminate analysis to compare load paths, stiffness, deformation, and coupling before detailed joint and damage assessments. Preserve the layup convention, ply order, thicknesses, fibre angles, property condition, and coordinate definitions in the design record. Thermal and moisture conditions can create self-equilibrated ply stresses even when external resultants vanish. Real qualification needs traceable allowables, processing controls, inspection, and representative tests. The verifier checks stiffness assembly and load recovery, not damage tolerance or manufactured quality.

## Further reading

- [MIT Roylance, Laminated Composite Plates](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/f193c908ec10d95c0bc67c904b65397a_MIT3_11F99_laminates.pdf) — freely hosted derivation of lamina and laminate constitutive equations.
- [NASA RP-1351, Basic Mechanics of Laminated Composite Plates](https://ntrs.nasa.gov/citations/19950009349) — official report record and download route for a fuller reference. The PDF route was identifiable; a prior full download attempt timed out.
