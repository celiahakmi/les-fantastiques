import random
import math

class Robot:
    def __init__(self,x,y,largeur, theta_deg, width, height,wheel_base, plateforme,vmax=4.0, amax=10.0):
        self.x = float(x)
        self.y = float(y)
        self.theta = math.radians(theta_deg)

        self.width = float(width)
        self.height = float(height)

        self.L = float(wheel_base)
        self.plateforme = plateforme

        self.vmax = float(vmax)
        self.amax = float(amax)

        self.vL = 0.0
        self.vR = 0.0
        self.target_vL = 0.0
        self.target_vR = 0.0

        self.range = None
        
    def set_wheel_targets(self, vL, vR):
        self.target_vL = max(-self.vmax, min(self.vmax, float(vL)))
        self.target_vR = max(-self.vmax, min(self.vmax, float(vR)))
        
    def _approach(self, cur, target, max_delta):
        if target > cur:
            return min(target, cur + max_delta)
        return max(target, cur - max_delta)
        
   # Capteur: on le lance depuis le CENTRE du robot
    def scan_distance(self, max_range=10.0):
        center_x = self.x + self.width / 2.0
        center_y = self.y + self.height / 2.0
        marge = 0.5 * math.sqrt(self.width**2 + self.height**2)

        self.range = self.plateforme.distance_jusqua_obstacle( center_x, center_y, self.theta, max_range=max_range, step=0.02,marge=marge )
        return self.range()


    def carre(self, cote):
        """ fait déplacer le robot en carré dans un plan continu"""
        for i in range(4):
            self.avancer(cote)
            self.tourner(90)

        
    

   
