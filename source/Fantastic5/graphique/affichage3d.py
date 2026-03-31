import math
from vpython import canvas, box, vector, color, rate

class Vue3D:
    def __init__(self, plateforme, robot):
        self.plateforme = plateforme
        self.robot_physique = robot 

        # La fenêtre
        self.vu = canvas(title='Simulation 3D', width=800, height=600)
        self.vu.center = vector(5.0, 0, 5.0) 
        
        # Plateforme
        self.sol = box(pos=vector(5.0, -0.1, 5.0), 
                       size=vector(10.0, 0.2, 10.0), 
                       color=color.gray(0.7))
        
        # dessin du Robot 
        self.robot_dessin = box(pos=vector(robot.x, 0.5, robot.y),
                                size=vector(1.0, 1.0, 1.0), 
                                color=color.blue)
        
        # Le traot rouge
        self.trait_robot = box(pos=vector(robot.x + 0.5, 0.5, robot.y), 
                               size=vector(0.3, 0.3, 0.3), 
                               color=color.red)
