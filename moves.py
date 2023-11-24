from test import test

def dernierCoup(coups: dict[int, list[list[int] | list]]):
    if (len(coups) < 2):
        return None

    last_index = len(coups) - 1
    prev_index = len(coups) - 2

    return (coups[prev_index], coups[last_index])


def annulerDernierCoup(coups: dict[int, list[list[int] | list]]):
    return


# TESTS
if __name__ == "__main__":

    # test fonction dernierCoup
    test(dernierCoup({0: [[3, 2, 1], [], []], 1: [[3, 2], [1], []]}), ([[3, 2, 1], [], []], [[3, 2], [1], []]), 1)
    test(dernierCoup({}), None, 2)
    test(dernierCoup({0: [[]]}), None, 3)

    # test fonction annulerDernierCoup
    test(annulerDernierCoup({0: [[3, 2, 1], [], []], 1: [[3, 2], [], [1]], 2: [[3], [2], [1]]}), {0: [[3, 2, 1], [], []], 1: [[3, 2], [], [1]]}, 4)