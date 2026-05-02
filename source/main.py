import time

from Fantastic5 import initialisation_simulation
from Fantastic5.adaptateur import AdaptateurIRL, AdaptateurSimu
from Fantastic5.strategie import (AvancerDroit,Choregraphie,Condition,ContournerObstacle,
Tourner,TournerArc,)


def obstacle_proche(adaptateur):
    return adaptateur.get_distance() <= 0.45


def creer_parcours_demo(adaptateur):
    rayon_virage = 0.25
    return Choregraphie(
        adaptateur,
        [
            AvancerDroit(adaptateur, 1.0),
            Tourner(adaptateur, 90),
            AvancerDroit(adaptateur, 1.0),
            Tourner(adaptateur, 90),
            AvancerDroit(adaptateur, 1.0),
            Tourner(adaptateur, 90),
            AvancerDroit(adaptateur, 1.0),
            Tourner(adaptateur, 90),
            AvancerDroit(adaptateur, 5.4),
            Tourner(adaptateur, 90),
            AvancerDroit(adaptateur, 3.35 - rayon_virage),
            TournerArc(adaptateur, 90, rayon=rayon_virage),
            AvancerDroit(adaptateur, 3.1 - rayon_virage),
            Tourner(adaptateur, -90),
            AvancerDroit(adaptateur, 1.75),
            Tourner(adaptateur, -90),
            AvancerDroit(adaptateur, 3.35),
            Tourner(adaptateur, 90),
            AvancerDroit(adaptateur, 2.1),
            Tourner(adaptateur, 90),
            AvancerDroit(adaptateur, 1.8),
        ],
    )


def creer_strategie(adaptateur):
    parcours = creer_parcours_demo(adaptateur)
    contournement = ContournerObstacle(
        adaptateur,
        angle_deg=90,
        distance_deport=0.9,
    )
    return Condition(
        adaptateur,
        obstacle_proche,
        contournement,
        parcours,
    )


def main():
    simu = True

    if simu:
        print("Mode simulation active")
        
        import pygame
        from Fantastic5.graphique import PygameView

        plateforme, robot = initialisation_simulation()
        view = PygameView(plateforme, robot, 50)
        adp = AdaptateurSimu(robot)
    else:
        print("Mode robot reel active")

        
        from Fantastic5.api.robotAPI import Robot2IN013

        robot_reel = Robot2IN013()
        adp = AdaptateurIRL(robot_reel)
        robot = None

    strategie = creer_strategie(adp)
    strategie.start()

    running = True
    while running:
        if not strategie.stop():
            strategie.step()
        else:
            adp.set_vitesse(0.0, 0.0)
            if not simu:
                running = False

        if simu:
            if not robot.update():
                adp.set_vitesse(0.0, 0.0)

            view.dessiner()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        time.sleep(0.01)

    if simu:
        pygame.quit()


if __name__ == "__main__":
    main()
