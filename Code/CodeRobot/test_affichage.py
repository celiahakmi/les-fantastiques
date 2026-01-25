robot = Robot(1, 2)
plateforme = Plateforme(6, 6)

print("Position logique du robot :")
robot.afficher()

print("\nPlateforme initiale :")
plateforme.placer_robot(robot)
plateforme.afficher()

print("Déplacement en carré...\n")
robot.carre()

print("Nouvelle position logique du robot :")
robot.afficher()

print("\nPlateforme après déplacement :")
plateforme.placer_robot(robot)
plateforme.afficher()

