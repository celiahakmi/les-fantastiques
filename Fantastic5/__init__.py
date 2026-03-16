from .robot import Robot
from .plateforme import Plateforme
from .affichage import PygameView

from .simulation import Robot, Plateforme
from .strategie import AvancerDroit, Tourner
from .Graphique.affichage import PygameView

__all__ = ["Robot", "Plateforme", "AvancerDroit", "Tourner", "PygameView"]
