import unittest
import math
from Fantastic5.simulation import Plateforme, Robot
from Fantastic5.adaptateur import AdaptateurSimu
from Fantastic5.strategie import AvancerDroit, Tourner

class TestAvancerDroit(unittest.TestCase):
    """tester la classe avancerDroit"""
    def setUp(self):
        self.plateforme = Plateforme(10.0, 10.0)
        self.robot = Robot(5.0, 5.0, 0.0, 0.5, 0.5, 0.7, self.plateforme)
        self.adaptateur = AdaptateurSimu(self.robot)
        self.strat = AvancerDroit(self.adaptateur, 2.0)

    def test_start(self):
        self.strat.start()
        # La stratégie demande V=0.1 et W=0.0
        # L'adaptateur doit régler les deux roues à 0.1
        self.assertEqual(self.robot.vL, 0.1)
        self.assertEqual(self.robot.vR, 0.1)

    def test_stop(self):
        self.strat.parcouru = 2.0
        self.assertTrue(self.strat.stop())

class TestTourner(unittest.TestCase):
    def setUp(self):
        self.plateforme = Plateforme(10.0, 10.0)
        self.robot = Robot(5.0, 5.0, 0.0, 0.5, 0.5, 0.7, self.plateforme)
        self.adaptateur = AdaptateurSimu(self.robot)
        self.strat = Tourner(self.adaptateur, 90)

    def test_start(self):
        self.strat.start()
        # La stratégie demande V=0.0 et W=0.1
        # Avec un empattement (L) de 0.5, l'adaptateur calcule vL=-0.025 et vR=0.025
        self.assertEqual(self.robot.vL, -0.025)
        self.assertEqual(self.robot.vR, 0.025)

    def test_stop(self):
        self.strat.angle_parcouru = math.radians(90)
        self.assertTrue(self.strat.stop())


if __name__ == '__main__':
    unittest.main()

