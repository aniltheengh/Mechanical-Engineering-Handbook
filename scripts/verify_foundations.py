"""Independent numerical checks for chapters 01, 02, 03, 34, 35 and capstone."""
from math import pi, exp, sqrt, isclose, log, ceil

checks = 0
def check(label, actual, expected, rel=1e-5, abs_tol=1e-8):
    global checks
    assert isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol), (label, actual, expected)
    checks += 1

# 01: dimensional conversions and differential sensitivity.
check("01 E1 hydraulic power", 998*9.81*(120e-3/60)*18, 352.45368)
check("01 E1 input power", 998*9.81*.002*18/.65, 542.236430769)
check("01 E2 area", pi*20**2/4, 314.159265359)
check("01 E2 uncertainty", pi*20/2*.05, 1.570796327)
check("01 exercise shaft power", 25*2*pi*1440/60/1000, 3.769911184)
check("01 exercise pressure", 250+98, 348)
check("01 exercise density uncertainty", sqrt(.01**2+.02**2), .0223606798)
# 02: exact response and residual-based matrix check.
tau=2*500/(25*.2)
check("02 E1 time constant", tau, 200)
check("02 E1 cooling", 20+60*exp(-300/tau), 33.387809609)
check("02 E2 row 1", 2*2+1, 5)
check("02 E2 row 2", 2+3*1, 5)
check("02 exercise work", 100*2+10*2**2, 240)
check("02 exercise sample SD", sqrt(sum((x-10)**2 for x in (9,10,11))/2), 1)
# 03: Newton residual and actual iterative integration versus analytical benchmark.
x=1.5
x=.5*(x+2/x)
check("03 E1 Newton 1", x, 1.41666666667)
x=.5*(x+2/x)
check("03 E1 Newton 2", x, 1.41421568627)
check("03 E1 residual", x*x-2, 6.00730488e-6, abs_tol=1e-12)
def euler(h):
    y=10.
    for _ in range(round(1/h)):
        y += h*(-.5*y)
    return y
check("03 E2 coarse",euler(.2),5.9049)
check("03 E2 fine",euler(.1),5.987369392)
check("03 E2 exact",10*exp(-.5),6.065306597)
check("03 exercise Simpson",(0+4*1+4)/3,8/3)
assert ceil(log(1000,2)) == 10
checks += 1
# 34: shear balance and calibrated wear with unit conversion.
check("34 E1 shear",.08*2/1e-4,1600)
check("34 E1 drag",.08*2/1e-4*.01,16)
check("34 E1 loss",.08*.01*2**2/1e-4,32)
check("34 E2 volume mm3",2e-6*500*10000/2e9*1e9,5)
check("34 E2 depth mm",5/100,.05)
check("34 exercise film ratio",.5/sqrt(.2**2+.3**2),1.386750491)
# 35: solve intersection analytically, then verify both independent curves.
q=sqrt((30-10)/(200000+300000))
check("35 E1 flow",q,.00632455532)
check("35 E1 pump head",30-200000*q*q,22)
check("35 E1 system head",10+300000*q*q,22)
check("35 E1 input kW",1000*9.81*q*22/.70/1000,1.949950756)
finish={"A":2}
finish["B"]=finish["A"]+3
finish["C"]=finish["A"]+4
finish["D"]=max(finish["B"],finish["C"])+2
check("35 E2 schedule",finish["D"],8)
check("35 exercise series reliability",.98*.99,.9702)
# Integrated hypothetical pumping capstone: direct loss balance.
flow=.003; diameter=.05; length=40; darcy=.025; minor=6; gravity=9.81
velocity=flow/(pi*diameter**2/4)
loss=(darcy*length/diameter+minor)*velocity**2/(2*gravity)
check("capstone speed",velocity,1.527887454)
check("capstone head loss",loss,3.093549534)
check("capstone electrical kW",998*gravity*flow*(12+loss)/(.70*.90)/1000,.703674217)
power=998*gravity*flow*(12+loss)/(.70*.90)/1000
check("capstone annual energy",power*4000,2814.696866)
check("capstone annual cost",power*4000*25,70367.42166)
check("capstone water mass",998*pi*diameter**2/4*2,3.919136835)
check("capstone thermal expansion mm",12e-6*10*40*1000,4.8)
check("capstone transmitter kPa",300*(12-4)/16,150)
print(f"PASS: {checks} foundation, tribology, systems, and capstone numeric checks.")
