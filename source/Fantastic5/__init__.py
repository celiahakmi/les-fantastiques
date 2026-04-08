from .graphique import PygameView 
from .simulation import Plateforme, Robot 
from .strategie import AvancerDroit, Tourner, Arreter, Choregraphie, Accelerer, Boucle, Condition

__all__ = ["PygameView", "Plateforme", "Robot", "AvancerDroit", "Tourner", "Arreter", "Choregraphie", "initialisation_simulation", "Accelerer","Boucle","Condition"]

def initialisation_simulation():
    """Création  d'une simulation avec des paramètres par défaut pour faire déplacer le robot en carré et le faire avancer dans un plan continu contenant des obstacles dans le main"""
    # Plateforme
    p = Plateforme(10.0, 10.0)
    #q1.1
    p.init_obstacle(4.0, 0.0, 2.0, 2.0) 
    p.init_obstacle(4.0, 4.0, 2.0, 2.0) 
    p.init_obstacle(4.0, 8.0, 2.0, 2.0) 


    #robot de la q1.1
    #r=Robot(0.6, 9.1,-90.0, 0.5, 0.6, 0.9, p)

    #Robot 1
    r1= Robot(0.6, 5,-90.0, 0.5, 0.6, 0.9, p)
    #robot 2
    r2= Robot(9.1, 5,-90.0, 0.5, 0.6, 0.9, p)

    return p, r1,r2
