from plateforme import Plateforme
from robot import Robot

def main():
    
    plateforme = Plateforme(10, 10)
    plateforme.init_obstacle(2, 2, 2, 1)
    plateforme.init_obstacle(5, 5, 1, 1)

    robot = Robot(1, 1, 0, L=0.5, larg=0.5, long=0.7)
      view = PygameView(p, r, TAILLE_PIXEL=50)

    nbcote = 0
    long_cote = 2
    etat = "avance"
    x0 = r.x
    y0 = r.y
    angle_acc = 0.0

    running = True

    while running:
        view.horloge.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if nbcote < 4:

            if etat == "avance":
                r.vL = 1.0
                r.vR = 1.0

                d = math.sqrt((r.x - x0)**2 + (r.y - y0)**2)

                if d < long_cote:
                    r.avancer()
                else:
                    etat = "tourner"
                    angle_acc = 0.0

            elif etat == "tourner":
                r.vL = -1.0
                r.vR = 1.0

                angle = (r.vR - r.vL) / r.L
                angle_acc += abs(angle * r.pas)

                if angle_acc < math.pi / 2:
                    r.tourner()
                else:
                    nbcote += 1
                    etat = "avance"
                    x0 = r.x
                    y0 = r.y

        else:
            r.vL = 0
            r.vR = 0

        view.dessiner()

    pygame.quit()


if __name__ == "__main__":
    main()
