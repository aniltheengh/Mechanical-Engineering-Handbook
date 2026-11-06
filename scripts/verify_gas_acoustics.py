"""Check four compressible-flow/acoustics examples and six solved exercises."""
from pathlib import Path
from math import sqrt,pi,log,log10,isclose
ROOT=Path(__file__).resolve().parents[1]
checks=0
def close(label,actual,expected,rel=8e-6,abs_tol=1e-10):
    global checks
    assert isclose(actual,expected,rel_tol=rel,abs_tol=abs_tol),(label,actual,expected)
    checks+=1
g=1.4;r=287.;cp=g*r/(g-1)
# Nozzle: closed-form mass-flow function versus sonic-state mass balance.
p0,t0,area=300000.,300.,1e-4
ratio=(2/(g+1))**(g/(g-1));ps=p0*ratio;ts=t0*2/(g+1)
sonic=sqrt(g*r*ts)
flow=area*p0/sqrt(t0)*sqrt(g/r)*(2/(g+1))**((g+1)/(2*(g-1)))
close('38 E1 critical ratio',ratio,.528282)
close('38 E1 sonic pressure',ps,158484.5)
close('38 E1 sonic temperature',ts,250)
close('38 E1 sonic speed',sonic,316.938)
close('38 E1 mass flow',flow,.0700068)
close('38 E1 independent density flow',ps/(r*ts)*sonic*area,flow)
assert 100000/p0 < ratio
# Shock: use jump relations, then independent conserved fluxes.
m1,p1,t1=2.,100000.,300.
m2=sqrt((1+(g-1)*m1*m1/2)/(g*m1*m1-(g-1)/2))
pr=1+2*g/(g+1)*(m1*m1-1);rr=(g+1)*m1*m1/(2+(g-1)*m1*m1)
p2=p1*pr;t2=t1*pr/rr
rho1=p1/(r*t1);rho2=p2/(r*t2)
v1=m1*sqrt(g*r*t1);v2=m2*sqrt(g*r*t2)
p01=p1*(1+(g-1)*m1*m1/2)**(g/(g-1))
p02=p2*(1+(g-1)*m2*m2/2)**(g/(g-1))
ds=cp*log(t2/t1)-r*log(p2/p1)
close('38 E2 downstream Mach',m2,.577350)
close('38 E2 pressure ratio',pr,4.5)
close('38 E2 density ratio',rr,2.66667)
close('38 E2 temperature',t2,506.25)
close('38 E2 total-pressure ratio',p02/p01,.720874)
close('38 E2 entropy',ds,93.9325)
close('38 E2 mass flux',rho1*v1,rho2*v2)
close('38 E2 momentum flux',p1+rho1*v1*v1,p2+rho2*v2*v2)
close('38 E2 total enthalpy',cp*t1+v1*v1/2,cp*t2+v2*v2/2)
close('38 E2 entropy alternative',-r*log(p02/p01),ds)
# Gas exercises.
close('38 X1 speed',.5*sqrt(g*r*300),173.594)
close('38 X1 total temperature',300*(1+.2*.5**2),315)
close('38 X1 total pressure',100000*(1+.2*.5**2)**3.5,118621.3)
area_ratio=1/2*(2/(g+1)*(1+(g-1)/2*2**2))**((g+1)/(2*(g-1)))
close('38 X2 area ratio',area_ratio,1.6875)
me=sqrt(2/(g-1)*((150000/100000)**((g-1)/g)-1))
close('38 X3 exit Mach',me,.783659)
close('38 X3 exit temperature',300/(1+.2*me*me),267.183)
assert 100000/150000 > ratio
# Plane wave: pressure/velocity intensity relation and peak/rms consistency.
p_ref=20e-6;pressure=.2;rho=1.2;sound_speed=343.;freq=1000.
z=rho*sound_speed;u=pressure/z;intensity=pressure**2/z
close('39 E1 pressure level',20*log10(pressure/p_ref),80)
close('39 E1 impedance',z,411.6)
close('39 E1 intensity',intensity,9.71817e-5)
close('39 E1 velocity',u,4.85909e-4)
close('39 E1 wavelength',sound_speed/freq,.343)
close('39 E1 pressure peak',pressure*sqrt(2),.282843)
close('39 E1 pressure-velocity flux',pressure*u,intensity)
# Incoherent sources: compare logarithmic addition with mean-square pressure sum.
combined=80+10*log10(2);distance_loss=20*log10(5);received=sqrt(2*(.2/5)**2)
close('39 E2 initial sum',combined,83.0103)
close('39 E2 distance loss',distance_loss,13.9794)
close('39 E2 final level',combined-distance_loss,69.0309)
close('39 E2 received pressure',received,.0565685)
close('39 E2 independent level',20*log10(received/p_ref),combined-distance_loss)
# Acoustic exercises.
close('39 X1 rms',.2/sqrt(2),.141421)
close('39 X1 level',20*log10(.2/sqrt(2)/p_ref),76.9897)
z1,z2=400.,1600.;rp=(z2-z1)/(z2+z1);tp=2*z2/(z1+z2)
reflection=rp*rp;transmission=tp*tp*z1/z2
close('39 X2 pressure reflection',rp,.6)
close('39 X2 reflected power',reflection,.36)
close('39 X2 transmitted power',transmission,.64)
close('39 X2 energy conservation',reflection+transmission,1)
close('39 X2 transmission loss',-10*log10(transmission),1.93820)
close('39 X3 first closed-open',343/(4*.5),171.5)
close('39 X3 second closed-open',3*343/(4*.5),514.5)
close('39 X3 first open-open',343/(2*.5),343)
for filename,tokens in {
    '38-compressible-flow.md':['0.528282','158,484.5','0.0700068','0.577350','506.250','0.720874','93.9325'],
    '39-engineering-acoustics.md':['80.0000','411.600','9.71817','0.343000','83.0103','69.0309','0.0565685'],
}.items():
    source=(ROOT/'chapters'/filename).read_text(encoding='utf-8').split('## Worked examples\n')[1].split('\n## Exercises')[0]
    for token in tokens: assert token in source,(filename,token)
print(f'PASS: 4 gas/acoustics worked examples, 6 exercises, {checks} numerical/conservation checks; printed values matched.')
