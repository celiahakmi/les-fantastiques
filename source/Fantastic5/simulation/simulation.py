import math

class Plateforme:
    def __init__(self, longueur: float, hauteur: float):
        """longueur et hauteur : dimensions de la plateforme
           obstacles : liste des rectangles déjà placés sur la plateforme.  sous forme de tuple : ("rect", x, y, hauteur, largeur)  """
        self.longueur: float = longueur  # affilié à x
        self.hauteur: float= hauteur     # affilié à y
        self.obstacles: list = [] #liste des obstacles présents 
        self.ballons: list = [] #liste des ballons présents 

    def init_obstacle(self, x: float, y:float, h: float, l: float):
        """Construire un rectangle où le sommet bas-gauche est de coordonnées x,y, de hauteur h et de largeur l"""
        if self.est_valide(x, y, l, h):
            self.obstacles.append(("rect", x, y, h, l))
            return True 
        return False  
    
    def init_ballon(self, x: float, y: float, rayon: float):
        self.ballons.append(Ballon(x, y, rayon))

    def est_valide(self, x: float, y: float, l: float, h: float):
        """Renvoie True si l'obstacle est valide """
        #Vérifie que l’obstacle ne sort pas de la plateforme
        if x < 0 or y < 0 or (x+l) > self.longueur or (y+h) > self.hauteur:
            return False
        #Vérifie qu’il ne chevauche pas un autre obstacle
        for obs in self.obstacles:
            _, ox, oy, oh, ol = obs 
            if (x < ox + ol and x + l > ox and
                y < oy + oh and y + h > oy):
                return False     
        return True

    def collision_robot(self, robot):
        """Renvoie True si le robot entre en collision avec un obstacle ou un mur"""
        long: float = robot.long / 2
        larg: float = robot.larg / 2

        # 4 coins: avant-droit, avant-gauche, arrière-gauche, arrière-droit
        coins_relatifs = [(long, larg), (long, -larg), (-long, -larg), (-long, larg)]

        coins_reels = []
        for dx, dy in coins_relatifs:
            # Rotation des points par rapport à l'angle theta
            cx: float = robot.x + (dx * math.cos(robot.theta) - dy * math.sin(robot.theta))
            cy: float = robot.y + (dx * math.sin(robot.theta) + dy * math.cos(robot.theta))
            coins_reels.append((cx, cy))

        # Vérifier si un des coins sort de la plateforme ou touche un obstacle
        for cx, cy in coins_reels:
            # sort de la plateforme 
            if cx < 0 or cx > self.longueur or cy < 0 or cy > self.hauteur:
                return True
            
            # collision avec obstacles 
            for obs in self.obstacles:
                _, ox, oy, oh, ol = obs
                # Si le point (cx, cy) est à l'intérieur du rectangle de l'obstacle
                if ox <= cx <= ox + ol and oy <= cy <= oy + oh:
                    return True
        return False
    def collision_ballon(self, ballon):
        bx : float = ballon.x + ballon.rayon
        by : float = ballon.y + ballon.rayon
        if  bx < 0 or bx > self.longueur or by < 0 or by > self.hauteur:
            return True 
    return False 

class Robot: 
    def __init__(self, x : float, y : float, theta : float, L : float, larg : float, long : float, plateforme):
        """ initialise le robot avec 
            - position 
            - orientation 
            - distance entre 2 roues (L)
            - forme robot (largeur/ longueur)"""
        # attribut fixe du robot
        self.x : float = x
        self.y : float = y
        self.theta: float = math.radians(theta)
        self.L : float = L 
        self.larg : float = larg
        self.long : float = long 
        self.plateforme = plateforme
        
        # attribut variable du robot 
        self.vL: float = 0.0
        self.vR: float = 0.0
        self.pas: float = 0.1 

    def update(self):
        """Calcule le prochain mouvement sans l'appliquer
        met à jour la position du robot après un petit pas de temps (pas), en utilisant les vitesses des roues"""
        # Sauvegarde de la position actuelle au cas ou on va annuler
        ancien_x: float = self.x
        ancien_y: float = self.y
        ancien_theta: float = self.theta

        # Calcul des vitesses 
        vitesse_lineaire: float = (self.vL + self.vR) / 2.0
        vitesse_angulaire: float = (self.vR - self.vL) / self.L

        # Calcul de la position 
        self.x += vitesse_lineaire  * math.cos(self.theta) * self.pas
        self.y += vitesse_lineaire  * math.sin(self.theta) * self.pas
        self.theta += vitesse_angulaire * self.pas

        # Vérification de la collision 
        if self.plateforme.collision_robot(self):
            # Collision détectée 
            print("Oups, le robot s'est cogné")
            #on retourne à l'ancienne position
            self.x, self.y, self.theta = ancien_x, ancien_y, ancien_theta
            #vitesses à 0
            self.vL = 0.0
            self.vR = 0.0
            return False 
            
        return True 

    def get_distance(self, distance_max=100.0, step=0.1):
        """Retourne la distance jusqu'au premier obstacle rencontré"""
        distance = 0.0 # point de départ
        
        while distance < distance_max: 
            # calculs de la position du point testé
            test_x: float = self.x + distance * math.cos(self.theta)
            test_y: float = self.y + distance * math.sin(self.theta)

            # vérifie la collision avec le mur 
            if (test_x < 0 or test_x > self.plateforme.longueur or test_y < 0 or test_y > self.plateforme.hauteur):
                return distance
            
            for ballon in self.plateforme.ballons:
                dx = test_x - ballon.x
                dy = test_y - ballon.y
                if math.sqrt(dx**2 + dy**2) <= ballon.rayon:
                    return distance
            
            # vérifie la collision avec les obstacles
            for obstacle in self.plateforme.obstacles:
                _, obstacle_x, obstacle_y, obstacle_h, obstacle_l = obstacle
                if obstacle_x <= test_x <= obstacle_x + obstacle_l and obstacle_y <= test_y <= obstacle_y + obstacle_h:
                    return distance
            distance += step
                
        return distance_max # si aucun (obstacle - mur) n'a été trouvé

    def get_position(self):
        return self.x, self.y, self.theta 
       
    def get_vitesse(self):
        return self.vL, self.vR

class Ballon:
    def __init__(self, x: float, y: float, theta : float, vitesse : float, rayon: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.vitesse = vitesse
        self.rayon = rayon
        self.pas: float = 0.1 
        
    def update():
        ancien_x: float = self.x
        ancien_y: float = self.y
        ancien_theta: float = self.theta

        # Calcul des vitesses 
        vitesse_lineaire: float = self.vitesse 
        vitesse_angulaire: float = self.vitesse 

        # Calcul de la position 
        self.x += vitesse_lineaire  * math.cos(self.theta) * self.pas
        self.y += vitesse_lineaire  * math.sin(self.theta) * self.pas
        self.theta += vitesse_angulaire * self.pas

        # Vérification de la collision 
        if self.plateforme.collision_robot(self):
            # Collision détectée 
            print("Oups, le robot s'est cogné")
            #on retourne à l'ancienne position
            self.x, self.y, self.theta = ancien_x, ancien_y, ancien_theta
            #vitesses à 0
            self.vL = 0.0
            self.vR = 0.0
            return False 
            
        return True 