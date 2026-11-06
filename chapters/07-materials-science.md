# 07. Materials science and selection

## Learning map

Prerequisites: chemistry fundamentals, stress and strain, energy, and temperature. Connect atomic bonding to microstructure, processing, properties, and service performance. Study elastic and plastic deformation, phase equilibrium, diffusion, fracture, fatigue, and creep. A material name alone is not a specification: composition, product form, heat treatment, orientation, and test conditions matter.

## Theory

Metals, ceramics, polymers, and composites possess different bonding and structural mechanisms. Metallic bonding permits dislocation motion, making many metals ductile. Ceramics often resist elastic deformation and high temperature but tolerate little tensile crack growth. Polymers have time- and temperature-dependent chain mobility. Composite properties depend on constituent materials, fiber direction, interfaces, and manufacturing defects.

Elastic deformation recovers after unloading; plastic deformation leaves a permanent component. Yield stress describes a chosen transition or proof criterion, whereas ultimate tensile strength is the maximum engineering stress in a tensile test. After necking begins, engineering and true stresses differ substantially because deformation is no longer uniform. Hardness is a local indentation response and cannot be converted universally into tensile strength.

Microstructure includes grain size, phases, precipitates, dislocation density, porosity, and texture. Strengthening often obstructs dislocation motion through grain boundaries, solute atoms, precipitates, or cold work. Increasing strength can reduce ductility or fracture tolerance, so maximizing one property is rarely the whole design objective. Heat treatment changes microstructure through temperature-time history; a phase diagram alone does not predict transformation speed.

An equilibrium phase diagram identifies stable phases at specified composition and temperature. A tie line gives phase compositions, while the lever rule gives phase fractions. Diffusion transports atoms down a chemical-potential gradient; simple concentration-gradient laws are useful approximations. Phase transformations require both thermodynamic driving force and kinetic pathways.

Failure depends on environment and duration. Fatigue can initiate under repeated stress below monotonic yield. Creep accumulates with time under sustained stress, especially at elevated homologous temperature. Corrosion, hydrogen, irradiation, and wear can change properties or introduce flaws. Material selection should therefore begin with a service envelope and credible failure modes, then use traceable data for the actual product condition.

## Formula handbook

**1. Engineering stress and strain**, with original area $A_0$ and length $L_0$:

$$
\sigma_e=F/A_0,\qquad\epsilon_e=(L-L_0)/L_0.
$$

**2. True measures**, with instantaneous area $A$ and uniform uniaxial deformation:

$$
\sigma_t=F/A,\qquad\epsilon_t=\ln(L/L_0).
$$

Before necking, approximately constant plastic volume gives $\sigma_t\approx\sigma_e(1+\epsilon_e)$.

**3. Elastic energy density**, for uniaxial linear elasticity:

$$
u_e=\tfrac12\sigma\epsilon=\frac{\sigma^2}{2E}.
$$

$u_e$ is J/m³, and stress and modulus are Pa.

**4. Free thermal expansion**, for approximately constant coefficient $\alpha_T$ in K⁻¹:

$$
\Delta L=\alpha_T L_0\Delta T.
$$

**5. Completely restrained uniaxial thermal stress**, assuming elastic behavior and no relaxation:

$$
\sigma_T=-E\alpha_T\Delta T.
$$

Heating produces compression in this sign convention.

**6. Binary two-phase lever rule**, with composition coordinate $C_\alpha<C_0<C_\beta$:

$$
f_\alpha=\frac{C_\beta-C_0}{C_\beta-C_\alpha},\qquad f_\beta=1-f_\alpha.
$$

The fractions use the same mass or mole basis as the composition coordinate.

**7. One-dimensional Fick laws**, constant diffusivity $D$ in m²/s:

$$
J=-D\frac{\partial C}{\partial x},\qquad \frac{\partial C}{\partial t}=D\frac{\partial^2C}{\partial x^2}.
$$

If $C$ is mol/m³, flux $J$ is mol/(m² s).

**8. Arrhenius diffusivity**, with molar activation energy $Q_d$:

$$
D=D_0\exp\left(-\frac{Q_d}{RT}\right).
$$

Use absolute $T$ in K and matching J/mol units for $Q_d$ and $R$.

**9. Hall–Petch empirical relation**, within its calibrated grain-size regime:

$$
\sigma_y=\sigma_0+k_y d_g^{-1/2}.
$$

Grain size $d_g$ is m; $k_y$ then has units Pa m$^{1/2}$.

**10. Mode-I stress intensity**, for a geometry with crack length parameter $a$:

$$
K_I=Y\sigma\sqrt{\pi a},\qquad a_c=\frac1\pi\left(\frac{K_{IC}}{Y\sigma}\right)^2.
$$

$K_I,K_{IC}$ are Pa m$^{1/2}$. The geometry factor $Y$ and plane-strain toughness assumptions must match the specimen and loading.

**11. Empirical steady creep law**:

$$
\dot\epsilon_c=A_c\sigma^n\exp\left(-\frac{Q_c}{RT}\right).
$$

$A_c$ has unit-dependent dimensions and must be calibrated for the stated material and stress units.

**12. Axial aligned continuous-fiber composite**, under ideal iso-strain loading:

$$
E_L=V_fE_f+(1-V_f)E_m.
$$

This rule does not predict transverse strength, interface failure, or a laminate's complete constitutive behavior.

## Derivation

For a binary alloy containing phases $\alpha$ and $\beta$, conservation gives $f_\alpha+f_\beta=1$ and $C_0=f_\alpha C_\alpha+f_\beta C_\beta$. Eliminating $f_\beta$ yields the lever rule. If $C_0$ approaches $C_\alpha$, the amount of $\beta$ approaches zero. The result requires the tie-line endpoint compositions, not the overall alloy composition substituted into both phase terms. A phase diagram supplies equilibrium endpoints; real cooling can preserve nonequilibrium structures.

## Worked examples

### Example 1: Thermal movement and restraint

A 2 m bar has $\alpha_T=11\times10^{-6}$ K⁻¹ and $E=200$ GPa. For a 60 K temperature rise, its free extension is $11\times10^{-6}(2)(60)=1.32$ mm. If perfectly restrained while remaining elastic, stress is $-200\times10^9(11\times10^{-6})(60)=-132$ MPa. These are two different boundary-condition cases: the bar cannot simultaneously achieve the full free extension and the fully restrained stress. Real support flexibility produces an intermediate response.

### Example 2: Critical crack-size estimate

Assume $K_{IC}=50$ MPa m$^{1/2}$, tensile stress 150 MPa, and approximately constant $Y=1.12$. Then $a_c=(50/(1.12\times150))^2/\pi=0.028195$ m, or 28.195 mm. This is the crack-length parameter used by the assumed geometry, not automatically a full crack length. A finite plate may require a size-dependent $Y$. The result is only meaningful if small-scale yielding and the toughness test's validity conditions hold.

## Exercises

1. A tie line has $C_\alpha=10$ and $C_\beta=50$ mass %. Find phase mass fractions for an alloy at 30 mass %.
2. Under the ideal axial composite model, $V_f=0.60$, $E_f=200$ GPa, and $E_m=3$ GPa. Find $E_L$.
3. Under the same crack geometry and toughness, how does critical crack size change when applied tensile stress doubles?

## Solutions

1. $f_\alpha=(50-30)/(50-10)=0.50$ and $f_\beta=0.50$. Both mass and composition balances are satisfied.
2. $E_L=0.6(200)+0.4(3)=121.2$ GPa. This is an axial modulus, not an isotropic modulus for the composite.
3. $a_c\propto1/\sigma^2$, so the critical size becomes one-quarter. This conclusion assumes $Y$ remains unchanged.

## Common mistakes

- Selecting a material from strength alone while ignoring toughness, corrosion, weldability, and temperature.
- Treating a phase diagram as a cooling-time diagram.
- Using engineering stress beyond necking as though area remained uniform.
- Mixing MPa m$^{1/2}$ with a crack length in mm without conversion.
- Treating tabulated typical properties as guaranteed design allowables for every product.

## Applications and limits

Use property-based screening to reduce candidate materials, then evaluate manufacturing and service constraints. A stainless steel may resist one water chemistry and suffer localized attack in another. A polymer may support a short test yet creep during years of use. Qualification needs the actual material condition, representative loading, environmental exposure, and an appropriate inspection strategy. This chapter explains models; it does not assign universal allowable stresses.

## Further reading

- [MIT OCW: Mechanics of Materials](https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/) — open modules connecting microstructure and mechanical behavior.
- [MIT OCW: Kinetic Processes in Materials](https://ocw.mit.edu/courses/3-21-kinetic-processes-in-materials-spring-2006/) — diffusion and transformation theory. Resources are linked for study, not reproduced.
