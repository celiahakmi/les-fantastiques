import pygame
import math

class PygameView:

    def __init__(self, plateforme, robot, TAILLE_PIXEL=40):
        self.plateforme = plateforme      
        self.robot = robot                
        self.TAILLE_PIXEL = int(TAILLE_PIXEL)  

        w = int(self.plateforme.taille * self.TAILLE_PIXEL)   
        h = int(self.plateforme.taille * self.TAILLE_PIXEL) 
        self.fenetre = pygame.display.set_mode((w, h))       
        pygame.display.set_caption("Simulation robot diff-drive")  
        self.horloge = pygame.time.Clock()                   

    def to_px(self, x, y):
        return (int(x * self.TAILLE_PIXEL), int(y * self.TAILLE_PIXEL)) 

    def dessiner(self):
        self.fenetre.fill((255, 255, 255))  

        # Grille
        for i in range(int(self.plateforme.taille) + 1):
            pygame.draw.line(
                self.fenetre, (220, 220, 220),
                (i * self.TAILLE_PIXEL, 0),
                (i * self.TAILLE_PIXEL, self.plateforme.taille * self.TAILLE_PIXEL)
            )

        for j in range(int(self.plateforme.taille) + 1):
            pygame.draw.line(
                self.fenetre, (220, 220, 220),
                (0, j * self.TAILLE_PIXEL),
                (self.plateforme.taille * self.TAILLE_PIXEL, j * self.TAILLE_PIXEL)
            )

        # Obstacles
        for obs in self.plateforme.obstacles:
            t = obs[0]
            if t != "rect":
                continue

            _, x, y, w, h = obs
            rect = pygame.Rect(
                x * self.TAILLE_PIXEL,
                y * self.TAILLE_PIXEL,
                w * self.TAILLE_PIXEL,
                h * self.TAILLE_PIXEL
            )
            pygame.draw.rect(self.fenetre, (135, 233, 144), rect)

        # Robot rectangle
        center_x = self.robot.x + self.robot.width / 2   # centre x
        center_y = self.robot.y + self.robot.height / 2  # centre y
        cx, cy = self.to_px(center_x, center_y)

        surf_w = int(self.robot.width * self.TAILLE_PIXEL)   # largeur px
        surf_h = int(self.robot.height * self.TAILLE_PIXEL)  # hauteur px

        robot_surf = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)  # surface
        robot_surf.fill((0, 0, 255))  # bleu

        angle_deg = -math.degrees(self.robot.theta)  # radians → degrés
        rotated = pygame.transform.rotate(robot_surf, angle_deg)  # rotation

        rect_rot = rotated.get_rect(center=(cx, cy))  # recentrage
        self.fenetre.blit(rotated, rect_rot.topleft)  # affichage

        # Flèche direction
        L = 1.2
        x2 = center_x + L * math.cos(self.robot.theta)
        y2 = center_y + L * math.sin(self.robot.theta)
        x2p, y2p = self.to_px(x2, y2)
        pygame.draw.line(self.fenetre, (255, 0, 0), (cx, cy), (x2p, y2p), 3)

        # Capteur distance
        if self.robot.range is not None:
            xr = center_x + self.robot.range * math.cos(self.robot.theta)
            yr = center_y + self.robot.range * math.sin(self.robot.theta)
            xrp, yrp = self.to_px(xr, yr)
            pygame.draw.line(self.fenetre, (0, 0, 0), (cx, cy), (xrp, yrp), 2)
            pygame.draw.circle(self.fenetre, (0, 0, 0), (xrp, yrp), 4)

        pygame.display.flip()  
