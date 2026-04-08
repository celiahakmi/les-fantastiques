from .graphique import PygameView 
from .simulation import Plateforme, Robot 
from .strategie import AvancerDroit, Tourner, Arreter, Choregraphie, Accelerer, Boucle, Condition 

__all__ = ["PygameView", "Plateforme", "Robot", "AvancerDroit", "Tourner", "Arreter", "Choregraphie", "initialisation_simulation", "Accelerer","Boucle","Condition"]

def initialisation_simulation():
    """Crée une simulation avec trois obstacles alignés verticalement au milieu."""
    # Plateforme
    p = Plateforme(10.0, 10.0)
    p.init_obstacle(4.5, 1.5, 1.0, 1.0)
    p.init_obstacle(4.5, 4.5, 1.0, 1.0)
    p.init_obstacle(4.5, 7.5, 1.0, 1.0)
    #Robot 
    r = Robot(1.0, 1.0, 0.0, 0.5, 0.5, 0.7, p)
    
    return p, r
