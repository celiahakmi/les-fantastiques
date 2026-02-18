import math

class Plateforme:
    def __init__(self, taille: float):
        """initialise le plan continu"""
        self.taille = float(taille)
        self.obstacles = []  

    def ajouter_rectangle(self, x: float, y:float, w:float , h:float):
        """ajoute un obstacle rectangulaire"""
        self.obstacles.append(("rect", float(x), float(y), float(w), float(h)))
   
    def collision_rectangle(self, x: float, y:float, w:float , h:float):
        """vérifie si un rectangle est en collision avec un mur ou un obstacle"""
        # bords
        if x < 0 or y < 0 or x + w > self.taille or y + h > self.taille:
            return True

        # obstacles
        for _, ox, oy, ow, oh in self.obstacles:
            if (x < ox + ow and x + w > ox and
                y < oy + oh and y + h > oy):
                return True
        return False

    # Capteur distance 
    def distance_jusqua_obstacle(self, x:float, y:float, angle:float , max_range: float =10.0,step: float =0.02,marge: float =0.0):
        """ retourne la distance jusqu'au premier obstacle ou mur detecté"""
        d = 0.0
        while d <= max_range:
            px = x + d * math.cos(angle)
            py = y + d * math.sin(angle)

            # bords avec marge
            if px < marge or py < marge or px > self.taille - marge or py > self.taille - marge:
                return d
                
            # obstacles avec marge
            for _, ox, oy, ow, oh in self.obstacles:
                if (ox - marge) <= px <= (ox + ow + marge) and (oy - marge) <= py <= (oy + oh + marge):
                    return d

            d += step

        return max_range
