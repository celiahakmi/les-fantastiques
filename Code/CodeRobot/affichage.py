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
        w = int(self.plateforme.taille * self.TAILLE_PIXEL)
        h = int(self.plateforme.taille * self.TAILLE_PIXEL)
        self.fenetre = pygame.display.set_mode((int(plateforme.taille * TAILLE_PIXEL), int(plateforme.taille * TAILLE_PIXEL)))
        pygame.display.set_caption("Plateforme Continue")  # Nom de la fenêtre
        self.horloge = pygame.time.Clock()  # Horloge pour contrôler le FPS (régulation du temps d'affichage)

    def to_px(self, x, y):
            return (int(x * self.TAILLE_PIXEL), int(y * self.TAILLE_PIXEL))
        
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
                (220, 220, 220),
                (i * self.TAILLE_PIXEL, 0),
                (i * self.TAILLE_PIXEL, self.plateforme.taille * self.TAILLE_PIXEL)
            )
        for j in range(self.plateforme.taille + 1): # dessin des lignes horizontales

            pygame.draw.line(
                self.fenetre,
                (220, 220, 220),
                (0, j * self.TAILLE_PIXEL),
                (self.plateforme.taille * self.TAILLE_PIXEL, j * self.TAILLE_PIXEL)
            )
       
        for obs in self.plateforme.obstacles:
            t = obs[0]                        
            if t != "rect":                  
                continue
            _, x, y, w, h = obs                
            rect = pygame.Rect(x * self.TAILLE_PIXEL, y * self.TAILLE_PIXEL,w * self.TAILLE_PIXEL,h * self.TAILLE_PIXEL)
            
            pygame.draw.rect(
                self.fenetre,
                (135, 233, 144), # Ta couleur verte
                (x * self.TAILLE_PIXEL, y * self.TAILLE_PIXEL, l * self.TAILLE_PIXEL, h * self.TAILLE_PIXEL)
            )

        # Création d'une surface pour le robot
        center_x = self.robot.x + self.robot.width / 2
        center_y = self.robot.y + self.robot.height / 2
        cx, cy = self.to_px(center_x, center_y)

        surf_w = int(self.robot.width * self.TAILLE_PIXEL)
        surf_h = int(self.robot.height * self.TAILLE_PIXEL)

        robot_surf = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)
        robot_surf.fill((0, 0, 255))  

     # Rotation 
        angle_deg = -math.degrees(self.robot.theta)
        rotated = pygame.transform.rotate(robot_surf, angle_deg)

     # placer le rectangle tourné au centre
        rect_rot = rotated.get_rect(center=(cx, cy))
        self.fenetre.blit(rotated, rect_rot.topleft)
    
    

        pygame.display.flip() #Actualisation de l'affichage



    
