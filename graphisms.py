from turtle import *
from board import posDisque_edited

# CONSTANTS
BACKGROUND_COLOR = "AntiqueWhite"
EPAISSEUR_DISQUE = 20
DISC_COLORS = ["aquamarine", "blue2", "BlueViolet", "brown1", "CadetBlue2", "chartreuse2", "chocolate1", "coral2", "CornflowerBlue", "DeepPink", "DarkOrchid"]


def init():
    clearscreen()
    mainloop()


def diametre_disque(disque_n: int):    #disque_n: numéro du disque de 1 à n
    return 40 + (disque_n-1)*30


def dessineTour(n: int, plateau, nTour: int):
    hauteur_tour = (n+1)*20
    epaisseur_tour = 6
    up()
    goto(-300+20*nTour+diametre_disque(n)*(nTour-1)+diametre_disque(n)/2-3, -180)
    down()
    pencolor('burlywood4')
    fillcolor('burlywood4')
    begin_fill()
    for i in range(2):
        forward(epaisseur_tour)
        left(90)
        forward(hauteur_tour)
        left(90)
    end_fill()
    pencolor('black')


def dessinePlateau(n: int, plateau: list[list[int] | list]):
    longueur_plateau = diametre_disque(n)*3 + 20*4
    hauteur_plateau = 20
    #tracé du plateau
    up()
    goto(-300, -201)
    down()
    pencolor('burlywood4')
    fillcolor('burlywood4')
    begin_fill()
    for i in range(2):
        forward(longueur_plateau)
        left(90)
        forward(hauteur_plateau)
        left(90)
    end_fill()
    pencolor('black')
    #tracé des tours
    for i in range(1, 4):
        dessineTour(n, plateau, i)
    up()


def dessineDisque(nd: int, plateau: list[list[int] | list], n: int, fill_color: str = None):
    """
    :param nd: Numero du disque à dessiner
    :param plateau: L'état actuel du plateau
    :param n: Nombre de disques dans le plateau
    """
    if fill_color is None:
        fill_color = DISC_COLORS[nd]

    position = posDisque_edited(plateau, nd)   # Contient la tour à l'index 0, et la position dans la tour à l'index 1
    longueur_disque = diametre_disque(nd)
    # Tracé du disque
    up()
    goto(-300+20*(position[0]+1)+diametre_disque(n)*(position[0])+(diametre_disque(n)-diametre_disque(nd))/2, -200+EPAISSEUR_DISQUE*(position[1]+1))
    down()
    pencolor(fill_color)
    fillcolor(fill_color)
    begin_fill()
    for i in range(2):
        forward(longueur_disque)
        left(90)
        forward(EPAISSEUR_DISQUE)
        left(90)
    end_fill()
    up()


def effaceDisque(nd: int, plateau: list[list[int] | list], n: int):
    """
    :param nd: Numero du disque à effacer
    :param plateau: L'état actuel du plateau
    :param n: Nombre de disques dans le plateau
    """

    # Suppresion du disque
    dessineDisque(nd, plateau, n, BACKGROUND_COLOR)

    # Retraçage de la tour
    (n_tour, pos_tour) = posDisque_edited(plateau, nd)
    dessineTour(n, plateau, n_tour+1)

    # On redessine les disques restants sur la tour pour éviter que la tour "passe devant" eux
    for n_disque in range(0, len(plateau[n_tour]) - 1):
        disc = plateau[n_tour][n_disque]
        dessineDisque(disc, plateau, n)


def dessineConfig(plateau: list[list[int] | list], n: int):
    for nd in range(n, 0, -1):
        dessineDisque(nd, plateau, n, DISC_COLORS[nd])


def effaceTout(plateau: list[list[int] | list], n: int):
    for tour in range(len(plateau)):
        for disque in plateau[tour]:
            effaceDisque(disque, plateau, n)


def resetPlateau(nouveauPlateau: list[list[int] | list], n:int):
    clearscreen()
    speed("fastest")
    bgcolor(BACKGROUND_COLOR)
    dessinePlateau(n, nouveauPlateau)
    dessineConfig(nouveauPlateau, n)


if __name__ == "__main__":
    plateau = [[5, 4, 3, 2, 1], [], []]
    speed("fastest")
    bgcolor(BACKGROUND_COLOR)
    dessinePlateau(5, plateau)
    dessineConfig(plateau, 5)
    effaceDisque(1, [[5, 4, 3, 2, 1], [], []], 5)
    dessineDisque(1, [[5, 4, 3, 2], [], [1]], 5)
    effaceDisque(2, [[5, 4, 3, 2], [], [1]], 5)
    dessineDisque(2, [[5, 4, 3], [2], [1]], 5)
    exitonclick()
