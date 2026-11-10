"""Illustrative liquid-piping engineering calculator — SI units only.

This module is NOT a pipe-code stress calculator, equipment selector,
or substitute for a transient / hydraulic network model.
Always verify input properties and project boundary conditions.
"""
from math import pi

g = 9.80665

def area(diameter_m: float) -> float:
    if diameter_m <= 0: raise ValueError("diameter must be > 0")
    return pi * diameter_m**2 / 4.0

def velocity(flow_m3_s: float, diameter_m: float) -> float:
    if flow_m3_s < 0: raise ValueError("flow must be >= 0")
    return flow_m3_s / area(diameter_m)

def darcy_head_loss(flow_m3_s: float, diameter_m: float, length_m: float, darcy_f: float) -> float:
    if length_m < 0 or darcy_f < 0: raise ValueError("length and Darcy f must be >= 0")
    v = velocity(flow_m3_s, diameter_m)
    return darcy_f * (length_m / diameter_m) * v**2 / (2*g)

def minor_head_loss(flow_m3_s: float, diameter_m: float, k_total: float) -> float:
    if k_total < 0: raise ValueError("K must be >= 0")
    v = velocity(flow_m3_s, diameter_m)
    return k_total * v**2/(2*g)

def thermal_growth(alpha_per_k: float, run_m: float, delta_temp_k: float) -> float:
    if alpha_per_k < 0 or run_m < 0: raise ValueError("alpha and length must be >= 0")
    return alpha_per_k*run_m*delta_temp_k

def npsha_open_tank(atm_head_m: float, surface_above_pump_m: float, suction_loss_m: float, vapor_head_m: float) -> float:
    if suction_loss_m < 0 or vapor_head_m < 0 or atm_head_m <= 0: raise ValueError("invalid head")
    return atm_head_m + surface_above_pump_m - suction_loss_m - vapor_head_m

def hydraulic_power_w(rho_kg_m3: float, flow_m3_s: float, head_m: float) -> float:
    if rho_kg_m3 <= 0 or flow_m3_s < 0 or head_m < 0: raise ValueError("invalid hydraulic inputs")
    return rho_kg_m3 * g * flow_m3_s * head_m

def shaft_power_w(rho_kg_m3: float, flow_m3_s: float, head_m: float, efficiency: float) -> float:
    if not (0 < efficiency <= 1): raise ValueError("pump efficiency must lie in (0,1]")
    return hydraulic_power_w(rho_kg_m3,flow_m3_s,head_m)/efficiency

def joukowsky_pressure_pa(rho_kg_m3: float, wave_speed_m_s: float, delta_v_m_s: float) -> float:
    if rho_kg_m3 <= 0 or wave_speed_m_s <= 0: raise ValueError("invalid fluid or wave speed")
    return rho_kg_m3 * wave_speed_m_s * delta_v_m_s

def capped_end_pressure_thrust_n(pressure_pa: float, diameter_m: float) -> float:
    if pressure_pa < 0: raise ValueError("pressure must be >= 0")
    return pressure_pa * area(diameter_m)

if __name__ == '__main__':
    q=50/3600
    for d in (0.0779,0.1023):
        print(f"D={d} m: v={velocity(q,d):.4f} m/s, Darcy hf={darcy_head_loss(q,d,50,0.02):.4f} m")
    print(f"Thermal expansion: {1000*thermal_growth(12e-6,30,60):.3f} mm")
    print(f"NPSHA (illustration only): {npsha_open_tank(10.33,1.5,0.6,0.32):.3f} m")
    print(f"Pump shaft power: {shaft_power_w(1000,q,24.2,0.65)/1000:.3f} kW")
    print(f"Joukowsky rise: {joukowsky_pressure_pa(998,1000,1)/1e6:.3f} MPa")
