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


       
