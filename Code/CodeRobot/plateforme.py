from robot import Robot
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

    //si il y a une collision on remet le robot a son ancienne position on reinitialise les vitesse et on retourne false
    def deplacer_si_possible(robot, plateforme, action):
    x, y, t = robot.x, robot.y, robot.theta
    action()
    if plateforme.collision_robot(robot):
        robot.x, robot.y, robot.theta = x, y, t
        robot.vL = 0.0
        robot.vR = 0.0
        return False
    return True


#Tests
if __name__ == "__main__":
    #Initialisation
    p = Plateforme(10, 10)
    print("Test 1: création plateforme 10x10")

    #Test ajout valide
    res1 = p.init_obstacle(5, 5, 1, 1)
    print(f"Test 2: ajout obstacle (5, 5, 1, 1) valide : {res1 == True}")
    print(f"Nombre d'obstacles : {len(p.obstacles)}")

    #Test dépassement bordure (x + l > longueur)
    res2 = p.init_obstacle(0, 10, 5, 10)
    print(f"Test 3: erreur dépassement bordure : {res2 == False}")

    #Test chevauchement (sur l'obstacle du Test 2)
    res3 = p.init_obstacle(4, 4, 10, 10) # Chevauche le premier
    print(f"Test 4: erreur chevauchement : {res3 == False}")

    # Test 5: Robot dans le coin
    r_coin = Robot(0.5, 0.5, 0, 1.0, 1.0, 1.0)
    print(f"Test 5: coin bas-gauche : {'True' if not p.collision_robot(r_coin) else 'False'}")

    # Test 6: Robot qui dépasse
    r_depasse = Robot(1, 1, 0, 1.0, 1.0, 1.0)
    print(f"Test 6: dépasse bord : {'True' if p.collision_robot(r_depasse) else 'False'}")

    # Test 7: Robot qui touche l'obstacle
    r_obstacle = Robot(5.5, 5, 0, 1.0, 1.0, 1.0)
    print(f"Test 7: touche obstacle : {'True' if p.collision_robot(r_obstacle) else 'False'}")
