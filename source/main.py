import time  
from Fantastic5.simulation import Plateforme, Robot
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, TracerCarre, Tourner, Choregraphie

def main():

    simu = True  

    if simu:
        print("Mode simulation activé ")

        import pygame
        from Fantastic5.graphique import PygameView 

        #le monde virtuel
        p = Plateforme(10.0, 10.0)
        p.init_obstacle(2.0, 2.0, 1.0, 1.0) 
        r = Robot(5.0, 5.0, 0.0, 0.5, 0.5, 0.7, p)

        view = PygameView(p, r, 50)
        adp = AdaptateurSimu(r)

    else:
        print("Mode robot réel activé ")
        # Ici on crée le vrai robot 
        # r =
        # adp = AdaptateurIRL(r)
        pass 

    strat_globale = TracerCarre(adp, 4.0)
    
    action1 = TracerCarre(adp, 2.0)
    action2 = AvancerDroit(adp, 90)
    strat_globale = Choregraphie(adp, [action1, action2])

    strat_globale.start()

    running = True

    while running:

        if not strat_globale.stop():
            strat_globale.step()
        else:
            adp.set_vitesse(0.0, 0.0) 
            if not simu:
                running = False 

        if simu:      
            if not r.update(): 
                pass # Le robot a touché un mur

            view.dessiner()

            # fermer la fenêtre 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        time.sleep(0.01)

    if simu:
        import pygame
        pygame.quit()

if __name__ == "__main__":
    main()
