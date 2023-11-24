from turtle import *
from board import posDisque_edited
from time import sleep

# CONSTANTS
BACKGROUND_COLOR = "AntiqueWhite"
DISC_COLOR = "black"
EPAISSEUR_DISQUE = 20


def init(plateau: list[list[int] | list], n: int):
    """
    :param n: Le nombre de disques
    :return: None
    """
    speed(10)
    bgcolor(BACKGROUND_COLOR)
    dessinePlateau(n, plateau)
    dessineConfig(plateau, n)
    exitonclick()


def diametre_disque(disque_n: int):    #disque_n: numéro du disque de 1 à n
    return 40 + (disque_n-1)*30


def dessineTour(n: int, plateau: list[list[int]], nTour: int):
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
    goto(-300, -200)
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


def dessineDisque(nd: int, plateau: list[list[int] | list], n: int, fill_color: str = DISC_COLOR):
    """
    :param nd: Numero du disque à dessiner
    :param plateau: L'état actuel du plateau
    :param n: Nombre de disques dans le plateau
    """
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
    print(n_tour, pos_tour)
    dessineTour(n, plateau, n_tour+1)

    # On redessine les disques restants sur la tour pour éviter que la tour "passe devant" eux
    for n_disque in range(0, len(plateau[n_tour]) - 1):
        disc = plateau[n_tour][n_disque]
        dessineDisque(disc, plateau, n, DISC_COLOR)


def dessineConfig(plateau: list[list[int] | list], n: int):
    for nd in range(n, 0, -1):
        dessineDisque(nd, plateau, n)


def effaceTout(plateau: list[list[int] | list], n: int):
    for nd in range(n, 0, -1):
        effaceDisque(nd, plateau, n)
