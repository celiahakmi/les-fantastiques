import matplotlib.pyplot as plt
from plateforme import Plateforme
from robot import Robot
from affichage import PygameView

#Test plateforme

#Test de la fonction ajouter_rectangle 
#On vérifie si l'obstacle est bien présent dans la plateforme
plateforme = Plateforme(20)
plateforme.ajouter_rectangle(2,2,3,3) 
print("Obstacles : ", plateforme.obstacles) 

#Test de la fonction collision_rectangle
#On vérifie la collision ou non
collision1= plateforme.collision_rectangle(0, 0, 1, 1)
print("Collision en (0,0,1,1) ? :", collision1) #False

collision2= plateforme.collision_rectangle(2, 2, 1, 1)
print("Collision en (2,2,1,1) ? :", collision2) #True

#Test de la fonction distance_jusqua_obstacle
#On vérifie la distance jusqu'au premier obstacle
distance1=plateforme.distance_jusqua_obstacle(0, 0, 0)  
print("Distance depuis (0,0) vers la droite :", distance1)

distance2= plateforme.distance_jusqua_obstacle(0, 0, 1.57)  
print("Distance depuis (0,0) vers le haut :", distance2)


#Test Robot
#On vérifie que le robot est initialisé correctement
robot= Robot(
    x=1.0,
    y=1.0,
    theta_deg=0,
    width=1.0,
    height=1.0,
    wheel_base=1.0,
    plateforme=plateforme
)
print("Position initiale : x =", robot.x, ", y =", robot.y, ", theta =", robot.theta)
