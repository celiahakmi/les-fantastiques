import time  
from Fantastic5 import initialisation_simulation 
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner,Arreter, Accelerer, Choregraphie, Condition, Boucle

def main():

    simu = True  

    if simu:
        print("Mode simulation activé ")

        import pygame
        from Fantastic5.graphique import PygameView 

        #le monde virtuel
        #q2.1
        p, r1,r2 = initialisation_simulation() 

        view = PygameView(p, r1,r2, 50)
        adp = AdaptateurSimu(r1)
        adp2 = AdaptateurSimu(r2)

    else:
        print("Mode robot réel activé ")
        # Ici on crée le vrai robot 
        # r =
        # adp = AdaptateurIRL(r)
        pass 

    def condition_distance(adaptateur):
        return adaptateur.get_distance() > 1.0
    
    strat_globale = Choregraphie(adp, [AvancerDroit(adp, 2), Tourner(adp, 90), AvancerDroit(adp, 2), Tourner(adp, 90), AvancerDroit(adp, 2), Tourner(adp, 90), AvancerDroit(adp, 2), Tourner(adp, 90), AvancerDroit(adp, 2), Tourner(adp, 90)])
    #pour q2.2 action2 = Condition(adp,condition_distance,Accelerer(adp, 20.0, 0.5, 0.01),Arreter(adp))
    #strat_globale = Choregraphie(adp, [action1, action2])
    strat_globale.start()

    action= Choregraphie(adp2, [AvancerDroit(adp2, 2),Tourner(adp2, 180),AvancerDroit(adp2, 2)])
    action.start()
   


    #q1.5
    #strat_hexa=Tracerhexagone(adp,3)
    #strat_hexa.start()
    #strat_hexa.step()

    # on peut utiliser la stratégie boucle ici en modifiant aussi le while running :
    #action1 = Choregraphie(adp, [AvancerDroit(adp, 2), Tourner(adp, 90)])
    #nbRepet = 4
    #boucle_action = Boucle(adp, action1, n_repetitions=4)
    #boucle_action.start()
    
    running = True

    while running:

        if not strat_globale.stop():
            strat_globale.step() 
        else:
            adp.set_vitesse(0.0, 0.0) 
            if not simu:
                running = False 

        if  not action.stop():
            action.step()
        else:
            adp2.set_vitesse(0.0, 0.0) 
            if not simu:
                running = False 



        if simu:      
            if not r1.update() or r2.update(): 
                pass # Le robot a touché un mur

            view.dessiner()

            # fermer la fenêtre 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        time.sleep(0.001)
        time.sleep(0.01)

    if simu:
        import pygame
        pygame.quit()

if __name__ == "__main__":
    main()
