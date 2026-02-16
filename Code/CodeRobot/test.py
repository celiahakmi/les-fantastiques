import matplotlib.pyplot as plt
from plateforme import Plateforme
from robot import Robot
from affichage import PygameView

#Test plateforme
plateforme = Plateforme(20)
plateforme.ajouter_rectangle(2,2,3,3) 
print("Obstacles : ", plateforme.obstacles) #test si l'obstacle est bien dans la plateforme
