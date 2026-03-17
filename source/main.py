import pygame
import math
from Fantastic5.simulation import Plateforme, Robot
from Fantastic5.strategie import AvancerDroit, Tourner, TracerCarre
from Fantastic5.Graphique.affichage import PygameView

def main():
    p = Plateforme(10, 10)
    p.init_obstacle(7, 1, 2, 1)
    p.init_obstacle(5, 5, 1, 1)

    r = Robot(5, 2, 0, 0.5, 0.5, 0.7, p)
    view = PygameView(p, r, 50)

    # instanciation d'une stratégie
    strat = AvancerDroit(r, 7.0) # avancer de 2m
    strat.start()

    running = True

    while running:
        view.horloge.tick(10) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # On demande à la stratégie de mettre à jour les vitesses vL et vR
        if not strat.stop():
            strat.step()
        else:
            r.vL, r.vR = 0, 0 # On s'arrête si la stratégie est finie


        # maj position robot
        r.update()

        # validation ou annulation de la plateforme
        p.collision_robot(r)

        view.dessiner()

    pygame.quit()

if __name__ == "__main__":
    main()
