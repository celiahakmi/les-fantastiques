import time  
from Fantastic5 import initialisation_simulation 
from Fantastic5.graphique.affichage3d import Vue3D
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner,Arreter, Accelerer, Choregraphie, Condition, Boucle

def main():

    simu = True  

    if simu:
        print("mode  3D activé ")
        from Fantastic5.graphique import Vue3D 

        p, r = initialisation_simulation() 

        #  initialise la vue 3D
        view = Vue3D(p, r)
        adp = AdaptateurSimu(r)

    else:
        print("Mode robot réel activé ")
        # Ici on crée le vrai robot 
        # r =
        # adp = AdaptateurIRL(r)
        pass 

    action1 = Choregraphie(adp, [AvancerDroit(adp, 2), Tourner(adp, 90), AvancerDroit(adp, 2), Tourner(adp, 90), AvancerDroit(adp, 2), Tourner(adp, 90), AvancerDroit(adp, 2), Tourner(adp, 90), AvancerDroit(adp, 2), Tourner(adp, 90)])
    action2 = Condition(adp, Accelerer(adp, 20.0, 0.5, 0.01), Arreter(adp), 1.0)
    strat_globale = Choregraphie(adp, [action1, action2])

    strat_globale.start()

    running = True


    while running:
        if not strat_globale.stop():
            strat_globale.step()
        else:
            adp.set_vitesse(0.0, 0.0) 
            if not simu:
                running = False 

        # on met à jour la physique et la 3D
        if simu:      
            # Le robot calcule sa nouvelle position
            if not r.update(): 
                print("Collision ou arrêt ")
                running = False 

            view.dessiner() 

        time.sleep(0.01)

    if simu:
        import pygame
        pygame.quit()

if __name__ == "__main__":
    main()
