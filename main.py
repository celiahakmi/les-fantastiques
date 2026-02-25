
import pygame
import math
from robot.plateforme import Plateforme
from robot import Robot
from robot.affichage import PygameView

def main():
    
    p = Plateforme(10, 10)
    p.init_obstacle(7, 6, 2, 1)
    p.init_obstacle(5, 5, 1, 1)

    r = Robot(5, 2, 0, 0.5, 0.5, 0.7, p)
    view = PygameView(p, r, 50)

    nbcote = 0
    long_cote = 2
    etat = "avance"
    x0 = r.x
    y0 = r.y
    angle_acc = 0.0

    chemin = [(8, 1), (8, 8), (2, 8)]
    idx_p = 0 #index du point courant
    etat="avance"
    
    running = True

    while running:
        view.horloge.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
#carré
        if etat == "avance":
            r.vL = 0.2
            r.vR = 0.2
            d = math.sqrt((r.x - x0)**2 + (r.y - y0)**2)
            if d < long_cote:
                p.deplacer_si_possible(r, r.avancer)
            else:
                etat = "tourner"
                angle_acc = 0.0

        elif etat == "tourner":
            r.vL = 0
            r.vR = 0.1
            p.deplacer_si_possible(r, r.tourner)
            angle = (r.vR - r.vL) / r.L
            angle_acc += abs(angle * r.pas)

            if angle_acc>= math.pi / 2:
                nbcote+=1
                if nbcote<4:
                    etat="avance"
                    x0 = r.x
                    y0 = r.y
                    angle_acc=0.0
                else:
                    etat="chemin"


        else:
            etat="chemin" 

        #chemin
        taille_chemin= len(chemin)

        if etat=="chemin" and idx_p<taille_chemin:
            tx,ty=chemin[idx_p]
            dx=tx-r.x
            dy=ty-r.y
            distance=math.sqrt(dx**2+dy**2)

            if distance<0.1:
                idx_p+=1
                r.vL=0
                r.vR=0

            else: #angle vers le point
                angle_cible=math.atan2(dy,dx) 
                erreur=angle_cible-r.theta
                erreur=(erreur +math.pi)%(2*math.pi)-math.pi

                if abs(erreur)>0.1:
                    r.vL= 0
                    r.vR=0.1
                    if not p.deplacer_si_possible(r, r.tourner):
                        r.vL=0
                        r.vR=0
                else:
                    r.vL=0.1
                    r.vR=0.1
                    if not p.deplacer_si_possible(r, r.avancer):
                        r.vL=0
                        r.vR=0
        
            
        view.dessiner()

    pygame.quit()


if __name__ == "__main__":
    main()
