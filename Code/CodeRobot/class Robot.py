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
        if self.x != (lignes - 1):
            self.x = self.x + 1 
        else: 
            print("Le robot rencontre un mur")
    def droite(self):
        if self.y != (colonnes - 1) :
            self.y = self.y + 1 
        else:
            print("Le robot rencontre un mur")
    def gauche(self): 
        if self.y != 0: 
            self.y = self.y - 1 
        else: 
            print("Le robot rencontre un mur")
    def diag_haut_droite(self):
        if self.x != 0  and self.y != (colonnes -1): 
            self.x = self.x - 1
            self.y = self.y + 1
        else: 
            print("Le robot rencontre un mur")
    def diag_haut_gauche(self):
        if self.x != 0 and self.y != 0:
            self.x = self.x - 1
            self.y = self.y - 1
        else : 
            print("Le robot rencntre un mur")
    def diag_bas_droite(self):
        if self.x != (lignes - 1) and self.y != (colonnes - 1):
            self.x = self.x + 1
            self.y = self.y + 1 
        else:
            print("Le robot rencontre un mur")
    def diag_bas_gauche(self):
        if self.x != (lignes - 1) and self.y != 0:
            self.x = self.x + 1 
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

        
lignes = int(input("Nombre de lignes de la plateforme : "))
colonnes = int(input("Nombre de colonnes de la plateforme : "))

if lignes <0 or colonnes <0:
    print("Les dimensions doivent etre 6positives")
else:
    plateforme = Plateforme(lignes, colonnes)

x = int(input("Entrez la position x du robot : "))
y = int(input("Entrez la position y du robot : "))

if 0 <= x < lignes and 0 <= y < colonnes:
    robot = Robot(x, y)   
else:
    print("valeurs hors plateforme ")
   

print("Position logique du robot :")
robot.afficher()

print("\nPlateforme initiale :")
plateforme.placer_robot(robot)
plateforme.afficher()

print("Déplacement en carré...\n")
robot.carre(plateforme)
