from class_plateforme import Plateforme

class Robot: 
    def __init__(self, x, y,plateforme):
        self.x = x 
        self.y = y
        self.plateforme = plateforme 

    def haut(self):
        new_y = self.y + 1
        if new_y < self.plateforme.hauteur and self.plateforme.est_vide(self.x, new_y):
            self.y = new_y
        else:
            print("Mur ou obstacle en haut")

    def bas(self):
        new_y = self.y - 1
        if new_y >= 0 and self.plateforme.est_vide(self.x, new_y):
            self.y = new_y
        else:
            print("Mur ou obstacle en bas")

    def droite(self):
        new_x = self.x + 1
        if new_x < self.plateforme.largeur and self.plateforme.est_vide(new_x, self.y):
            self.x = new_x
        else:
            print("Mur ou obstacle à droite")

    def gauche(self):
        new_x = self.x - 1
        if new_x >= 0 and self.plateforme.est_vide(new_x, self.y):
            self.x = new_x
        else:
            print("Mur ou obstacle à gauche")

    
    def diag_haut_gauche(self):
        new_x = self.x - 1
        new_y = self.y + 1
        if new_x >= 0 and new_y < self.plateforme.hauteur and self.plateforme.est_vide(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            print("Mur ou obstacle en diagonale haut-gauche")

    def diag_haut_droite(self):
        new_x = self.x + 1
        new_y = self.y + 1
        if new_x < self.plateforme.largeur and new_y < self.plateforme.hauteur and self.plateforme.est_vide(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            print("Mur ou obstacle en diagonale haut-droite")

    def diag_bas_gauche(self):
        new_x = self.x - 1
        new_y = self.y - 1
        if new_x >= 0 and new_y >= 0 and self.plateforme.est_vide(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            print("Mur ou obstacle en diagonale bas-gauche")

    def diag_bas_droite(self):
        new_x = self.x + 1
        new_y = self.y - 1
        if new_x < self.plateforme.largeur and new_y >= 0 and self.plateforme.est_vide(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            print("Mur ou obstacle en diagonale bas-droite")

            
    def afficher(self):
        print(f"x : {self.x}, y = {self.y}")
        
    def carre(self): 
            self.droite()
            print("Nouvelle position du robot :")
            self.afficher()
            print("\nPlateforme après déplacement :")
            self.plateforme.placer_robot(self)
            self.plateforme.afficher()
    
            self.bas()
            print("Nouvelle position du robot :")
            self.afficher()
            print("\nPlateforme après déplacement :")
            self.plateforme.placer_robot(self)
            self.plateforme.afficher()
    
            self.gauche()
            print("Nouvelle position du robot :")
            self.afficher()
            print("\nPlateforme après déplacement :")
            self.plateforme.placer_robot(self)
            self.plateforme.afficher()
    
            self.haut()
            print("Nouvelle position du robot :")
            self.afficher()
            print("\nFin du déplacement en carré :")
            self.plateforme.placer_robot(self)
            self.plateforme.afficher()


        
