import math
import pygame

class PygameView:
    def __init__(self, plateforme, robot, TAILLE_PIXEL: int =40):
        self.plateforme = plateforme
        self.robot = robot
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
    
    def coins_robot(self):
        demi_long = self.robot.long / 2
        demi_larg = self.robot.larg / 2
        coins_relatifs = [
            (demi_long, demi_larg),
            (demi_long, -demi_larg),
            (-demi_long, -demi_larg),
            (-demi_long, demi_larg),]

        coins = []
        for dx, dy in coins_relatifs:
            x = self.robot.x + (dx * math.cos(self.robot.theta) - dy * math.sin(self.robot.theta))
            y = self.robot.y + (dx * math.sin(self.robot.theta) + dy * math.cos(self.robot.theta))
            coins.append(self.to_px(x, y))
        return coins
        
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
            pygame.draw.rect(self.fenetre, (0, 0, 0), rect)
            
        # Robot
        cx, cy = self.to_px(self.robot.x, self.robot.y)
        coins = self.coins_robot()
        pygame.draw.polygon(self.fenetre, (255, 182, 193), coins)
        pygame.draw.polygon(self.fenetre, (200, 105, 140), coins, 2)
        
        # Fleche rouge pour indiquer la direction  
        L_fleche: float = max(self.robot.long, 0.2)
        x2: float = self.robot.x + L_fleche * math.cos(self.robot.theta)
        y2: float = self.robot.y + L_fleche * math.sin(self.robot.theta)
        x2p, y2p = self.to_px(x2, y2)
        pygame.draw.line(self.fenetre, (255, 0, 0), (cx, cy), (x2p, y2p), 2)
            
        pygame.display.flip()
