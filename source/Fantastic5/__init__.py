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
    p = Plateforme(10.0, 10.0)

    p.init_obstacle(x=0, y=7, h=0.5, l=6)    # Mur haut gauche
    p.init_obstacle(x=4, y=5, h=0.5, l=6)    # Mur milieu droite
    p.init_obstacle(x=0, y=3, h=0.5, l=6)    # Mur bas gauche
    p.init_obstacle(x=7, y=0, h=4, l=0.5)    # Entrée du goulot (vertical)
    p.init_obstacle(x=9.5, y=0, h=4, l=0.5)  # Mur extérieur droit
    p.init_obstacle(x=7, y=0, h=0.5, l=3)    # Fond du cul-de-sac

    #Robot 
    r = Robot(1.0, 1.0, 0.0, 0.5, 0.5, 0.7, p)
    
    return p, r
