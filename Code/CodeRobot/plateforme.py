from robot import Robot

class Plateforme:
    def __init__(self, taille):
        self.taille = taille
        self.obstacles = [] 
        
    def ajouter_cercle(self, x, y, rayon):
        self.obstacles.append(("cercle", x, y, rayon))

    def ajouter_carre(self, x, y, cote):
        self.obstacles.append(("carre", x, y, cote))

    def ajouter_triangle(self, x, y, cote):
        self.obstacles.append(("triangle", x, y, cote))

    def verifier_position(self, x, y, largeur, hauteur):
        #Vérification des bords 
        if x < 0 or y < 0 or x + largeur > self.taille or y + hauteur > self.taille:
            return False

        for obs in self.obstacles:
            type_obs = obs[0]

            # collision cercle 
            if type_obs == "cercle":
                _, ox, oy, r = obs
                # Trouver le point sur le rectangle le plus proche du centre du cercle
                proche_x = max(x, min(ox, x + largeur))
                proche_y = max(y, min(oy, y + hauteur))
                
                # Calculer la distance entre ce point et le centre
                dist_x = ox - proche_x
                dist_y = oy - proche_y
                if (dist_x**2 + dist_y**2) < r**2: 
                    return False

            #  collision carré triangle 
            elif type_obs in ["carre", "triangle"]:
                _, ox, oy, c = obs
                # Vérifier si deux rectangles se touchent
                if (x < ox + c and x + largeur > ox and 
                    y < oy + c and y + hauteur > oy):
                    return False

        return True

