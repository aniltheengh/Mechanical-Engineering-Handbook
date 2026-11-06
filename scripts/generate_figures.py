"""Generate quantitative teaching figures. Optional NumPy + Matplotlib dependency."""
from pathlib import Path
import os

ROOT=Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR",str(ROOT/".cache"/"matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT=ROOT/"assets"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.titlesize":14,
                     "axes.labelsize":11,"figure.facecolor":"#f7fafc","axes.facecolor":"white",
                     "axes.spines.top":False,"axes.spines.right":False,"svg.hashsalt":"mechanical-handbook-v1"})
blue="#1565c0";orange="#d66b00";green="#16806a"

def draw_pump(ax):
    q=np.linspace(0,9,301);si=q/1000
    ax.plot(q,30-200000*si**2,color=blue,lw=2.4,label="Assumed pump characteristic")
    ax.plot(q,10+300000*si**2,color=orange,lw=2.4,label="Assumed system characteristic")
    qp=np.sqrt(20/500000)*1000
    ax.scatter([qp],[22],c=green,zorder=5,s=50)
    ax.annotate("Operating point\n6.325 L/s, 22 m",(qp,22),xytext=(1,35),arrowprops={"arrowstyle":"->","color":green})
    ax.set(xlabel="Flow Q (L/s)",ylabel="Head H (m)",title="A pump operates with its system",ylim=(0,40))
    ax.legend(loc="lower left",fontsize=9)

def draw_cooling(ax):
    t=np.linspace(0,1000,301);temperature=20+60*np.exp(-t/200)
    ax.plot(t,temperature,color=blue,lw=2.4,label="Lumped thermal model")
    ax.axhline(20,color=orange,ls="--",label="Ambient = 20 °C")
    ax.scatter([300],[20+60*np.exp(-1.5)],c=green,zorder=5)
    ax.annotate("300 s: 33.388 °C",(300,20+60*np.exp(-1.5)),xytext=(410,56),arrowprops={"arrowstyle":"->"})
    ax.set(xlabel="Time t (s)",ylabel="Temperature (°C)",title="A first-order thermal response",ylim=(15,85))
    ax.legend(fontsize=9)

def draw_vibration(ax):
    r=np.linspace(0,3,601)
    for z,color in [(.05,blue),(.2,orange),(.7,green)]:
        mag=1/np.sqrt((1-r*r)**2+(2*z*r)**2)
        ax.plot(r,mag,color=color,lw=2,label=f"Damping ratio ζ = {z}")
    ax.set(xlabel="Frequency ratio r = ω / ωₙ",ylabel="Displacement / static deflection",title="Damping changes resonant response",ylim=(0,11))
    ax.legend(fontsize=9)

def draw_error(ax):
    h=np.array([.2,.1,.05,.025,.0125]);exact=10*np.exp(-.5)
    numeric=np.array([10*(1-.5*step)**round(1/step) for step in h])
    error=np.abs(numeric-exact)
    ax.loglog(h,error,"o-",color=blue,lw=2,label="Explicit Euler absolute error")
    ax.loglog(h,error[-1]*(h/h[-1]),"--",color=orange,label="Slope 1 reference")
    ax.set(xlabel="Time step h (s)",ylabel="Error at t = 1 s (K)",title="Refinement reveals convergence order")
    ax.legend(fontsize=9)

drawers=[("pump-operating-point",draw_pump),("thermal-response",draw_cooling),("vibration-response",draw_vibration),("numerical-convergence",draw_error)]
for name,draw in drawers:
    fig,ax=plt.subplots(figsize=(8,5),layout="constrained")
    draw(ax);ax.grid(alpha=.2)
    fig.savefig(OUT/f"{name}.png",dpi=170)
    fig.savefig(OUT/f"{name}.svg",metadata={"Date":None})
    svg_path=OUT/f"{name}.svg"
    svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8",newline="\n")
    plt.close(fig)
fig,axes=plt.subplots(2,2,figsize=(14,9),layout="constrained")
for ax,(_,draw) in zip(axes.flat,drawers): draw(ax);ax.grid(alpha=.2)
fig.suptitle("Mechanical Engineering Handbook · Quantitative visual guide",fontsize=19)
fig.savefig(OUT/"visual-overview.png",dpi=140)
plt.close(fig)
print("Generated 4 PNG/SVG figure pairs and one overview PNG.")
