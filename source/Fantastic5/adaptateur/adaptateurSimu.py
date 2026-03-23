from .adaptateur import Adaptateur 
class AdaptateurSimu(Adaptateur):
    def __init__(self, robot_simu):
        super().__init__(robot_simu) 
    
    def set_vitesse(self, v_lineaire, v_angulaire):
        # Calcul des vitesses de roues
        v_gauche = v_lineaire - (v_angulaire * self.robot.L / 2)
        v_droite = v_lineaire + (v_angulaire * self.robot.L / 2)
        
        self.robot.vL = v_gauche
        self.robot.vR = v_droite

    def get_position(self):
        return (self.robot.x, self.robot.y, self.robot.theta)

    def get_distance(self):
            return self.robot.get_distance()
