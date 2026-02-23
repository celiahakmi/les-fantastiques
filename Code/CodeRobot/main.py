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
    
    vue = PygameView(plateforme, robot, TAILLE_PIXEL=60)

    # carré auto
    auto = False
    etat = "avance"
    nb = 0
    cote = 2.0
    x0, y0 = robot.x, robot.y
    angle = 0.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    auto = True
                    etat = "avance"
                    nb = 0
                    x0, y0 = robot.x, robot.y
                    angle = 0.0

        keys = pygame.key.get_pressed()
        robot.vL = 0.0
        robot.vR = 0.0
        manuel = False


if __name__ == "__main__":
    main()

