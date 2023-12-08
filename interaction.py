import coups
from board import *
from graphisms import dessineDisque, effaceDisque, resetPlateau, effaceTout, dessineConfig
from copy import deepcopy

def askForDiscsNumber():
    """Demande le nombre de disques que le joueur souhaite sur le plateau"""
    num_discs = int(input("Entrez le nombre de disques souhaités : "))
    # num_discs = turtle.numinput("Nombre de disques", "Entrez le nombre de disques souhaités : ")
    while num_discs < 2:
        num_discs = int(input("Entrez le nombre de disques souhaités (sup ou égal à 2) : "))
        # num_discs = turtle.numinput("Nombre de disques", "Entrez le nombre de disques souhaités (sup ou égal à 2) : ")
    return int(num_discs)


def askForAutoPlay():
    """Demande au joueur s'il souhaite que le jeu se déroule automatiquement"""
    auto = None
    while auto != "o" and auto != "n":
        auto = input("Souhaitez vous activer le jeu automatique ? (o/n) ")
        # auto = turtle.textinput("Jeu auto", "Souhaitez vous activer le jeu automatique ? (o/n) ")
    return auto == "o"

def askForDifficulty(n: int):
    """Demande la difficulté souhaitée au joueur"""
    difficulties = {}
    difficulties["simple"] = None
    difficulties["medium"] = 2 ** n + 1
    difficulties["hard"] = 2 ** n - 1

    diff = input(f"Choisissez un niveau de difficulté : ({', '.join(difficulties)}) ")
    # diff = turtle.textinput("Difficulté", f"Choisissez un niveau de difficulté : ({', '.join(difficulties)}) ")
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
    """Demande une confirmation au joueur quand il veut arrêter le jeu"""
    inp = -1
    while inp != "o" and inp != "n":
        inp = input("Arrêter le jeu ? (o / n) ").lower()
    return inp == "o"


def jouerUnCoup(plateau: list[list[int]], n: int, num_start=None, num_arrival=None):
    if num_start is None and num_arrival is None:
        (num_start, num_arrival) = lireCoords()

    # Si le numéro de départ est -1, on arrête la partie
    if (num_start == -1 and num_arrival is None):
        return "stop"

    # Si le déplacement n'est pas autorisé, on redemande des coordonées au joueur
    while not verifDepl(plateau, num_start, num_arrival):
        print("Ce déplacement n'est pas autorisé.\nRéessayez de placer un disque plus petit sur un disque plus grand.")
        (num_start, num_arrival) = lireCoords()


    # On déplace le disque
    ancien_plateau = deepcopy(plateau)
    start_tower = plateau[num_start]
    arrival_tower = plateau[num_arrival]

    disque_sup = disqueSup(ancien_plateau, num_start)

    arrival_tower.append(disque_sup)
    plateau[num_start].pop(len(start_tower) - 1)

    effaceDisque(disque_sup, ancien_plateau, n)
    dessineDisque(disque_sup, plateau, n)

    print(f"Je déplace le disque {disque_sup} de la tour {num_start} à la tour {num_arrival}")


def afficheCoupsRestants(coups, maxCoups):
    # On affiche le nombre de coups restants si le nombre de coups max est défini
    if maxCoups is None:
        print(f"\nCoup n°{coups + 1}")
    elif maxCoups is not None and maxCoups - coups == 1:
        print(f"\nCoup n°{coups + 1}. Dernier essai !!")
    else:
        print(f"\nCoup n°{coups + 1}. Il vous reste {maxCoups - coups} essais.")


def boucleJeu(plateau: list[list[int] | list], n: int, maxCoups: int = None):
    coupsJoues = 0
    historiqueCoups = { 0: [row[:] for row in plateau] }
    print(plateau, "plateau original")

    # On joue tant qu'il reste des essais et que l'on a pas gagné
    while not verifVictoire(plateau, n):
        # Si le joueur à épuisé tous ses coups, on arrête le jeu
        if maxCoups is not None and maxCoups + 1 > maxCoups:
            return coupsJoues, False

        afficheCoupsRestants(coupsJoues, maxCoups)
        coup = jouerUnCoup(plateau, n)

        # On rajoute la configuration actuelle du plateau dans historiqueCoups en faisant une copie de la liste plateau
        historiqueCoups[len(historiqueCoups)] = [row[:] for row in plateau]

        # On demande si le joueur veut annuler son coup, et on l'annule si oui
        annulerCoup = input("Voulez vous annuler ce coup ? (o/n) ")
        if annulerCoup == "o":
            plateau = coups.annulerDernierCoup(historiqueCoups)[coupsJoues]
            coupsJoues -= 1

        # On arrête le jeu si le joueur veut arrêter
        if coup == "stop":
            return None, None
        coupsJoues += 1
    return coupsJoues, True
