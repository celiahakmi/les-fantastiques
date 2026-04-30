import time  
from Fantastic5 import initialisation_simulation 
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner, Arreter, Choregraphie, Condition

def main():
    simu = True  # False pour robot réel

    if simu:
        print("Mode simulation activé")
        import pygame
        from Fantastic5.graphique import PygameView

        p, r = initialisation_simulation()
        view = PygameView(p, r, 50)
        adp = AdaptateurSimu(r)

    else:
        print("Mode robot réel activé")
        from Fantastic5.API.robotAPI import Robot2IN013

        robot_reel = Robot2IN013()
        adp = AdaptateurIRL(robot_reel)

    carre = Choregraphie(adp, [
        AvancerDroit(adp, 2),
        Tourner(adp, 90),
        AvancerDroit(adp, 2),
        Tourner(adp, 90),
        AvancerDroit(adp, 2),
        Tourner(adp, 90),
        AvancerDroit(adp, 2),
        Tourner(adp, 90)
    ])

    seuil_obstacle = 0.5 if simu else 300

    mur = Condition(
        adp,
        lambda adp: adp.get_distance() > seuil_obstacle,
        Arreter(adp),
        Arreter(adp)
    )


    strat_globale = Choregraphie(adp, [carre, mur])

    strat_globale.start()

    running = True

    while running:
        if not strat_globale.stop():
            strat_globale.step()
        else:
            adp.set_vitesse(0.0, 0.0)
            running = False

        if simu:
            r.update()
            view.dessiner()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        time.sleep(0.01)

    adp.set_vitesse(0.0, 0.0)

    if simu:
        pygame.quit()


if __name__ == "__main__":
    main()