# 17. Mass transfer

## Learning map

Prerequisites: conservation laws, concentration units, fluid flow and differential equations. Learn to distinguish molecular diffusion from bulk transport, use film coefficients consistently, account for interfacial equilibrium and estimate transient approach to equilibrium. Applications include drying, membranes, gas absorption, corrosion control and water-treatment aeration.

## Theory

Mass transfer is transport of a chemical species relative to a chosen reference frame or through a chosen boundary. Molecular diffusion arises from molecular motion and chemical-potential differences. In simple dilute systems, concentration gradients can represent the driving force. Bulk advection transports species with the mixture velocity. Mixing can reduce concentration differences in the bulk while a thin near-interface region still controls the overall transfer rate.

A concentration must include its basis. Molar concentration is moles per volume; mass concentration is mass per volume; mole fraction and mass fraction are dimensionless but are not numerically identical unless the components have equal molecular masses. Gas concentrations also depend on pressure and temperature. A concentration reported in mg/L must be converted carefully before combining with SI diffusivity or flow quantities.

Diffusive flux is defined relative to a reference velocity, such as the molar-average or mass-average velocity. Total flux through a stationary surface includes bulk transport as well as diffusion. In equimolar counterdiffusion, the total molar flux can vanish while each species still diffuses in opposite directions. Evaporation through stagnant carrier gas creates a net molar flow, so the simplest linear Fick expression for total flux needs correction.

Film models replace a detailed concentration boundary layer by a transfer coefficient multiplying a bulk-to-interface concentration difference. The coefficient depends on flow and geometry; it is not solely a material property. At an interface, concentrations on the two sides generally differ according to equilibrium, even when chemical potentials match. Therefore an overall resistance must convert both sides to a common driving-force basis.

Diffusion, reaction and advection often compete. A reaction can maintain a low concentration and enhance uptake, or deplete a reactant before it reaches the desired location. A well-mixed tank model assumes the liquid bulk is uniform; it does not imply infinite transfer through bubble or wall boundary layers. The volumetric coefficient $k_La$ combines a liquid-side coefficient with interfacial area per liquid volume, making it useful for aeration and absorption models.

## Formula handbook

Use diffusivity $D_{AB}$ in m2/s, concentration $c_A$ in mol/m3, molar flux in mol/(m2 s), transfer coefficient $k_c$ in m/s, and time in s. Mass-concentration equations have analogous forms when the basis is used consistently.

1. Binary Fickian diffusive molar flux relative to the molar-average velocity, constant total concentration $c$:

$$
\mathbf J_A=-cD_{AB}\nabla y_A=-D_{AB}\nabla c_A.
$$

2. Total molar flux through a stationary plane:

$$
N_A=J_A+y_A(N_A+N_B).
$$

3. Steady one-dimensional diffusion through a slab, constant $D$ and equimolar counterdiffusion or no bulk transport:

$$
N_A=D_{AB}\frac{c_{A,1}-c_{A,2}}{L},\qquad \dot n_A=AN_A.
$$

4. Species balance with constant diffusivity, incompressible mixture and molar production rate $r_A$:

$$
\frac{\partial c_A}{\partial t}+\mathbf u\cdot\nabla c_A=D_{AB}\nabla^2c_A+r_A.
$$

5. Characteristic diffusion time:

$$
t_D\sim L^2/D_{AB}.
$$

This is an order-of-magnitude timescale; exact approach times depend on geometry and boundary conditions.

6. Film transfer law:

$$
N_A=k_c(c_{A,s}-c_{A,b}).
$$

Subscripts $s$ and $b$ denote interface and bulk; sign follows the chosen direction.

7. Sherwood, Schmidt and mass Peclet numbers:

$$
Sh=\frac{k_cL}{D_{AB}},\qquad Sc=\frac{\nu}{D_{AB}},\qquad Pe_m=\frac{VL}{D_{AB}}=Re\,Sc.
$$

8. First-order reaction-diffusion comparison, rate constant $k_r$ in 1/s:

$$
Da_D=\frac{k_rL^2}{D_{AB}}.
$$

9. Gas-liquid interfacial equilibrium in one specified concentration convention:

$$
c_{A,g}^{*}=m\,c_{A,l}.
$$

Here $m$ is the dimensionless gas-to-liquid concentration partition ratio for both concentrations in mol/m3. Other Henry-law conventions have different units and reciprocal forms.

10. Two-film overall coefficient on the gas concentration basis:

$$
N_A=K_g(c_{A,g,b}-m c_{A,l,b}),\qquad \frac1{K_g}=\frac1{k_g}+\frac{m}{k_l}.
$$

11. Well-mixed batch liquid with constant equilibrium concentration and no reaction:

$$
\frac{dC}{dt}=k_La(C^*-C),\qquad C(t)=C^*-(C^*-C_0)e^{-k_Lat}.
$$

$k_La$ is in 1/s; $C$ may be mass concentration if every term uses that basis.

12. Binary ideal-gas diffusion of A through stagnant B, constant pressure and temperature:

$$
N_A=\frac{D_{AB}c}{L}\ln\left(\frac{1-y_{A,2}}{1-y_{A,1}}\right),\qquad N_B=0.
$$

13. Simple solution-diffusion membrane model:

$$
N_A=\frac{\mathcal P_A}{L}(p_{A,1}-p_{A,2}),\qquad \mathcal P_A=D_AS_A.
$$

Solubility $S_A$ is mol/(m3 Pa), so permeability $\mathcal P_A$ is mol/(m s Pa). Actual membranes may show nonlinear sorption and coupled transport.

## Derivation

Derive the two-film overall resistance to make the concentration basis explicit. At steady transfer from gas to liquid, the same flux crosses each film:

$$
N_A=k_g(c_{g,b}-c_{g,i})=k_l(c_{l,i}-c_{l,b}).
$$

Interfacial equilibrium gives $c_{g,i}=m c_{l,i}$. Add the gas-film drop to $m$ times the liquid-film drop:

$$
c_{g,b}-m c_{l,b}=N_A\left(\frac1{k_g}+\frac{m}{k_l}\right).
$$

Comparison with the overall transfer law gives the resistance relation. A large gas-to-liquid partition ratio amplifies the liquid-film resistance on this gas concentration basis. Swapping to a pressure-based Henry constant without converting units would change the equation and produce a dimensional error.

## Worked examples

### Example 17-A: diffusion across a stagnant layer

A dilute species diffuses through a 0.0020 m layer over area 0.10 m2. Use constant diffusivity $2.0\times10^{-9}$ m2/s and boundary concentrations 5.0 and 1.0 mol/m3. Assume steady one-dimensional diffusion, no reaction and no relevant bulk transport. Flux is $D\Delta c/L=\mathbf{4.0\times10^{-6}\ mol/(m^2s)}$. Transfer rate is **$4.0\times10^{-7}$ mol/s**, or **0.00144 mol/h**. Doubling thickness at the same boundary concentrations halves this steady rate; it also increases the diffusion timescale by a factor of four.

### Example 17-B: dissolved-gas approach to equilibrium

A well-mixed 2.0 m3 liquid tank begins with dissolved-gas concentration zero. The maintained equilibrium concentration is 8.0 mg/L and the supplied $k_La$ is 0.030 s-1. Ignore reaction, outflow and variation of equilibrium conditions. After 100 s, $C=8[1-e^{-0.03(100)}]=\mathbf{7.60170\ mg/L}$. Since 1 mg/L equals 0.001 kg/m3, the tank then contains $2(0.00760170)=\mathbf{0.0152034\ kg}$ of dissolved gas. This is a transfer model with prescribed parameters, not an aerator performance prediction.

## Exercises

1. A 0.0010 m slab has diffusivity $10^{-9}$ m2/s and concentration difference 2.0 mol/m3. Find steady flux under the same assumptions as Example 17-A.
2. A film coefficient is $10^{-4}$ m/s, reference length 0.010 m and diffusivity $2\times10^{-9}$ m2/s. Find Sherwood number.
3. A batch tank begins at zero concentration and has constant $k_La=0.020$ s-1. Find the time to reach 90% of equilibrium concentration.

## Solutions

1. $N_A=10^{-9}(2)/0.001=2.0\times10^{-6}$ mol/(m2 s). Its diffusion timescale is approximately $L^2/D=1000$ s, so a steady approximation should be justified relative to the observation time.
2. $Sh=10^{-4}(0.010)/(2\times10^{-9})=500$. This dimensionless value compares the film coefficient with a diffusion scale; it is not an efficiency.
3. $0.9=1-e^{-0.020t}$ gives $t=-\ln(0.1)/0.020=115.129$ s.

## Common mistakes

Distinguish total flux from diffusive flux and specify the reference frame. Do not confuse mass fraction with molar concentration. A tabulated Henry constant must be used with its exact convention and temperature. Transfer coefficients depend on hydrodynamics and area definition. The gas-liquid interface can have unequal concentrations in the two phases while still satisfying equilibrium. Increasing agitation does not necessarily change equilibrium solubility, although it often changes the rate of approach.

## Applications and limits

These balances appear in drying, evaporation, humidification, membrane separation and oxygen transfer. Coupled heat and mass transfer can change surface temperature and thus the equilibrium driving force. Real aeration needs measured or justified $k_La$, oxygen demand, gas-phase depletion and water-quality corrections. Reactive absorption, multicomponent diffusion and porous media require additional constitutive relations beyond the binary dilute models introduced here.

## Further reading

- [TU Delft: Mass transfer introduction](https://ocw.tudelft.nl/course-lectures/mass-transfer-introduction/) — freely viewable transport course material.
- [TU Delft: The Basics of Transport Phenomena](https://ocw.tudelft.nl/courses/basics-transport-phenomena/) — connections among momentum, heat and mass transport.
- [MIT OCW: Intermediate Heat and Mass Transfer](https://ocw.mit.edu/courses/2-51-intermediate-heat-and-mass-transfer-fall-2008/) — deeper analytical treatment after the introductory balances.
