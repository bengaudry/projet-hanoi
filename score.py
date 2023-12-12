def sauvScore(score_joueurs: dict[str, list[list[int]]], nom: str, nombre_disques: int, nombre_coups: int, temps_partie):
    if nom in score_joueurs.keys():
        score_joueurs[nom].append([nombre_disques, nombre_coups, temps_partie])
    else:
        score_joueurs[nom] = [[nombre_disques, nombre_coups, temps_partie]]


def affichageScore(score_joueurs: dict[str, list[list[int]]], nombre_disques: int):
    """Demande le dictionnaire de scores ainsi que le nombre de disques pour
    afficher les scores des parties à n disques"""
    liste_scores = []

    # Ajouter tous les noms et scores à liste_scores
    for nom in score_joueurs:
        for scores in score_joueurs[nom]:
            if scores[0] == nombre_disques:
                liste_scores.append([nom, scores[1], scores[2]])

    # Algorithme de tri par sélection
    n = len(liste_scores)
    for i in range(n):
        # Trouver l'indice du minimum dans le reste de la liste
        min_index = i
        for j in range(i + 1, n):
            if liste_scores[j][1] < liste_scores[min_index][1]:
                min_index = j

        # Échanger les éléments
        liste_scores[i], liste_scores[min_index] = liste_scores[min_index], liste_scores[i]

    # Affichage des scores
    print(f"\nAffichage des scores pour les parties à {nombre_disques} disques:\n")
    for i in range(len(liste_scores)):
        print(f"{i + 1}. {liste_scores[i][0]}: {liste_scores[i][1]} coups, {liste_scores[i][2]} minutes")


def reflexionMoy(score_joueurs: dict[str, list[list[int]]], nom: str):
    """Calcule le temps de reflexion moyen par coup du pour toutes les parties du joueur"""
    total_coups = 0
    total_temps = 0
    for partie in score_joueurs[nom]:
        total_coups += partie[1]
        total_temps += partie[2]
    #retourne la moyenne en secondes
    return round((total_coups/total_temps)*60)

def affichageReflexion(score_joueurs: dict[str, list[list[int]]]):
    #Ajouter à une liste tous les temps moyens de chaque joueur
    liste_temps_joueurs = []
    for nom in score_joueurs:
        liste_temps_joueurs.append([nom, reflexionMoy(score_joueurs, nom)])

    #Trier la liste du plus rapide au plus lent
    n = len(liste_temps_joueurs)
    for i in range(n):
        # Trouver l'indice du minimum dans le reste de la liste
        min_index = i
        for j in range(i + 1, n):
            if liste_temps_joueurs[j][1] < liste_temps_joueurs[min_index][1]:
                min_index = j

        # Échanger les éléments
        liste_temps_joueurs[i], liste_temps_joueurs[min_index] = liste_temps_joueurs[min_index], liste_temps_joueurs[i]

    #Affichage des temps de relfexion moyens
    print(f"\nAffichage des temps de reflexion moyens par joueur:\n")
    for i in range(len(liste_temps_joueurs)):
        print(f"{i + 1}. {liste_temps_joueurs[i][0]}: {liste_temps_joueurs[i][1]} secondes")


if __name__ == "__main__":
    dico_scores = {'Albert': [[3, 5, 12], [3, 16, 2]], 'Tom': [[3, 4, 13], [3, 23, 9]]}
    affichageReflexion(dico_scores)
    affichageScore(dico_scores, 3)
