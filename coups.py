from test import test
import graphisms

def dernierCoup(coups: dict[int, list[list[int] | list]]):
    if (len(coups) < 2):
        return None

    last_index = len(coups) - 1
    prev_index = len(coups) - 2

    return (coups[prev_index], coups[last_index])


def annulerDernierCoup(coups: dict[int, list[list[int]]]):
    avant_dernier, dernier_coup = dernierCoup(coups)
    n_disque = None
    nb_disques = 0

    # Obtenir le numéro de disque à déplacer pour annuler le coup
    for i in range(3):
        if len(dernier_coup[i]) > len(avant_dernier[i]):
            n_disque = dernier_coup[i][-1]

    # obtenir le nombre de disques
    for i in dernier_coup:
        nb_disques += len(i)

    # annulation du dernier coup
    graphisms.effaceDisque(n_disque, dernier_coup, nb_disques)
    graphisms.dessineDisque(n_disque, avant_dernier, nb_disques)
    del coups[len(coups) - 1]

    return coups


# TESTS
if __name__ == "__main__":

    # test fonction dernierCoup
    test(dernierCoup({0: [[3, 2, 1], [], []], 1: [[3, 2], [1], []]}), ([[3, 2, 1], [], []], [[3, 2], [1], []]), 1)
    test(dernierCoup({}), None, 2)
    test(dernierCoup({0: [[]]}), None, 3)

    # test fonction annulerDernierCoup
    test(annulerDernierCoup({0: [[3, 2, 1], [], []], 1: [[3, 2], [], [1]], 2: [[3], [2], [1]]}), {0: [[3, 2, 1], [], []], 1: [[3, 2], [], [1]]}, 4)