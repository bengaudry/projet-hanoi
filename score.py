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
                liste_scores.append([nom, scores[1]])

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
    print(f"Affichage des scores pour les parties à {nombre_disques} disques:\n")
    for i in range(len(liste_scores)):
        print(f"{i + 1}. {liste_scores[i][0]}: {liste_scores[i][1]} coups")


if __name__ == "__main__":
    dico_scores = {'Albert': [[3, 5], [3, 16]], 'Tom': [[3, 4], [3, 23]]}
    affichageScore(dico_scores, 3)
