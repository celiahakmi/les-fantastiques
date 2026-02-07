import matplotlib.pyplot as plt

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

#Test
plateforme = Plateforme(20)
plateforme.initialiser_plan()
plt.show()
