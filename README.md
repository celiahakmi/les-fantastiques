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



