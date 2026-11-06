"""Check four fracture/composite examples and six exercises using stdlib only."""
from pathlib import Path
from math import sqrt, pi, isclose

ROOT=Path(__file__).resolve().parents[1]
checks=0
def close(label, actual, expected, rel=8e-6, abs_tol=1e-10):
    global checks
    assert isclose(actual,expected,rel_tol=rel,abs_tol=abs_tol),(label,actual,expected)
    checks+=1

# Fracture example 1: intensity, energy, and two plastic-zone estimates.
y,stress,crack,modulus,nu,yield_stress=1.12,100,.005,210e9,.3,300
intensity=y*stress*sqrt(pi*crack)
close('36 E1 intensity',intensity,14.03712)
effective_modulus=modulus/(1-nu**2)
energy=(intensity*1e6)**2/effective_modulus
close('36 E1 energy',energy,853.843)
close('36 E1 plane-stress zone mm',(intensity/yield_stress)**2/(2*pi)*1000,.348444)
close('36 E1 plane-strain zone mm',(intensity/yield_stress)**2/(6*pi)*1000,.116148)
critical=40/(y*sqrt(pi*crack))
close('36 E1 critical stress',critical,284.9588)
close('36 E1 inverse intensity',y*critical*sqrt(pi*crack),40)
# Fracture example 2: analytical cycle integral against composite Simpson quadrature.
c,exponent,delta_sigma,ai,af=1e-12,3,80,.001,.01
b=c*(y*delta_sigma*sqrt(pi))**exponent
cycles=2/b*(1/sqrt(ai)-1/sqrt(af))
close('36 E2 cycles',cycles,10796739)
close('36 E2 initial rate',b*ai**1.5,1.266627e-10,abs_tol=1e-16)
close('36 E2 final rate',b*af**1.5,4.005427e-9,abs_tol=1e-16)
n=10000;h=(af-ai)/n
rate=lambda a:c*(y*delta_sigma*sqrt(pi*a))**exponent
integral=h/3*(1/rate(ai)+1/rate(af)+sum((4 if i%2 else 2)/rate(ai+i*h) for i in range(1,n)))
close('36 E2 independent quadrature',integral,cycles,rel=1e-9)
# Fracture exercises.
close('36 X1 intensity ratio',sqrt(8/2),2)
close('36 X1 energy ratio',8/2,4)
close('36 X2 plane-stress G',(20e6)**2/200e9,2000)
close('36 X2 plane-strain G',(20e6)**2/(200e9/(1-.3**2)),1820)
close('36 X3 cycle factor',1/2**3,.125)
# Composite example 1: constituent strain compatibility and force fraction.
ef,em,vf=230e9,3.5e9,.6;vm=1-vf
el=vf*ef+vm*em;et=1/(vf/ef+vm/em)
close('37 E1 longitudinal GPa',el/1e9,139.4)
close('37 E1 transverse GPa',et/1e9,8.554729)
close('37 E1 density',vf*1800+vm*1200,1560)
strain=.001
close('37 E1 fibre MPa',ef*strain/1e6,230)
close('37 E1 matrix MPa',em*strain/1e6,3.5)
close('37 E1 average MPa',(vf*ef+vm*em)*strain/1e6,139.4)
close('37 E1 fibre fraction',vf*ef/el,.989957)
# Composite example 2: assemble A/B/D from ply coordinates, then recover loads.
e1,e2,g12,v12=135e9,10e9,5e9,.3
v21=v12*e2/e1;den=1-v12*v21
q11,q22,q12,q66=e1/den,e2/den,v12*e2/den,g12
q0=[[q11,q12,0],[q12,q22,0],[0,0,q66]]
q90=[[q22,q12,0],[q12,q11,0],[0,0,q66]]
plies=[q0,q90,q90,q0]
def assemble(scale=1):
    z=[scale*x for x in [-.00025,-.000125,0,.000125,.00025]]
    matrices=[[[0.]*3 for _ in range(3)] for _ in range(3)]
    for k,q in enumerate(plies):
        for power,matrix in enumerate(matrices,start=1):
            factor=(z[k+1]**power-z[k]**power)/power
            for i in range(3):
                for j in range(3): matrix[i][j]+=q[i][j]*factor
    return matrices
a,bmat,d=assemble()
close('37 E2 Q11 GPa',q11/1e9,135.9060)
close('37 E2 Q22 GPa',q22/1e9,10.06711)
close('37 E2 Q12 GPa',q12/1e9,3.020134)
close('37 E2 A11 MN/m',a[0][0]/1e6,36.49329)
close('37 E2 A12 MN/m',a[0][1]/1e6,1.510067)
close('37 E2 A66 MN/m',a[2][2]/1e6,2.5)
for row in bmat:
    for value in row: close('37 E2 zero coupling',value,0,abs_tol=1e-9)
nx=50000.;det=a[0][0]*a[1][1]-a[0][1]**2
eps=[nx*a[1][1]/det,-nx*a[0][1]/det,0]
close('37 E2 axial strain',eps[0],.001372465)
close('37 E2 transverse strain',eps[1],-.00005679165)
stress0=[q11*eps[0]+q12*eps[1],q12*eps[0]+q22*eps[1]]
stress90_local=[q11*eps[1]+q12*eps[0],q12*eps[1]+q22*eps[0]]
for actual,expected in zip(stress0+stress90_local,[186.3548e6,3.573300e6,-3.573300e6,13.64524e6]):
    close('37 E2 local stress',actual,expected)
close('37 E2 recovered axial load',.00025*(stress0[0]+stress90_local[1]),nx)
close('37 E2 recovered transverse load',.00025*(stress0[1]+stress90_local[0]),0,abs_tol=1e-7)
ply_energy=sum(.5*.000125*sum(eps[i]*q[i][j]*eps[j] for i in range(3) for j in range(3)) for q in plies)
close('37 E2 strain energy consistency',ply_energy,.5*nx*eps[0])
# Composite exercises: reciprocity, thickness scaling, changed constituent fraction.
close('37 X1 reciprocal Poisson',.28*10/140,.02)
aa,bb,dd=assemble(2)
for i in range(3):
    for j in range(3):
        close('37 X2 A scaling',aa[i][j],2*a[i][j])
        close('37 X2 B symmetry',bb[i][j],0,abs_tol=1e-9)
        close('37 X2 D scaling',dd[i][j],8*d[i][j])
close('37 X2 strain scaling',nx*aa[1][1]/(aa[0][0]*aa[1][1]-aa[0][1]**2),eps[0]/2)
close('37 X3 modulus GPa',.4*230+.6*3.5,94.1)
close('37 X3 density',.4*1800+.6*1200,1440)
close('37 X3 stress MPa',(.4*230e9+.6*3.5e9)*.001/1e6,94.1)
# Couple key checked outputs to the published example sections.
for filename,tokens in {
    '36-fracture-mechanics.md':['14.03712','853.843','284.9588','10,796,739','1.266627','4.005427'],
    '37-composite-materials.md':['139.400','8.554729','1560','36.49329','0.001372465','186.3548','13.64524'],
}.items():
    source=(ROOT/'chapters'/filename).read_text(encoding='utf-8').split('## Worked examples\n')[1].split('\n## Exercises')[0]
    for token in tokens: assert token in source,(filename,token)
print(f'PASS: 4 advanced-mechanics worked examples, 6 exercises, {checks} numerical/balance checks; printed values matched.')
