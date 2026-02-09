import pygame
from plateforme import Plateforme
from robot import Robot 
from affichage import PygameView

# Création de la  la plateforme
plateforme = Plateforme(taille=20)

# OBSTACLES PREDEFINIS
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
    largeur=1,
    longueur=1,
    angle=angle,
    plateforme=plateforme
)

# configuration  de Pygame et la View
pygame.init()
view = PygameView(plateforme, robot, TAILLE_PIXEL=40)
# Boucle principale 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    view.dessiner()

pygame.quit()
