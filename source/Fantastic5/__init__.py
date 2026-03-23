from .graphique import PygameView 
from .simulation import Plateforme, Robot 
from .strategie import AvancerDroit, Tourner, TracerCarre, Choregraphie 

from .adaptateur import AdaptateurSimu

__all__ = ["PygameView", "Plateforme", "Robot", "AvancerDroit", "Tourner", "TracerCarre", "Choregraphie", "initialisation_simulation"]

def initialisation_simulation():
    """Création  d'une simulation avec des paramètres par défaut pour faire déplacer le robot en carré et le faire avancer dans un plan continu contenant des obstacles dans le main"""
    # Plateforme
    p = Plateforme(10, 10)
    p.init_obstacle(8, 3, 2, 1)
    p.init_obstacle(5, 5, 1, 1)
    
    # Robot
    r = Robot(5, 2, 0, 0.5, 0.5, 0.7, p)

    #adaptateur
    adp = AdaptateurSimu(r)
    
    # Stratégie
    liste_actions = [TracerCarre(adp, 2.0), AvancerDroit(adp, 5.0)]
    strat = Choregraphie(adp, liste_actions)
    strat.start()
    
    return p, r, strat,adp
