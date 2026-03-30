import time  
from Fantastic5 import initialisation_simulation 
from Fantastic5.simulation import Plateforme, Robot
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner, Choregraphie

def main():

    simu = True  

    if simu:
        print("Mode simulation activé ")

        import pygame
        from Fantastic5.graphique import PygameView 

        #le monde virtuel
        p, r = initialisation_simulation() 

        view = PygameView(p, r, 50)
        adp = AdaptateurSimu(r)

    else:
        print("Mode robot réel activé ")
        # Ici on crée le vrai robot 
        # r =
        # adp = AdaptateurIRL(r)
        pass 

    parcours = [] 
    #carre
    #boucle pour remplir la liste avec les 4 côtés
    for i in range(4):
        parcours.append(AvancerDroit(adp, 2.0)) 
        parcours.append(Tourner(adp, 90))       
        
    #après le carre on fonce vers le mur et on s'arrête à 1m
    parcours.append(ApprocherLeMur(adp, 1))
    
    strat_globale = Choregraphie(adp, parcours)
    strat_globale.start()


    running = True

    while running:

        if not strat_globale.stop():
            strat_globale.step()
        else:
            adp.set_vitesse(0.0, 0.0) 
            if not simu:
                running = False 

        if simu:      
            if not r.update(): 
                print("Arrêt de la simulation (collision)")
                running = False # Le robot a touché un mur/obstacle

            view.dessiner()

            # fermer la fenêtre 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        time.sleep(0.01)

    if simu:
        import pygame
        pygame.quit()

if __name__ == "__main__":
    main()
