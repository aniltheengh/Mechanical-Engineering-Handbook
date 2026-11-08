"""Chapter 42 numerical/source checks; Python standard library only.

Run from any directory. Checks the stated educational models, not certification.
"""
from math import cos, isclose, pi, sin, sqrt
from pathlib import Path
import re

checks = 0


def close(a, b, label, atol=1e-10, rtol=1e-10):
    global checks
    assert isclose(a, b, abs_tol=atol, rel_tol=rtol), f"{label}: {a} != {b}"
    checks += 1


def vector(a, b, label, atol=1e-10):
    assert len(a) == len(b)
    for i, (x, y) in enumerate(zip(a, b)):
        close(x, y, f"{label}[{i}]", atol)


def matrix(a, b, label, atol=1e-10):
    assert len(a) == len(b)
    for i, (x, y) in enumerate(zip(a, b)):
        vector(x, y, f"{label}[{i}]", atol)


def diagonal(v):
    return [[v[i] if i == j else 0.0 for j in range(3)] for i in range(3)]


I = diagonal([1.0] * 3)
ZERO = diagonal([0.0] * 3)


def transpose(a):
    return list(map(list, zip(*a)))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def mv(a, b):
    return [dot(row, b) for row in a]


def mm(a, b):
    return [[dot(row, col) for col in transpose(b)] for row in a]


def add(a, b, factor=1.0):
    return [[a[i][j] + factor*b[i][j] for j in range(3)] for i in range(3)]


def scale(a, factor):
    return [[factor*x for x in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(3))


def contract(a, b):
    return sum(dot(x, y) for x, y in zip(a, b))


def det(a):
    return dot(a[0], cross(a[1], a[2]))


def inverse(a):
    cofactors = [cross(a[1], a[2]), cross(a[2], a[0]), cross(a[0], a[1])]
    return scale(transpose(cofactors), 1.0/det(a))


def rotation(angle):
    return [[cos(angle), -sin(angle), 0.0], [sin(angle), cos(angle), 0.0], [0.0, 0.0, 1.0]]


def green(f):
    return scale(add(mm(transpose(f), f), I, -1), 0.5)


def compliance(stress, young, nu):
    return add(scale(stress, (1+nu)/young), I, -nu*trace(stress)/young)


def deviator(a):
    return add(a, I, -trace(a)/3)


def mises(stress):
    dev = deviator(stress)
    return sqrt(1.5*contract(dev, dev))


# Example 1: finite stretch followed by rotation, mass and line-length checks.
lengths = [0.100, 0.040, 0.020]
stretch = diagonal([1.10, 0.95, 1.00])
f = mm(rotation(pi/6), stretch)
j = det(f)
v0 = lengths[0]*lengths[1]*lengths[2]
v = j*v0
rho0 = 7800.0
rho = rho0/j
close(j, 1.045, "Example 1 volume ratio")
close(v, 0.00008360, "Example 1 volume")
close(rho, 7464.1148, "Example 1 density", 0.00005)
close(rho*v, 0.624000, "Example 1 mass")
close(rho*v, rho0*v0, "Mass conservation")
matrix(f, [[0.95262794, -0.475, 0], [0.55, 0.82272413, 0], [0, 0, 1]],
       "Printed deformation gradient", 5e-9)
eg = green(f)
matrix(eg, diagonal([0.105000, -0.048750, 0]), "Example 1 Green strain")
matrix(eg, green(stretch), "Superposed rotation does not alter Green strain")
edges = [mv(f, [lengths[k] if i == k else 0.0 for i in range(3)]) for k in range(3)]
vector([sqrt(dot(edge, edge)) for edge in edges], [0.110, 0.038, 0.020], "Line lengths")
close(dot(edges[0], cross(edges[1], edges[2])), v, "Independent edge-based volume")
h = add(f, I, -1)
linear = scale(add(h, transpose(h)), 0.5)
vector([linear[0][0], linear[1][1], linear[0][1]],
       [-0.0473721, -0.1772759, 0.037500], "Linearized strains", 5e-8)
matrix(add(linear, scale(mm(transpose(h), h), 0.5)), eg, "Exact quadratic correction")
matrix(mm(f, inverse(f)), I, "Matrix inverse")

# Example 2: all computation in SI; stress comparisons below convert to MPa.
stress = [[120e6, 30e6, 0], [30e6, 40e6, 0], [0, 0, 20e6]]
n = [0.6, 0.8, 0.0]
t = mv(stress, n)
sn = dot(n, t)
ts = [t[i]-sn*n[i] for i in range(3)]
close(dot(n, n), 1, "Unit normal")
vector([x/1e6 for x in t], [96, 50, 0], "Example 2 traction")
close(sn/1e6, 97.600, "Normal traction")
vector([x/1e6 for x in ts], [37.44, -28.08, 0], "Shear traction")
close(sqrt(dot(ts, ts))/1e6, 46.800, "Shear magnitude")
close(dot(n, ts), 0, "Orthogonal traction components", 1e-8)
mean = (stress[0][0]+stress[1][1])/2
radius = sqrt(((stress[0][0]-stress[1][1])/2)**2 + stress[0][1]**2)
principal = [mean+radius, mean-radius, stress[2][2]]
vector([x/1e6 for x in principal], [130, 30, 20], "Principal stresses")
for value, direction in zip(principal, [[3, 1, 0], [-1, 3, 0], [0, 0, 1]]):
    vector(mv(stress, direction), [value*x for x in direction], "Eigen-equation")
close(trace(stress)/1e6, 180, "First invariant")
close(det(stress), principal[0]*principal[1]*principal[2], "Third invariant")
close(mises(stress)/1e6, 105.35654, "Von Mises stress", 5e-6)
young, nu = 210e9, 0.30
g = young/(2*(1+nu))
k = young/(3*(1-2*nu))
lame = k-2*g/3
eps = compliance(stress, young, nu)
close(g/1e9, 80.76923, "Shear modulus", 5e-6)
close(k/1e9, 175, "Bulk modulus")
vector([eps[i][i] for i in range(3)], [0.0004857143, -0.00000952381, -0.0001333333],
       "Example 2 normal strains", 5e-11)
close(eps[0][1], 0.0001857143, "Tensor shear", 5e-11)
close(2*eps[0][1], 0.0003714286, "Engineering shear", 5e-11)
close(trace(eps), 0.0003428571, "Volumetric strain", 5e-11)
close(trace(eps), trace(stress)/(3*k), "Independent volumetric elastic relation")
matrix(add(scale(eps, 2*g), I, lame*trace(eps)), stress, "Stiffness recovery", 1e-7)
energy = 0.5*contract(stress, eps)
close(energy, 33190.476, "Energy density", 0.0005)
energy_split = contract(deviator(stress), deviator(stress))/(4*g) + trace(stress)**2/(18*k)
close(energy, energy_split, "Volumetric/deviatoric energy decomposition")
q = rotation(37*pi/180)
rot_stress = mm(mm(q, stress), transpose(q))
rot_eps = mm(mm(q, eps), transpose(q))
vector(mv(rot_stress, mv(q, n)), mv(q, t), "Traction covariance", 1e-7)
close(trace(rot_stress), trace(stress), "Trace rotation invariant")
close(det(rot_stress), det(stress), "Determinant rotation invariant")
close(mises(rot_stress), mises(stress), "Von Mises rotation invariant")
close(0.5*contract(rot_stress, rot_eps), energy, "Energy rotation invariant")

# Finite-kinematic stress transformations and work conjugacy, without Hooke's law.
finv = inverse(f)
p = scale(mm(stress, transpose(finv)), j)
s = mm(finv, p)
matrix(s, transpose(s), "Second Piola stress symmetry", 1e-7)
area = cross(mv(f, [0, 1, 0]), mv(f, [0, 0, 1]))
vector(area, [j*x for x in mv(transpose(finv), [1, 0, 0])], "Nanson area formula")
vector(mv(stress, area), mv(p, [1, 0, 0]), "Reference/current traction force", 1e-7)
velgrad = [[0.02, 0.03, 0], [-0.01, -0.005, 0.004], [0, 0.002, 0.01]]
fdot = mm(velgrad, f)
d = scale(add(velgrad, transpose(velgrad)), 0.5)
egdot = scale(add(mm(transpose(fdot), f), mm(transpose(f), fdot)), 0.5)
close(contract(p, fdot), contract(s, egdot), "Piola work conjugacy")
close(contract(p, fdot), j*contract(stress, d), "Reference/current stress power")
step = 1e-5
jdot_fd = (det(add(f, fdot, step))-det(add(f, fdot, -step)))/(2*step)
close(jdot_fd, j*trace(d), "Jacobian rate finite difference", 1e-9)

# Exercise 1: large rigid rotation, finite versus infinitesimal strain.
quarter = rotation(pi/2)
close(det(quarter), 1, "Exercise 1 determinant")
matrix(green(quarter), ZERO, "Exercise 1 finite strain")
rh = add(quarter, I, -1)
matrix(scale(add(rh, transpose(rh)), 0.5), diagonal([-1, -1, 0]),
       "Exercise 1 linearized strain")

# Exercise 2: hydrostatic compression.
hydro = diagonal([-15e6]*3)
hydro_eps = compliance(hydro, 200e9, 0.25)
matrix(hydro_eps, diagonal([-0.000037500]*3), "Exercise 2 strains")
close(trace(hydro_eps), -0.000112500, "Exercise 2 volume strain")
close(mises(hydro), 0, "Exercise 2 von Mises")
close(200/(3*(1-2*0.25)), 133.3333, "Exercise 2 bulk modulus GPa", 0.00005)

# Exercise 3: local differentiation plus independent surface quadrature.
box = [0.1, 0.2, 0.01]
alpha, beta, density = 2000.0, 1000.0, 1000.0


def field(position):
    x, y, _ = position
    return [[alpha*x, beta*y, 0], [beta*y, 0, 0], [0, 0, 0]]


point = [0.04, 0.07, 0.003]
div = [0.0]*3
for axis in range(3):
    plus, minus = point.copy(), point.copy()
    plus[axis] += step
    minus[axis] -= step
    a, b = field(plus), field(minus)
    for i in range(3):
        div[i] += (a[i][axis]-b[i][axis])/(2*step)
vector(div, [3000, 0, 0], "Exercise 3 stress divergence", 1e-7)
body = [-x/density for x in div]
vector(body, [-3, 0, 0], "Exercise 3 body force per mass")
volume = box[0]*box[1]*box[2]
close(volume, 0.000200, "Exercise 3 volume")
body_force = [density*volume*x for x in body]
vector(body_force, [-0.600000, 0, 0], "Exercise 3 net body force")
surface_force, surface_moment = [0.0]*3, [0.0]*3
for axis in range(3):
    tangents = [i for i in range(3) if i != axis]
    face_area = box[tangents[0]]*box[tangents[1]]
    for side in (0, 1):
        normal = [0.0]*3
        normal[axis] = 2*side-1
        # Two-point Gauss rule integrates these linear forces/quadratic moments exactly.
        for eta in (-1/sqrt(3), 1/sqrt(3)):
            for zeta in (-1/sqrt(3), 1/sqrt(3)):
                position = [0.0]*3
                position[axis] = side*box[axis]
                for tangent, coord in zip(tangents, (eta, zeta)):
                    position[tangent] = box[tangent]*(1+coord)/2
                force = [x*face_area/4 for x in mv(field(position), normal)]
                moment = cross(position, force)
                for i in range(3):
                    surface_force[i] += force[i]
                    surface_moment[i] += moment[i]
body_moment = cross([x/2 for x in box], body_force)
vector(surface_force, [0.6, 0, 0], "Integrated boundary traction")
vector([a+b for a, b in zip(surface_force, body_force)], [0]*3, "Net force equilibrium")
vector([a+b for a, b in zip(surface_moment, body_moment)], [0]*3, "Net moment equilibrium")

# Printed-value checks prevent the chapter and these calculations silently diverging.
chapter = Path(__file__).resolve().parents[1]/"chapters"/"42-continuum-mechanics.md"
source = chapter.read_text(encoding="utf-8")
tokens = ["0.95262794", "0.82272413", "**1.045**", "0.00008360", "7464.1148",
          "0.624000", "0.105000", "-0.048750", "0.110, 0.038, and 0.020",
          "-0.0473721", "-0.1772759", "0.037500", "(96,50,0)", "97.600",
          "37.44,-28.08,0", "46.800", "130, 30, and 20", "I_1=180", "105.35654",
          "80.76923", "K=175", "0.0004857143", "-0.00000952381", "-0.0001333333",
          "0.0001857143", "0.0003714286", "0.0003428571", "33190.476", "J=1",
          r"\mathbf E_G=\mathbf0", "(-1,-1,0)", "133.3333", "-0.000037500",
          "-0.000112500", r"\sigma_{vm}=0", "3000,0,0", "(-3,0,0)", "0.000200",
          "(-0.600000,0,0)"]
for token in tokens:
    assert token in source, f"Printed result missing or changed: {token}"
assert re.findall(r"^## (.+)$", source, re.MULTILINE) == [
    "Learning map", "Theory", "Formula handbook", "Derivation", "Worked examples",
    "Exercises", "Solutions", "Common mistakes", "Applications and limits", "Further reading"]
assert len(re.findall(r"^### Example [12]:", source, re.MULTILINE)) == 2
for section in ("Exercises", "Solutions"):
    body_text = source.split(f"## {section}\n", 1)[1].split("\n## ", 1)[0]
    assert re.findall(r"^(\d)\. ", body_text, re.MULTILINE) == ["1", "2", "3"]
for local_link in re.findall(r"\]\(([^:()]+\.md)\)", source):
    assert (chapter.parent/local_link).is_file(), f"Broken local link: {local_link}"
print(f"PASS: 2 continuum-mechanics worked examples and 3 solved exercises; "
      f"{checks} numerical, invariant, and conservation checks; {len(tokens)} printed-value checks.")
print(f"PASS: chapter structure and local links; {len(source.split())} source words.")
