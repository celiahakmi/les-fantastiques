import math

class AvancerDroit:
    def __init__(self, robot, distance):
        self.robot = robot
        self.distance = distance
        self.parcouru = 0.0
        self.x_prec = 0.0
        self.y_prec = 0.0

    def start(self):
        """Initialise les variables au moment de démarrer."""
        self.parcouru = 0.0
        self.x_prec = self.robot.x
        self.y_prec = self.robot.y
        # On donne la vitesse aux moteurs pour aller tout droit
        self.robot.vL = 1.0
        self.robot.vR = 1.0
