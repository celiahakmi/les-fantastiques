import matplotlib.pyplot as plt

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

        
    

   
