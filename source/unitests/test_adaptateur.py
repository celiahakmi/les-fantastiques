import unittest
import math
from Fantastic5.simulation import Plateforme, Robot
from Fantastic5.adaptateur import AdaptateurSimu

class TestAdaptateurSimu(unittest.TestCase):
    def setUp(self):
        self.plateforme = Plateforme(10.0, 10.0)
        # On place le robot en (0,0) pour faciliter les calculs
        self.robot = Robot(0.0, 0.0, 0.0, 0.5, 0.5, 0.7, self.plateforme)
        self.adaptateur = AdaptateurSimu(self.robot)

    def test_get_distance_parcourue(self):
        # On simule un déplacement du robot vers la position (3,4)
        self.robot.x = 3.0
        self.robot.y = 4.0
        # D'après le théorème de Pythagore, la distance (hypoténuse) doit être 5.0
        distance = self.adaptateur.get_distance_parcourue()
        self.assertEqual(distance, 5.0)

    def test_get_angle_parcouru(self):
        # On simule une rotation du robot de 90 degrés
        self.robot.theta = math.radians(90)
        angle = self.adaptateur.get_angle_parcouru()
        self.assertEqual(angle, math.radians(90))

if __name__ == '__main__':
    unittest.main()
