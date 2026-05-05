import math
from .adaptateur import Adaptateur  

class AdaptateurIRL(Adaptateur):
    def __init__(self, robot_reel):
        super().__init__(robot_reel)
        # On récupère les constantes physiques depuis l'API du robot
        self.L = self.robot.WHEEL_BASE_WIDTH 
        self.diametre = self.robot.WHEEL_DIAMETER
        self.precL, self.precR= self.robot.get_motor_position()

    def set_vitesse(self, v_lineaire, v_angulaire):
        # Calcul des vitesses des roues
        v_gauche = v_lineaire - (v_angulaire * self.L / 2)
        v_droite = v_lineaire + (v_angulaire * self.L / 2)

        # Rayon = diametre / 2
        rayon = self.diametre / 2
        # Conversion m/s en dps
        dps_gauche = (v_gauche / rayon) * (180 / math.pi)
        dps_droite = (v_droite / rayon) * (180 / math.pi)

        # Envoi des commandes aux moteurs réels 
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dps_gauche)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps_droite)

    def get_distance(self):
        # Méthode déjà existante dans l'API
        return self.robot.get_distance()

    def get_distance_parcourue(self):
        angleL, angleR = self.robot.get_motor_position()
    
        deltaL = angleL - self.precL
        deltaR = angleR - self.precR
    
        self.precL= angleL
        self.precR = angleR
    
        # conversion en mm
        distL= deltaL * self.robot.WHEEL_CIRCUMFERENCE / 360
        distR = deltaR * self.robot.WHEEL_CIRCUMFERENCE / 360
    
        # moyenne
        return (distL + distR) / 2
    
    def get_angle_parcouru(self):
        angleL, angleR = self.robot.get_motor_position()
    
        deltaL = angleL - self.precL
        deltaR = angleR - self.precR
    
        self.precL = angleL
        self.precR = angleR
    
        distL = deltaL * self.robot.WHEEL_CIRCUMFERENCE / 360
        distR = deltaR * self.robot.WHEEL_CIRCUMFERENCE / 360
    
        return (distL - distR) / self.robot.WHEEL_BASE_WIDTH

    def get_position(self):
        return self.robot.get_motor_position()
