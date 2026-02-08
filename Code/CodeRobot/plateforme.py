import matplotlib.pyplot as plt
import math 

class Plateforme:
    def __init__(self, taille):
        self.taille = taille
        self.fig, self.ax = plt.subplots()

    def initialiser_plan(self):
        """Initialise la plateforme avec une grille"""
        self.ax.set_xlim(0, self.taille)
        self.ax.set_ylim(0, self.taille)
        #Ajouter une grille
        self.ax.grid(True)
        
    def afficher_robot(self, robot):
        """Afficher le robot dans le plan -> cercle rouge"""
        self.point, = self.ax.plot(robot.y, robot.x, 'ro')
    def ajouter_cercle(self, x, y, rayon):
        self.obstacles.append(("cercle", x, y, rayon))

    def ajouter_carre(self, x, y, cote):
        self.obstacles.append(("carre", x, y, cote))

    def ajouter_triangle(self, x, y, cote):
        self.obstacles.append(("triangle", x, y, cote))
#Test
plateforme = Plateforme(20)
plateforme.initialiser_plan()
plt.show()
