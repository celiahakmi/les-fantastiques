import math

class Robot: 
    def __init__(self, x : float, y : float, theta : float, 
                 L : float, larg : float, long : float):
        """ initialise le robot avec 
            - position 
            - orientation 
            - distance entre 2 roues (L)
            - forme robot (largeur/ longueur)"""
        #attribut fixe du robot
        self.x = float(x)
        self.y = float(y)
        self.theta = math.radians(theta)
        self.L = float(L)
        self.larg = float(larg)
        self.long = float(long)
        #attribut variable du robot 
        self.vL: float = 0.0
        self.vR: float = 0.0
        self.pas: float = 0.1 
    def avancer(self):
        """ fait avancer le robot, condition : vL=vR"""
        v = (self.vL + self.vR)/ 2 #calcul de la vitesse du robot
        #calcul des déplacement de x et y pendant le pas 
        delta_x = v * math.cos(self.theta) * self.pas
        delta_y = v * math.sin(self.theta) * self.pas 
        #Sauvegarde de l'ancienne position 
        ancien_x = self.x
        ancien_y = self.y
        #calcul des nouvelles positions x et y du robot
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        #if plateforme.collision_robot(self):
            #si collision, on annule le mouvement
            #self.x = ancien_x
            #self.y = ancien_y
            #on arrête les roues
            #self.vL = 0.0
            #self.vR = 0.0
            
    def tourner(self):
        """faire tourner le robot sur lui même 
            condition : les roues n'ont pas la même vitesse"""
        #calcul de la vitesse angulaire
        v_ang = ( self.vR - self.vL)/ self.L 
        #calcul et attribution du nouvel angle du robot après rotation
        self.theta = self.theta + ( v_ang * self.pas )
    def carre(self):
        nbcote = 0
        long_cote = 2
        etat = "avance"
        x0 = self.x
        y0 = self.y
        theta0 = self.theta
        angle_acc = 0.0

        while nbcote < 4:
            if etat == "avance":
                self.vL = 1.0
                self.vR = 1.0
                # distance parcourue sur le côté
                d = math.sqrt((self.x - x0)**2 + (self.y - y0)**2)
                if d < long_cote:
                    self.avancer()
                else:
                    etat = "tourner"
                    angle_acc = 0.0
                    theta0 = self.theta

            elif etat == "tourner":
                self.vL = -1.0
                self.vR = 1.0
                omega = (self.vR - self.vL) / self.L
                angle_acc += abs(omega * self.pas)
                if angle_acc < math.pi / 2:
                    self.tourner()
                else:
                    nbcote += 1
                    etat = "avance"
                    x0 = self.x
                    y0 = self.y

                    
if __name__ == "__main__":

    print("=== TESTS CLASSE ROBOT ===\n")

    # -------------------------
    # Test 1 : Initialisation
    # -------------------------
    r = Robot(x=0, y=0, theta=0, L=2, larg=1, long=2)

    print("Test 1 : Initialisation")
    print(f"x = {r.x} (attendu 0)")
    print(f"y = {r.y} (attendu 0)")
    print(f"theta = {r.theta} rad (attendu 0)")
    print(f"L = {r.L} (attendu 2)")
    print()

    # -------------------------
    # Test 2 : Avancer droit
    # -------------------------
    r.vL = 1.0
    r.vR = 1.0
    x0, y0, theta0 = r.x, r.y, r.theta

    r.avancer()

    print("Test 2 : Avancer droit")
    print(f"x a changé : {r.x != x0}")
    print(f"y inchangé : {abs(r.y - y0) < 1e-6}")
    print(f"theta inchangé : {abs(r.theta - theta0) < 1e-6}")
    print()

    # -------------------------
    # Test 3 : Tourner sur place
    # -------------------------
    r.vL = 1.0
    r.vR = -1.0
    x0, y0, theta0 = r.x, r.y, r.theta

    r.tourner()

    print("Test 3 : Tourner sur place")
    print(f"x inchangé : {abs(r.x - x0) < 1e-6}")
    print(f"y inchangé : {abs(r.y - y0) < 1e-6}")
    print(f"theta a changé : {r.theta != theta0}")
    print()

    # -------------------------
    # Test 4 : Déplacement en carré
    # -------------------------
    # Réinitialisation du robot
    r.x = 0
    r.y = 0
    r.theta = 0

    # Appel de la fonction carré
    r.carre()  # Attention : cette version complète le carré en "instantané"

    print("Test 4 : Déplacement en carré")
    print(f"x final ≈ 0 : {abs(r.x) < 1e-6}")
    print(f"y final ≈ 0 : {abs(r.y) < 1e-6}")
    print(f"theta final ≈ 0 : {abs(r.theta % (2*math.pi)) < 1e-6}")
                

            


            


        

