import time  
from Fantastic5.strategie import AvancerDroit, TracerCarre, Tourner, Choregraphie, ApprocherLeMur
from Fantastic5 import initialisation_simulation

def main():
    
    simu = True  
    
    if simu:
        print("Mode simulation activé ")
  
        import pygame
        from Fantastic5.graphique import PygameView 

        p,r,adp= initialisation_simulation()
        view= PygameView(p,r,50)
        
        
        
    else:
        print("Mode robot réel activé ")
        # Ici on crée le vrai robot 
        # r =
        # adp = AdaptateurIRL(r)
        pass 

    
    action1 = TracerCarre(adp, 2.0)
    action2 = AvancerDroit(adp, 90)
    action3 = ApprocherLeMur(adp, distance_securite=0.5)
    
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

        if simu:      
            if not r.update(): 
                pass # Le robot a touché un mur
                
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
