from board import *
from graphisms import dessineDisque, effaceDisque
def lireCoords(plateau: list[list[int] | list]):
    num_start = None
    num_arrival = None
    while num_start != 0 and num_start != 1 and num_start != 2 and num_start != -1:
        num_start = int(input("Entrez le numéro de la tour de départ (0, 1, 2), ou -1 pour stopper le jeu : "))

    if num_start == -1:
        return (-1, None)

    while num_arrival != 0 and num_arrival != 1 and num_arrival != 2:
          num_arrival = int(input("Entrez le numéro de la tour d'arrivée (0, 1, 2) : "))

    return (num_start, num_arrival)


def jouerUnCoup(plateau: list[list[int] | list], n: int):
    (num_start, num_arrival) = lireCoords(plateau)

    if (num_start == -1 and num_arrival is None):
        return "stop"

    while not verifDepl(plateau, num_start, num_arrival):
        print("Ce déplacement n'est pas autorisé.\nRéessayez de placer un disque plus petit sur un disque plus grand.")
        (num_start, num_arrival) = lireCoords(plateau)

    start_tower = plateau[num_start]
    arrival_tower = plateau[num_arrival]

    arrival_tower.append(disqueSup(plateau, num_start))
    start_tower.pop(len(start_tower) - 1)

    # effaceDisque()
    # dessineDisque()

    return None


def boucleJeu(plateau: list[list[int] | list], n: int, maxCoups: int = -1):
    i = 1
    print(plateau)
    while not verifVictoire(plateau, n) and (maxCoups > 0 and i + 1 <= maxCoups):
        coup = jouerUnCoup(plateau, n)

        if coup == "stop":
            return None, None

        print(plateau)
        i += 1

    if maxCoups < 0:
        return (i, True)
    return (i, i <= maxCoups)


if __name__ == "__main__":
    num_tours = int(input("Entrez le nombre de tours souhaitées : "))
    while num_tours < 2:
        num_tours = int(input("Entrez le nombre de tours souhaitées (sup ou égal à 2) : "))

    plateau = init(num_tours)
    (nombre_essais, victoire) = boucleJeu(plateau, 3, 7)

    if nombre_essais is None and victoire is None:
        print(f"Vous avez abandonné.")
    else:
        print(f"Nombre d'essais: {nombre_essais},\nVictoire : {victoire}")
