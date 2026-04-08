from .simulation import Plateforme, Robot
__all__ = ["Plateforme", "Robot"]

#question 1.1
def simulation_trois_obstacles():
    p=Plateforme(10.0,10.0) #plateforme
    p.init_obstacle(6.0,1.0,1.0,1.0)#bas
    p.init_obstacle(6.0,5.0,1.0,1.0)#centre
    p.init_obstacle(6.0,8.0,1.0,1.0)#haut
    r=Robot(1.0,1.0,0.0,0.5,0.5,0.7,p) #robot coin inférieur gauche
    r2=Robot(9.0, 5.0, 0.0, 0.5, 0.5, 0.7, p)
    return p,r,r2




