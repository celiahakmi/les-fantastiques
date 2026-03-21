class AdaptateurSimu(AdaptateurABC):
    def set_vitesse(self, v_lineaire, v_angulaire):
        # Calcul des vitesses de roues
        v_gauche = v_lineaire - (v_angulaire * self.robot.L / 2)
        v_droite = v_lineaire + (v_angulaire * self.robot.L / 2)
        
        self.robot.vL = v_gauche
        self.robot.vR = v_droite

    def get_position(self):
        return (self.robot.x, self.robot.y)

    def get_distance(self):
            return self.robot.plateforme.distance_obstacle(self.robot)
