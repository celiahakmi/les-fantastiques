import pygame
import math
from robot import Robot
from plateforme2 import Plateforme
from affichage import PygameView


def main():

    p = Plateforme(10, 10)
    p.init_obstacle(5, 5, 2, 2)
    p.init_obstacle(1, 1, 1, 2)
    

    r = Robot(6, 7, 0, 1.0, 0.8, 1.2,plateforme=p)
    
    view = PygameView(p, r, TAILLE_PIXEL=50)

   
if __name__ == "__main__":
    main()
