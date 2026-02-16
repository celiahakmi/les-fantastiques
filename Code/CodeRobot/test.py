import matplotlib.pyplot as plt
from plateforme import Plateforme
from robot import Robot
from affichage import PygameView

#Test plateforme
plateforme = Plateforme(20)
plateforme.ajouter_rectangle(2,2,3,3) 
print("Obstacles : ", plateforme.obstacles) #test si l'obstacle est bien dans la plateforme

#Tests de la fonction collision_rectangle
collision1= plateforme.collision_rectangle(0, 0, 1, 1)
print("Collision en (0,0,1,1) ? :", collision1) #False

collision2= plateforme.collision_rectangle(2, 2, 1, 1)
print("Collision en (2,2,1,1) ? :", collision2) #True

#Tests de la fonction distance_jusqua_obstacle
distance1=plateforme.distance_jusqua_obstacle(0, 0, 0)  
print("Distance depuis (0,0) vers la droite :", distance1)

distance2= plateforme.distance_jusqua_obstacle(0, 0, 1.57)  
print("Distance depuis (0,0) vers le haut :", distance2)
