# 10. Fluid mechanics

## Learning map

Prerequisites: vectors, Newton's laws, calculus and thermodynamic properties. Learn to distinguish hydrostatics from flow, choose a control volume, and apply conservation of mass, momentum and energy. Build confidence with idealized problems before introducing viscous resistance, turbulence or compressibility. Pipe systems and turbomachinery apply these same balances to particular geometries.

## Theory

A fluid deforms continuously under a sustained shear stress. Pressure is a normal compressive stress; viscosity relates shear stress to deformation rate. Density measures mass per volume and does not determine viscosity. Under the continuum model, properties are smooth fields over length scales large compared with molecular scales. This approximation can fail in very rarefied gases or microscopic passages.

A static fluid has no shear deformation rate, so its pressure gradient balances body forces. Pressure increases with depth in a gravitational field. The hydrostatic force on a submerged surface must be integrated because lower portions carry greater pressure. Buoyancy is the resulting upward force from the surrounding pressure field and equals the weight of displaced fluid, provided the usual hydrostatic assumptions apply.

Eulerian descriptions follow fields at fixed spatial points; Lagrangian descriptions follow fluid particles. A streamline is tangent to the instantaneous velocity field. In steady flow, streamlines and particle paths coincide. A control volume is useful when the desired result is a net force or mass flow. The momentum equation must include pressure forces, weight and support forces as well as momentum crossing the boundary.

Viscosity dissipates organized mechanical energy. For a Newtonian fluid, shear stress is proportional to strain rate, with dynamic viscosity as the proportionality coefficient. Water and air are often adequately Newtonian for ordinary engineering flow; slurries, polymer melts and some food products may not be. Turbulence produces fluctuating velocity and enhanced transport. It does not remove viscosity or eliminate the no-slip condition at an ordinary stationary wall.

Bernoulli's relation is a mechanical-energy statement for restrictive conditions. In its elementary form it connects points along one streamline in steady, incompressible, inviscid flow with gravity as the body force. Pumps, turbines, heat-driven density changes and significant viscous losses require a more general balance. The velocity in a control-volume energy equation may also require a kinetic-energy correction for a nonuniform profile.

## Formula handbook

Use density $\rho$ in kg/m3, speed $V$ in m/s, dynamic viscosity $\mu$ in Pa s, pressure $p$ in Pa, length in m and force in N.

1. Hydrostatics, upward coordinate $z$, constant density over depth $h$:

$$
\frac{dp}{dz}=-\rho g,\qquad p=p_0+\rho gh.
$$

2. Hydrostatic force on a plane area, measured against a uniform reference pressure:

$$
F=\rho g h_c A.
$$

Here $h_c$ is centroid depth. For a vertical plane, center-of-pressure depth is

$$
h_{cp}=h_c+\frac{I_G}{h_cA},
$$

where $I_G$ is the second moment of area about its horizontal centroidal axis.

3. Buoyant force in a uniform-density fluid:

$$
F_B=\rho g V_{disp}.
$$

4. Volume and mass flow for a section with mean normal speed:

$$
Q=AV,\qquad \dot m=\rho Q.
$$

5. Steady mass conservation:

$$
\sum\dot m_{in}=\sum\dot m_{out}.
$$

6. Steady vector momentum balance for uniform port profiles:

$$
\sum\mathbf F=\sum_{out}\dot m\mathbf V-\sum_{in}\dot m\mathbf V.
$$

7. Bernoulli relation under the assumptions given above:

$$
\frac{p}{\rho g}+\frac{V^2}{2g}+z=\text{constant along a streamline}.
$$

8. Newtonian simple-shear law and kinematic viscosity:

$$
\tau=\mu\frac{du}{dy},\qquad \nu=\mu/\rho.
$$

9. Incompressible Newtonian momentum equation, constant viscosity:

$$
\rho\left(\frac{\partial\mathbf u}{\partial t}+\mathbf u\cdot\nabla\mathbf u\right)=-\nabla p+\mu\nabla^2\mathbf u+\rho\mathbf g,\qquad \nabla\cdot\mathbf u=0.
$$

10. Reynolds, Mach and Froude numbers:

$$
Re=\frac{\rho VL}{\mu},\qquad Ma=\frac{V}{a},\qquad Fr=\frac{V}{\sqrt{gL}}.
$$

$L$ must match the geometry and comparison; $a$ is local sound speed.

11. Drag force, with declared reference area $A_{ref}$:

$$
F_D=\frac12\rho V^2 C_D A_{ref}.
$$

12. Surface-tension pressure jump for a spherical liquid droplet:

$$
\Delta p=2\sigma/R.
$$

Here $\sigma$ is surface tension in N/m. A thin soap bubble has two interfaces and a different factor.

## Derivation

Take a small static rectangular fluid element of horizontal area $A$ and height $dz$. The upward pressure force at the bottom is $pA$; the downward pressure force at the top is $(p+dp)A$. Its weight is $\rho gA,dz$. Force balance gives $pA-(p+dp)A-\rho gA,dz=0$, so $dp/dz=-\rho g$. For constant density, integrate to obtain the linear pressure-depth relation.

For a vertical plane area, integrate $dF=\rho gh,dA$. The first area moment gives $F=\rho gh_cA$. Equating moments about the free-surface line gives $Fh_{cp}=\rho g\int h^2dA$. Using the parallel-axis theorem yields the center-of-pressure formula. Its extra positive term explains why the resultant lies below the centroid for a surface with its upper side nearer the free surface.

## Worked examples

### Example 10-A: force on a submerged gate

A vertical rectangular gate is 2 m wide and 3 m high; its top is 1 m below the water surface. Both free surface and dry side are at atmospheric pressure. Use $\rho=1000$ kg/m3 and $g=9.81$ m/s2. Area is 6 m2 and centroid depth is 2.5 m. Resultant net force is $1000(9.81)(2.5)(6)=\mathbf{147,150\ N}$. The centroidal second moment is $2(3^3)/12=4.5$ m4. Thus $h_{cp}=2.5+4.5/(2.5\times6)=\mathbf{2.80\ m}$. The gate hinges and supports must balance both this force and its moment.

### Example 10-B: an ideal horizontal nozzle

Water flows at 0.010 m3/s through a horizontal nozzle contracting from 0.100 to 0.050 m diameter. Assume steady incompressible inviscid flow with uniform section speeds. Continuity gives $V_1=1.27324$ m/s and $V_2=5.09296$ m/s. Bernoulli gives $p_1-p_2=\rho(V_2^2-V_1^2)/2=\mathbf{12.159\ kPa}$. The pressure reduction supplies the kinetic-energy increase. A real nozzle needs additional pressure drop to overcome losses; outlet speed at the specified flow is still fixed by area.

## Exercises

1. What gauge pressure occurs 4 m below a water surface? Use $\rho=1000$ kg/m3 and $g=9.81$ m/s2.
2. A 0.020 m3 body is fully submerged in water. Find buoyancy with the same density and gravity. Does its own mass enter the buoyancy formula?
3. Oil with $\rho=850$ kg/m3 and $\mu=0.10$ Pa s flows at 0.50 m/s in a 0.020 m diameter pipe. Calculate Reynolds number.

## Solutions

1. $p_g=\rho gh=39,240$ Pa, or 39.24 kPa. Add the actual surface absolute pressure to obtain absolute pressure.
2. $F_B=1000(9.81)(0.020)=196.2$ N. Body mass determines its weight and resulting motion, not the surrounding fluid's buoyant force for this prescribed displacement.
3. $Re=850(0.50)(0.020)/0.10=85$. This is firmly in the laminar range for ordinary fully developed circular-pipe flow.

## Common mistakes

Pressure acting on an open control-volume face is a force and cannot be ignored in a momentum balance. Equal volume flow does not imply equal speed in different areas. Gauge pressure is convenient only when a consistent atmospheric reference cancels. Use area moments in m4 for hydrostatics, not mass moments of inertia in kg m2. A Reynolds threshold from pipe flow is not a universal threshold for every geometry.

## Applications and limits

These balances support tank, gate, nozzle, jet, duct, bearing and piping calculations. Before using a drag coefficient, match its reference area, Reynolds range, geometry and roughness. Before neglecting compressibility, assess density variation and Mach number; low speed alone does not eliminate density changes caused by strong heating. Free-surface, multiphase, cavitating and non-Newtonian flows require additional constitutive and interface models.

## Further reading

- [MIT: Fluid Mechanics graduate-area guide](https://ga3.mit.edu/fluid-mechanics/) — topic map linking conservation laws, viscous flow, scaling and compressibility.
- [MIT Open Learning: Advanced Fluid Mechanics fundamentals](https://openlearning.mit.edu/courses-programs/mitx-courses/advanced-fluid-mechanics-1-fundamentals) — course overview and route to structured study; platform access conditions may vary.
- [TU Delft: The Basics of Transport Phenomena](https://ocw.tudelft.nl/courses/basics-transport-phenomena/) — freely viewable momentum, heat and mass transport materials.
