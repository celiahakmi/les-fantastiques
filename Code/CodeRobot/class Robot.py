class Robot: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def haut(self): 
        if self.x != 0 :
            self.x = self.x - 1 
        else: 
            print("Le robot rencontre un mur")
    def bas(self): 
        if self.x != 5:
            self.x = self.x + 1 
        else: 
            print("Le robot rencontre un mur")
    def droite(self):
        if self.y != 5: 
            self.y = self.y + 1 
        else:
            print("Le robot rencontre un mur")
    def gauche(self): 
        if self.y != 0: 
            self.y = self.y - 1 
        else: 
            print("Le robot rencontre un mur")
    def carre(self): 
        self.droite()
        self.bas()
        self.gauche()
        self.haut()
    def afficher(self):
        print(f"x : {self.x}, y = {self.y}")

RobotTest = Robot(2,2)
RobotTest.afficher()
RobotTest.carre() 
RobotTest.afficher()
