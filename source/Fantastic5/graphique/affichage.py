import math
import pygame

class PygameView:
    def __init__(self, plateforme, robot1,robot2, TAILLE_PIXEL: int =40):
        self.plateforme = plateforme
        self.robot1 = robot1
        self.robot2 = robot2
        self.TAILLE_PIXEL = int(TAILLE_PIXEL)

        if not pygame.get_init():
            pygame.init()

        w: int = int(self.plateforme.longueur * self.TAILLE_PIXEL)
        h: int = int(self.plateforme.hauteur * self.TAILLE_PIXEL)
        self.fenetre: pygame.Surface = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Simulation robot diff-drive")
        self.horloge: pygame.time.Clock = pygame.time.Clock()

    def to_px(self, x: float, y : float):
        return (int(x * self.TAILLE_PIXEL), int(y * self.TAILLE_PIXEL))
        
    def dessiner(self):
        self.fenetre.fill((255, 255, 255))

        # Grille verticale
        for i in range(int(self.plateforme.longueur) + 1):
            x: int = i * self.TAILLE_PIXEL
            pygame.draw.line(
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
            pygame.draw.rect(self.fenetre, (135, 233, 144), rect)
            
        # Robot1
        cx, cy = self.to_px(self.robot1.x, self.robot1.y)
        surf_w: int = max(1, int(self.robot1.long * self.TAILLE_PIXEL))
        surf_h: int = max(1, int(self.robot1.larg * self.TAILLE_PIXEL))
        robot_surf : pygame.Surface = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)
        robot_surf.fill((0, 0, 255))
        angle_deg: float = -math.degrees(self.robot1.theta)
        rotated: pygame.Surface = pygame.transform.rotate(robot_surf, angle_deg)
        rect_rot: pygame.Rect  = rotated.get_rect(center=(cx, cy))
        self.fenetre.blit(rotated, rect_rot.topleft)
        

        #Robot 2
        cx2, cy2 = self.to_px(self.robot2.x, self.robot2.y)
        surf_w2: int = max(1, int(self.robot2.long * self.TAILLE_PIXEL))
        surf_h2: int = max(1, int(self.robot2.larg * self.TAILLE_PIXEL))
        robot_surf2: pygame.Surface = pygame.Surface((surf_w2, surf_h2), pygame.SRCALPHA)
        robot_surf2.fill((0, 0, 255))
        angle_deg2: float = -math.degrees(self.robot2.theta)
        rotated2: pygame.Surface = pygame.transform.rotate(robot_surf2, angle_deg2)
        rect_rot2: pygame.Rect  = rotated2.get_rect(center=(cx2, cy2))
        self.fenetre.blit(rotated2, rect_rot2.topleft)
        
        # Fleche rouge pour indiquer la direction  
        L_fleche: float = max(self.robot1.long, 0.2)
        xr2: float = self.robot1.x + L_fleche * math.cos(self.robot1.theta)
        yr2: float = self.robot1.y + L_fleche * math.sin(self.robot1.theta)
        x2rp, y2rp = self.to_px(xr2, yr2)
        pygame.draw.line(self.fenetre, (255, 0, 0), (cx, cy), (x2rp, y2rp), 2)

        # Fleche rouge pour indiquer la direction  
        L_fleche2: float = max(self.robot2.long, 0.2)
        xrr2: float = self.robot2.x + L_fleche2 * math.cos(self.robot2.theta)
        yrr2: float = self.robot2.y + L_fleche2* math.sin(self.robot2.theta)
        x2rrp, y2rrp = self.to_px(xrr2, yrr2)
        pygame.draw.line(self.fenetre, (255, 0, 255), (cx2, cy2), (x2rrp, y2rrp), 2)
            
        pygame.display.flip()
