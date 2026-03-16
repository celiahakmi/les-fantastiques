import math

class Plateforme:
    def __init__(self, longueur: float, hauteur: float):
        self.longueur = longueur #affilié à x
        self.hauteur = hauteur #affilié à y
        self.obstacles = []

    
    def init_obstacle(self, x: float, y:float, h: float, l: float):
        """Construire un rectancle où le sommet bas-gauche est de coordonées x,y, de hauteur h et de largeur l"""
        if self.est_valide(x, y, l, h):
            self.obstacles.append(("rect", float(x), float(y), float(h), float(l)))
            return True 
        return False  

    
    def est_valide(self, x: float, y: float, l: float, h: float):
        """Renvoie True si l'obstacle est valide """
        if x < 0 or y < 0 or (x+l) > self.longueur or (y+h) > self.hauteur:
            return False
        
        for obs in self.obstacles:
            _, ox, oy, oh, ol = obs 
            if (x < ox + ol and x + l > ox and
                y < oy + oh and y + h > oy):
                return False     
        return True

    
    def collision_robot(self, robot):
        """Renvoie True si le robot entre en collision avec un obstacle ou un mur"""

        long = robot.long / 2
        larg = robot.larg / 2

        #4 coins: avant-droit, avant-gauche, arrière-gauche, arrière-droit
        coins_relatifs = [(long, larg), (long, -larg), (-long, -larg), (-long, larg)]

        coins_reels = []
        for dx, dy in coins_relatifs:
            #Rotation des points par rapport à l'angle theta
            cx = robot.x + (dx * math.cos(robot.theta) - dy * math.sin(robot.theta))
            cy = robot.y + (dx * math.sin(robot.theta) + dy * math.cos(robot.theta))
            coins_reels.append((cx, cy))

        #Vérifier si un des coins sort de la plateforme ou touche un obstacle
        for cx, cy in coins_reels:
            #sort de la plateforme 
            if cx < 0 or cx > self.longueur or cy < 0 or cy > self.hauteur:
                return True
            
            #collision avec obstacles 
            for obs in self.obstacles:
                _, ox, oy, oh, ol = obs
                #Si le point (cx, cy) est à l'intérieur du rectangle de l'obstacle
                if ox <= cx <= ox + ol and oy <= cy <= oy + oh:
                    return True
        return False

    #si il y a une collision on remet le robot a son ancienne position on reinitialise les vitesse et on retourne false
    def deplacer_si_possible(self, robot, action):
        x, y, t = robot.x, robot.y, robot.theta
        action()
        if self.collision_robot(robot):
            robot.x, robot.y, robot.theta = x, y, t
            robot.vL = 0.0
            robot.vR = 0.0
            return False
        return True


class Robot: 
    def __init__(self, x : float, y : float, theta : float, L : float, larg : float, long : float,plateforme):
        """ initialise le robot avec 
            - position 
            - orientation 
            - distance entre 2 roues (L)
            - forme robot (largeur/ longueur)"""
        #attribut fixe du robot
        self.x = float(x)
        self.y = float(y)
        self.theta = math.radians(theta)
        self.L = float(L)
        self.larg = float(larg)
        self.long = float(long)
        self.plateforme=plateforme
        #attribut variable du robot 
        self.vL: float = 0.0
        self.vR: float = 0.0
        self.pas: float = 0.1 
                     
    
    def deplacer(self):
        #Sauvegarde de l'ancienne position
        ancien_x = self.x
        ancien_y = self.y
        ancien_theta = self.theta

        #Calcul des vitesses globale et angulaire
        v = (self.vL + self.vR) / 2.0
        w = (self.vR - self.vL) / self.L

        #Mise à jour de la position et de l'orientation
        self.x = self.x + v * math.cos(self.theta) * self.pas
        self.y = self.y + v * math.sin(self.theta) * self.pas
        self.theta = self.theta + w * self.pas
       
    def carre(self):
        nbcote = 0
        long_cote = 2
        etat = "avance"
        x0 = self.x
        y0 = self.y
        theta0 = self.theta
        angle_acc = 0.0
        max_iter = 10000
        n_iter = 0

        while nbcote < 4 and n_iter < max_iter:
            n_iter += 1
            if etat == "avance":
                self.vL = 1.0
                self.vR = 1.0
                # distance parcourue sur le côté
                d = math.sqrt((self.x - x0)**2 + (self.y - y0)**2)
                if d < long_cote:
                    self.deplacer()
                else:
                    etat = "tourner"
                    angle_acc = 0.0
                    theta0 = self.theta

            elif etat == "tourner":
                self.vL = -1.0
                self.vR = 1.0
                omega = (self.vR - self.vL) / self.L
                angle_acc += abs(omega * self.pas)
                if angle_acc < math.pi / 2:
                    self.deplacer()
                else:
                    nbcote += 1
                    etat = "avance"
                    x0 = self.x
                    y0 = self.y
        self.vL = 0.0
        self.vR = 0.0


             
