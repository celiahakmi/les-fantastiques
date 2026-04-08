import math
import pygame

class PygameView:
    def __init__(self, plateforme, robot, TAILLE_PIXEL: int =40):
        self.plateforme = plateforme
        self.robot = robot
        self.TAILLE_PIXEL = int(TAILLE_PIXEL)
        self.trace_points = []
        self.trace_couleur = (0, 0, 255)


        if not pygame.get_init():
            pygame.init()

        w: int = int(self.plateforme.longueur * self.TAILLE_PIXEL)
        h: int = int(self.plateforme.hauteur * self.TAILLE_PIXEL)
        self.fenetre: pygame.Surface = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Simulation robot diff-drive")
        self.horloge: pygame.time.Clock = pygame.time.Clock()
        self.trace_points: list[tuple[int, int]] = []
        self.trace_couleur: tuple[int, int, int] = (0, 0, 255)
        
    def change_couleur(self, couleur):
            if couleur == "a":
                self.trace_couleur = (255, 0, 0)
            elif couleur == "b":
                self.trace_couleur = (0, 255, 0)
            elif couleur == "c":
                self.trace_couleur = (0, 0, 255)
            elif couleur == "d":
                self.trace_couleur = (255, 255, 0)
            elif couleur == "e":
                self.trace_couleur = (0, 0, 0)


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
                 
        # Robot
        cx, cy = self.to_px(self.robot.x, self.robot.y)
        if self.robot.trace_active:
            self.trace_points.append((cx, cy))

        if len(self.trace_points) >= 2:
            pygame.draw.lines(self.fenetre, self.trace_couleur, False, self.trace_points, 2)

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
        
        cx, cy = self.to_px(self.robot.x, self.robot.y)

        pygame.display.flip()
