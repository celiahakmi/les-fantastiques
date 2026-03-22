from abc import ABC, abstractmethod

class Adaptateur(ABC):
    def __init__(self, robot):
        self.robot = robot 

    def set_vitesse(self, v_lineaire, v_angulaire):
        """Initialise les vitesses des roues"""
        pass

    def get_position(self):
        """Retourne la position actuelle des roues ou du robot"""
        pass

    def get_distance(self):
        """Retourne la distance avec l'obstacle le plus proche"""
        return self.robot.get_distance()
