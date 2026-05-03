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

    def get_distance(self, angle_offset=0.0): # Doit être identique ici
        pass

    def get_distance_parcourue(self):
        """Retourne la distance parcourue"""
        pass

    def get_angle_parcouru(self):
        """Retourne la distance parcourue de angle"""
        pass
