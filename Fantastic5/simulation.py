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
                     

    def update(self):
        """Calcule le prochain mouvement sans l'appliquer"""
        #Sauvegarde de la position actuelle au cas où on doive annuler
        ancien_x, ancien_y, ancien_theta = self.x, self.y, self.theta

        # Calcul des vitesses 
        vitesse_lineaire = (self.vL + self.vR) / 2.0
        vitesse_angulaire = (self.vR - self.vL) / self.L

        # Calcul de la position 
        self.x += vitesse_lineaire  * math.cos(self.theta) * self.pas
        self.y += vitesse_lineaire  * math.sin(self.theta) * self.pas
        self.theta += vitesse_angulaire * self.pas

        # Vérification de la collision via la plateforme
        if self.plateforme.collision_robot(self):
            # Collision détectée 
            print("Oups, le robot s'est congné")
            self.vL = 0.0
            self.vR = 0.0
            return False 
            
        return True 
   

             
