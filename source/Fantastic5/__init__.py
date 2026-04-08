from .graphique import PygameView 
from .simulation import Plateforme, Robot 
from .strategie import AvancerDroit, Tourner, Arreter, Choregraphie, Accelerer, Boucle, Condition 

__all__ = ["PygameView", "Plateforme", "Robot", "AvancerDroit", "Tourner", "Arreter", "Choregraphie", "initialisation_simulation", "inititialisation_simulation_tmesolo", "Accelerer","Boucle","Condition"]

def initialisation_simulation():
    """Création  d'une simulation avec des paramètres par défaut pour faire déplacer le robot en carré et le faire avancer dans un plan continu contenant des obstacles dans le main"""
    # Plateforme
    p = Plateforme(10.0, 10.0)
    p.init_obstacle(4.5, 1.0, 1.0, 1.0) 
    p.init_obstacle(4.5, 4.5, 1.0, 1.0) 
    p.init_obstacle(4.5, 8.0, 1.0, 1.0) 
    p.init_ballon(3.0, 2.0, 1.0)
    #Robot 
    r = Robot(5.0, 5.0, 0.0, 0.5, 0.5, 0.7, p)
    
    return p, r

def inititialisation_simulation_tmesolo(): 
    """"""
    #Plateforme 
    p = Plateforme(10.0, 10.0) 
    p.init_obstacle(4.5, 1.0, 1.0, 1.0) 
    p.init_obstacle(4.5, 4.5, 1.0, 1.0) 
    p.init_obstacle(4.5, 8.0, 1.0, 1.0) 
    r = Robot(9.0, 9.0, .0, 0.5, 0.5, 0.7, p)
    return p, r 

