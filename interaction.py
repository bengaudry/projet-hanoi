from board import *
from graphisms import dessineDisque, effaceDisque

def askForDiscsNumber():
    num_discs = int(input("Entrez le nombre de disques souhaités : "))
    while num_discs < 2:
        num_discs = int(input("Entrez le nombre de disques souhaités (sup ou égal à 2) : "))
    return num_discs


def askForDifficulty(n: int):
    difficulties = {}
    difficulties["simple"] = None
    difficulties["medium"] = 2 ** n + 1
    difficulties["hard"] = 2 ** n - 1

    diff = input(f"Choisissez un niveau de difficulté : ({', '.join(difficulties)}) ")
    if diff not in difficulties.keys():
        return difficulties["medium"]
    return difficulties[diff]


def lireCoords():
    """Demande le numéro de la tour de départ, et d'arrivée au joueur"""
    num_start = None
    num_arrival = None
    while num_start != 0 and num_start != 1 and num_start != 2 and num_start != -1:
        num_start = int(input("Tour de départ ? (0, 1, 2) "))

    # Si le numéro de départ est -1, on arrête la partie
    if num_start == -1:
        if veutArreterJeu():
            return (-1, None)
        else:
            print("D'accord, reprenons la partie !")
            while num_start != 0 and num_start != 1 and num_start != 2:
                num_start = int(input("Tour de départ ? (0, 1, 2) "))

    while num_arrival != 0 and num_arrival != 1 and num_arrival != 2:
          num_arrival = int(input("Tour d'arrivée ? (0, 1, 2) "))

    return (num_start, num_arrival)


def veutArreterJeu():
    inp = -1
    while inp != "o" and inp != "n":
        inp = input("Arrêter le jeu ? (o / n) ").lower()
    return inp == "o"


def jouerUnCoup(plateau: list[list[int] | list], n: int):
    (num_start, num_arrival) = lireCoords()

    # Si le numéro de départ est -1, on arrête la partie
    if (num_start == -1 and num_arrival is None):
        return "stop"

    # Si le déplacement n'est pas autorisé, on redemande des coordonées au joueur
    while not verifDepl(plateau, num_start, num_arrival):
        print("Ce déplacement n'est pas autorisé.\nRéessayez de placer un disque plus petit sur un disque plus grand.")
        (num_start, num_arrival) = lireCoords()

    disque_sup = disqueSup(plateau, num_start)

    # On déplace le disque
    start_tower = plateau[num_start]
    arrival_tower = plateau[num_arrival]

    effaceDisque(disque_sup, plateau, n)

    arrival_tower.append(disque_sup)
    start_tower.pop(len(start_tower) - 1)

    dessineDisque(disque_sup, plateau, n)

    print(f"Je déplace le disque {disque_sup} de la tour {num_start} à la tour {num_arrival}")


def boucleJeu(plateau: list[list[int] | list], n: int, num_discs, maxCoups: int = None):
    i = 0
    # On joue tant qu'il reste des essais et que l'on a pas gagné
    while not verifVictoire(plateau, n):
        if maxCoups is not None and i + 1 > maxCoups:
            return i, False

        if maxCoups is None:
            print(f"\nCoup n°{i+1}")
        elif maxCoups is not None and maxCoups - i == 1:
            print(f"\nCoup n°{i+1}. Dernier essai !!")
        else:
            print(f"\nCoup n°{i+1}. Il vous reste {maxCoups - i} essais.")


        coup = jouerUnCoup(plateau, n)

        # On arrête le jeu si le joueur veut arrêter
        if coup == "stop":
            return None, None

        i += 1

    return i, True
