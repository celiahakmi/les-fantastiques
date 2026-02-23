import math
import pygame


class PygameView:
    def __init__(self, plateforme, robot, TAILLE_PIXEL=40):
        self.plateforme = plateforme
        self.robot = robot
        self.TAILLE_PIXEL = int(TAILLE_PIXEL)

        if not pygame.get_init():
            pygame.init()

        w = int(self.plateforme.longueur * self.TAILLE_PIXEL)
        h = int(self.plateforme.hauteur * self.TAILLE_PIXEL)
        self.fenetre = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Simulation robot diff-drive")
        self.horloge = pygame.time.Clock()

        def to_px(self, x, y):
            return (int(x * self.TAILLE_PIXEL), int(y * self.TAILLE_PIXEL))
        
        def dessiner(self):
        self.fenetre.fill((255, 255, 255))

        # Grille verticale
        for i in range(int(self.plateforme.longueur) + 1):
            x = i * self.TAILLE_PIXEL
            pygame.draw.line(
                self.fenetre,
                (220, 220, 220),
                (x, 0),
                (x, int(self.plateforme.hauteur * self.TAILLE_PIXEL)),
            )
       
   
