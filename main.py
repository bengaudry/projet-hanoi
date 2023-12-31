import time
import turtle
import plateau
import graphismes
import interaction
import jeu_auto
import score


def formatDuration(time_start: time.struct_time, time_end: time.struct_time):
    diff = (time_end.tm_sec + time_end.tm_min * 60 + time_end.tm_hour * 3600) - (time_start.tm_sec + time_start.tm_min * 60 + time_start.tm_hour * 3600)
    return round(diff/60, 1)


# ===========================================================
# MAIN GAME PROCESS
# ===========================================================

still_playing = True

# On lance la fenêtre graphique turtle
turtle.title("Tours de Hanoi")
turtle.hideturtle()

# Création du dictionnaire des scores pour les prochaines parties
scores_joueurs = {}

while still_playing:
    print("Bienvenue dans les Tours de Hanoi")
    # On récupère le nombre de disques sur le plateau que le joueur souhaite
    num_discs = interaction.askForDiscsNumber()
    plateau_jeu = plateau.init(num_discs)

    # On demande au joueur s'il veut jouer en mode automatique
    mode_auto = interaction.askForAutoPlay()

    # On reset le plateau graphique (turtle)
    graphismes.resetPlateau(plateau_jeu, num_discs)

    # On récupère la date de démarrage du jeu
    time_start = time.localtime()

    # BOUCLE PRINCIPALE
    if mode_auto:
        (nombre_essais, victoire) = jeu_auto.boucleJeuAuto(plateau_jeu, num_discs)
    else:
        # On définit le nombre de coups max selon la difficulté choisie par le joueur
        max_coups = interaction.askForDifficulty(num_discs)
        (nombre_essais, victoire) = interaction.boucleJeu(plateau_jeu, num_discs, max_coups)

    # On récupère la date d'arrivée du jeu
    time_end = time.localtime()

    # Gestion de la fin du jeu
    if nombre_essais is None and victoire is None:  # Le joueur à abandonné
        print(f"\nVous avez abandonné au bout de {formatDuration(time_start, time_end)}.")
    else:  # Le joueur à terminé le jeu (gagné ou perdu)
        if victoire:
            print("\nBravo vous avez gagné !")
            nom_joueur = turtle.textinput("Nom du joueur", "Entrez un nom pour sauvegarder votre score : ")
            score.sauvScore(scores_joueurs, nom_joueur, num_discs, nombre_essais, formatDuration(time_start, time_end))
        else:
            print("\nVous avez perdu...")
        print(f"Nombre d'essais: {nombre_essais}")
        print(f"Il faut minimum {2**num_discs-1} essais pour réussir")
        print(f"Durée de jeu: {formatDuration(time_start, time_end)} minutes")

        # Affichage du tableau des scores
        if turtle.textinput("Afficher les scores", "\nAfficher le tableau des scores ? (o / n) ") == 'o':
            nb_disques = int(turtle.numinput("Nombre de disques", "Pour combien de disques ? "))
            score.affichageScore(scores_joueurs, nb_disques)

        # Affichage du tableau des temps de réflexion
        if turtle.textinput("Afficher les temps", "\nAfficher le tableau des temps de réfelexion ? (o / n) ") == 'o':
            score.affichageReflexion(scores_joueurs)

    ask_still_playing = turtle.textinput("Rejouer", "\nRejouer ? (o / n) ")
    still_playing = ask_still_playing.lower() == "o"

    # On quitte l'interface graphique
    if not still_playing:
        turtle.bye()
        print("Au revoir !")

# ===========================================================
# MAIN GAME PROCESS END
# ===========================================================
