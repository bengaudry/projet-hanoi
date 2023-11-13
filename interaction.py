
def lireCoords(plateau: list[list[int] | list]):
    num_start = -1
    num_arrival = -1
    while num_start != 0 and num_start != 1 and num_start != 2:
        num_start = int(input("Entrez le numéro de la tour de départ (0, 1, 2) : "))

    while num_arrival != 0 and num_arrival != 1 and num_arrival != 2:
          num_arrival = int(input("Entrez le numéro de la tour d'arrivée (0, 1, 2) : "))

    return (num_start, num_arrival)


def jouerUnCoup(plateau: list[list[int] | list], n: int):
    (num_start, num_arrival) = lireCoords(plateau)
    print(num_start)
    print(num_arrival)

