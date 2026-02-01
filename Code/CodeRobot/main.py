import tkinter as tk
from class_plateforme import Plateforme
from Robot import Robot
from interface import InterfacePlateforme

# Inputs
lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))

if lignes <=0 or colonnes <=0:
    print("Les dimensions doivent être positives")
    
plateforme = Plateforme(lignes, colonnes)

x = int(input("Position x du robot : "))
y = int(input("Position y du robot : "))

if not (0 <= x < lignes and 0 <= y < colonnes):
    print("Position hors plateforme")
   
robot = Robot(x, y, plateforme) 

print("Position logique du robot :")
robot.afficher()

print("\nPlateforme initiale :")
plateforme.placer_robot(robot)
plateforme.afficher()

print("Déplacement en carré...\n")
robot.carre(plateforme)  

# Interface Tkinter
root = tk.Tk()
root.title("Simulation du robot")
interface = InterfacePlateforme(root, plateforme, robot)
root.mainloop()
