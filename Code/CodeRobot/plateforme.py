import matplotlib.pyplot as plt
from robot import Robot

class Plateforme:
    def __init__(self, taille):
        self.taille = taille
        self.fig, self.ax = plt.subplots()
        self.obstacles = [] 
   
    def initialiser_plan(self):
        """Initialise la plateforme avec une grille"""

        self.ax.set_xlim(0, self.taille)
        self.ax.set_ylim(0, self.taille)
        #Ajouter une grille
        self.ax.grid(True)
        
    def afficher_robot(self, robot):
        """Afficher le robot dans le plan -> cercle rouge"""

        self.point, = self.ax.plot(robot.y, robot.x, 'ro')

    def ajouter_rectangle(self, x, y, cote1, cote2):
        self.obstacles.append(("carre", x, y, cote1, cote2))

    def verifier_position(self, x, y, largeur, hauteur):
        # On calcule les bords en partant du centre
        gauche = x - (largeur / 2)
        droite = x + (largeur / 2)
        haut = y - (hauteur / 2)
        bas = y + (hauteur / 2)

        # Vérification des bords de la plateforme
        if gauche < 0 or haut < 0 or droite > self.taille or bas > self.taille:
            return False

        # Vérification des obstacles
        for obs in self.obstacles:
            _, ox, oy, o_l, o_h = obs
            
            # Collision ajustée au centre du robot
            if (gauche < ox + o_l and droite > ox and haut < oy + o_h and bas > oy):
                return False
        return True
