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

def draw_fracture(ax):
    crack_mm=np.linspace(.1,50,401)
    geometry=1.12; stress_mpa=100; toughness=40
    intensity=geometry*stress_mpa*np.sqrt(np.pi*crack_mm/1000)
    critical_mm=1000*(toughness/(geometry*stress_mpa))**2/np.pi
    ax.plot(crack_mm,intensity,color=blue,lw=2.4,label="Assumed constant Y = 1.12, stress = 100 MPa")
    ax.axhline(toughness,color=orange,ls="--",label="Assumed toughness = 40 MPa √m")
    ax.scatter([critical_mm],[toughness],c=green,zorder=5)
    ax.annotate(f"Model intersection\na = {critical_mm:.2f} mm",(critical_mm,toughness),xytext=(12,45),arrowprops={"arrowstyle":"->"})
    ax.set(xlabel="Crack size parameter a (mm)",ylabel=r"Mode-I stress intensity $K_I$ (MPa $\sqrt{\mathrm{m}}$)",title="A longer crack raises stress intensity",ylim=(0,53))
    ax.legend(loc="lower right",fontsize=9)

def draw_acoustics(ax):
    distance=np.geomspace(1,16,300)
    single=80-20*np.log10(distance)
    double=single+10*np.log10(2)
    ax.semilogx(distance,single,color=blue,lw=2.4,label="One source: 80 dB at 1 m")
    ax.semilogx(distance,double,color=orange,lw=2.4,label="Two equal incoherent sources")
    level=80+10*np.log10(2)-20*np.log10(5)
    ax.scatter([5],[level],c=green,zorder=5)
    ax.annotate(f"Two sources at 5 m\n{level:.3f} dB",(5,level),xytext=(1.8,58),arrowprops={"arrowstyle":"->"})
    ax.set(xlabel="Equal distance from sources r (m)",ylabel="Sound pressure level (dB re 20 μPa)",title="Distance and source addition are logarithmic",ylim=(53,86))
    ax.set_xticks([1,2,4,8,16],labels=["1","2","4","8","16"])
    ax.legend(fontsize=9)

def draw_void_fraction(ax):
    quality=np.geomspace(1e-5,.1,401)
    for slip,color in [(1,blue),(2,orange),(5,green)]:
        alpha=quality*1000/(quality*1000+(1-quality)*1.2*slip)
        ax.semilogx(quality*100,alpha,color=color,lw=2.3,label=f"Velocity ratio S = {slip}")
    x=.001;alpha=x*1000/(x*1000+(1-x)*1.2)
    ax.scatter([x*100],[alpha],c=blue,zorder=5)
    ax.annotate(f"S = 1: 0.1% gas by mass\n{100*alpha:.2f}% gas by volume",(x*100,alpha),xytext=(.003,.75),arrowprops={"arrowstyle":"->"},fontsize=10)
    ax.set(xlabel="Gas mass-flow quality x (%)",ylabel="Gas void fraction α (dimensionless)",title="Mass fraction differs from occupied volume",ylim=(0,1.04))
    ax.legend(loc="lower right",fontsize=9)

def draw_tank_response(ax):
    minutes=np.linspace(0,50,401)
    concentration=100*(1-np.exp(-minutes/10))
    ax.plot(minutes,concentration,color=blue,lw=2.4,label="Perfectly mixed constant-volume tank")
    ax.axhline(100,color=orange,ls="--",label="Inlet tracer = 100 mg/L")
    at_tau=100*(1-np.exp(-1));t95=-10*np.log(.05)
    ax.scatter([10,t95],[at_tau,95],c=green,zorder=5)
    ax.annotate("One residence time\n10 min: 63.21 mg/L",(10,at_tau),xytext=(17,32),arrowprops={"arrowstyle":"->"},fontsize=10)
    ax.annotate("95% response\n29.96 min",(t95,95),xytext=(33,70),arrowprops={"arrowstyle":"->"},fontsize=10)
    ax.set(xlabel="Time after inlet step (min)",ylabel="Tank / outlet tracer concentration (mg/L)",title="Residence time is not full replacement time",ylim=(0,112))
    ax.legend(loc="lower right",fontsize=9)

drawers=[("pump-operating-point",draw_pump),("thermal-response",draw_cooling),("vibration-response",draw_vibration),("numerical-convergence",draw_error),("fracture-intensity",draw_fracture),("sound-distance",draw_acoustics),("void-fraction-quality",draw_void_fraction),("tank-tracer-response",draw_tank_response)]
for name,draw in drawers:
    fig,ax=plt.subplots(figsize=(8,5),layout="constrained")
    draw(ax);ax.grid(alpha=.2)
    fig.savefig(OUT/f"{name}.png",dpi=170)
    fig.savefig(OUT/f"{name}.svg",metadata={"Date":None})
    svg_path=OUT/f"{name}.svg"
    svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8",newline="\n")
    plt.close(fig)
fig,axes=plt.subplots(4,2,figsize=(14,18),layout="constrained")
for ax,(_,draw) in zip(axes.flat,drawers): draw(ax);ax.grid(alpha=.2)
fig.suptitle("Mechanical Engineering Handbook · Quantitative visual guide",fontsize=19)
fig.savefig(OUT/"visual-overview.png",dpi=140)
plt.close(fig)
print(f"Generated {len(drawers)} PNG/SVG figure pairs and one overview PNG.")
