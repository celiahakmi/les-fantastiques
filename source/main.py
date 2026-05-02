import time  
from Fantastic5 import initialisation_simulation 
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner, Arreter, Choregraphie, Condition

def main():
    simu = True

    if simu:
        print("Mode simulation activé")
        print("Mode simulation activé")

        import pygame
        from Fantastic5.graphique import PygameView

        # Monde virtuel
        p, r = initialisation_simulation()

        view = PygameView(p, r, 50)
        adp = AdaptateurSimu(r)

    else:
        print("Mode robot réel activé")
        from Fantastic5.api.robotAPI import Robot2IN013

        robot_reel = Robot2IN013()
        adp = AdaptateurIRL(robot_reel)

    action1 = Choregraphie(adp, [
        AvancerDroit(adp, 1),
        Tourner(adp, 90),
        AvancerDroit(adp, 1),
        Tourner(adp, 90),
        AvancerDroit(adp, 1),
        Tourner(adp, 90),
        AvancerDroit(adp, 1),
        Tourner(adp, 90),
        AvancerDroit(adp, 1)
    ])

    action2 = Choregraphie(adp,[
    AvancerDroit(adp, 4.5),    
    Tourner(adp, 90),          
    AvancerDroit(adp, 3.0),    
    Tourner(adp, 90),          
    AvancerDroit(adp, 4.0),    
    Tourner(adp, 270),  
    AvancerDroit(adp, 2.0),   
    Tourner(adp, 270),         
    AvancerDroit(adp, 2.5),  
    Tourner(adp, 90),          
    AvancerDroit(adp, 3.0)   
])

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
                pass  # Le robot a touché un mur

            view.dessiner()

            # Fermer la fenêtre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        time.sleep(0.0000000000000001)

    if simu:
        import pygame
        pygame.quit()


if __name__ == "__main__":
    main()
