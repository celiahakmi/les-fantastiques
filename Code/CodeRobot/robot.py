class Robot:
    def __init__(self,x,y,largeur,longueur,plateforme):
        self.x=x
        self.y=y
        self.largeur=largeur
        self.longueur=longueur
        self.plateforme = plateforme 
     def haut(self, d):
            new_y = self.y + d
            if self.plateforme.position_valide(self.x, new_y, self.largeur, self.hauteur):
                self.y = new_y
            else:
                print("Mur ou obstacle en haut")

    def bas(self, d):
            new_y = self.y - d
            if self.plateforme.position_valide(self.x, new_y, self.largeur, self.hauteur):
                self.y = new_y
            else:
                print("Mur ou obstacle en bas")

     def droite(self, d):
            new_x = self.x + d
            if self.plateforme.position_valide(new_x, self.y, self.largeur, self.hauteur):
                self.x = new_x
            else:
                print("Mur ou obstacle a droite")

    def gauche(self, d):
            new_x = self.x - d
            if self.plateforme.position_valide(new_x, self.y, self.largeur, self.hauteur):
                self.x = new_x
            else:
                print("Mur ou obstacle a gauche")

    def afficher(self):
        print(f"Position : x={self.x:.2f}, y={self.y:.2f}")

    


    


       
