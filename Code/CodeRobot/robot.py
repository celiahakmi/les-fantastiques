import random
import math

class Robot:
    def __init__(self,x,y,largeur, theta_deg, width, height,wheel_base, plateforme,vmax=4.0, amax=10.0):
        self.x = float(x)
        self.y = float(y)
        self.theta = math.radians(theta_deg)

        self.width = float(width)
        self.height = float(height)

        self.L = float(wheel_base)
        self.plateforme = plateforme

        self.vmax = float(vmax)
        self.amax = float(amax)

        self.vL = 0.0
        self.vR = 0.0
        self.target_vL = 0.0
        self.target_vR = 0.0

        self.range = None
        
    def set_wheel_targets(self, vL, vR):
        self.target_vL = max(-self.vmax, min(self.vmax, float(vL)))
        self.target_vR = max(-self.vmax, min(self.vmax, float(vR)))
        
    def contourner(self):
        """Change la direction du robot de manière aléatoire"""
        angles_possibles = [45, 90, 135, 180, 225, 270]
        nouvel_angle = random.choice(angles_possibles)
        self.tourner(nouvel_angle)
    
    def avancer(self, distance):
        """Fait avancer le robot dans la direction que l'on veut"""
        
        angle_rad = math.radians(self.angle)

        dx = distance * math.cos(angle_rad) #projection horizontale
        dy = distance * math.sin(angle_rad) #projection verticale

        new_x = self.x + dx #translation
        new_y = self.y + dy #translation

        if self.plateforme.verifier_position(new_x, new_y, self.largeur, self.longueur):
            self.x = new_x
            self.y = new_y
        else:
            print("Mur ou obsatcle")
            self.contourner()


    def carre(self, cote):
        """ fait déplacer le robot en carré dans un plan continu"""
        for i in range(4):
            self.avancer(cote)
            self.tourner(90)

        
    

   
