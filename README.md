# les-fantastiques

Dans notre dossier se trouvent :

- Le fichier principal :
    - main.py : le programme principal qui lance la simulation ou le robot réel

- Les modules du projet (dossier Fantastic5) :
    - adaptateur :
        - adaptateur.py : classe abstraite de base
        - adaptateurSimu.py : gestion du robot en simulation
        - adaptateurIRL.py : gestion du robot réel
    - strategie :
        - strategie.py : contient toutes les stratégies (Avancer, Tourner, Chorégraphie, Condition…)
    - simulation.py :
        - initialise la plateforme et le robot simulé
    - graphique :
        - affichage du robot avec pygame
    - API :
        - robotAPI.py : interface avec le robot réel (capteurs, moteurs, etc.)

- Les classes principales :
    - Plateforme : gestion du terrain et des obstacles
    - Robot : simulation du robot (position, mouvement, collisions)

- Les dépendances :
    - pygame (affichage)
    - math, time (calculs)
    - easygopigo3 (robot réel uniquement)

A savoir :

- Le fichier main.py permet de choisir entre :
    - mode simulation (simu = True)
    - mode robot réel (simu = False)

- Le robot fonctionne avec un système de stratégies :
    - AvancerDroit : avance sur une distance
    - Tourner : rotation
    - Choregraphie : enchaînement d’actions
    - Condition : permet de changer de comportement selon une condition (ex : obstacle)

- La détection d’obstacle utilise :
    - get_distance() en simulation (calcul géométrique)
    - capteur ultrason sur robot réel

- Si le robot touche un mur :
    - la fonction collision_robot annule le mouvement
    - et le robot s’arrête automatiquement

- La vitesse de la boucle principale est importante :
    - une valeur trop faible de time.sleep peut bloquer ou perturber le robot
    - valeur conseillée : time.sleep(0.01)

- En cas de problème d’import :
    - lancer le programme depuis le dossier "source"
    - vérifier la structure du projet et les noms des dossiers (respect de la casse)





