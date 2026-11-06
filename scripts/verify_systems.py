"""Recompute the 20 numbered examples in chapters 24--33 with stdlib only.

Checks establish arithmetic and selected balance/limiting-case consistency.
They do not validate real equipment, commercial solvers, or every chapter claim.
Run from any directory: python scripts/verify_systems.py
"""

import math


def close(actual, expected, *, rel=1e-6, abs_tol=1e-10):
    assert math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol), (
        actual, expected
    )


def main():
    count = 0

    # 24.1: compare element equilibrium with continuum extension and energy.
    modulus, area, length, force = 200e9, 200e-6, 1.0, 10000.0
    stiffness = modulus * area / length
    displacement = force / stiffness
    close(displacement, 0.00025)
    close(force / area, 50e6)
    close(0.5 * stiffness * displacement**2, 1.25)
    close(-stiffness * displacement, -force)
    count += 1

    # 24.2: series equilibrium, compatibility, and stresses.
    k1, k2, force = 200e9 * 100e-6 / 0.5, 200e9 * 200e-6 / 0.5, 5000
    u_middle = force / k1
    u_tip = u_middle + force / k2
    close(u_middle, 0.000125)
    close(u_tip, 0.0001875)
    close((k1 + k2) * u_middle - k2 * u_tip, 0)
    close(force / 100e-6, 50e6)
    close(force / 200e-6, 25e6)
    count += 1

    # 25.1: boundedness of explicit diffusion at the selected time step.
    alpha, dx, dt = 1e-5, 0.002, 0.1
    close(dx**2 / (2 * alpha), 0.2)
    fourier = alpha * dt / dx**2
    close(fourier, 0.25)
    updated = (1 - 2 * fourier) * 0 + fourier * (100 + 0)
    close(updated, 25)
    assert 0 <= updated <= 100
    count += 1

    # 25.2: extrapolation recovers an explicitly second-order data set.
    fine, medium, coarse, ratio = 100.25, 101.0, 104.0, 2
    order = math.log(abs((coarse - medium) / (medium - fine))) / math.log(ratio)
    extrapolated = fine + (fine - medium) / (ratio**order - 1)
    close(order, 2)
    close(extrapolated, 100)
    close(abs(fine - extrapolated) / extrapolated, 0.0025)
    count += 1

    # 26.1: loaded divider checked against node-current balance.
    supply, upper, lower, load = 12, 2000, 1000, 1000
    equivalent = 1 / (1 / lower + 1 / load)
    voltage = supply * equivalent / (upper + equivalent)
    close(supply * lower / (upper + lower), 4)
    close(voltage, 2.4)
    close((supply - voltage) / upper, 0.0048)
    close((supply - voltage) / upper, voltage / lower + voltage / load)
    count += 1

    # 26.2: electrical input, conversion, and mechanical power balance.
    input_power = math.sqrt(3) * 400 * 10 * 0.85
    shaft_power = 0.9 * input_power
    speed = 2 * math.pi * 1500 / 60
    torque = shaft_power / speed
    close(input_power, 5888.9727457)
    close(shaft_power, 5300.0754712)
    close(torque, 33.7413283998)
    close(torque * speed, shaft_power)
    count += 1

    # 27.1: DC gain and time constant from closed-loop polynomial.
    plant_gain, plant_tau, controller = 2, 5, 3
    loop_gain = plant_gain * controller
    close(plant_tau / (1 + loop_gain), 5 / 7)
    close(loop_gain / (1 + loop_gain), 6 / 7)
    close(1 - loop_gain / (1 + loop_gain), 1 / 7)
    close(-(1 + loop_gain) / plant_tau, -1.4)
    count += 1

    # 27.2: standard underdamped response predictions.
    damping, natural_frequency = 0.5, 10
    damped_frequency = natural_frequency * math.sqrt(1 - damping**2)
    close(damped_frequency, 8.660254038)
    close(math.pi / damped_frequency, 0.362759873)
    close(math.exp(-math.pi * damping / math.sqrt(1 - damping**2)), 0.163033535)
    close(4 / (damping * natural_frequency), 0.8)
    count += 1

    # 28.1: sensor inverse map and ADC pressure resolution.
    sensitivity = (4.5 - 0.5) / 1000
    quantum = 5 / 2**12
    close(sensitivity, 0.004)
    close(quantum, 0.001220703125)
    close(quantum / sensitivity, 0.30517578125)
    close(quantum / (2 * sensitivity), 0.152587890625)
    close((2.5 - 0.5) / sensitivity, 500)
    count += 1

    # 28.2: gearbox kinematics, power, and reflected inertia.
    motor_torque, motor_rpm, ratio, efficiency = 0.2, 3000, 20, 0.8
    output_rpm = motor_rpm / ratio
    output_torque = efficiency * ratio * motor_torque
    input_power = motor_torque * motor_rpm * 2 * math.pi / 60
    output_power = output_torque * output_rpm * 2 * math.pi / 60
    close(output_rpm, 150)
    close(output_torque, 3.2)
    close(input_power, 62.83185307)
    close(output_power, 50.26548246)
    close(output_power / input_power, efficiency)
    close(0.04 / ratio**2, 0.0001)
    count += 1

    # 29.1: forward kinematics with inverse-kinematics consistency.
    l1, l2, th1, th2 = 0.4, 0.3, math.pi / 6, math.pi / 3
    x = l1 * math.cos(th1) + l2 * math.cos(th1 + th2)
    y = l1 * math.sin(th1) + l2 * math.sin(th1 + th2)
    close(x, 0.3464101615)
    close(y, 0.5)
    close(l1 * l2 * math.sin(th2), 0.1039230485)
    c2 = (x*x + y*y - l1*l1 - l2*l2) / (2*l1*l2)
    close(math.acos(c2), th2)
    count += 1

    # 29.2: differential drive linear/angular motion consistency.
    radius, track, right, left = 0.05, 0.30, 12, 8
    speed = radius * (right + left) / 2
    yaw = radius * (right - left) / track
    close(speed, 0.5)
    close(yaw, 2/3)
    close(speed / yaw, 0.75)
    close(yaw * 3, 2)
    count += 1

    # 30.1: both constraints and active-constraint status.
    force, length, modulus, density = 30000, 2, 200e9, 7850
    strength_area = force / 150e6
    stiffness_area = force * length / (modulus * 0.0005)
    selected_area = max(strength_area, stiffness_area)
    close(strength_area, 200e-6)
    close(selected_area, 600e-6)
    close(density * selected_area * length, 9.42)
    close(force / selected_area, 50e6)
    close(force * length / (modulus * selected_area), 0.0005)
    count += 1

    # 30.2: optimum, equal-volume alternative, and stationarity.
    volume = 2 * math.pi * 1e-3
    radius = (volume / (2 * math.pi))**(1/3)
    height = volume / (math.pi * radius**2)
    area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height
    alternative_radius = 0.08
    alternative_height = volume / (math.pi * alternative_radius**2)
    alternative_area = 2 * math.pi * alternative_radius**2 + 2 * volume / alternative_radius
    close(radius, 0.1)
    close(height, 0.2)
    close(area, 0.1884955592)
    close(alternative_height, 0.3125)
    close(alternative_area, 0.1972920186)
    close(4 * math.pi * radius - 2 * volume / radius**2, 0)
    assert alternative_area > area
    count += 1

    # 31.1: mission survival and independent series product.
    rate, duration = 1 / 5000, 1000
    reliability = math.exp(-rate * duration)
    close(rate, 0.0002)
    close(reliability, 0.8187307531)
    close(reliability**2, 0.6703200460)
    close(reliability**2, math.exp(-2 * rate * duration))
    count += 1

    # 31.2: enumerate success probability and uptime fraction.
    first, second = 0.9, 0.8
    parallel = first * second + first * (1-second) + (1-first) * second
    close(parallel, 0.98)
    close(first * second, 0.72)
    close(500 / (500 + 5), 0.9900990099)
    count += 1

    # 32.1: explicit yearly discounted sum versus annuity factor.
    rate, years, savings, cost = 0.05, 5, 300000, 1000000
    factor = (1 - (1 + rate)**(-years)) / rate
    present = sum(savings / (1 + rate)**year for year in range(1, years+1))
    close(factor, 4.329476671)
    close(present, savings * factor)
    close(present - cost, 298843.0012)
    close(cost / savings, 10/3)
    count += 1

    # 32.2: annual equivalent checked against full present-worth flow.
    rate, years, initial, annual, salvage = 0.05, 10, 2000000, 100000, 200000
    crf = rate * (1 + rate)**years / ((1 + rate)**years - 1)
    sinking = rate / ((1 + rate)**years - 1)
    equivalent = initial * crf + annual - salvage * sinking
    present_cost = initial + sum(annual/(1+rate)**t for t in range(1,years+1)) - salvage/(1+rate)**years
    close(crf, 0.129504574965)
    close(sinking, 0.079504574965)
    close(equivalent, 343108.23494)
    close(equivalent / crf, present_cost)
    count += 1

    # 33.1: flow kinetic energy and conversion balance.
    density, area, wind, coefficient, efficiency = 1.2, 10, 8, 0.4, 0.9
    mass_flow = density * area * wind
    available = 0.5 * mass_flow * wind**2
    close(available, 3072)
    close(coefficient * available, 1228.8)
    close(efficiency * coefficient * available, 1105.92)
    assert coefficient < 16/27
    count += 1

    # 33.2: equal-service energy, carbon, and simple payback.
    saved_kwh = (10 - 8) * 4000
    close(saved_kwh, 8000)
    close(saved_kwh * 3.6e6 / 1e9, 28.8)
    emissions = saved_kwh * 0.4
    close(emissions, 3200)
    close(1600 / emissions, 0.5)
    count += 1

    assert count == 20
    print(f"PASS: {count} worked examples in chapters 24--33; arithmetic and selected balance checks.")


if __name__ == "__main__":
    main()
