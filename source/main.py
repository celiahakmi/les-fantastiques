import time  
from Fantastic5 import initialisation_simulation 
from Fantastic5.API import Robot2IN013
from Fantastic5.adaptateur import AdaptateurSimu, AdaptateurIRL
from Fantastic5.strategie import AvancerDroit, Tourner, Arreter, Accelerer, Choregraphie, Condition

def main():

    simu = False

    if simu:
        print("Mode simulation activé")
        _, r, _ = initialisation_simulation()
        adp = AdaptateurSimu(r)
    else:
        print("Mode robot réel activé")
        r2 = Robot2IN013(nb_img=5, fps=25)
        adp = AdaptateurIRL(r2)

    # Définition de la stratégie globale
    action1 = Choregraphie(adp, [
        AvancerDroit(adp, 2), Tourner(adp, 90),
        AvancerDroit(adp, 2), Tourner(adp, 90),
        AvancerDroit(adp, 2), Tourner(adp, 90),
        AvancerDroit(adp, 2), Tourner(adp, 90)
    ])
    
    action2 = Condition(adp, Accelerer(adp, 20.0, 0.5, 0.01), Arreter(adp), 1.0)
    
    strat_globale = Choregraphie(adp, [action1, action2])

    strat_globale.start()

    running = True

    while running:
        if not strat_globale.stop():
            strat_globale.step()
        else:
            adp.set_vitesse(0.0, 0.0)
            running = False

        # Mise à jour simulation si nécessaire
        if simu:
            if not r.update():
                print("Collision ou arrêt détecté dans la simulation")
                running = False

        time.sleep(0.01)

    # Arrêt du robot réel
    if not simu:
        adp.set_vitesse(0.0, 0.0)

if __name__ == "__main__":
    main()
