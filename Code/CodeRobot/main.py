import pygame
from class_plateforme import Plateforme
from class_robot import Robot

#l'utilisateur peut entrer le nb de lignes et colonnes qu'il souhaite
lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))

if lignes <= 0 or colonnes <= 0:
    print("Dimensions invalides")
    exit()

plateforme = Plateforme(lignes, colonnes)

#  Position de départ du robot
x = int(input("Position x du robot : "))
y = int(input("Position y du robot : "))

#  si le robot est bien sur la grille
if not (0 <= x < colonnes and 0 <= y < lignes):
    print("Position hors plateforme")
    exit()

#on demande à l'utilisateur la vitesse de déplacement 
vitesse = int(input("À quelle vitesse voulez-vous aller ? : "))

robot = Robot(x, y, plateforme, vitesse) #création du robot

# Config de Pygame 
TAILLE = 60 # Taille d'une case en pixels
LARG = colonnes * TAILLE
HAUT = lignes * TAILLE

pygame.init()
fenetre = pygame.display.set_mode((LARG, HAUT))
pygame.display.set_caption("Ma simulation de robot")
horloge = pygame.time.Clock()

# Liste des touches sont appuyées
touches = set()

# dessiner l'interface 
def dessiner():
    fenetre.fill((255, 255, 255))  # Fond blanc

    # Dessiner la grille (lignes et colonnes)
    for i in range(lignes):
        for j in range(colonnes):
            case = pygame.Rect(j*TAILLE, i*TAILLE, TAILLE, TAILLE)
            pygame.draw.rect(fenetre, (0,0,0), case, 1) # Bordure noire

    # Dessiner les obstacles en noir
    for (ox, oy) in plateforme.obstacles:
        # On inverse le Y pour que le 0 soit en bas
        ligne_obs = plateforme.lignes - 1 - oy
        mur = pygame.Rect(ox*TAILLE, ligne_obs*TAILLE, TAILLE, TAILLE)
        pygame.draw.rect(fenetre, (0,0,0), mur)

    # Dessiner un rond qui represente le robot 
    y_robot = (plateforme.lignes - 1 - robot.y) * TAILLE
    robot_rond = pygame.Rect(robot.x*TAILLE + 5, y_robot + 5, TAILLE - 10, TAILLE - 10)
    pygame.draw.ellipse(fenetre, (255,0,0), robot_rond)

    pygame.display.flip() # Mettre à jour l'image

#  Boucle principale 
marche = True
while marche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            marche = False 

        elif event.type == pygame.KEYDOWN:
            touches.add(event.key)
            # Si on appuie sur Espace on fait le carré
            if event.key == pygame.K_SPACE:
                actions = [robot.droite, robot.bas, robot.gauche, robot.haut]
                for bouger in actions:
                    bouger()     # Le robot bouge
                    dessiner()   # On redessine tout de suite
                    pygame.time.delay(400) # Petite pause pour voir le mouvement

        elif event.type == pygame.KEYUP:
            if event.key in touches:
                touches.remove(event.key)

#Déplacements continus avec les flèches du clavier
    if pygame.K_UP in touches:
        robot.haut()
    if pygame.K_DOWN in touches:
        robot.bas()
    if pygame.K_LEFT in touches:
        robot.gauche()
    if pygame.K_RIGHT in touches:
        robot.droite()

    #Déplacements pour les diagonales
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

pygame.quit() #fin 

