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
    def __init__(self, adaptateur , angle_deg: float):
        super().__init__("Tourner") 
        self.adaptateur= adaptateur
        self.angle: float = math.radians(angle_deg)
        self.angle_parcouru: float = 0.0

    def start(self):
        """initialisation des variables"""
        self.angle_parcouru = 0.0
        self.adaptateur.set_vitesse(0.0,0.1) #rotation sur place

    def step(self):
        """execute un pas de la stratégie"""
        if self.stop():
            self.adaptateur.set_vitesse(0.0, 0.0)
            return

        self.adaptateur.set_vitesse(0.0, 0.1)

        #récupération de l'angle du pas
        self.angle_parcouru += self.adaptateur.get_angle_parcouru()

    def stop(self):
        """renvoie true si angle demandé atteint"""
        return self.angle_parcouru >= self.angle

class Arreter(Strategie):
    def __init__(self, adaptateur):
        super().__init__("Arreter") 
        self.adaptateur = adaptateur

    def start(self):
        """Coupe les moteurs au démarrage"""
        self.adaptateur.set_vitesse(0.0, 0.0)

    def step(self):
        """Arrêt à chaque pas de temps"""
        self.adaptateur.set_vitesse(0.0, 0.0)

    def stop(self):
        """Ne s'arrête jamais"""
        return False 


class Choregraphie(Strategie):
    def __init__(self, adaptateur, liste_actions: list):
        super().__init__("Chorégraphie") 
        self.adaptateur= adaptateur
        self.actions: list = liste_actions
        self.index: int = 0

    def start(self):
        """Initialise la chorégraphie"""
        self.index = 0
        if len(self.actions) > 0:
            self.actions[self.index].start()

    def step(self):
        """Exécute l'action courante et passe à la suivante si elle est finie"""
        if self.stop():
            return

        action_en_cours = self.actions[self.index]
        action_en_cours.step()

        if action_en_cours.stop():
            self.index += 1
            if not self.stop():
                self.actions[self.index].start()

    def stop(self):
        """Vrai quand toutes les actions de la liste sont terminées"""
        return self.index >= len(self.actions)

 
class Condition(Strategie): 
    def __init__(self, adaptateur, condition_func, stratA, stratB) :
        super().__init__("Condition") 
        self.adaptateur = adaptateur
        self.condition = condition_func
        self.stratA = stratA
        self.stratB = stratB
        self.current_strat = None

    def start(self):
        """Initialisation"""
        self.current_strat = None

    def step(self):
        """Choisit la stratégieselon la condition"""
        # évalue la condition 
        if self.condition(self.adaptateur):
            nouvelle_strat = self.stratA
        else:
            nouvelle_strat = self.stratB

        # Si on change, on demarre la nouvelle strat
        if nouvelle_strat != self.current_strat:
            self.current_strat = nouvelle_strat
            self.current_strat.start() 
        #on éxecute la stratégie courante
        self.current_strat.step() 

    def stop(self):
        """ On met a false"""
        return False
    
class Boucle(Strategie): 
    def __init__(self, adaptateur, action, nbRepet):
        super().__init__("Boucle") 
        self.adaptateur = adaptateur 
        self.action = action 
        self.nbRepet = nbRepet
        self.compteur = 0

    def start(self): 
        """démarre la boucle"""
        self.compteur = 0
        self.action.start() #on commence la premiere répétition

    def step(self):
        """Exécute l'action en boucle"""
        #toutes les répétitions ont été faites :
        if self.compteur >= self.nbRepet:
            return
        self.action.step() #exécute un pas de l'action
        #si l'action est terminé
        if self.action.stop(): 
            self.compteur += 1 
            #si la boucle n'est pas terminé on recommence l'action
            if self.compteur < self.nbRepet:
                self.action.start() 

    def stop(self):
        """False pour que le robot ne puisse pas s'arrêter et continue la boucle"""
        return self.compteur >= self.nbRepet
    

    
