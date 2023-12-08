import time
import turtle
import board
import graphisms
import interaction
import auto_play
import threading


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


# MAIN GAME PROCESS
still_playing = True

# On lance la fenêtre graphique turtle de manière asynchrone
turtle_thread = threading.Thread(target=lambda: graphisms.init())
turtle_thread.start()
turtle.title("Tours de Hanoi")
turtle.hideturtle()

while still_playing:
    print("Bienvenue dans les Tours de Hanoi")
    # On récupère le nombre de disques sur le plateau que le joueur souhaite
    num_discs = interaction.askForDiscsNumber()
    plateau = board.init(num_discs)

    # On demande au joueur s'il veut jouer en mode automatique
    jeu_auto = interaction.askForAutoPlay()

    # On reset le plateau graphique (turtle)
    graphisms.resetPlateau(plateau, num_discs)

    # On récupère la date de démarrage du jeu
    time_start = time.localtime()

    # BOUCLE PRINCIPALE
    if jeu_auto:
        (nombre_essais, victoire) = auto_play.boucleJeuAuto(plateau, num_discs)
    else:
        # On définit le nombre de coups max selon la difficulté choisie par le joueur
        max_coups = interaction.askForDifficulty(num_discs)
        (nombre_essais, victoire) = interaction.boucleJeu(plateau, num_discs, max_coups)

    # On récupère la date d'arrivée du jeu
    time_end = time.localtime()

    # Gestion de la fin du jeu
    if nombre_essais is None and victoire is None: # Le joueur à abandonné
        print(f"\nVous avez abandonné au bout de {formatDuration(time_start, time_end)}.")
    else: # Le joueur à terminé le jeu (gagné ou perdu)
        if victoire:
            print("\nBravo vous avez gagné !")
        else:
            print("\nVous avez perdu...")
        print(f"Nombre d'essais: {nombre_essais}")
        print(f"Il faut minimum {2**num_discs-1} essais pour réussir")
        print(f"Durée de jeu : {formatDuration(time_start, time_end)}")

    ask_still_playing = input("\nRejouer ? (o / n) ")
    still_playing = ask_still_playing.lower() == "o"

# On quitte l'interface graphique
turtle.bye()
print("Au revoir !")
quit()
