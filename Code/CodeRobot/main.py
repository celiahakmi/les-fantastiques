import pygame
from plateforme import Plateforme
from affichage import PygameView

# Création de la  la plateforme
plateforme = Plateforme(taille=20)

# configuration  de Pygame et la View
pygame.init()
view = PygameView(plateforme, TAILLE_PIXEL=40)