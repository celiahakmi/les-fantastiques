class Plateforme:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.matrice = []
        self.initialiser_matrice()

    def initialiser_matrice(self):
        self.matrice = []
        for i in range(self.lignes):
            ligne = []
            for j in range(self.colonnes):
                ligne.append(".")
            self.matrice.append(ligne)

    def matrice_est_vide(self):
        for ligne in self.matrice:
            for case in ligne:
                    if case != ".":
                        return False
        return True

    def placer_robot(self, robot):
        self.initialiser_matrice()
        self.matrice[robot.x][robot.y] = "R"

    def afficher(self):
        for ligne in self.matrice:
            print(" ".join(ligne))
        print()
