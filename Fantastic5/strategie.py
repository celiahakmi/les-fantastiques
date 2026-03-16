import math

class AvancerDroit:
    def __init__(self, robot, distance):
        self.robot = robot
        self.distance = distance
        self.parcouru = 0.0
        self.x_prec = 0.0
        self.y_prec = 0.0

    def start(self):
        """Initialise les variables au moment de démarrer"""
        self.parcouru = 0.0
        self.x_prec = self.robot.x
        self.y_prec = self.robot.y
        # vitesse moteurs pour aller tout droit
        self.robot.vL = 1.0
        self.robot.vR = 1.0
   
    def step(self):
        """on fait avancer le robot d'un pas et on calcule la distance"""
        # si on a fini on coupe les moteurs et on s'arrête
        if self.stop():
            self.robot.vL = 0.0
            self.robot.vR = 0.0
            return

        # sinon on déplace le robot
        self.robot.deplacer()

        # on calcule la distance qu'on vient de parcourir sur ce pas
        distance_du_pas = math.sqrt((self.robot.x - self.x_prec)**2 + (self.robot.y - self.y_prec)**2)
        self.parcouru += distance_du_pas
        
        # on met à jour les coordonnées pour le prochain calcul
        self.x_prec = self.robot.x
        self.y_prec = self.robot.y

    def stop(self):
        return self.parcouru >= self.distance


class Tourner:
    def __init__(self, robot, angle_deg):
        self.robot = robot
        self.angle = math.radians(angle_deg)
        self.angle_parcouru = 0.0
        self.theta_prec = 0.0




    
    

        
    
