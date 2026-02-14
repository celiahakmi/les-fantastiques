import pygame
import math

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
            # On dépaquette 5 valeurs : type, x, y, largeur, hauteur
            # On utilise _ pour le type car on sait que c'est un rectangle
            _, x, y, l, h = obs 
            
            pygame.draw.rect(
                self.fenetre,
                (135, 233, 144), # Ta couleur verte
                (x * self.TAILLE_PIXEL, y * self.TAILLE_PIXEL, l * self.TAILLE_PIXEL, h * self.TAILLE_PIXEL)
            )

        # Création d'une surface pour le robot
        surface = pygame.Surface((self.robot.largeur * self.TAILLE_PIXEL, self.robot.longueur * self.TAILLE_PIXEL), pygame.SRCALPHA) # Ajout de SRCALPHA pour la transparence
        surface.fill((0, 0, 255))  # rectangle bleu (0, 0, 255 = formabt RGB : bleu)

        # Rotation selon l'angle du robot
        rotated_surface = pygame.transform.rotate(surface, -self.robot.angle)

        # Calcul du rectangle après rotation
        rect = rotated_surface.get_rect(center=(self.robot.x * self.TAILLE_PIXEL,
                                       self.robot.y * self.TAILLE_PIXEL))

        # Affichage du robot tourné
        self.fenetre.blit(rotated_surface, rect.topleft)
        

        #création et affichage du vecteur de déplacement

        #position de départ
        x1= self.robot.x * self.TAILLE_PIXEL
        y1= self.robot.y * self.TAILLE_PIXEL

        longueur=40 #longueur qui sera affichée à l'écran
        angle_radian= math.radians(self.robot.angle) #on convertit l'angle en radians

        #point d'arrivée 
        x2= x1+longueur*math.cos(angle_radian)
        y2= y1 +longueur*math.sin(angle_radian)

        #on dessine le vecteur après l'avoir crée 
        pygame.draw.line(
            self.fenetre,
            (255,0,0), #couleur=rouge=
            (x1,y1),
            (x2,y2),
            3 #épaisseur de la ligne
        )

        pygame.display.flip() #Actualisation de l'affichage

        self.horloge.tick(30) #Limitation du FPS (régulation du temps d'affichage, fps = frame par seconde)


    
