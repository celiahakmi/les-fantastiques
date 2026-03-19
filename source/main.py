import pygame
import math
import time
from Fantastic5.Graphique.affichage import PygameView
from Fantastic5.Simulation.simulation import Plateforme, Robot
from Fantastic5.Strategie.strategie import AvancerDroit, Tourner, TracerCarre


def main():
    p = Plateforme(10, 10)
    p.init_obstacle(8, 3, 2, 1)
    p.init_obstacle(5, 5, 1, 1)

    r = Robot(5, 2, 0, 0.5, 0.5, 0.7, p)
    view = PygameView(p, r, 50)

    strat = TracerCarre(r, 2.0) 
    strat.start()
    
    avancer = False 
    running = True

    while running:
        view.horloge.tick(300)

        if not strat.stop():
            strat.step()
        else:
            # Si le carré est finit 
            if not avancer:
                print("Carré terminé")
                # On remplace la stratégie par une nouvelle
                strat = AvancerDroit(r, 10.0) # Avance de 10m
                strat.start()
                avancer = True 
            else:
                # Si la deuxième stratégie est aussi finie
                r.vL, r.vR = 0.0, 0.0
        r.update()
        time.sleep(0.01)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        view.dessiner()
    pygame.quit()

if __name__ == "__main__":
    main()
