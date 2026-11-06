# 34 · Tribology: friction, lubrication, and wear

## Learning map

Prerequisites are statics, fluid viscosity, stress, and heat transfer. Tribology studies interacting surfaces in relative motion. It connects machine design to the condition of contacts, lubricants, contamination, and wear debris. After this chapter, distinguish a friction estimate from a lubrication model and a calibrated wear model from a universal service-life prediction.

## Theory

Real surfaces touch through asperities rather than over their complete apparent area. Local pressures can be much greater than the nominal load divided by projected area. Friction can arise from adhesion, deformation, ploughing, and viscous shear. A coefficient of friction is a property of the interacting system and its condition, not a permanent material constant. Surface finish, temperature, speed, humidity, contamination, and running-in can change it.

Static friction adjusts to oppose impending relative motion up to a limiting magnitude. Kinetic friction is often approximated with a constant coefficient, but velocity dependence, stick-slip, and transition effects may matter. Rolling contact reduces some sliding losses, yet bearing contacts can still contain microslip, hysteretic loss, lubricant churning, and fatigue.

Lubrication regimes are distinguished by how the load is supported. In boundary lubrication, surface films and asperity contacts dominate. In mixed lubrication, fluid pressure and asperity contacts both carry load. In full-film lubrication, a fluid film largely separates the surfaces. Hydrodynamic pressure arises from viscous flow through a converging gap; hydrostatic bearings receive pressure from an external supply. Elastohydrodynamic contacts combine elastic deformation with strong pressure effects on viscosity, as in many rolling bearings and gears.

Wear is progressive material loss or damage associated with surface interaction. Abrasive wear involves cutting or ploughing; adhesive wear involves junction formation and transfer; fatigue wear develops through repeated contact loading; corrosive wear involves chemistry; erosion involves particle or fluid impact. More than one mechanism can operate at once. A test that reproduces only the nominal pressure may fail to reproduce the real wear mechanism.

Lubricant selection must consider viscosity at operating temperature, additives, compatibility with seals and materials, contamination control, oxidation, supply, and maintenance. Increasing viscosity can improve film formation but increase viscous losses and impair cold starts. The Stribeck curve organizes friction trends with operating conditions; it is not a universal numerical design curve independent of geometry.

## Formula handbook

1. Coulomb static limit: $|F_t|\leq\mu_sN$, where normal force $N$ and tangential force $F_t$ are in N. Equality describes impending slip.
2. A simple sliding model is $F_t=\mu_kN$ in magnitude, with friction opposite relative motion.
3. Frictional heat generation: $P_f=F_t v$ in W for sliding speed $v$ in m/s. Heat partition between bodies requires a thermal model.
4. For a uniformly loaded circular friction surface with inner and outer radii $r_i,r_o$, the effective radius under uniform pressure is $r_m=(2/3)(r_o^3-r_i^3)/(r_o^2-r_i^2)$. Torque is $T=\mu Nr_m$ per friction interface.
5. Under the ideal uniform-wear assumption for an annular interface, $r_m=(r_o+r_i)/2$. Do not interchange this assumption with uniform pressure.
6. Newtonian shear: $\tau=\mu\,du/dy$, with dynamic viscosity $\mu$ in Pa s. In a simple parallel Couette film of thickness $h$, $\tau=\mu U/h$.
7. Couette drag power over area $A$: $P=\mu A U^2/h$, assuming constant viscosity and no pressure-driven contribution.
8. Kinematic viscosity: $\nu=\mu/\rho$ in m²/s. One centistoke is $10^{-6}\ \mathrm{m^2/s}$.
9. Specific film ratio: $\lambda=h_{\min}/\sqrt{R_{q1}^2+R_{q2}^2}$, using minimum film thickness and RMS roughnesses in consistent length units. Regime boundaries are approximate, not universal guarantees.
10. Archard's simplified wear law: $V=kWL/H$, where $V$ is removed volume in m³, load $W$ in N, sliding distance $L$ in m, hardness $H$ in Pa, and $k$ a dimensionless calibrated wear coefficient. Alternative definitions of wear coefficient have different units.
11. For uniform wear over area $A$, mean depth is $d=V/A$; actual scars are rarely perfectly uniform.
12. In a stationary-coordinate thin incompressible film, the one-dimensional Reynolds equation for constant viscosity and spatially uniform surface velocities $U_1,U_2$ is

$$
\frac{d}{dx}\left(h^3\frac{dp}{dx}\right)=6\mu(U_1+U_2)\frac{dh}{dx}+12\mu\frac{\partial h}{\partial t}.
$$

It assumes a thin film, negligible inertia, no slip, and appropriate pressure/cavitation boundary conditions. The steady form omits the squeeze term. The gap $h$ is in m, pressure $p$ in Pa, and $x$ in m.

## Derivation

For a flat moving plate separated from a fixed plate by a uniform Newtonian film, take steady flow, no pressure gradient, negligible inertia, and no slip. The momentum equation reduces to $d^2u/dy^2=0$. Integrating twice gives $u=C_1y+C_2$. Boundary conditions $u(0)=0$ and $u(h)=U$ give $u=Uy/h$. Therefore $\tau=\mu U/h$, total force $F=\tau A$, and power $P=FU=\mu AU^2/h$. Halving the gap doubles the ideal viscous loss at fixed speed and viscosity. Real contacts may instead heat the lubricant and change viscosity, so the constant-property prediction is not automatically self-consistent.

## Worked examples

### Example 1: Viscous sliding loss

A plate of area 0.01 m² moves at 2 m/s across a 0.1 mm oil film. Assume $\mu=0.08\ \mathrm{Pa\,s}$, parallel surfaces, and negligible pressure gradient. Convert $h=10^{-4}$ m. Shear stress is $0.08(2)/10^{-4}=1600$ Pa; force is $1600(0.01)=16$ N; power is $16(2)=32$ W. The contact must reject this heat at steady state. This estimate does not establish film stability or account for edges, starvation, or heating-induced viscosity change.

### Example 2: Calibrated wear estimate

A laboratory wear model uses $k=2\times10^{-6}$, $W=500$ N, $L=10000$ m, and $H=2\times10^9$ Pa. Archard's relation gives $V=2\times10^{-6}(500)(10000)/(2\times10^9)=5\times10^{-9}$ m³, or 5 mm³. If spread uniformly over 100 mm², mean depth is 0.05 mm. This is a model result for the supplied coefficient, not a material's guaranteed wear rate. A different lubricant, abrasive contamination, or transition of mechanism can invalidate the coefficient entirely.

## Exercises

1. A block has normal load 200 N and static friction coefficient 0.30. What tangential force initiates slip in the ideal Coulomb model?
2. If the film gap in Example 1 doubles with all other parameters unchanged, find drag power.
3. Two surfaces have $R_q=0.2$ and 0.3 micrometres. A calculated minimum film thickness is 0.5 micrometres. Find $\lambda$ and explain what it cannot prove.

## Solutions

1. The limiting force is $\mu_sN=60$ N. Below this value, actual static friction balances the applied tangential load rather than remaining at 60 N.
2. Since $P\propto1/h$, power becomes 16 W. The changed gap may also alter load support in a real bearing, outside this simple Couette model.
3. $\lambda=0.5/\sqrt{0.2^2+0.3^2}=1.387$. This suggests substantial surface interaction may need consideration; it does not certify separation everywhere or establish wear life. Roughness statistics, film prediction, alignment, and transient loading remain relevant.

## Common mistakes

Using a dry friction coefficient for a lubricated contact, treating hardness in MPa as Pa, and confusing dynamic with kinematic viscosity are major errors. Archard's coefficient must come from a comparable contact and be defined with its units. A polished surface is not always optimal: lubricant retention, texture direction, and surface chemistry matter.

## Applications and limits

For bearings, seals, gears, guides, clutches, and brakes, combine contact mechanics, lubrication, thermal balance, and contamination control. Record the observed damage mechanism before choosing a corrective action. Vibration, oil debris, temperature, and inspection provide complementary evidence. A lower friction coefficient does not automatically imply lower wear or higher reliability. Manufacturer limits and representative testing are necessary for real selection.

## Further reading

- [ESA, Space Tribology Handbook overview](https://www.esa.int/esapub/bulletin/bullet94/ROB.pdf) — institutional overview of tribological phenomena and space-specific considerations; not the full handbook.
- [ASM Handbook Volume 18 publisher contents](https://www.asminternational.org/wp-content/uploads/files/27533578/27533578-toc.pdf) — topic map for a commercial reference; this link is a contents preview, not a free full textbook.
