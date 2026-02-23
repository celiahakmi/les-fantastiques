import math
import pygame
from affichage import PygameView
from plateforme import Plateforme
from robot import Robot




//si il y a une collision on remet le robot a son ancienne position on reinitialise les vitesse et on retourne false 
def deplacer_si_possible(robot, plateforme, action):
    x, y, t = robot.x, robot.y, robot.theta
    action()
    if plateforme.collision_robot(robot):
        robot.x, robot.y, robot.theta = x, y, t
        robot.vL = 0.0
        robot.vR = 0.0
        return False
    return True

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

