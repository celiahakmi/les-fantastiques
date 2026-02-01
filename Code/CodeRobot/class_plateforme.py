class Plateforme:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.matrice = []
    # placer les obstacles
        self.obstacles = [(1, 2), (3, 3), (4, 1)]
        self.initialiser_matrice()

    
    def initialiser_matrice(self):
        self.matrice = []
        for i in range(self.lignes):
            ligne = []
            for j in range(self.colonnes):
                ligne.append(".")
            self.matrice.append(ligne)
    # placer les obstacles X
        for (x, y) in self.obstacles:
            self.matrice[x][y] = "X"

    
    # Est-ce que la plateforme est vide
    def matrice_est_vide(self):
        for ligne in self.matrice:
            for case in ligne:
                    if case != ".":
                        return False
        return True

    
    # Est-ce qu'il y a un robot dans la plateforme 
    def contient_robot(self):
        for ligne in self.matrice:
            for case in ligne:
                if case == "R":
                    return True
        return False

    
    def placer_robot(self, robot):
        self.initialiser_matrice()
        self.matrice[robot.x][robot.y] = "R"

    
    def afficher(self):
        for ligne in self.matrice:
            print(" ".join(ligne))
        print()
