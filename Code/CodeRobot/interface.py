import tkinter as tk
from class_plateforme import Plateforme
from Robot import Robot

#taille en pixels de chaque case de la grille 
TAILLE_CASE = 40

class InterfacePlateforme:
    def __init__(self, root, plateforme, robot):
        self.root = root
        self.plateforme = plateforme
        self.robot = robot

        #zone de dessin:
        self.canvas = tk.Canvas(
            root, width=plateforme.colonnes * TAILLE_CASE, height=plateforme.lignes * TAILLE_CASE, bg="white"
        )
        #marge de 10 pixels
        self.canvas.pack(pady=10)

        #bouton "Déplacement en carré" quand on clique le robot fait un carré 
        self.btn_carre = tk.Button(
            root, text="Déplacement en carré", command=self.deplacement_carre
        )
        self.btn_carre.pack()

        self.dessiner_plateforme()

    def dessiner_plateforme(self):
        self.canvas.delete("all")
       
        #Dessine un rectangle noir pour chaque case
        for i in range(self.plateforme.lignes):
            for j in range(self.plateforme.colonnes):
                x1 = j * TAILLE_CASE
                y1 = i * TAILLE_CASE
                x2 = x1 + TAILLE_CASE
                y2 = y1 + TAILLE_CASE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="white")

        #Dessine un cercle rouge oval dans la case du robot avec une marge pour qu'elle touche pas les bords
        rx1 = self.robot.y * TAILLE_CASE
        ry1 = self.robot.x * TAILLE_CASE
        rx2 = rx1 + TAILLE_CASE
        ry2 = ry1 + TAILLE_CASE
        self.canvas.create_oval(rx1+5, ry1+5, rx2-5, ry2-5, fill="red")

    def deplacement_carre(self):
        self.robot.droite()
        self.dessiner_plateforme()
        self.root.after(500, self.bas)

    def bas(self):
        self.robot.bas()
        self.dessiner_plateforme()
        self.root.after(500, self.gauche)

    def gauche(self):
        self.robot.gauche()
        self.dessiner_plateforme()
        self.root.after(500, self.haut)

    def haut(self):
        self.robot.haut()
        self.dessiner_plateforme()




