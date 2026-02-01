from class_plateforme import Plateforme

class Robot: 
    def __init__(self, x, y,plateforme):
        self.x = x 
        self.y = y
        self.plateforme = plateforme 
    def haut(self): 
        if self.x != 0 :
            self.x = self.x - 1 
        else: 
            print("Le robot rencontre un mur")
    def bas(self): 
        if self.x != (self.plateforme.lignes - 1):
            self.x = self.x + 1 
        else: 
            print("Le robot rencontre un mur")
    def droite(self):
        if self.y != (self.plateforme.colonnes - 1) :
            self.y = self.y + 1 
        else:
            print("Le robot rencontre un mur")
    def gauche(self): 
        if self.y != 0: 
            self.y = self.y - 1 
        else: 
            print("Le robot rencontre un mur")
    def diag_haut_droite(self):
        if self.x != 0  and self.y != (self.plateforme.colonnes -1): 
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
        if self.x != (self.plateforme.lignes - 1) and self.y != (self.plateforme.colonnes - 1):
            self.x = self.x + 1
            self.y = self.y + 1 
        else:
            print("Le robot rencontre un mur")
    def diag_bas_gauche(self):
        if self.x != (self.plateforme.lignes - 1) and self.y != 0:
            self.x = self.x + 1 
            self.y = self.y - 1 
        else: 
            print("Le robot rencontre un mur")
    def afficher(self):
        print(f"x : {self.x}, y = {self.y}")
    def carre(self, plateforme): 
        
        self.droite()
        print("Nouvelle position du robot :")
        self.afficher()

        print("\nPlateforme après déplacement :")
        plateforme.placer_robot(self)
        plateforme.afficher()

        self.bas()
        print("Nouvelle position du robot :")
        self.afficher()

        print("\nPlateforme après déplacement :")
        plateforme.placer_robot(self)
        plateforme.afficher()

        self.gauche()
        print("Nouvelle position  du robot :")
        self.afficher()

        print("\nPlateforme après déplacement :")
        plateforme.placer_robot(self)
        plateforme.afficher()

        self.haut()
        print("Nouvelle position du robot :")
        self.afficher()

        print("\nFin du déplacement en carré :")
        plateforme.placer_robot(self)
        plateforme.afficher()

        
