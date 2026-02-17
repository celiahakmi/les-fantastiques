import pygame
from plateforme import Plateforme
from robot import Robot
from affichage import PygameView


def main():
    pygame.init()

    plateforme = Plateforme(20)
    #obstacles
    plateforme.ajouter_rectangle(2, 2, 3, 7)
    plateforme.ajouter_rectangle(12, 4, 4, 3)
    plateforme.ajouter_rectangle(8, 14, 6, 2)
    #paramètre initiaux 
    x = float(input("Position x : "))
    y = float(input("Position y : "))
    angle = float(input("Angle (degrés) : "))
    
    robot = Robot(
        x=x,
        y=y,
        theta_deg=angle,
        width=2.0,
        height=1.2,
        wheel_base=2.0,
        plateforme=plateforme
    )

    view = PygameView(plateforme, robot, 40)

    longueur_cote= 1.5
    base_speed = 3
    turn_speed = 2

    etat = "avance" 
    cote_compte = 0

    x_start = robot.x
    y_start = robot.y 
    angle_accumule = 0.0

    running = True
    while running:

        dt = view.horloge.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if etat == "avance":
            #distance parcourue depuis le début du coté
            distance = math.sqrt( (robot.x - x_start)**2 + (robot.y - y_start)**2) #distance entre deux points
            if distance < longueur_cote: 
                #Avancer tout droit 
                vL = base_speed
                vR = base_speed
            else: 
                #Fin du côté -> début de la rotation du robot 
                etat = "tourne" 
                angle_accumule = 0.0 
                vL = 0.0
                vR = 0.0
        robot.set_wheel_targets(vL, vR)
        robot.step(dt)

        view.dessiner()

    pygame.quit()


if __name__ == "__main__":
    main()





