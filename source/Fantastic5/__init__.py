from .simulation import Plateforme, Robot
from .strategie import (Arreter,AvancerDroit,Boucle,Choregraphie,Condition,ContournerObstacle,Tourner,TournerArc,)

__all__ = ["PygameView","Plateforme","Robot","AvancerDroit","Tourner","TournerArc","Arreter","Choregraphie","initialisation_simulation","Boucle","Condition","ContournerObstacle",]


def __getattr__(name):
    if name == "PygameView":
        from .graphique import PygameView

        return PygameView
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def initialisation_simulation():
    """Création  d'une simulation avec des paramètres par défaut pour faire déplacer le robot en carré et le faire avancer dans un plan continu contenant des obstacles dans le main"""
    # Plateforme
    p = Plateforme(11.0, 11.0)

    p.init_obstacle(x=0.5, y=7, h=0.5, l=5)    
    p.init_obstacle(x=4, y=5, h=0.5, l=6.5)    
    p.init_obstacle(x=0.5, y=3, h=0.5, l=5)   
    p.init_obstacle(x=10.5, y=0.5, h=10, l=0.5)  
    p.init_obstacle(x=0, y=0, h=0.5, l=11)  
    p.init_obstacle(x=0, y=10.5, h=0.5, l=11)
    p.init_obstacle(x=0, y=0.5, h=7, l=0.5)   

    p.init_obstacle(x=6, y=9, h=1, l=1)  
    
 
    #Robot 
    r = Robot(1.0, 1.0, 0.0, 0.5, 0.5, 0.7, p)
    
    return p, r
