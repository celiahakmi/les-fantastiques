import time  
from Fantastic5 import initialisation_simulation 
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner,Arreter, Accelerer, Choregraphie, Condition, Boucle

def main():

    simu = False   
    
    if simu:
        print("Mode simulation activé ")
        from Fantastic5.graphique import PygameView 
        #le monde virtuel
        p, r, _ = initialisation_simulation() 

        view = PygameView(p, r, r2, 50)
        adp = AdaptateurSimu(r)
        p, r, _ = initialisation_simulation() 
        #  initialise la vue 3D
        view = PygameView(p, r, r2, 50)
        adp = AdaptateurSimu(r)

    else:
        from Fantastic5.API.robotAPI import Robot2IN013
        _, _, r2 = initialisation_simulation() 

        print("Mode robot réel activé ")
        adp = AdaptateurIRL(r2)
        pass 

    
    action1 = Choregraphie(adp, [AvancerDroit(adp, 10), AvancerDroit(adp, 1)])
    action2 = Condition(adp, Accelerer(adp, 20.0, 0.5, 0.01), Arreter(adp), 1.0)
    action3 = Choregraphie(adp, [AvancerDroit(adp, 1), Tourner(adp, 60), AvancerDroit(adp, 1), Tourner(adp, 60), AvancerDroit(adp, 1), Tourner(adp, 60), AvancerDroit(adp, 1), Tourner(adp, 60), AvancerDroit(adp, 1), Tourner(adp, 60), AvancerDroit(adp, 1), Tourner(adp, 60)])
    strat_globale = Choregraphie(adp, [action1])

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

        time.sleep(0.001)
        time.sleep(0.01)

    if simu:
        import pygame
        pygame.quit()

if __name__ == "__main__":
    main()
