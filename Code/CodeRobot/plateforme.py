class Plateforme:
    def __init__(self, longueur: float, hauteur: float):
        self.longueur = longueur #affilié à x
        self.hauteur = hauteur #affilié à y
        self.obstacles = []

    
    def init_obstacle(self, x: float, y:float, h: float, l: float):
        """Construire un rectancle où le sommet bas-gauche est de coordonées x,y, de hauteur h et de largeur l"""
        if self.est_valide(x, y, l, h):
            self.obstacles.append(("rect", float(x), float(y), float(h), float(l)))

    
    def est_valide(self, x: float, y: float, l: float, h: float):
        """Renvoie True si l'obstacle est valide """
        if x < 0 or y < 0 or (x+l) > self.longueur or (y+h) > self.hauteur:
            return False
        
        for obs in self.obstacles:
            _, ox, oy, oh, ol = obs 
            
            if (x < ox + ol and x + l > ox and
                y < oy + oh and y + h > oy):
                return False 
                
        return True


#Tests
if __name__ == "__main__":
    #Initialisation
    p = Plateforme(10, 10)
    print("Test 1: Création plateforme 10x10 : OK")

    #Test ajout valide
    res1 = p.init_obstacle(5, 5, 1, 1)
    print(f"Test 2: Ajout obstacle (5, 5, 1, 1) valide : {res1 == True}")
    print(f"Nombre d'obstacles : {len(p.obstacles)}")

    #Test dépassement bordure (x + l > longueur)
    res2 = p.init_obstacle(0, 10, 5, 10)
    print(f"Test 3: Erreur dépassement bordure : {res2 == False}")

    # 4. Test chevauchement (sur l'obstacle du Test 2)
    res3 = p.init_obstacle(4, 4, 10, 10) # Chevauche le premier
    print(f"Test 4: Erreur chevauchement : {res3 == False}")
    
    # Vérification finale du nombre d'obstacles (devrait être 1)
    print(f"Total obstacles final : {len(p.obstacles)}")
