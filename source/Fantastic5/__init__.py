from .graphique import PygameView 
from .simulation import Plateforme, Robot 
from .strategie import AvancerDroit, Tourner, TracerCarre, Choregraphie 

__all__ = ["PygameView", "Plateforme", "Robot", "AvancerDroit", "Tourner", "TracerCarre", "Choregraphie", "initialisation_simulation"]

def initialisation_simulation():
    """Création  d'une simulation avec des paramètres par défaut pour faire déplacer le robot en carré et le faire avancer dans un plan continu contenant des obstacles dans le main"""
    # Plateforme
    p = Plateforme(10, 10)
    p.init_obstacle(8, 3, 2, 1)
    p.init_obstacle(5, 5, 1, 1)
    
    # Robot
    r = Robot(5, 2, 0, 0.5, 0.5, 0.7, p)
    
    # Stratégie
    liste_actions = [TracerCarre(r, 2.0), AvancerDroit(r, 5.0)]
    strat = Choregraphie(r, liste_actions)
    strat.start()
    
    return p, r, strat