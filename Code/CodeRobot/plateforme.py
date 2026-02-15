from robot import Robot

class Plateforme:
    def __init__(self, taille):
        self.taille = taille
        self.obstacles = [] 
   
    def ajouter_rectangle(self, x, y, w, h):
        self.obstacles.append(("rect", float(x), float(y), float(w), float(h)))


    def collision_rectangle(self, x, y, w, h):
        # bords
        if x < 0 or y < 0 or x + w > self.taille or y + h > self.taille:
            return True

        # obstacles
        for _, ox, oy, ow, oh in self.obstacles:
            if (x < ox + ow and x + w > ox and
                y < oy + oh and y + h > oy):
                return True
        return False

        
