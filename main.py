import board
import graphisms
import interaction

# MAIN GAME PROCESS

num_discs = int(input("Entrez le nombre de disques souhaités : "))
while num_discs < 2:
    num_discs = int(input("Entrez le nombre de disques souhaités (sup ou égal à 2) : "))

plateau = board.init(num_discs)
graphisms.init(plateau, num_discs)
(nombre_essais, victoire) = interaction.boucleJeu(plateau, 3, 7)

if nombre_essais is None and victoire is None:
    print(f"Vous avez abandonné.")
else:
    print(f"Nombre d'essais: {nombre_essais},\nVictoire : {victoire}")