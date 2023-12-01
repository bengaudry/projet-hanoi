import graphisms
import interaction

def hanoiAuto(n, depart, intermediaire, arrivee, coups):
    if n == 1:
        coups.append((depart, arrivee))
    else:
        hanoiAuto(n - 1, depart, arrivee, intermediaire, coups)
        coups.append((depart, arrivee))
        hanoiAuto(n - 1, intermediaire, depart, arrivee, coups)

def animeCoupsAuto(coups_auto, plateau, n):
    for coup in coups_auto:
        depart, arrivee = coup
        graphisms.dessineConfig(plateau, n)
        interaction.jouerUnCoup(plateau, n, depart, arrivee)


def boucleJeuAuto(plateau: list[list[int] | list], n: int):
    i = 0
    auto_moves = {
        2: [(0, 1), (0, 2), (1, 2)],
        3: [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2)],
        4: [(0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (1, 2), (0, 1), (0, 2), (1, 2)],
        5: [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), (0, 1), (2, 1), (2, 0), (1, 0), (2, 1), (0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), (1, 2), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), (0, 1), (2, 1), (2, 0), (1, 0), (2, 1), (0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2)],
    }

    print("Mode de jeu : automatique")

    # On joue tant qu'il reste des essais et que l'on a pas gagné
    for (depart, arrivee) in auto_moves[n]:
        # On affiche le nombre de coups restants si le nombre de coups max est défini
        interaction.jouerUnCoup(plateau, n, depart, arrivee)
    return len(auto_moves[n]), True



