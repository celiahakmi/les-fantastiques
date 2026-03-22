import pygame
import math
import time  
from Fantastic5 import initialisation_simulation
from Fantastic5.graphique import PygameView 
from Fantastic5.strategie import Tourner, AvancerDroit, Choregraphie, TracerCarre
from Fantastic5.simulation import Robot, Plateforme 

def main():

    p, r, strat = initialisation_simulation()
    view = PygameView(p, r, 50)

    running = True
    mouvement = True 

    while running:
        if mouvement: 
            if not strat.stop():
                strat.step()
            else:
                if not avancer:
                    print("Carré terminé ")
                    # On remplace la stratégie par une nouvelle
                    strat = AvancerDroit(r, 10.0)  # avance de 10m
                    strat.start()
                    avancer = True
                else:
                    # Si la deuxième stratégie est aussi finie
                    r.vL, r.vR = 0.0, 0.0

            # On fige le robot s'il se cogne 
            if not r.update():
                mouvement = False  

        time.sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        view.dessiner()

    pygame.quit()

if __name__ == "__main__":
    main()
