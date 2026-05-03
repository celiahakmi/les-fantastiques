import math
from .adaptateur import Adaptateur 
class AdaptateurSimu(Adaptateur):
    def __init__(self, robot_simu):
        super().__init__(robot_simu)
        self.x_prec = robot_simu.x
        self.y_prec = robot_simu.y
        self.theta_prec = robot_simu.theta
    
    def set_vitesse(self, v_lineaire, v_angulaire):
        # Calcul des vitesses de roues
        v_gauche = v_lineaire - (v_angulaire * self.robot.L / 2)
        v_droite = v_lineaire + (v_angulaire * self.robot.L / 2)
        
        self.robot.vL = v_gauche
        self.robot.vR = v_droite

    def get_distance(self, angle_offset=0.0):
        # On transmet l'angle au robot pour qu'il puisse regarder ailleurs que devant lui
        return self.robot.get_distance(angle_offset=angle_offset)

    def get_distance_parcourue(self):
        x = self.robot.x
        y = self.robot.y
    
        dx = x - self.x_prec
        dy = y - self.y_prec

        # distance euclidienne
        distance = math.sqrt(dx**2 + dy**2)
    
        # mise à jour
        self.x_prec = x
        self.y_prec = y
    
        return distance

    def get_angle_parcouru(self):
        theta = self.robot.theta
        delta_theta = theta - self.theta_prec
        self.theta_prec = theta
        return delta_theta
    
    def get_position(self):
        return self.robot.x, self.robot.y, self.robot.theta
    
    
