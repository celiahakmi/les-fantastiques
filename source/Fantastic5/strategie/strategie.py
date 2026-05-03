import math
from abc import ABC, abstractmethod

class Strategie(ABC):
    def __init__(self, nom: str):
        self.nom = nom

    @abstractmethod
    def start(self):
        """Initialisation de la stratégie"""
        pass

    @abstractmethod
    def step(self):
        """Exécution d'une étape de la stratégie"""
        pass

    @abstractmethod
    def stop(self):
        """Condition d'arrêt de la stratégie"""
        pass

class AvancerDroit(Strategie):
    def __init__(self, adaptateur, distance: float):
        super().__init__("Avancer Droit") 
        self.adaptateur = adaptateur
        self.distance: float = distance
        self.parcouru: float = 0.0

    def start(self):
        """Initialise les variables au moment de démarrer"""
        self.parcouru = 0.0
        # on appelle set_vitesse
        self.adaptateur.set_vitesse(0.1, 0.0)
          
    def step(self):
        """on fait avancer le robot d'un pas et on calcule la distance"""
        # si on a fini on coupe les moteurs et on s'arrête
        if self.stop():
            self.adaptateur.set_vitesse(0.0, 0.0)
            return

        self.adaptateur.set_vitesse(0.1, 0.0)
        
        # on calcule la distance qu'on vient de parcourir sur ce pas
        self.parcouru+=self.adaptateur.get_distance_parcourue()
        

    def stop(self):
        return self.parcouru >= self.distance



class Tourner(Strategie):
    def __init__(self, adaptateur, angle_deg: float, vitesse_angulaire: float = 0.1):
        super().__init__("Tourner")
        self.adaptateur = adaptateur
        self.angle = math.radians(angle_deg)
        self.vitesse_angulaire = abs(vitesse_angulaire)
        self.angle_parcouru = 0.0
        self.sens = 1.0 if self.angle >= 0 else -1.0

    def start(self):
        self.angle_parcouru = 0.0
        self.sens = 1.0 if self.angle >= 0 else -1.0
        self.adaptateur.set_vitesse(0.0, self.sens * self.vitesse_angulaire)

    def step(self):
        if self.stop():
            self.adaptateur.set_vitesse(0.0, 0.0)
            return

        self.adaptateur.set_vitesse(0.0, self.sens * self.vitesse_angulaire)
        self.angle_parcouru += abs(self.adaptateur.get_angle_parcouru())

    def stop(self):
        return self.angle_parcouru >= abs(self.angle)


class TournerArc(Strategie):
    def __init__(self,adaptateur,angle_deg: float,rayon: float = 0.4,vitesse_lineaire: float = 0.1,):
        super().__init__("Tourner Arc")
        self.adaptateur = adaptateur
        self.angle = math.radians(angle_deg)
        self.rayon = abs(rayon)
        self.vitesse_lineaire = abs(vitesse_lineaire)
        self.angle_parcouru = 0.0
        self.sens = 1.0 if self.angle >= 0 else -1.0

    def start(self):
        self.angle_parcouru = 0.0
        self.sens = 1.0 if self.angle >= 0 else -1.0
        vitesse_angulaire = self.sens * (self.vitesse_lineaire / self.rayon)
        self.adaptateur.set_vitesse(self.vitesse_lineaire, vitesse_angulaire)

    def step(self):
        if self.stop():
            self.adaptateur.set_vitesse(0.0, 0.0)
            return

        vitesse_angulaire = self.sens * (self.vitesse_lineaire / self.rayon)
        self.adaptateur.set_vitesse(self.vitesse_lineaire, vitesse_angulaire)
        self.angle_parcouru += abs(self.adaptateur.get_angle_parcouru())

    def stop(self):
        return self.angle_parcouru >= abs(self.angle)


class Arreter(Strategie):
    def __init__(self, adaptateur):
        super().__init__("Arreter")
        self.adaptateur = adaptateur

    def start(self):
        self.adaptateur.set_vitesse(0.0, 0.0)

    def step(self):
        self.adaptateur.set_vitesse(0.0, 0.0)

    def stop(self):
        return False


class Choregraphie(Strategie):
    def __init__(self, adaptateur, liste_actions: list):
        super().__init__("Choregraphie")
        self.adaptateur = adaptateur
        self.actions = liste_actions
        self.index = 0

    def start(self):
        self.index = 0
        if self.actions:
            self.actions[self.index].start()

    def step(self):
        if self.stop():
            return

        action_en_cours = self.actions[self.index]
        action_en_cours.step()

        if action_en_cours.stop():
            self.index += 1
            if not self.stop():
                self.actions[self.index].start()

    def stop(self):
        return self.index >= len(self.actions)


class Condition(Strategie):
    def __init__(self, adaptateur, condition_func, stratA, stratB):
        super().__init__("Condition")
        self.adaptateur = adaptateur
        self.condition = condition_func
        self.stratA = stratA
        self.stratB = stratB
        self._en_evitement = False
 
    def start(self):
        self._en_evitement = False
        self.stratB.start()
 
    def step(self):
        if self._en_evitement:
            if not self.stratA.stop():
                self.stratA.step()
            else:
                self._en_evitement = False
    
            return 
 
        if self.stratB.stop():
            return
 
        if self.condition(self.adaptateur):
            print(" Obstacle détecté! Lancement du contournement.")
            self._en_evitement = True
            self.stratA.start()
            self.stratA.step()
        else:
            self.stratB.step()
 
    def stop(self):
        if self._en_evitement:
            return False
        return self.stratB.stop()


class Boucle(Strategie):
    def __init__(self, adaptateur, action, nbRepet):
        super().__init__("Boucle")
        self.adaptateur = adaptateur
        self.action = action
        self.nbRepet = nbRepet
        self.compteur = 0

    def start(self):
        self.compteur = 0
        self.action.start()

    def step(self):
        if self.compteur >= self.nbRepet:
            return

        self.action.step()

        if self.action.stop():
            self.compteur += 1
            if self.compteur < self.nbRepet:
                self.action.start()

    def stop(self):
        return self.compteur >= self.nbRepet


class ContournerObstacle(Strategie):
    ETATS = [
        "AVANCER",
        "TOURNER_DROITE_1",
        "LONGER_1",
        "TOURNER_GAUCHE_1",
        "PASSER_DEVANT",
        "TOURNER_GAUCHE_2",
        "REJOINDRE",
        "TOURNER_DROITE_2",
    ]
 
    def __init__(self, adaptateur,
                 vitesse: float = 0.1,
                 vitesse_rot: float = 0.1,
                 seuil_detection: float = 0.5,
                 seuil_obstacle_cote: float = 1.5,
                 dist_rejoindre: float = 0.8):
        super().__init__("ContournerObstacle")
        self.adaptateur = adaptateur
        self.vitesse = vitesse
        self.vitesse_rot = vitesse_rot
        self.seuil_detection = seuil_detection
        self.seuil_obstacle_cote = seuil_obstacle_cote
        self.dist_rejoindre = dist_rejoindre
 
        self._etat = "AVANCER"
        self._action_courante = None
 

 



