import math
class Robot: 
    def __init__(self, x : float, y : float, theta : float, 
                 L : float, larg : float, long : float):
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
        self.pas: float = 0.1 
    def avancer(self):
        """ fait avancer le robot, condition : vL= vR"""
        v = ( self.vL + self.vR)/ 2 #calcul de la vitesse du robot
        #calcul des déplacement de x et y pendant le pas 
        delta_x = v * math.cos(self.theta) * self.pas
        delta_y = v * math.sin(self.theta) * self.pas 
        #calcul des nouvelles positions x et y du robot
        self.x = self.x + delta_x
        self.y = self.y + delta_y
    def tourner(self):
        """faire tourner le robot sur lui même 
            condition : les roues n'ont pas la même vitesse"""
        #calcul de la vitesse angulaire
        v_ang = ( self.vR - self.vL)/ self.L 
        #calcul et attribution du nouvel angle du robot après rotation
        self.theta = self.theta + ( v_ang * self.pas )
    def carre(self):
        nbcote = 0
        long_cote = 2
        etat = "avance"
        x0 = self.x
        y0 = self.y
        angle_acc = 0.0

        while nbcote < 4:
            if etat == "avance":
                self.vL = 1.0
                self.vR = 1.0
                d = math.sqrt((self.x - x0)**2 + (self.y - y0)**2)
                if d < long_cote:
                    self.avancer()
                else:
                    etat = "tourner"
                    angle_acc = 0.0

            elif etat == "tourner":
                self.vL = -1.0
                self.vR = 1.0
                omega = (self.vR - self.vL) / self.L
                angle_acc += abs(omega * self.pas)
                if angle_acc < math.pi / 2:
                    self.tourner()
                else:
                    nbcote += 1
                    etat = "avance"
                    x0 = self.x
                    y0 = self.y

