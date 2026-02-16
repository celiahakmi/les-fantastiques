import matplotlib.pyplot as plt
from plateforme import Plateforme
from robot import Robot
from affichage import PygameView

#Test plateforme
plateforme = Plateforme(20)
plateforme.ajouter_rectangle(2,2,3,3) 
print("Obstacles : ", plateforme.obstacles) #test si l'obstacle est bien dans la plateforme

#Test de la fonction collision_rectangle
collision1= plateforme.collision_rectangle(0, 0, 1, 1)
print("Collision en (0,0,1,1) ? :", collision1) #False

collision2= plateforme.collision_rectangle(2, 2, 1, 1)
print("Collision en (2,2,1,1) ? :", collision2) #True
