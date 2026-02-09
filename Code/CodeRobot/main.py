import pygame
from plateforme import Plateforme
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

# configuration  de Pygame et la View
pygame.init()
view = PygameView(plateforme, TAILLE_PIXEL=40)
# Boucle principale 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    view.dessiner()

pygame.quit()
