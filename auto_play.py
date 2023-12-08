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
    auto_moves = []
    hanoi(n, 0, 2, 1, auto_moves)
    print(auto_moves)

    print("Mode de jeu : automatique")

    # On joue tant qu'il reste des essais et que l'on a pas gagné
    for (depart, arrivee) in auto_moves:
        # On affiche le nombre de coups restants si le nombre de coups max est défini
        interaction.jouerUnCoup(plateau, n, depart, arrivee)
    return len(auto_moves), True



def hanoi (nb_disques, depart, arrivee, intermediaire, deplacements):
    if deplacements is None:
        deplacements = []

    if nb_disques > 0:
        hanoi(nb_disques-1, depart, intermediaire, arrivee, deplacements)
        print(f"Deplacement de {depart} vers {arrivee}")
        deplacements.append((depart, arrivee))
        hanoi(nb_disques-1, intermediaire, arrivee, depart, deplacements)

if __name__ == "__main__":
    deplacements = []
    hanoi(3, 0, 2, 1, deplacements)
    print(deplacements)