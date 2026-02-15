import math

class Robot:
    def __init__(self, x: float, y: float, theta_deg: float,
                 width: float, height: float,
                 wheel_base:float,
                 plateforme,
                 vmax: float =4.0,
                 amax: float =10.0):
        """ Initialisation du robot :
            - coordonnées x et y 
            - theta_deg : orientation en degré
            - largeur et hauteur : dimension du robot
            - dist_roue : distance entre les roues
            - vmax : vitesse max d'une roue 
            - amax : accélération maximale d'une roue
            """

        # x,y = coin haut-gauche du rectangle robot
        self.x = float(x)
        self.y = float(y)
        self.theta = math.radians(theta_deg)

        self.width = float(width)
        self.height = float(height)

        self.L = float(wheel_base)
        self.plateforme = plateforme

        self.vmax = float(vmax)
        self.amax = float(amax)
        # vitesses actuelles des roues
        self.vL: float = 0.0
        self.vR: float = 0.0
        # vitesses cibles    
        self.target_vL: float= 0.0
        self.target_vR: float = 0.0

        self.range = None

    def set_wheel_targets(self, vL: float, vR: float):
        """ définit les vitesses cibles des roues
            vl : vitesse cible roue gauche
            vr : vitesse cible roue droite 
        """
        self.target_vL = max(-self.vmax, min(self.vmax, float(vL)))
        self.target_vR = max(-self.vmax, min(self.vmax, float(vR)))

    def _approach(self, cur: float, target: float, max_delta: float):
        """ Cette fonction permet de faire varier une valeur petit à petit vers une cible, sans la changer brutalement d’un coup.
            - cur = valeur actuelle
            - target = valeur cible 
            - max_delta = variation maximale autorisé"""
        if target > cur:
            return min(target, cur + max_delta)
        return max(target, cur - max_delta)

    def scan_distance(self, max_range: float=10.0):
        """capteur de distance à l'avant du robot sous la forme d'un rayon
            max range : portée maximale du capteur"""
        center_x = self.x + self.width / 2.0
        center_y = self.y + self.height / 2.0
        #marge : rayon du cercle englobant le rectangle
        marge = 0.5 * math.sqrt(self.width**2 + self.height**2)

        self.range = self.plateforme.distance_jusqua_obstacle(
            center_x, center_y, self.theta,
            max_range=max_range,
            step=0.02,
            marge=marge
        )
        return self.range

    def step(self, dt: float):
        """ la fonction permet de mettre à jour l'état du robot sur un pas de temps (dt)"""
        dt = min(dt, 0.05)

        # accélération limitée
        max_delta = self.amax * dt
        self.vL = self._approach(self.vL, self.target_vL, max_delta)
        self.vR = self._approach(self.vR, self.target_vR, max_delta)

        v = (self.vR + self.vL) / 2.0
        omega = (self.vR - self.vL) / self.L

        dist = abs(v) * dt
        step_max = 0.03
        n = max(1, int(dist / step_max) + 1)
        sub_dt = dt / n

        for _ in range(n):
            new_theta = self.theta + omega * sub_dt
            new_x = self.x + v * math.cos(self.theta) * sub_dt
            new_y = self.y + v * math.sin(self.theta) * sub_dt
            #gestion des collision 
            if not self.plateforme.collision_rectangle(new_x, new_y, self.width, self.height):
                self.x, self.y, self.theta = new_x, new_y, new_theta
            else:
                # stop net si collision
                self.vL = 0.0
                self.vR = 0.0
                break
