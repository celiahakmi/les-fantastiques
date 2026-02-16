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

    width= float(input("Largeur du robot:"))
    height= float(input("Hauteur du robot:"))
    wheel_base= float(input("Distance entre les roues:"))
    
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
    #paramètre capteurs 
    d_stop = 0.05
    d_go = 0.08
    brake = False

    base_speed = 3
    turn_speed = 2

    running = True
    while running:

        dt = view.horloge.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        d = robot.scan_distance()

        forward = 0
        turn = 0

        if keys[pygame.K_UP]:
            forward = 1
        if keys[pygame.K_DOWN]:
            forward = -1
        if keys[pygame.K_LEFT]:
            turn = 1
        if keys[pygame.K_RIGHT]:
            turn = -1

        vL = forward * base_speed - turn * turn_speed
        vR = forward * base_speed + turn * turn_speed

        if not brake and d <= d_stop:
            brake = True
        elif brake and d >= d_go:
            brake = False

        mean = (vL + vR) / 2
        diff = (vR - vL) / 2

        if brake and mean > 0:
            mean = 0
            robot.vL = 0
            robot.vR = 0

        vL = mean - diff
        vR = mean + diff

        robot.set_wheel_targets(vL, vR)
        robot.step(dt)

        view.dessiner()

    pygame.quit()


if __name__ == "__main__":
    main()





