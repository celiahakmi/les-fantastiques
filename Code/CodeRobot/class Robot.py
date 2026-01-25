class Robot: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def haut(self, x, y): 
        if self.x != 0 :
            self.x = self.x - 1 
        else: 
            print("Le robot rencontre un mur")
            