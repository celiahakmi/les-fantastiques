from .graphique import PygameView 
from .simulation import Plateforme, Robot, Robot2
from .strategie import AvancerDroit, Tourner, Arreter, Choregraphie, Accelerer, Boucle, Condition, Cercle

__all__ = ["PygameView", "Plateforme", "Robot", "Robot2", "AvancerDroit", "Tourner", "Arreter", "Choregraphie", "initialisation_simulation", "Accelerer","Boucle","Condition", "Cercle"]

def initialisation_simulation():
    """Création  d'une simulation avec des paramètres par défaut pour faire déplacer le robot en carré et le faire avancer dans un plan continu contenant des obstacles dans le main"""
    # Plateforme
    p = Plateforme(10.0, 10.0)
    p.init_obstacle(4.5, 4.5, 1.0, 1.0) 
    p.init_obstacle(4.5, 1.0, 1.0, 1.0) 
    p.init_obstacle(4.5, 8.0, 1.0, 1.0) 
    #Robot 
    r = Robot(1.0, 7.0, 0.0, 0.5, 0.5, 0.7, p)
    r2 = Robot2(8.0, 4.5, 0.0, 0.5, 0.5, 0.7, p)
    
    return p, r, r2
