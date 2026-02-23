
from plateforme import Plateforme
from robot import Robot

def main():
    
    plateforme = Plateforme(10, 10)
    plateforme.init_obstacle(2, 2, 2, 1)
    plateforme.init_obstacle(5, 5, 1, 1)

    robot = Robot(1, 1, 0, L=0.5, larg=0.5, long=0.7)
    
    print("Plateforme :", plateforme.longueur, "x", plateforme.hauteur)
    print("Obstacles :", plateforme.obstacles)
    print("Robot initial position :", robot.x, robot.y, "angle :", robot.theta)

    #on avance
    robot.vL = 1.0
    robot.vR = 1.0
    robot.avancer()
    print("Robot après avancer :", robot.x, robot.y)

    # on tourne
    robot.vL = 0.5
    robot.vR = 1.0
    robot.tourner()
    print("Robot après tourner :", robot.x, robot.y, "angle :", robot.theta)

if __name__ == "__main__":
    main()
