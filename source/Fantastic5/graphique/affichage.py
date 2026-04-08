import math
import pygame

class PygameView:
    def __init__(self, plateforme, robot, robot2,  TAILLE_PIXEL: int =40):
        self.plateforme = plateforme
        self.robot = robot
        self.robot2 = robot2
        self.TAILLE_PIXEL = int(TAILLE_PIXEL)

        if not pygame.get_init():
            pygame.init()

        w: int = int(self.plateforme.longueur * self.TAILLE_PIXEL)
        h: int = int(self.plateforme.hauteur * self.TAILLE_PIXEL)
        #crée la fenêtre pygame de taille w*h pixels
        self.fenetre: pygame.Surface = pygame.display.set_mode((w, h))
        #titre en haut de la fenêtre
        pygame.display.set_caption("Simulation robot diff-drive")
        #permet de controler le framerate -> limite la vitesse de simu
        self.horloge: pygame.time.Clock = pygame.time.Clock()

    def to_px(self, x: float, y : float):
        return (int(x * self.TAILLE_PIXEL), int(y * self.TAILLE_PIXEL))
        
    def dessiner(self):
        self.fenetre.fill((255, 255, 255))

        # Grille verticale
        for i in range(int(self.plateforme.longueur) + 1):
            x: int = i * self.TAILLE_PIXEL
            #crée les lignes verticales de la grille
            pygame.draw.line(
                #couleur grise
                self.fenetre,
                (220, 220, 220),
                (x, 0),
                (x, int(self.plateforme.hauteur * self.TAILLE_PIXEL)),
            )
        # Grille horizontale
        for j in range(int(self.plateforme.hauteur) + 1):
            y: int = j * self.TAILLE_PIXEL
            pygame.draw.line(
                self.fenetre,
                (220, 220, 220),
                (0, y),
                (int(self.plateforme.longueur * self.TAILLE_PIXEL), y),
            )
        # Obstacles
        for obs in self.plateforme.obstacles:
            if obs[0] != "rect":
                continue
            _, x, y, hauteur, largeur = obs
            rect: pygame.Rect = pygame.Rect(
                int(x * self.TAILLE_PIXEL),
                int(y * self.TAILLE_PIXEL),
                int(largeur * self.TAILLE_PIXEL),
                int(hauteur * self.TAILLE_PIXEL),
            )
            #dessine le rectangle
            pygame.draw.rect(self.fenetre, (135, 233, 144), rect)
        # Robot 1 
        cx, cy = self.to_px(self.robot.x, self.robot.y)
        surf_w: int = max(1, int(self.robot.long * self.TAILLE_PIXEL))
        surf_h: int = max(1, int(self.robot.larg * self.TAILLE_PIXEL))
        robot_surf : pygame.Surface = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)
        robot_surf.fill((0, 0, 255))
        angle_deg: float = -math.degrees(self.robot.theta)
        rotated: pygame.Surface = pygame.transform.rotate(robot_surf, angle_deg)
        rect_rot: pygame.Rect  = rotated.get_rect(center=(cx, cy))
        self.fenetre.blit(rotated, rect_rot.topleft)
        
        
        
        # Fleche rouge pour indiquer la direction  
        L_fleche: float = max(self.robot.long, 0.2)
        x2: float = self.robot.x + L_fleche * math.cos(self.robot.theta)
        y2: float = self.robot.y + L_fleche * math.sin(self.robot.theta)
        x2p, y2p = self.to_px(x2, y2)
        pygame.draw.line(self.fenetre, (255, 0, 0), (cx, cy), (x2p, y2p), 2)
            
        #Robot 2 
        cx2, cy2 = self.to_px(self.robot2.x, self.robot2.y)
        surf_w2: int = max(1, int(self.robot2.long * self.TAILLE_PIXEL))
        surf_h2: int = max(1, int(self.robot2.larg * self.TAILLE_PIXEL))
        robot2_surf : pygame.Surface = pygame.Surface((surf_w2, surf_h2), pygame.SRCALPHA)
        robot2_surf.fill((0, 0, 255))
        angle_deg: float = -math.degrees(self.robot2.theta)
        rotated: pygame.Surface = pygame.transform.rotate(robot2_surf, angle_deg)
        rect_rot: pygame.Rect  = rotated.get_rect(center=(cx2, cy2))
        self.fenetre.blit(rotated, rect_rot.topleft)

        L_fleche3: float = max(self.robot2.long, 0.2)
        x3: float = self.robot2.x + L_fleche3 * math.cos(self.robot2.theta)
        y3: float = self.robot2.y + L_fleche3 * math.sin(self.robot2.theta)
        x3p, y3p = self.to_px(x3, y3)
        pygame.draw.line(self.fenetre, (255, 0, 0), (cx2, cy2), (x3p, y3p), 2)

        pygame.display.flip()
