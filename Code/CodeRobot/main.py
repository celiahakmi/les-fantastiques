import pygame
from plateforme import Plateforme
from robot import Robot 
from affichage import PygameView

#Création de la plateforme
plateforme = Plateforme(taille=20)

#Obstacles prédéfinis
plateforme.ajouter_cercle(4, 4, 2)
plateforme.ajouter_carre(16, 4, 3)
plateforme.ajouter_triangle(10, 10, 3)

#Paramètre du robot
x = float(input("Position initiale x du robot : "))
y = float(input("Position initiale y du robot : "))
angle = float(input("Angle initial du robot (en degrés) : "))

robot = Robot(
    x=x,
    y=y,
    largeur=2,
    longueur=1,
    angle=angle,
    plateforme=plateforme
)

# configuration  de Pygame et la View
pygame.init()
view = PygameView(plateforme, robot, TAILLE_PIXEL=40)
#longueur d'un coté du carré
carre_cote = 3 

# Boucle principale 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Déplacement carré étape par étape
                robot.avancer(carre_cote)
                view.dessiner()
                pygame.time.delay(400)

                robot.tourner(90)
                view.dessiner()
                pygame.time.delay(400)

                robot.avancer(carre_cote)
                view.dessiner()
                pygame.time.delay(400)

                robot.tourner(90)
                view.dessiner()
                pygame.time.delay(400)

                robot.avancer(carre_cote)
                view.dessiner()
                pygame.time.delay(400)

                robot.tourner(90)
                view.dessiner()
                pygame.time.delay(400)

                robot.avancer(carre_cote)
                view.dessiner()
                pygame.time.delay(400)

                robot.tourner(90)
                view.dessiner()
                pygame.time.delay(400)
            
    keys = pygame.key.get_pressed()
    # Avancer/reculer
    if keys[pygame.K_UP]:
        robot.avancer(1.0)   # avancer
    if keys[pygame.K_DOWN]:
        robot.avancer(-1.0)  # reculer

    # Tourner
    if keys[pygame.K_LEFT]:
        robot.tourner(-5)    # tourner 5° à gauche
    if keys[pygame.K_RIGHT]:
        robot.tourner(5)     # tourner 5° à droite

    view.dessiner()
    view.horloge.tick(30)

pygame.quit()
