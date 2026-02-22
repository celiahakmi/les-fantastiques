import math
class Robot: 
    def __init__(self, x : float, y : float, theta : float, 
                 L : float, larg : float, long : float ):
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
        #attribut variable du robot 
        self.vL: float = 0.0
        self.vR: float = 0.0
        

