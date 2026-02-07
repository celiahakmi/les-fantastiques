import pygame
from plateforme0 import Plateforme
from robot0 import Robot

#l'utilisateur choisit la taille de la plateforme
lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))

if lignes <= 0 or colonnes <= 0: #vérification des dimensions
    print("Dimensions invalides")
    exit()

plateforme = Plateforme(lignes, colonnes) #création de la plateforme

#position de départ du robot
x = int(input("Position x du robot : "))
y = int(input("Position y du robot : "))

#vérification: si le robot est bien sur la grille
if not (0 <= x < colonnes and 0 <= y < lignes):
    print("Position hors plateforme")
    exit()

#on demande à l'utilisateur la vitesse de déplacement 
vitesse = int(input("À quelle vitesse voulez-vous aller ? : "))

robot = Robot(x, y, plateforme, vitesse) #création du robot

#configuration de Pygame
TAILLE = 60 #taille en pixels d'une case
LARG = colonnes * TAILLE
HAUT = lignes * TAILLE

pygame.init()
fenetre = pygame.display.set_mode((LARG, HAUT))
pygame.display.set_caption("Ma simulation de robot")
horloge = pygame.time.Clock()

#ensemble des touches qui sont actuellement appuyées
touches = set()

#fonction pour dessiner l'interface à l'écran
def dessiner():
    fenetre.fill((255, 255, 255)) #fond blanc

    #dessiner de la grille (lignes et colonnes)
    for i in range(lignes):
        for j in range(colonnes):
            case = pygame.Rect(j*TAILLE, i*TAILLE, TAILLE, TAILLE)
            pygame.draw.rect(fenetre, (0,0,0), case, 1) # Bordure noire

    #dessin des obstacles en noir
    for (ox, oy) in plateforme.obstacles:
        #on inverse le Y pour que le 0 soit en bas
        ligne_obs = plateforme.lignes - 1 - oy
        mur = pygame.Rect(ox*TAILLE, ligne_obs*TAILLE, TAILLE, TAILLE)
        pygame.draw.rect(fenetre, (0,0,0), mur)

    #dessin d'un rond représentant le robot
    y_robot = (plateforme.lignes - 1 - robot.y) * TAILLE
    robot_rond = pygame.Rect(robot.x*TAILLE + 5, y_robot + 5, TAILLE - 10, TAILLE - 10)
    pygame.draw.ellipse(fenetre, (255,0,0), robot_rond)

    pygame.display.flip() #mis à jour de l'écran

#boucle principale 
marche = True
while marche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            marche = False 

        elif event.type == pygame.KEYDOWN:
            touches.add(event.key)
            #si on appuie sur Espace le robot fait un carré
            if event.key == pygame.K_SPACE:
                actions = [robot.droite, robot.bas, robot.gauche, robot.haut]
                for bouger in actions:
                    bouger()     #le robot bouge
                    dessiner()   #on redesine tout de suite
                    pygame.time.delay(400) #petite pause pour voir chaque mouvement

        elif event.type == pygame.KEYUP:
            if event.key in touches:
                touches.remove(event.key)

    #Déplacements avec les flèches du clavier
    if pygame.K_UP in touches:
        robot.haut()
    if pygame.K_DOWN in touches:
        robot.bas()
    if pygame.K_LEFT in touches:
        robot.gauche()
    if pygame.K_RIGHT in touches:
        robot.droite()

    #Déplacements pour les diagonales à l'aide des touches a,z,q,s
    if pygame.K_a in touches:
        robot.diag_haut_gauche()
        
    if pygame.K_z in touches:
        robot.diag_haut_droite()
        
    if pygame.K_q in touches:
        robot.diag_bas_gauche()
        
    if pygame.K_s in touches:
        robot.diag_bas_droite()
        


#raffraichit l'écran
    dessiner()
    horloge.tick(10) #vitesse de la boucle

pygame.quit() #fin de pygame

