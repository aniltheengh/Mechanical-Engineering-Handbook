"""Check four corrosion/welding examples and six exercises; no code qualification."""
from pathlib import Path
from math import sqrt,log,log10,isclose
ROOT=Path(__file__).resolve().parents[1]
checks=0
def close(label,actual,expected,rel=8e-6,abs_tol=1e-12):
    global checks
    assert isclose(actual,expected,rel_tol=rel,abs_tol=abs_tol),(label,actual,expected)
    checks+=1
faraday=96485.33212;gas_constant=8.314462618;year=365*24*3600
# Uniform iron loss: charge route versus current-density route and coupon units.
current=.005;time=30*24*3600;molar_mass=.055845;density=7870.;area=.01;valence=2
charge=current*time;mass=molar_mass*charge/(valence*faraday)
depth=mass/(density*area);rate=depth/time
close('40 E1 charge',charge,12960)
close('40 E1 mass g',mass*1000,3.75058)
close('40 E1 penetration mm',depth*1000,.0476566)
close('40 E1 annual penetration',rate*1000*year,.579822)
close('40 E1 current-density route',molar_mass*(current/area)/(valence*faraday*density),rate)
coupon_rate=87.6*(mass*1e6)/((density/1000)*(area*1e4)*(time/3600))
close('40 E1 coupon-unit conversion',coupon_rate,rate*1000*year)
# Nernst: natural-log versus base-ten forms and Gibbs energy.
temperature=298.15;quotient=100.;standard=1.1
potential=standard-gas_constant*temperature/(2*faraday)*log(quotient)
coefficient=gas_constant*temperature/faraday*log(10)
close('40 E2 coefficient',coefficient,.05915935)
close('40 E2 potential',potential,1.04084)
close('40 E2 base-ten consistency',standard-coefficient/2*log10(quotient),potential)
free_energy=-2*faraday*potential
close('40 E2 free energy kJ/mol',free_energy/1000,-200.852)
close('40 E2 chemical alternative',-2*faraday*standard+gas_constant*temperature*log(quotient),free_energy)
# Corrosion exercises.
loss=.002/(7870*.025)
close('40 X1 average depth mm',loss*1000,.0101652)
close('40 X1 annual rate',loss*1000*365/60,.0618382)
current_density=1e-6/1e-4
close('40 X2 current conversion',current_density,.01)
penetration=molar_mass*current_density/(2*faraday*density)
close('40 X2 rate m/s',penetration,3.67721e-13,abs_tol=1e-18)
close('40 X2 rate mm/year',penetration*1000*year,.0115964)
close('40 X3 potential change',-coefficient/2,-.0295797)
# Welding example 1: energy per length versus power-time energy.
voltage,current,efficiency,speed,length=24.,180.,.8,.005,.3
arc_power=voltage*current;net_power=efficiency*arc_power
arc_per_length=arc_power/speed;heat_per_length=net_power/speed;arc_time=length/speed
close('41 E1 arc power',arc_power,4320)
close('41 E1 net power',net_power,3456)
close('41 E1 arc energy kJ/mm',arc_per_length/1e6,.864)
close('41 E1 net heat kJ/mm',heat_per_length/1e6,.6912)
close('41 E1 run time',arc_time,60)
close('41 E1 net energy kJ',net_power*arc_time/1000,207.36)
close('41 E1 energy-length balance',heat_per_length*length,net_power*arc_time)
# Welding example 2: geometry, load recovery, and ideal bead mass.
leg=.006;effective_length=.1;force=20000.;throat=leg/sqrt(2)
weld_area=2*throat*effective_length;stress=force/weld_area
close('41 E2 throat mm',throat*1000,4.24264)
close('41 E2 throat area mm2',weld_area*1e6,848.528)
close('41 E2 nominal stress MPa',stress/1e6,23.5702)
close('41 E2 per-weld force',stress*throat*effective_length,10000)
close('41 E2 total force recovery',2*stress*throat*effective_length,force)
bead_volume=2*leg**2/2*effective_length
close('41 E2 bead volume mm3',bead_volume*1e9,3600)
close('41 E2 bead mass g',7850*bead_volume*1000,28.26)
# Welding exercises.
close('41 X1 heat input',60*.75*22*160/(1000*240),.660)
area_ex=2*(5/sqrt(2))*80
close('41 X2 throat area mm2',area_ex,565.685)
close('41 X2 stress MPa',12000/area_ex,21.2132)
close('41 X3 free movement mm',12e-6*.5*400*1000,2.4)
close('41 X3 elastic restrained MPa',-200e9*12e-6*400/1e6,-960)
for filename,tokens in {
    '40-corrosion-engineering.md':['3.75058','0.0476566','0.579822','1.04084','200.852'],
    '41-welding-engineering.md':['4320','3456','0.8640','0.6912','207.36','4.24264','848.528','23.5702','28.26'],
}.items():
    source=(ROOT/'chapters'/filename).read_text(encoding='utf-8').split('## Worked examples\n')[1].split('\n## Exercises')[0]
    for token in tokens: assert token in source,(filename,token)
print(f'PASS: 4 corrosion/welding worked examples, 6 exercises, {checks} numerical/balance checks; printed values matched.')
