class Robot: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def haut(self, x): 
        if self.x != 0 :
            self.x = self.x - 1 
        else: 
            print("Le robot rencontre un mur")
    def bas(self, x): 
        if self.x != 5:
            self.x = self.x + 1 
        else: 
            print("Le robot rencontre un mur")
    def droite(self, y):
        if self.y != 5: 
            self.y = self.y + 1 
        else:
            print("Le robot rencontre un mur")
    def gauche(self, y): 
        if self.y != 0: 
            self.y = self.y - 1 
        else: 
            print("Le robot rencontre un mur")