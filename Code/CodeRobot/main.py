import pygame
import math
from plateforme import Plateforme
from robot import Robot
from affichage import PygameView

def main():
    
    p = Plateforme(10, 10)
    p.init_obstacle(2, 2, 2, 1)
    p.init_obstacle(5, 5, 1, 1)

    r = Robot(5, 4, 0, 0.5, 0.5, 0.7, p)
    view = PygameView(p, r, 50)

    nbcote = 0
    long_cote = 2
    etat = "avance"
    x0 = r.x
    y0 = r.y
    angle_acc = 0.0
    chemin = [(8, 2), (8, 8), (2, 8)]
    idx_p = 0 #index du point courant
    
    running = True

    while running:
        view.horloge.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if nbcote < 4:

            if etat == "avance":
                r.vL = 0.1
                r.vR = 0.1

                d = math.sqrt((r.x - x0)**2 + (r.y - y0)**2)

                if d < long_cote:
                    r.avancer()
                else:
                    etat = "tourner"
                    angle_acc = 0.0

            elif etat == "tourner":
                r.vL = 0
                r.vR = 0.1

                angle = (r.vR - r.vL) / r.L
                angle_acc += abs(angle * r.pas)

                if angle_acc < math.pi / 2:
                    r.tourner()
                else:
                    nbcote += 1
                    etat = "avance"
                    x0 = r.x
                    y0 = r.y

        else:
            etat="chemin" 

        view.dessiner()

    pygame.quit()


if __name__ == "__main__":
    main()
