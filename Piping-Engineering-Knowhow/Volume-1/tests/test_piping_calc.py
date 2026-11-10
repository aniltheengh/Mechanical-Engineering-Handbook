import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import piping_calc as p

class PhysicsTests(unittest.TestCase):
    def test_continuity(self):
        self.assertAlmostEqual(p.velocity(50/3600,0.0779), 2.9144, places=3)
    def test_pressure_loss(self):
        self.assertAlmostEqual(p.darcy_head_loss(50/3600,0.0779,50,0.02),5.56,places=2)
        self.assertAlmostEqual(p.darcy_head_loss(50/3600,0.1023,50,0.02),1.42,places=2)
    def test_expansion(self):
        self.assertAlmostEqual(p.thermal_growth(12e-6,30,60),0.0216)
    def test_npsha(self):
        self.assertAlmostEqual(p.npsha_open_tank(10.33,1.5,0.6,0.32),10.91)
    def test_shaft_power(self):
        self.assertAlmostEqual(p.shaft_power_w(1000,50/3600,24.2,0.65),p.hydraulic_power_w(1000,50/3600,24.2)/0.65)
    def test_transient_screen(self):
        self.assertAlmostEqual(p.joukowsky_pressure_pa(998,1000,1),998000)
    def test_thrust(self):
        self.assertAlmostEqual(p.capped_end_pressure_thrust_n(600000,0.1),4712.38898,places=4)
    def test_bad_inputs(self):
        for f in (lambda:p.velocity(1,0),lambda:p.shaft_power_w(1000,1,5,0),lambda:p.minor_head_loss(1,0.1,-1)):
            with self.assertRaises(ValueError): f()

if __name__=='__main__':unittest.main()
