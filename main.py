import time
import turtle

import board
import graphisms
import interaction
import threading
import os


def formatDuration(time_start: time.struct_time, time_end: time.struct_time):
    diff = (time_end.tm_sec + time_end.tm_min * 60 + time_end.tm_hour * 3600) -(time_start.tm_sec + time_start.tm_min * 60 + time_start.tm_hour * 3600)
    if diff == 1:
        return f"1 seconde"
    elif diff < 60:
        return f"{diff} secondes"
    elif int(diff / 60) == 1:
        return f"1 minute"
    else:
        return f"{round(diff / 60)} minutes"


clear = lambda: os.system("cls")


# MAIN GAME PROCESS
still_playing = True

while still_playing:
    print("Bienvenue dans les Tours de Hanoi")
    num_discs = interaction.askForDiscsNumber()
    plateau = board.init(num_discs)
    max_coups = interaction.askForDifficulty(num_discs)

    # Launching the graphical ui asynchronously
    turtle_thread = threading.Thread(target=lambda: graphisms.init(plateau, num_discs))
    turtle_thread.start()

    time_start = time.localtime()
    (nombre_essais, victoire) = interaction.boucleJeu(plateau, 3, 7, max_coups)
    time_end = time.localtime()

    if nombre_essais is None and victoire is None:
        print(f"\nVous avez abandonné au bout de {formatDuration(time_start, time_end)}.")
    else:
        if victoire:
            print("\nBravo vous avez gagné !")
        else:
            print("\nVous avez perdu...")
        print(f"Nombre d'essais: {nombre_essais}")
        print(f"Il faut minimum {2**num_discs-1} essais pour réussir")
        print(f"Durée de jeu : {formatDuration(time_start, time_end)}")

    ask_still_playing = input("\nRejouer ? (o / n) ")
    still_playing = ask_still_playing.lower() == "o"
    clear()
turtle.bye()
print("Au revoir !")
