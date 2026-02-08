import pygame
from plateforme import Plateforme
from affichage import PygameView

# Création de la  la plateforme
plateforme = Plateforme(taille=20)

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