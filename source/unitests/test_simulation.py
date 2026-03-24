import unittest
from Fantastic5.simulation import Plateforme, Robot

class TestPlateforme(unittest.TestCase):
    def setUp(self):
        self.plateforme = Plateforme(10.0, 10.0)

    def test_est_valide(self):
        # On teste à la fois un cas valide et un cas invalide 
        self.assertTrue(self.plateforme.est_valide(5, 5, 1, 1))
        self.assertFalse(self.plateforme.est_valide(15, 5, 1, 1))

    def test_init_obstacle(self):
        self.assertTrue(self.plateforme.init_obstacle(2, 2, 2, 2))
        self.assertEqual(len(self.plateforme.obstacles), 1)

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.plateforme = Plateforme(10.0, 10.0)
        self.robot = Robot(5.0, 5.0, 0.0, 0.5, 0.5, 0.7, self.plateforme)

    def test_init(self):
        self.assertEqual(self.robot.x, 5.0)
        self.assertEqual(self.robot.theta, 0.0)
        self.assertEqual(self.robot.vL, 0.0)
        self.assertEqual(self.robot.vR, 0.0)

if __name__ == '__main__':
    unittest.main()
