import pygame
from plateforme import Plateforme
from robot import Robot 
from affichage import PygameView


def main():
    pygame.init()
    #Création de la plateforme
    plateforme = Plateforme(taille=20)
    
    #Obstacles prédéfinis
    plateforme.ajouter_rectangle(16, 4, 3, 3)
    plateforme.ajouter_rectangle(2, 2, 2, 7)
    plateforme.ajouter_rectangle(16, 16, 5, 5)


    #Paramètre du robot
    # position minimale est x = 1.0 et y = 0.5
    x = float(input("Position initiale x du robot : "))
    y = float(input("Position initiale y du robot : "))
    angle = float(input("Angle initial du robot (en degrés) : "))

    robot = Robot(
        x=x,
        y=y,
        theta_deg=angle,
        width=2.0,
        height=1.2,
        wheel_base=2.0,
        plateforme=plateforme
    )


view = PygameView(plateforme, robot, TAILLE_PIXEL=40)
d_stop = 0.05
d_go = 0.08
brake = False
base_speed = 3
turn_speed = 2

# Boucle principale 
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

       

    view.dessiner()

pygame.quit()
