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


class ApprocherLeMur:
    def __init__(self, adaptateur, distance_securite=0.5):
        self.adaptateur=adaptateur
        self.distance_securite: float = distance_securite

    def start(self):
        """initialise la stratégie d'approcher le mur"""
        self.adaptateur.set_vitesse(0.0,0.0)

    def step(self):
        """fait avancer le robot en ajustant la vitesse selon la distance au mur """
        distance= self.adaptateur.get_distance()
        if distance>2:
            self.adaptateur.set_vitesse(0.2,0.0)
        elif distance>self.distance_securite:
            self.adaptateur.set_vitesse(0.05,0.0)
        else:
            self.adaptateur.set_vitesse(0.0,0.0)

    def stop(self):
        """True quand le robot est suffisamment proche du mur"""
        return self.adaptateur.get_distance()<=self.distance_securite
    
class Boucle: 
    def __init__(self, adaptateur, action):
        self.adaptateur = adaptateur 
        self.action = action 
    def start(self): 
        """démarre la boucle"""
        self.action.start()
    def step(self):
        """Exécute l'action en boucle"""
        self.action.step()
        if self.action.stop(): 
            self.action.start() #la boucle s'effectue ici puisqu'on redémarre l'action 
    def stop(self):
        """False pour que le robot ne puisse pas s'arrêter et continue la boucle"""
        return False

    


