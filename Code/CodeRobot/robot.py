
import math

class Robot:
    def __init__(self,x,y,largeur,longueur,angle,plateforme):
        self.x=x
        self.y=y
        self.largeur=largeur
        self.longueur=longueur
        self.angle = angle   # position actuelle du robot en degrés
        self.plateforme = plateforme
        
        
    def tourner(self, delta_angle):
        """ pour faire tourner le robot"""
        
        self.angle = (self.angle + delta_angle) % 360 # de combien est ce que on veut tourner notre robot

    def avancer(self, distance):
    
        """pour faire  avancer le robot dans la direction qu'on veut """
        
        angle_rad = math.radians(self.angle)

        dx = distance * math.cos(angle_rad) #projection horizontale
        dy = distance * math.sin(angle_rad) #projection verticale

        new_x = self.x + dx #translation
        new_y = self.y + dy #translation

        if self.plateforme.position_valide(new_x, new_y, self.largeur, self.longueur):
            self.x = new_x
            self.y = new_y
        else:
            print("Mur ou obsatcle")

    def afficher(self):
        print(f"Position : ({self.x:.2f}, {self.y:.2f}) , Angle : {self.angle}°")

    def carre(self, cote) :
        """ fait déplacer le robot en carré dans un plan continu"""
        for i in range(4):
            self.avancer(cote)
            self.afficher()
            self.tourner(90)

        
    

   
