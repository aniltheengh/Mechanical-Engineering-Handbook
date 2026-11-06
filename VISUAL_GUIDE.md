# Quantitative visual guide

These original figures are generated from the equations and assumed inputs below. They illustrate model behaviour, not measured equipment performance. Regenerate them with `python scripts/generate_figures.py` after installing NumPy and Matplotlib. All four plots are available as PNG for reading and SVG for scalable reuse.

## Pump operating point

![Pump and system head curves with their intersection](assets/pump-operating-point.png)

For flow $Q$ in m³/s, the assumed pump curve is $H_p=30-200000Q^2$ m and the system curve is $H_s=10+300000Q^2$ m. Their intersection gives 6.325 L/s and 22 m. The graph displays flow in L/s, so its horizontal values must be converted before substitution into these equations. Read [systems engineering, Example 1](chapters/35-systems-engineering.md). [SVG](assets/pump-operating-point.svg).

## Thermal response

![Cooling from 80 degrees Celsius toward ambient temperature](assets/thermal-response.png)

The lumped model is $T(t)=20+60e^{-t/200}$ °C with time in seconds. At 300 s it predicts 33.388 °C. The time constant is 200 s, and the model approaches ambient asymptotically. Read [engineering mathematics, Example 1](chapters/02-engineering-mathematics.md). [SVG](assets/thermal-response.svg).

## Vibration response

![Forced vibration amplification for three damping ratios](assets/vibration-response.png)

For a linear single-degree-of-freedom oscillator under harmonic force, $X/(F_0/k)=1/\sqrt{(1-r^2)^2+(2\zeta r)^2}$, where $r=\omega/\omega_n$. This is force-driven displacement amplification relative to static deflection; it is not the base-motion transmissibility. The three curves use damping ratios 0.05, 0.2, and 0.7. Read [vibrations](chapters/20-vibrations.md). [SVG](assets/vibration-response.svg).

## Numerical convergence

![Euler integration error decreases as the time step decreases](assets/numerical-convergence.png)

For $\dot\theta=-0.5\theta$ with initial excess temperature 10 K, the exact value at 1 s is $10e^{-0.5}$ K. The plotted error compares it with repeated explicit Euler steps. The first-order reference is scaled to the smallest-step error; it indicates the expected trend, not an independent error bound. Read [numerical methods, Example 2](chapters/03-numerical-methods.md). [SVG](assets/numerical-convergence.svg).
