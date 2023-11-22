from turtle import *
from board import posDisque_edited
from time import sleep


def init():
    dessinePlateau(3)
    dessineConfig([[3, 2, 1], [], []], 3)
    mainloop()

def diametre_disque(disque_n):    #disque_n: numéro du disque de 1 à n
    return 40 + (disque_n-1)*30


def dessineTour(n, nTour):
    hauteur_tour = (n+1)*20
    epaisseur_tour = 6
    up()
    goto(-300+20*nTour+diametre_disque(n)*(nTour-1)+diametre_disque(n)/2-3, -180)
    down()
    pencolor('blue')
    fillcolor('blue')
    begin_fill()
    for i in range(2):
        forward(epaisseur_tour)
        left(90)
        forward(hauteur_tour)
        left(90)
    end_fill()
    pencolor('black')


def dessinePlateau(n):
    longueur_plateau = diametre_disque(n)*3 + 20*4
    hauteur_plateau = 20
    #tracé du plateau
    up()
    goto(-300, -200)
    down()
    pencolor('blue')
    fillcolor('blue')
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
        dessineTour(n, i)
    up()


def dessineDisque(nd, plateau, n):
    position = posDisque_edited(plateau, nd)   # Contient la tour à l'index 0, et la position dans la tour à l'index 1
    hauteur_disque = 19
    longueur_disque = diametre_disque(nd)
    #tracé du disque
    up()
    goto(-300+20*(position[0]+1)+diametre_disque(n)*(position[0])+(diametre_disque(n)-diametre_disque(nd))/2, -199+20*(position[1]+1))
    down()
    left(90)
    forward(hauteur_disque)
    right(90)
    forward(longueur_disque)
    right(90)
    forward(hauteur_disque+1)
    left(90)
    up()


def effaceDisque(nd, plateau, n):
    #suppresion du disque
    pencolor('white')
    dessineDisque(nd, plateau, n)
    pencolor('black')
    #retraçage de la tour
    position = posDisque(plateau, nd)
    dessineTour(n, position[0]+1)


def dessineConfig(plateau, n):
    for nd in range(n, 0, -1):
        dessineDisque(nd, plateau, n)


def effaceTout(plateau, n):
    for nd in range(n, 0, -1):
        effaceDisque(nd, plateau, n)


if __name__ == "__main__":
    init()
