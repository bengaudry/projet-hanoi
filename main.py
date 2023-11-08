
def init(n: int):
    """Recoit en argument un entier n (le nombre de disques), et qui renvoie la liste représentant la configuration initiale du plateau"""
    discs = []
    for i in range (n, 0, -1):
        discs.append(i)

    return [discs, [], []]


def nbDisques(plateau: list[list[int] | list], numtour: int):
    """Renvoie le nombre de disques sur la tour indiquée"""
    if 0 < numtour > 2:
        return f"ERROR : Numtour must be between 0 and 2"
    return len(plateau[numtour])


def disqueSup(plateau: list[list[int] | list], numtour: int):
    """Renvoie le numéro du disque au sommet de la tour indiquée"""
    if not plateau[numtour] or len(plateau[numtour]) == 0:
        return -1
    return plateau[numtour][len(plateau[numtour]) - 1]


def posDisque(plateau: list[list[int] | list], numdisque: int):
    """Renvoie le numéro de la tour sur laquelle se trouve un disque"""
    if numdisque in plateau[0]:
        return 0
    elif numdisque in plateau[1]:
        return 1
    elif numdisque in plateau[2]:
        return 2
    else:
        return -1


def verifDepl(plateau: list[list[int] | list], nt1: int, nt2: int):
    """Renvoie True si le déplacement est autorisé et False sinon"""
    disc1 = plateau[nt1][len(plateau[nt1]) - 1]
    if len(plateau[nt1]) > 0 and (len(plateau[nt2]) == 0 or plateau[nt2][len(plateau[nt2]) - 1] > disc1):
        return True
    return False


def verifVictoire(plateau: list[list[int] | list], n: int):
    """Renvoie True si la victoire a été atteinte et False sinon"""
    if len(plateau[0]) > 0 or len(plateau[1]) > 0:
        return False

    expectedTower = []
    for i in range (n, 0, -1):
        expectedTower.append(i)

    if plateau[2] != expectedTower:
        return False
    return True







# TESTS BELOW, DO NOT DELETE

def test(output, expected, testIndex: str | int = ""):
    if output == expected:
        print(f"TEST {testIndex} : OK")
    else:
        print(f"TEST {testIndex} : FAILED")
        print(f"Expected output : {expected}")
        print(f"Your output : {output}")


if __name__ == "__main__":
    # TESTS

    # test fonction init
    test(init(4), [[4, 3, 2, 1], [], []], 1)
    test(init(0), [[], [], []], 2)

    # test fonction nbDisques
    test(nbDisques([[], [], []], 4),"ERROR : Numtour must be between 0 and 2", 3)
    test(nbDisques([[3, 2, 1], [], [4]], 0),3, 4)
    test(nbDisques([[3, 2, 1], [], [4]], 1),0, 5)

    # test fonction disqueSup
    test(disqueSup([[3, 2, 1], [], [4]], 0), 1, 6)
    test(disqueSup([[3, 2, 1], [], [4]], 1), -1, 7)
    test(disqueSup([[3, 2, 1], [], [4]], 2), 4, 8)

    # test fonction posDisque
    test(posDisque([[3, 2, 1], [], [4]], 4), 2, 9)
    test(posDisque([[3, 2, 1], [], [4]], 2), 0, 10)
    test(posDisque([[3, 2, 1], [], [4]], 5), -1, 11)

    # test fonction verifDepl
    test(verifDepl([[2, 1], [], [3]], 0, 2), True, 12)
    test(verifDepl([[2], [3], [1]], 0, 2), False, 13)
    test(verifDepl([[2], [], [3, 1]], 0, 1), True, 14)

    # test fonction verifVictoire
    test(verifVictoire([[], [], [3, 2, 1]], 3), True, 15)
    test(verifVictoire([[4], [], [3, 2, 1]], 3), False, 16)
    test(verifVictoire([[], [], [4, 3, 2, 1]], 3), False, 17)
    test(verifVictoire([[], [], [1, 2, 3]], 3), False, 18)
    test(verifVictoire([[], [], [4, 3, 2, 1]], 4), True, 19)


