import matplotlib.pyplot as plt
from plateforme import Plateforme
from robot import Robot
from affichage import PygameView

#Test plateforme
plateforme = Plateforme(20)
plateforme.initialiser_plan()
plt.show()
