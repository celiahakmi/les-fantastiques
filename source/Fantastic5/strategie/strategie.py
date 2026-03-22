import math

class AvancerDroit:
    def __init__(self, adaptateur, distance: float):
        self.adaptateur = adaptateur
        self.distance: float = distance
        self.parcouru: float = 0.0
        self.x_prec: float = 0.0
        self.y_prec: float = 0.0

    def start(self):
        """Initialise les variables au moment de démarrer"""
        self.parcouru = 0.0
        #on passe par l'adaptateur pour récupérer x et y 
        self.x_prec, self.y_prec = self.adaptateur.get_position()
        #on appelle set_vitesse
        self.adaptateur.set_vitesse(0.1, 0.0)
          
    def step(self):
        """on fait avancer le robot d'un pas et on calcule la distance"""
        # si on a fini on coupe les moteurs et on s'arrête
        if self.stop():
            self.adaptateur.set_vitesse(0.0, 0.0)
            return

        self.adaptateur.set_vitesse(0.1, 0.0)
        
        # on calcule la distance qu'on vient de parcourir sur ce pas
        x,y= self.adaptateur.get_position()
        distance_du_pas: float = math.sqrt((x - self.x_prec)**2 + (y - self.y_prec)**2)
        self.parcouru += distance_du_pas
        
        # on met à jour les coordonnées pour le prochain calcul
        self.x_prec, self.y_prec = x, y

    def stop(self):
        return self.parcouru >= self.distance


class Tourner:
    def __init__(self, adaptateur , angle_deg: float):
        self.adaptateur= adaptateur
        self.angle: float = math.radians(angle_deg)
        self.angle_parcouru: float = 0.0
        self.theta_prec: float = 0.0

    def start(self):
        """initialisation des variables"""
        self.angle_parcouru = 0.0
        self.theta_prec = self.adaptateur.get_orientation()

        #rotation sur place
        self.adaptateur.set_vitesse(0.0, 0.1)

    def step(self):
        """execute un pas de la stratégie"""
        if self.stop():
            self.adaptateur.set_vitesse(0.0, 0.0)
            return

        self.adaptateur.set_vitesse(0.0, 0.1)


        #on calcule la variation d'angle dpuis le dernier pas
        #on recupère le theta actuel 
        theta_acc: float = self.adaptateur.get_orientation()
        difftheta: float = abs( theta_acc - self.theta_prec)

        self.angle_parcouru = difftheta + self.angle_parcouru
        #maj ancien angle
        self.theta_prec = theta_acc

    def stop(self):
        """renvoie true si angle demandé atteint"""
        return self.angle_parcouru >= self.angle


class TracerCarre:
    def __init__(self, adaptateur, cote: float):
        self.adaptateur= adaptateur
        self.cote: float = cote
        self.nb_cotes: int = 0         
        self.strategie = None   #sous-strategie actuelle
        self.tourner_apres: bool = False  

    def start(self):
        """initialisation des variables"""
        self.nb_cotes = 0
        self.tourner_apres = False
        #on commence par avancer
        self.strategie = AvancerDroit(self.adaptateur, self.cote)
        self.strategie.start()  

    def step(self):
        if self.stop():
            return
        self.strategie.step()
        
        if self.strategie.stop():
            if not self.tourner_apres:
                #apres avoir avancer on tourne de 90 degres
                self.strategie = Tourner(self.adaptateur, 90)
                self.tourner_apres = True
            else:
                #sinon on incremente le nb de cotes
                self.nb_cotes += 1
                #on recommence 
                if self.nb_cotes < 4:
                    self.strategie = AvancerDroit(self.adaptateur, self.cote)
                    self.tourner_apres = False

            self.strategie.start()
            
    def stop(self):
        #on s'arrete lorsqu'on a tracé nos 4 cotes
        return self.nb_cotes >= 4


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

        

    
