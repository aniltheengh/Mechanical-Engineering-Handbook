"""Verify 20 worked examples in chapters 04-07 and 18-23 using the standard library.

These checks cover arithmetic and selected independent physical identities, not
engineering certification or an exhaustive validation of all chapter prose.
Run: python -B scripts/verify_mechanics.py
"""

from math import atan, atan2, cos, degrees, exp, hypot, isclose, pi, sin, sqrt
from pathlib import Path
from statistics import mean, stdev

checks = 0
examples = 0


def close(actual, expected, *, rel=2e-5, absolute=1e-10):
    global checks
    assert isclose(actual, expected, rel_tol=rel, abs_tol=absolute), (actual, expected)
    checks += 1


def truth(condition):
    global checks
    assert condition
    checks += 1


# 04.1: independently check the published beam reactions by equilibrium.
ra, rb, load, span, position, udl = 14000, 10000, 12000, 6, 2, 2000
close(ra + rb - load - udl * span, 0)
close(rb * span - load * position - udl * span**2 / 2, 0)
examples += 1

# 04.2: contact force and static-friction feasibility.
weight, slope = 80 * 9.81, 25 * pi / 180
normal, tangential = weight * cos(slope), weight * sin(slope)
close(normal, 711.27)
close(tangential, 331.67)
close(0.5 * normal, 355.64)
truth(tangential < 0.5 * normal)
close(degrees(atan(0.5)), 26.565)
examples += 1

# 05.1: cart force, motion, and independent work-energy balance.
mass, drive, resistance, duration = 15, 80, 20, 3
acceleration = (drive - resistance) / mass
velocity, distance = acceleration * duration, acceleration * duration**2 / 2
close(acceleration, 4)
close(velocity, 12)
close(distance, 18)
close((drive - resistance) * distance, mass * velocity**2 / 2)
close(mass * velocity**2 / 2, 1080)
examples += 1

# 05.2: disk work and angular impulse.
inertia, torque, duration = 10 * 0.2**2 / 2, 4, 2
alpha = torque / inertia
omega, rotation = alpha * duration, alpha * duration**2 / 2
close(inertia, 0.2)
close(alpha, 20)
close(omega, 40)
close(rotation, 40)
close(torque * rotation, 160)
close(torque * rotation, inertia * omega**2 / 2)
close(torque * duration, inertia * omega)
examples += 1

# 06.1: cantilever stress, deflection, and strain-energy consistency.
force, length, width, height, young = 1000, 0.5, 0.04, 0.06, 200e9
second_moment = width * height**3 / 12
close(second_moment, 7.2e-7)
close(force * length * height / (2 * second_moment) / 1e6, 20.833)
deflection = force * length**3 / (3 * young * second_moment)
close(deflection * 1000, 0.28935)
energy = force**2 * length**3 / (6 * young * second_moment)
close(2 * energy / force, deflection)
examples += 1

# 06.2: circular shaft and equivalent stress.
polar = pi * 0.04**4 / 32
shear = 400 * 0.02 / polar
twist = 400 / (80e9 * polar)
close(polar, 2.51327e-7)
close(shear / 1e6, 31.831)
close(twist, 0.019894)
close(degrees(twist), 1.140, rel=4e-4)
close(sqrt(3) * shear / 1e6, 55.133)
examples += 1

# 07.1: distinct free and restrained thermal cases.
thermal_strain = 11e-6 * 60
close(thermal_strain * 2 * 1000, 1.32)
close(-200e9 * thermal_strain / 1e6, -132)
close((-200e9 * thermal_strain) / 200e9 + thermal_strain, 0)
examples += 1

# 07.2: reconstruct stress intensity at the critical crack length.
critical_a = (50e6 / (1.12 * 150e6))**2 / pi
close(critical_a * 1000, 28.195)
close(1.12 * 150e6 * sqrt(pi * critical_a), 50e6)
examples += 1

# 18.1: ideal gearbox and power conservation.
input_power, rpm, ratio, diameter = 5000, 1500, 3, 0.060
input_torque = input_power / (2 * pi * rpm / 60)
output_rpm, output_torque = rpm / ratio, ratio * input_torque
tangential_force = 2 * input_torque / diameter
close(input_torque, 31.831)
close(output_rpm, 500)
close(output_torque, 95.493)
close(tangential_force, 1061.03)
close(tangential_force * sin(20 * pi / 180) / cos(20 * pi / 180), 386.18)
close(output_torque * 2 * pi * output_rpm / 60, input_power)
examples += 1

# 18.2: basic bearing rating life, unit conversion, and load scaling.
life_million = (20 / 5)**3
close(life_million, 64)
close(life_million * 1e6 / (60 * 1200), 888.89)
close((20 / 2.5)**3 / life_million, 8)
examples += 1

# 19.1: compare analytical slider velocity with a central difference.
radius, rod, angle, speed = 0.05, 0.2, pi / 3, 10


def slider(theta):
    return radius * cos(theta) + sqrt(rod**2 - radius**2 * sin(theta)**2)


derivative = -radius * sin(angle) - radius**2 * sin(angle) * cos(angle) / sqrt(
    rod**2 - radius**2 * sin(angle)**2
)
step = 1e-6
finite_difference = (slider(angle + step) - slider(angle - step)) / (2 * step)
close(slider(angle), 0.220256)
close(derivative, -0.0488454)
close(derivative, finite_difference, rel=1e-8)
close(derivative * speed, -0.488454)
examples += 1

# 19.2: generic four-bar mobility and strict Grashof inequality.
lengths = sorted([30, 70, 80, 100])
close(3 * (4 - 1) - 2 * 4, 1)
close(lengths[0] + lengths[-1], 130)
close(lengths[1] + lengths[2], 150)
truth(lengths[0] + lengths[-1] < lengths[1] + lengths[2])
examples += 1

# 20.1: oscillator free response and characteristic roots.
mass, stiffness, damping = 2, 800, 8
wn = sqrt(stiffness / mass)
critical = 2 * sqrt(stiffness * mass)
zeta = damping / critical
wd = wn * sqrt(1 - zeta**2)
close(wn, 20)
close(wn / (2 * pi), 3.18310)
close(critical, 80)
close(zeta, 0.1)
close(wd, 19.89975)
close(exp(-zeta * wn), 0.135335)
root = complex(-zeta * wn, wd)
close(abs(mass * root**2 + damping * root + stiffness), 0)
examples += 1

# 20.2: complex dynamic stiffness and phase.
frequency, force_amplitude = 10, 10
dynamic_stiffness = complex(stiffness - mass * frequency**2, damping * frequency)
response = force_amplitude / dynamic_stiffness
close(abs(dynamic_stiffness), 605.310)
close(abs(response) * 1000, 16.5205)
close(atan2(dynamic_stiffness.imag, dynamic_stiffness.real), 0.132552)
close(degrees(atan2(dynamic_stiffness.imag, dynamic_stiffness.real)), 7.59464)
close(abs(dynamic_stiffness * response - force_amplitude), 0)
examples += 1

# 21.1: turning estimate in consistent millimetre/minute units.
rpm = 1000 * 120 / (pi * 50)
feed_speed = 0.20 * rpm
time_minutes = 100 / feed_speed
close(rpm, 763.944)
close(feed_speed, 152.789)
close(time_minutes, 0.654498)
close(time_minutes * 60, 39.2699)
close(1000 * 120 * 0.20 * 2, 48000)
examples += 1

# 21.2: economic intersection and values on each side.
quantity = (30000 - 5000) / (7 - 2)
close(quantity, 5000)
close(30000 + 2 * quantity, 40000)
close(5000 + 7 * quantity, 40000)
close(30000 + 2 * 1000, 32000)
close(5000 + 7 * 1000, 12000)
close(30000 + 2 * 10000, 50000)
close(5000 + 7 * 10000, 75000)
examples += 1

# 22.1: directly calculate sample statistics and uncertainty terms.
readings = [10.01, 10.00, 9.99, 10.02, 9.98]
average, sample_sd = mean(readings), stdev(readings)
repeatability = sample_sd / sqrt(len(readings))
calibration, resolution = 0.008 / 2, 0.01 / sqrt(12)
combined = sqrt(repeatability**2 + calibration**2 + resolution**2)
close(average, 10)
close(sample_sd, 0.0158114)
close(repeatability, 0.00707107)
close(resolution, 0.00288675)
close(combined, 0.00862168)
close(2 * combined, 0.0172434)
examples += 1

# 22.2: process capability and centering.
lower, upper, process_mean, process_sd = 9.950, 10.050, 10.020, 0.010
cp = (upper - lower) / (6 * process_sd)
cpu = (upper - process_mean) / (3 * process_sd)
cpl = (process_mean - lower) / (3 * process_sd)
close(cp, 1.6667, rel=3e-5)
close(cpu, 1)
close(cpl, 2.3333)
close(min(cpu, cpl), 1)
close(min(upper - 10, 10 - lower) / (3 * process_sd), cp)
examples += 1

# 23.1: enumerate all endpoint fit combinations.
clearances = [hole - shaft for hole in (40.000, 40.025) for shaft in (39.980, 39.990)]
close(min(clearances), 0.010)
close(max(clearances), 0.045)
truth(all(clearance > 0 for clearance in clearances))
examples += 1

# 23.2: verify all coordinates, radii, and adjacent center distances.
coordinates = [(50 * cos(pi / 6 + i * pi / 3), 50 * sin(pi / 6 + i * pi / 3)) for i in range(6)]
published = [(43.3013, 25), (0, 50), (-43.3013, 25), (-43.3013, -25), (0, -50), (43.3013, -25)]
for (x, y), (px, py) in zip(coordinates, published):
    close(x, px)
    close(y, py)
    close(hypot(x, y), 50)
for index, (x, y) in enumerate(coordinates):
    xn, yn = coordinates[(index + 1) % 6]
    close(hypot(xn - x, yn - y), 50)
examples += 1

# Additional exercise checks catch transcription outside worked examples.
close(sqrt(100**2 + 3 * 30**2), 112.694)
close(sqrt(1 + 0.6**2) / sqrt((1 - 9)**2 + 0.6**2), 0.145365)
close(degrees(atan((40 - 20) / (2 * 100))), 5.71059)

assert examples == 20
print(f"PASS: {examples} mechanics/design worked examples; {checks} numerical and physical-identity checks.")

if __name__ == '__main__':
    chapter_dir = Path(__file__).resolve().parents[1] / 'chapters'
    chapter_ids = {4, 5, 6, 7, 18, 19, 20, 21, 22, 23}
    chapters = [p for p in sorted(chapter_dir.glob('*.md')) if int(p.name[:2]) in chapter_ids]
    required = ['Learning map', 'Theory', 'Formula handbook', 'Derivation', 'Worked examples', 'Exercises', 'Solutions', 'Common mistakes', 'Applications and limits', 'Further reading']
    assert len(chapters) == 10
    for path in chapters:
        source = path.read_text(encoding='utf-8')
        assert all(f'## {section}' in source for section in required), path
        assert source.count('### Example ') == 2, path
        assert source.count('\n$$\n') % 2 == 0, path
        print(f'{path.name}: {len(source.split())} source words; {source.count(chr(10) + "$$" + chr(10)) // 2} display equations')
    print(f'TOTAL: {sum(len(p.read_text(encoding="utf-8").split()) for p in chapters)} source words')
