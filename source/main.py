import time  
from Fantastic5 import initialisation_simulation 
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner, Arreter, Choregraphie, Condition, ContournerObstacle


def obstacle_proche(adaptateur):
    """Fonction de condition : renvoie True si un mur/obstacle est à moins de 5mm"""
    d = adaptateur.get_distance()
    print(f"Distance capteur : {d}")
    return d <= 0.5

def main():
    simu = True

    if simu:
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
    Tourner(adp, -90),  
    AvancerDroit(adp, 2.0),   
    Tourner(adp, -90),         
    AvancerDroit(adp, 4.5),  
    Tourner(adp, 90),          
     
])
    contournement = ContournerObstacle(adp)

    strat_globale = Choregraphie(adp, [action1, action2, contournement, Arreter(adp)])

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
                print("le robot a trouvé la sortie")  
                adp.set_vitesse(0.0, 0.0)
                running = False  
                

            view.dessiner()

            # Fermer la fenêtre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        time.sleep(0.01)

    if simu:
        import pygame
        pygame.quit()


if __name__ == "__main__":
    main()