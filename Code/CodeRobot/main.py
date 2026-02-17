import pygame
import math
from plateforme import Plateforme
from robot import Robot
from affichage import PygameView


def main():
    pygame.init()

    plateforme = Plateforme(20)
    #obstacles
    plateforme.ajouter_rectangle(2, 2, 3, 7)
    plateforme.ajouter_rectangle(8, 14, 6, 2)
    
    #paramètre initiaux 
    x = float(input("Position x : "))
    y = float(input("Position y : "))
    angle = float(input("Angle (degrés) : "))
    
    robot = Robot(
        x=x,
        y=y,
        theta_deg=angle,
        width=2.0,
        height=1.2,
        wheel_base=2.0,
        plateforme=plateforme
    )

    view = PygameView(plateforme, robot, 40)

    longueur_cote= 1.5
    base_speed = 2
    turn_speed = 1

    etat = "avance" 
    cote_compte = 0

    x_start = robot.x
    y_start = robot.y 
    angle_accumule = 0.0

    # Chemin prédéfini
    chemin = [(15, 5), (15, 15), (0, 0)]
    idx_p = 0
    
    running = True
    while running:
        dt = view.horloge.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        vL, vR = 0.0, 0.0

        if etat == "avance":
            #distance parcourue depuis le début du coté
            distance = math.sqrt( (robot.x - x_start)**2 + (robot.y - y_start)**2) #distance entre deux points
            if distance < longueur_cote: 
                #Avancer tout droit 
                vL = base_speed
                vR = base_speed
            else: 
                #Fin du côté -> début de la rotation du robot 
                etat = "tourne" 
                angle_accumule = 0.0 
                
        elif etat == "tourne":
                omega = (2* turn_speed) / robot.L
                #calcul de l'angle déjà tourné pendant la rotation
                if angle_accumule < (math.pi / 2): #90 degrés
                    #rotation sur place
                    vL = -turn_speed #roue gauche en arrière
                    vR = turn_speed # roue droite en avant
                    angle_accumule += abs(omega * dt)
                else : 
                    #fin de la rotation 
                    cote_compte +=1 
                    if cote_compte < 4:
                        etat = "avance"
                        x_start = robot.x 
                        y_start = robot.y
                    else:
                        etat = "chemin"
        #chemin 
        elif etat == "chemin" and idx_p < len(chemin):
            tx, ty = chemin[idx_p]
            dx = tx - robot.x
            dy = ty - robot.y
            dist = math.sqrt(dx**2 + dy**2)
            if dist < 0.5: 
                idx_p += 1
            else:
                err = math.atan2(dy, dx) - robot.theta
                err = (err + math.pi) % (2 * math.pi) - math.pi 
                vL = 2.0 - err * 3
                vR = 2.0 + err * 3

        # Réaction face aux obstacles
        if robot.reaction_obstacle(distance_seuil=1.5) == "rien":
            robot.set_wheel_targets(vL, vR)
            
        #Mise à jour du robot
        robot.set_wheel_targets(vL, vR)
        robot.step(dt)

        view.dessiner()

    pygame.quit()


if __name__ == "__main__":
    main()





