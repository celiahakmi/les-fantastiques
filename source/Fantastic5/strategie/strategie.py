import math

class AvancerDroit:
    def __init__(self, adaptateur, distance: float):
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


class Tourner:
    def __init__(self, adaptateur , angle_deg: float):
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
        self.angle_parcouru+= abs(self.adaptateur.get_angle_parcouru())

    def stop(self):
        """renvoie true si angle demandé atteint"""
        return self.angle_parcouru >= self.angle

class Arreter:
    def __init__(self, adaptateur):
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


class Choregraphie:
    def __init__(self, adaptateur, liste_actions: list):
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


class Accelerer:
    def __init__(self, adaptateur, distance: float, v_max: float, acceleration: float):
        self.adaptateur = adaptateur
        self.distance = distance
        self.v_max = v_max
        self.accel = acceleration 
        self.v_actuelle = 0.0
        self.parcouru = 0.0

    def start(self):
        self.parcouru = 0.0
        self.v_actuelle = 0.0 

    def step(self):
        # On augmente la vitesse sans dépasser le max
        if self.v_actuelle < self.v_max:
            self.v_actuelle += self.accel
        
        # On applique la vitesse
        self.adaptateur.set_vitesse(self.v_actuelle, 0.0)
        
        # On mesure le chemin fait
        self.parcouru += self.adaptateur.get_distance_parcourue()

    def stop(self):
        return self.parcouru >= self.distance
    
        
class Condition: 
    def __init__(self, adaptateur, stratA, stratB, distance_securite: float) :
        self.adaptateur = adaptateur
        self.strat_libre = stratA
        self.strat_obstacle = stratB
        self.securite = distance_securite
        self.current_strat = None

    def start(self):
        """Initialisation"""
        self.current_strat = None

    def step(self):
        """Choisit la stratégie en fonction du capteur à chaque pas"""
        # On interroge le capteur via l'adaptateur
        distance = self.adaptateur.get_distance() 

        # Choix de la stratégie selon la condition 
        if distance > self.securite:
            nouvelle_strat = self.strat_libre
        else:
            nouvelle_strat = self.strat_obstacle

        # Si on change, on demarre la nouvelle strat
        if nouvelle_strat != self.current_strat:
            self.current_strat = nouvelle_strat
            self.current_strat.start() 

        self.current_strat.step() 

    def stop(self):
        """ On met a false"""
        return False
    
class Boucle: 
    def __init__(self, adaptateur, action, nb_iterations: int):
        self.adaptateur = adaptateur 
        self.action = action 
        self.nb_iterations = nb_iterations  # Le nombre total de tours à faire
        self.compteur = 0                   # Le suivi des tours effectués

    def start(self): 
        """Démarre la boucle et réinitialise le compteur"""
        self.compteur = 0
        self.action.start()

    def step(self):
        """Exécute l'action et incrémente le compteur à chaque fin d'action"""
        if self.stop():
            return

        self.action.step()
        
        # Si l'action vient de se terminer, on passe au tour suivant
        if self.action.stop(): 
            self.compteur += 1
            # On ne redémarre l'action que s'il reste des tours à faire
            if not self.stop():
                self.action.start()

    def stop(self):
        """S'arrête quand le compteur atteint le nombre d'itérations"""
        return self.compteur >= self.nb_iterations
    

    
