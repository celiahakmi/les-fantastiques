import unittest
import math

from Fantastic5.Simulation.simulation import Plateforme, Robot
from Fantastic5.Strategie.strategie import AvancerDroit, Tourner, TracerCarre

#les unittests de la classe plateforme
class TestPlateforme(unittest.TestCase):
    def setUp(self):
        self.plateforme = Plateforme(10.0, 10.0)

    def test_est_valide(self):
        # On teste à la fois un cas ( valide et invalide) 
        self.assertTrue(self.plateforme.est_valide(5, 5, 1, 1))
        self.assertFalse(self.plateforme.est_valide(15, 5, 1, 1))

    def test_init_obstacle(self):
        self.assertTrue(self.plateforme.init_obstacle(2, 2, 2, 2))
        self.assertEqual(len(self.plateforme.obstacles), 1)

#les unittests de la classe Robot
class TestRobot(unittest.TestCase):
    def setUp(self):
        self.plateforme = Plateforme(10.0, 10.0)
        self.robot = Robot(5.0, 5.0, 0.0, 0.5, 0.5, 0.7, self.plateforme)

    def test_init(self):
        self.assertEqual(self.robot.x, 5.0)
        self.assertEqual(self.robot.theta, 0.0)
        self.assertEqual(self.robot.vL, 0.0)
        self.assertEqual(self.robot.vR, 0.0)

#les unittests pour les stratégies 

class TestAvancerDroit(unittest.TestCase):
    def setUp(self):
        self.plateforme = Plateforme(10.0, 10.0)
        self.robot = Robot(5.0, 5.0, 0.0, 0.5, 0.5, 0.7, self.plateforme)
        self.strat = AvancerDroit(self.robot, 2.0)

    def test_start(self):
        self.strat.start()
        self.assertEqual(self.robot.vL, 0.1)
        self.assertEqual(self.robot.vR, 0.1)

    def test_stop(self):
        self.strat.parcouru = 2.0
        self.assertTrue(self.strat.stop())


