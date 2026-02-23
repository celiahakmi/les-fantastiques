import math
import pygame
from affichage import PygameView
from plateforme import Plateforme
from robot import Robot


def main():
    
    plateforme = Plateforme(10, 10)
    plateforme.init_obstacle(2, 2, 2, 1)
    plateforme.init_obstacle(5, 5, 1, 1)

    robot = Robot(1, 1, 0, L=0.5, larg=0.5, long=0.7)
    
    vue = PygameView(plateforme, robot, TAILLE_PIXEL=60)

    # carré automatique
    auto = False # Mode automatique désactivé au départ
    etat = "avance"  # le robot commence par avancer
    nb = 0
    cote = 2.0
    x0, y0 = robot.x, robot.y
    angle = 0.0

    running = True   # Variable pour garder la boucle active
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
        manuel = False #Indique si on utilise le contrôle manuel
        
        # manuel
        if keys[pygame.K_UP]:
            manuel = True
            auto = False
            robot.vL = 1.0
            robot.vR = 1.0
            plateforme.deplacer_si_possible(robot, robot.avancer)

        elif keys[pygame.K_DOWN]:
            manuel = True
            auto = False
            robot.vL = -1.0
            robot.vR = -1.0
            plateforme.deplacer_si_possible(robot, robot.avancer)

        elif keys[pygame.K_LEFT]:
            manuel = True
            auto = False
            robot.vL = -1.0
            robot.vR = 1.0
            plateforme.deplacer_si_possible(robot, robot.tourner)

        elif keys[pygame.K_RIGHT]:
            manuel = True
            auto = False
            robot.vL = 1.0
            robot.vR = -1.0
            plateforme.deplacer_si_possible(robot, robot.tourner)
            
        # animé
        if auto and not manuel:
            if etat == "avance":
                robot.vL = 1.0
                robot.vR = 1.0
                if plateforme.deplacer_si_possible(robot, robot.avancer):
                    if math.hypot(robot.x - x0, robot.y - y0) >= cote:
                        etat = "tourne"
                        angle = 0.0
                else:
                    auto = False # Stop si collision

            elif etat == "tourne":
                # Rotation sur place
                robot.vL = -1.0
                robot.vR = 1.0
                if plateforme.deplacer_si_possible(robot, robot.tourner):
                    # Calcul de la vitesse angulaire et accumulation de l’angle tourné
                    angle += abs((robot.vR - robot.vL) / robot.L) * robot.pas
                    # Si 90° atteint
                    if angle >= math.pi / 2:
                        nb += 1  #Un côté terminé
                        if nb == 4:
                            # Carré terminé
                            auto = False
                            robot.vL = 0.0
                            robot.vR = 0.0
                        else:
                            # Repartir pour le côté suivant
                            etat = "avance"
                            x0, y0 = robot.x, robot.y
                else:
                    auto = False # Stop si collision

      
        vue.dessiner()
        vue.horloge.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()

