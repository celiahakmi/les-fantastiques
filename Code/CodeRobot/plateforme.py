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
