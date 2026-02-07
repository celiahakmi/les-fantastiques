class Plateforme:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes      #nombre de lignes
        self.colonnes = colonnes  #nombre de colonnes
        self.hauteur = lignes 
        self.largeur = colonnes
        self.matrice = [] #représente la grille
    #obstacles prédéfinis 
        self.obstacles = [(1, 2), (3, 3), (4, 1)]
        self.initialiser_matrice()
        self.placer_obstacles()

    def initialiser_matrice(self):
        """Remplit la matrice de '.' """
        self.matrice = [["." for _ in range(self.colonnes)] for _ in range(self.lignes)]

    def placer_obstacles(self):
        """Place les obstacles X"""
        for (x, y) in self.obstacles:
            ligne = self.lignes - 1 - y  #conversion y (index ligne)
            colonne = x
            self.matrice[ligne][colonne] = "X"

    def matrice_est_vide(self):
        """Retourne True si la matrice ne contient ni robot ni obstacle"""
        for ligne in self.matrice:
            for case in ligne:
                if case != ".":
                    return False
        return True

    def contient_robot(self):
        """Retourne True si le robot est dans la matrice"""
        for ligne in self.matrice:
            for case in ligne:
                if case == "R":
                    return True
        return False

    def placer_robot(self, robot):
        """Place le robot sur la matrice sans effacer les obstacles"""
        self.initialiser_matrice()
        self.placer_obstacles()  #remet les obstacles
        ligne = self.lignes - 1 - robot.y
        colonne = robot.x
        self.matrice[ligne][colonne] = "R"

    def est_vide(self, x, y):
        """Retourne True si la case (x,y) est libre"""
        ligne = self.lignes - 1 - y
        return self.matrice[ligne][x] == "."

    def afficher(self):
        for ligne in self.matrice:
            print(" ".join(ligne))
        print()

