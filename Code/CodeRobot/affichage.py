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
        # Grille horizontale
        for j in range(int(self.plateforme.hauteur) + 1):
            y = j * self.TAILLE_PIXEL
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
            rect = pygame.Rect(
                int(x * self.TAILLE_PIXEL),
                int(y * self.TAILLE_PIXEL),
                int(largeur * self.TAILLE_PIXEL),
                int(hauteur * self.TAILLE_PIXEL),
            )
            pygame.draw.rect(self.fenetre, (135, 233, 144), rect)
            
        # Robot
        cx, cy = self.to_px(self.robot.x, self.robot.y)
        surf_w = max(1, int(self.robot.long * self.TAILLE_PIXEL))
        surf_h = max(1, int(self.robot.larg * self.TAILLE_PIXEL))
        robot_surf = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)
        robot_surf.fill((0, 0, 255))
        angle_deg = -math.degrees(self.robot.theta)
        rotated = pygame.transform.rotate(robot_surf, angle_deg)
        rect_rot = rotated.get_rect(center=(cx, cy))
        self.fenetre.blit(rotated, rect_rot.topleft)
        
        # Fleche rouge pour indiquer la direction  
        L_fleche = max(self.robot.long, 0.2)
        x2 = self.robot.x + L_fleche * math.cos(self.robot.theta)
        y2 = self.robot.y + L_fleche * math.sin(self.robot.theta)
        x2p, y2p = self.to_px(x2, y2)
        pygame.draw.line(self.fenetre, (255, 0, 0), (cx, cy), (x2p, y2p), 2)
            
            
        pygame.display.flip()

           
       
