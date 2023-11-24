import board
import graphisms
import interaction
import threading

# MAIN GAME PROCESS

print("Bienvenue dans les Tours de Hanoi")
num_discs = interaction.askForDiscsNumber()
plateau = board.init(num_discs)

# Launching the graphical ui asynchronously
turtle_thread = threading.Thread(target=lambda: graphisms.init(plateau, num_discs))
turtle_thread.start()

(nombre_essais, victoire) = interaction.boucleJeu(plateau, 3, 7)

if nombre_essais is None and victoire is None:
    print(f"Vous avez abandonné.")
else:
    print(f"Nombre d'essais: {nombre_essais},\nVictoire : {victoire}")
