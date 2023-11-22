import board
import graphisms
import interaction
import moves
import scores_time
import game


# MAIN GAME PROCESS

num_tours = int(input("Entrez le nombre de tours souhaitées : "))
while num_tours < 2:
    num_tours = int(input("Entrez le nombre de tours souhaitées (sup ou égal à 2) : "))

plateau = board.init(num_tours)
(nombre_essais, victoire) = interaction.boucleJeu(plateau, 3, 7)

if nombre_essais is None and victoire is None:
    print(f"Vous avez abandonné.")
else:
    print(f"Nombre d'essais: {nombre_essais},\nVictoire : {victoire}")