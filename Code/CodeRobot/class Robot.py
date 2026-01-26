from class_plateforme import Plateforme

class Robot: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def haut(self): 
        if self.x != 0 :
            self.x = self.x - 1 
        else: 
            print("Le robot rencontre un mur")
    def bas(self): 
        if self.x != 5:
            self.x = self.x + 1 
        else: 
            print("Le robot rencontre un mur")
    def droite(self):
        if self.y != 5: 
            self.y = self.y + 1 
        else:
            print("Le robot rencontre un mur")
    def gauche(self): 
        if self.y != 0: 
            self.y = self.y - 1 
        else: 
            print("Le robot rencontre un mur")
    def afficher(self):
        print(f"x : {self.x}, y = {self.y}")
    def carre(self, plateforme): 
        
        self.droite()
        print("Nouvelle position logique du robot :")
        self.afficher()

        print("\nPlateforme après déplacement :")
        plateforme.placer_robot(robot)
        plateforme.afficher()

        self.bas()
        print("Nouvelle position logique du robot :")
        self.afficher()

        print("\nPlateforme après déplacement :")
        plateforme.placer_robot(robot)
        plateforme.afficher()

        self.gauche()
        print("Nouvelle position logique du robot :")
        self.afficher()

        print("\nPlateforme après déplacement :")
        plateforme.placer_robot(robot)
        plateforme.afficher()

        self.haut()
        print("Nouvelle position logique du robot :")
        self.afficher()

        print("\nFin du déplacement en carré :")
        plateforme.placer_robot(robot)
        plateforme.afficher()

   
