import pygame

class PygameView:
    """Classe permettant d'afficher toute nos fonctions controllant le robot 
        Partie View de la méthode MVC""" 
    def __init__(self, plateforme, robot, TAILLE_PIXEL=30):
        """ Initialise l'interface graphique Pygame pour afficher la plateforme.
        Paramètres : 
            - Plateforme (Objet : notre plan continu)
            - TAILLE_PIXEL (int : La taille d'une unité de la plateforme en pixels
        """
        self.plateforme = plateforme   # plateforme = notre plan continu avec la grille
        self.robot = robot 
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
        self.fenetre.fill((255, 255, 255)) # Fond blanc
        
        for i in range(self.plateforme.taille + 1): # dessin des lignes verticales
            pygame.draw.line(
                self.fenetre,
                (0, 0, 0),
                (i * self.TAILLE_PIXEL, 0),
                (i * self.TAILLE_PIXEL, self.plateforme.taille * self.TAILLE_PIXEL)
            )
        for j in range(self.plateforme.taille + 1): # dessin des lignes horizontales

            pygame.draw.line(
                self.fenetre,
                (0, 0, 0),
                (0, j * self.TAILLE_PIXEL),
                (self.plateforme.taille * self.TAILLE_PIXEL, j * self.TAILLE_PIXEL)
            )
       
        for obs in self.plateforme.obstacles:
            #cercle (surface, couleur, centre, rayon)
            if obs[0] == "cercle":
                _, x, y, r = obs
                pygame.draw.circle(self.fenetre, (212, 115, 212),(int(x*self.TAILLE_PIXEL), int(y*self.TAILLE_PIXEL)),int(r*self.TAILLE_PIXEL))

            #carre (surface, couleur, C)
            elif obs[0] == "carre":
                _, x, y, c = obs
                # C = (x, y, largeur, hauteur) multiplié par la taille des pixels
                pygame.draw.rect(self.fenetre, (135, 233, 144),(x*self.TAILLE_PIXEL, y*self.TAILLE_PIXEL,c*self.TAILLE_PIXEL,c*self.TAILLE_PIXEL))

            #triangle(surface, couleur, points)
            elif obs[0] == "triangle":
                _, x, y, c = obs
                # Calcul des 3 sommets du triangle en fonction de la taille 'c'
                points = [(x*self.TAILLE_PIXEL, y*self.TAILLE_PIXEL),((x+c)*self.TAILLE_PIXEL, y*self.TAILLE_PIXEL),((x+c/2)*self.TAILLE_PIXEL, (y-c)*self.TAILLE_PIXEL)]
                pygame.draw.polygon(self.fenetre,(253, 108, 158), points)

        rect = pygame.Rect(
            self.robot.x * self.TAILLE_PIXEL,      # x en pixels
            self.robot.y * self.TAILLE_PIXEL,      # y en pixels
            self.robot.largeur * self.TAILLE_PIXEL,  # largeur en pixels
            self.robot.longueur * self.TAILLE_PIXEL  # longueur en pixels
        )
        pygame.draw.rect(self.fenetre, (0, 0, 255), rect)  # rectangle bleu (0, 0, 255 = formabt RGB : bleu)
        pygame.display.flip() #Actualisation de l'affichage

        self.horloge.tick(30) #Limitation du FPS (régulation du temps d'affichage, fps = frame par seconde)


    


