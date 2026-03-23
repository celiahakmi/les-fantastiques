import math

class Plateforme:
    def __init__(self, longueur: float, hauteur: float):
        self.longueur: float = longueur 
        self.hauteur: float= hauteur 
        self.obstacles: list = []

    def init_obstacle(self, x: float, y:float, h: float, l: float):
        if self.est_valide(x, y, l, h):
            self.obstacles.append(("rect", x, y, h, l))
            return True 
        return False  

    def est_valide(self, x: float, y: float, l: float, h: float):
        if x < 0 or y < 0 or (x+l) > self.longueur or (y+h) > self.hauteur:
            return False
        
        for obs in self.obstacles:
            _, ox, oy, oh, ol = obs 
            if (x < ox + ol and x + l > ox and
                y < oy + oh and y + h > oy):
                return False     
        return True

    def collision_robot(self, robot):
        long: float = robot.long / 2
        larg: float = robot.larg / 2

        coins_relatifs = [(long, larg), (long, -larg), (-long, -larg), (-long, larg)]

        coins_reels = []
        for dx, dy in coins_relatifs:
            cx: float = robot.x + (dx * math.cos(robot.theta) - dy * math.sin(robot.theta))
            cy: float = robot.y + (dx * math.sin(robot.theta) + dy * math.cos(robot.theta))
            coins_reels.append((cx, cy))

        for cx, cy in coins_reels:
            if cx < 0 or cx > self.longueur or cy < 0 or cy > self.hauteur:
                return True
            
            for obs in self.obstacles:
                _, ox, oy, oh, ol = obs
                if ox <= cx <= ox + ol and oy <= cy <= oy + oh:
                    return True
        return False


class Robot: 
    def __init__(self, x : float, y : float, theta : float, L : float, larg : float, long : float,plateforme):
        self.x : float = x
        self.y : float = y
        self.theta: float = math.radians(theta)
        self.L : float = L 
        self.larg : float = larg
        self.long : float = long 
        self.plateforme: Plateforme =plateforme
        
        self.vL: float = 0.0
        self.vR: float = 0.0
        self.pas: float = 0.1 

    def update(self):
        ancien_x: float = self.x
        ancien_y: float = self.y
        ancien_theta: float = self.theta

        vitesse_lineaire: float = (self.vL + self.vR) / 2.0
        vitesse_angulaire: float = (self.vR - self.vL) / self.L

        self.x += vitesse_lineaire  * math.cos(self.theta) * self.pas
        self.y += vitesse_lineaire  * math.sin(self.theta) * self.pas
        self.theta += vitesse_angulaire * self.pas

        if self.plateforme.collision_robot(self):
            print("Oups, le robot s'est congné")
            self.x, self.y, self.theta = ancien_x, ancien_y, ancien_theta
            self.vL = 0.0
            self.vR = 0.0
            return False 
            
        return True 

    def get_distance(self,distance_max=100.0,step=0.1):
        distance=0.0
        while distance < distance_max: 
            test_x:float= self.x +distance *math.cos(self.theta)
            test_y:float= self.y +distance *math.sin(self.theta)

            if (test_x<0 or test_x> self.plateforme.longueur or test_y<0 or test_y >self.plateforme.hauteur):
                return distance
            for obstacle in self.plateforme.obstacles:
                _, obstacle_x, obstacle_y, obstacle_h, obstacle_l=obstacle
                if obstacle_x <= test_x <= obstacle_x + obstacle_l and obstacle_y <=test_y <=obstacle_y +obstacle_h:
                    return distance
            distance+=step
                
        return distance_max 

    def get_position(self):
        return self.x, self.y, self.theta 
       
    def get_vitesse(self):
        return self.vL, self.vR
