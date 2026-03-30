from .graphique import PygameView 
from .simulation import Plateforme, Robot 
from .strategie import AvancerDroit, Tourner, Choregraphie 


__all__ = ["PygameView", "Plateforme", "Robot", "AvancerDroit", "Tourner", "Choregraphie", "initialisation_simulation"]

def initialisation_simulation():
    """Création  d'une simulation avec des paramètres par défaut pour faire déplacer le robot en carré et le faire avancer dans un plan continu contenant des obstacles dans le main"""
    # Plateforme
    p = Plateforme(10.0, 10.0)
    p.init_obstacle(2.0, 2.0, 1.0, 1.0) 
    #Robot 
    r = Robot(5.0, 5.0, 0.0, 0.5, 0.5, 0.7, p)
    
    return p, r
