import math
import pygame

class PygameView:
    def __init__(self, plateforme, robot, robot2, ballon, TAILLE_PIXEL: int =40):
        self.plateforme = plateforme
        self.robot = robot
        self.robot2 = robot2
        self.ballon = ballon
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
            if obs[0] == "rect":
                _, x, y, hauteur, largeur = obs
                rect: pygame.Rect = pygame.Rect(
                    int(x * self.TAILLE_PIXEL),
                    int(y * self.TAILLE_PIXEL),
                    int(largeur * self.TAILLE_PIXEL),
                    int(hauteur * self.TAILLE_PIXEL),
                )
                pygame.draw.rect(self.fenetre, (150, 0, 255), rect)

            elif obs[0] == "cercle":
                # Structure attendue : ("cercle", x_centre, y_centre, rayon)
                _, cx, cy, rayon = obs
                pos_px = self.to_px(cx, cy)
                rayon_px = int(rayon * self.TAILLE_PIXEL)
                pygame.draw.circle(self.fenetre, (255, 100, 100), pos_px, rayon_px)
            
            elif obs[0] == "triangle":
                # Structure attendue : ("triangle", [(x1, y1), (x2, y2), (x3, y3)])
                _, points = obs
                # Conversion de tous les points en pixels
                points_px = [self.to_px(p[0], p[1]) for p in points]
                pygame.draw.polygon(self.fenetre, (100, 100, 255), points_px)


        # Robot1
        cx, cy = self.to_px(self.robot.x, self.robot.y)
        surf_w: int = max(1, int(self.robot.long * self.TAILLE_PIXEL))
        surf_h: int = max(1, int(self.robot.larg * self.TAILLE_PIXEL))
        robot_surf : pygame.Surface = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)
        robot_surf.fill((0, 0, 0))
        angle_deg: float = -math.degrees(self.robot.theta)
        rotated: pygame.Surface = pygame.transform.rotate(robot_surf, angle_deg)
        rect_rot: pygame.Rect  = rotated.get_rect(center=(cx, cy))
        self.fenetre.blit(rotated, rect_rot.topleft)
        pygame.draw.line(self.fenetre, (0, 0, 255), (cx, cy), (cx, cy), 5)
        
        # Robot2
        cx2, cy2 = self.to_px(self.robot2.x2, self.robot2.y2)
        surf_w: int = max(1, int(self.robot2.long2 * self.TAILLE_PIXEL))
        surf_h: int = max(1, int(self.robot2.larg2 * self.TAILLE_PIXEL))
        robot_surf : pygame.Surface = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)
        robot_surf.fill((0, 0, 0))
        angle_deg: float = -math.degrees(self.robot2.theta)
        rotated: pygame.Surface = pygame.transform.rotate(robot_surf, angle_deg)
        rect_rot: pygame.Rect  = rotated.get_rect(center=(cx2, cy2))
        self.fenetre.blit(rotated, rect_rot.topleft)

        # Fleche rouge pour indiquer la direction  
        L_fleche: float = max(self.robot.long, 0.2)
        x2: float = self.robot.x + L_fleche * math.cos(self.robot.theta)
        y2: float = self.robot.y + L_fleche * math.sin(self.robot.theta)
        x2p, y2p = self.to_px(x2, y2)
        pygame.draw.line(self.fenetre, (100, 100, 100), (x2p, y2p), (cx, cy), 2)
        
        L_fleche: float = max(self.robot2.long2, 0.2)
        x2: float = self.robot2.x2 + L_fleche * math.cos(self.robot2.theta)
        y2: float = self.robot2.y2 + L_fleche * math.sin(self.robot2.theta)
        x2p, y2p = self.to_px(x2, y2)
        pygame.draw.line(self.fenetre, (100, 100, 100), (cx2, cy2), (x2p, y2p), 2)

        pygame.display.flip()
