import time  
from Fantastic5 import initialisation_simulation, inititialisation_simulation_tmesolo, inititialisation_simulation_q2_1
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner,Arreter, Accelerer, Choregraphie, Condition, Boucle

def main():

    simu = True  

    if simu:
        print("Mode simulation activé ")

        import pygame
        from Fantastic5.graphique import PygameView 

        #le monde virtuel
        p, r1, r2, = inititialisation_simulation_q2_1() 
        

        view = PygameView(p, r1, r2, 50)
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
    action1 = Choregraphie(adp2, [AvancerDroit(adp2, 2), Tourner(adp2, 90), AvancerDroit(adp2, 2), Tourner(adp2, 90), AvancerDroit(adp2, 2), Tourner(adp2, 90), AvancerDroit(adp2, 2), Tourner(adp2, 90), AvancerDroit(adp2, 2), Tourner(adp2, 90)])
    action2 = Choregraphie(adp,[Tourner(adp, 270),AvancerDroit(adp, 4), Tourner(adp, 180), AvancerDroit(adp, 4)])
    
    action1.start()
    action2.start()

    running = True

    while running:
        if not action1.stop() :
            action1.step()
            

        else:
            adp2.set_vitesse(0.0, 0.0) 
            if not simu:
                running = False 
        if not action2.stop():
            action2.step()

        else : 
            adp.set_vitesse(0.0,0.0)
            if not simu:
                running = False
        if simu:      
            if not r2.update() or r1.update(): 
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
