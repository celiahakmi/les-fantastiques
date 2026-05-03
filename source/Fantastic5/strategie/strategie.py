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
        self.current_strat = None

    def start(self):
        self.current_strat = self.stratB
        self.stratB.start()

    def step(self):
        # Si on est déjà en train de contourner (stratA)
        if self.current_strat is self.stratA:
            if not self.stratA.stop():
                self.stratA.step()
                return # On continue le contournement
            else:
                # Contournement fini, on reprend le parcours initial
                self.current_strat = self.stratB
                # On ne fait pas start() ici pour ne pas recommencer le parcours au début
                # mais on peut appeler step() si besoin

        # Si on est sur le parcours normal (stratB)
        if self.stratB.stop():
            return

        # Vérification de la condition pour déclencher le contournement
        if self.condition(self.adaptateur):
            print("Obstacle détecté ! Lancement du contournement.")
            self.stratA.start()
            self.current_strat = self.stratA
            self.stratA.step()
        else:
            self.stratB.step()

    def stop(self):
        if self.current_strat is self.stratA and not self.stratA.stop():
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
    def __init__(
        self,
        adaptateur,
        angle_deg: float = 90.0,
        distance_deport: float = 0.9,
        distance_avance: float = 0.6,
    ):
        super().__init__("Contourner Obstacle")
        self.adaptateur = adaptateur
        self.angle_deg = abs(angle_deg)
        self.distance_deport = distance_deport
        self.distance_avance = distance_avance
        self.sens_precedent = 1
        self.manoeuvre = None

    def _distance_laterale(self, angle_offset):
        try:
            return self.adaptateur.get_distance(angle_offset=angle_offset)
        except TypeError:
            return None

    def _choisir_angle(self):
        distance_gauche = self._distance_laterale(math.pi / 2)
        distance_droite = self._distance_laterale(-math.pi / 2)

        if distance_gauche is not None and distance_droite is not None:
            if distance_gauche > distance_droite + 1e-6:
                self.sens_precedent = 1
                return self.angle_deg
            if distance_droite > distance_gauche + 1e-6:
                self.sens_precedent = -1
                return -self.angle_deg

        self.sens_precedent *= -1
        return self.sens_precedent * self.angle_deg

    def start(self):
        angle = self._choisir_angle()
        self.manoeuvre = Choregraphie(
            self.adaptateur,
            [   Tourner(self.adaptateur, angle),
                AvancerDroit(self.adaptateur, self.distance_deport),
                Tourner(self.adaptateur, -angle),
                AvancerDroit(self.adaptateur, self.distance_avance),
            ],
        )
        self.manoeuvre.start()

    def step(self):
        if not self.stop():
            self.manoeuvre.step()

    def stop(self):
        return self.manoeuvre is not None and self.manoeuvre.stop()

