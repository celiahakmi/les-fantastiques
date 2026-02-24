import pygame
import math
from robot import Robot
from plateforme2 import Plateforme
from affichage import PygameView


def main():

    p = Plateforme(10, 10)
    p.init_obstacle(5, 5, 2, 2)
    p.init_obstacle(1, 1, 1, 2)
    

    r = Robot(6, 7, 0, 1.0, 0.8, 1.2,plateforme=p)
    
    view = PygameView(p, r, TAILLE_PIXEL=50)

    nbcote = 0
    long_cote = 2
    etat = "avance"
    x0 = r.x
    y0 = r.y
    angle_acc = 0.0

    running = True

    while running:
        view.horloge.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if nbcote < 4:

            if etat == "avance":
                r.vL = 1.0
                r.vR = 1.0

                d = math.sqrt((r.x - x0)**2 + (r.y - y0)**2)

                if d < long_cote:
                    r.avancer()
                else:
                    etat = "tourner"
                    angle_acc = 0.0

            elif etat == "tourner":
                r.vL = -1.0
                r.vR = 1.0

                omega = (r.vR - r.vL) / r.L
                angle_acc += abs(omega * r.pas)

                if angle_acc < math.pi / 2:
                    r.tourner()
                else:
                    nbcote += 1
                    etat = "avance"
                    x0 = r.x
                    y0 = r.y

        else:
            r.vL = 0
            r.vR = 0

        view.dessiner()

    pygame.quit()


if __name__ == "__main__":
    main()
