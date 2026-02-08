import pygame

class PygameView:
    """Classe permettant d'afficher toute nos fonctions controllant le robot 
        Partie View de la méthode MVC""" 
    def __init__(self, plateforme, TAILLE_PIXEL=30):
        """ Initialise l'interface graphique Pygame pour afficher la plateforme.
        Paramètres : 
            - Plateforme (Objet : notre plan continu)
            - TAILLE_PIXEL (int : La taille d'une unité de la plateforme en pixels
        """
        self.plateforme = plateforme   # plateforme = notre plan continu avec la grille
        self.TAILLE_PIXEL = TAILLE_PIXEL  # Taille d'une case en pixels

        # Création de la fenêtre Pygame
        self.fenetre = pygame.display.set_mode((int(plateforme.taille * TAILLE_PIXEL), int(plateforme.taille * TAILLE_PIXEL)))
        pygame.display.set_caption("Plateforme Continue")  # Nom de la fenêtre

        self.horloge = pygame.time.Clock()  # Horloge pour contrôler le FPS (régulation du temps d'affichage)

    def dessiner(self):
        """fonction permettant de dessiner la plateforme dans la fenêtre Pygame en plusieurs étapes : 
            - Remplit le fond en blanc
            - Trace la grille 
            - Actualise l'affichage
            - Limite la vitesse de la boucle pour que l'affichage soit fluide
        """ 
        self.fenetre.fill((255, 255, 255)) 


    


