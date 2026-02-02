class Robot: 
    def __init__(self, x, y,plateforme,vitesse):
        self.x = x 
        self.y = y
        self.plateforme = plateforme 
        self.vitesse = vitesse

    def haut(self):
        for i in range(self.vitesse):
            new_y = self.y + 1
            if new_y < self.plateforme.hauteur and self.plateforme.est_vide(self.x, new_y):
                self.y = new_y
            else:
                print("Mur ou obstacle en haut")
                break


    def bas(self):
        for i in range(self.vitesse):
            new_y = self.y - 1
            if new_y >= 0 and self.plateforme.est_vide(self.x, new_y):
                self.y = new_y
            else:
                print("Mur ou obstacle en bas")
                break


    def droite(self):
        for i in range(self.vitesse):
            new_x = self.x + 1
            if new_x < self.plateforme.largeur and self.plateforme.est_vide(new_x, self.y):
                self.x = new_x
            else:
                print("Mur ou obstacle à droite")
                break


    def gauche(self):
        for i in range(self.vitesse):
            new_x = self.x - 1
            if new_x >= 0 and self.plateforme.est_vide(new_x, self.y):
                self.x = new_x
            else:
                print("Mur ou obstacle à gauche")
                break


    
    def diag_haut_gauche(self):
        for i in range(self.vitesse):
            new_x = self.x - 1
            new_y = self.y + 1
            if new_x >= 0 and new_y < self.plateforme.hauteur and self.plateforme.est_vide(new_x, new_y):
                self.x = new_x
                self.y = new_y
            else:
                print("Mur ou obstacle en diagonale haut-gauche")
                break


    def diag_haut_droite(self):
        for i in range(self.vitesse):
            new_x = self.x + 1
            new_y = self.y + 1
            if (
                new_x < self.plateforme.largeur
                and new_y < self.plateforme.hauteur
                and self.plateforme.est_vide(new_x, new_y)
            ):
                self.x = new_x
                self.y = new_y
            else:
                print("Mur ou obstacle en diagonale haut-droite")
                break


    def diag_bas_gauche(self):
        for i in range(self.vitesse):
            new_x = self.x - 1
            new_y = self.y - 1
            if (
                new_x >= 0
                and new_y >= 0
                and self.plateforme.est_vide(new_x, new_y)
            ):
                self.x = new_x
                self.y = new_y
            else:
                print("Mur ou obstacle en diagonale bas-gauche")
                break


    def diag_bas_droite(self):
        for i in range(self.vitesse):
            new_x = self.x + 1
            new_y = self.y - 1
            if (
                new_x < self.plateforme.largeur
                and new_y >= 0
                and self.plateforme.est_vide(new_x, new_y)
            ):
                self.x = new_x
                self.y = new_y
            else:
                print("Mur ou obstacle en diagonale bas-droite")
                break


            
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



        
