import random
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
        """ Fait tourner le robot en fonction d'un angle"""
        
        self.angle = (self.angle + delta_angle) % 360 # de combien est ce que on veut tourner notre robot
    
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

        if self.plateforme.position_valide(new_x, new_y, self.largeur, self.longueur):
            self.x = new_x
            self.y = new_y
        else:
            print("Mur ou obsatcle")
            self.contourner()

    def afficher(self):
        print(f"Position : ({self.x:.2f}, {self.y:.2f}) , Angle : {self.angle}°")

    def carre(self, cote, view=None) :
        """Fait déplacer le robot en carré dans un plan continu"""
        for i in range(4):
            self.avancer(cote)
            self.afficher()
            if view is not None:
                view.dessiner()     
                pygame.time.delay(400)
            self.tourner(90)

        
    

   
