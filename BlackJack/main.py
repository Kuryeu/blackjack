# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

from JeuDeCarte import JeuDeCarte

def coups_possible(main_joueur, historique_coups, main_croupier, nombre_main_joueur):
    liste_coups_possible = ["Arreter"]
    is_as = False
    nombre_as = 0
    for carte in main_joueur:
        if carte[0][:2] == 'as':
            nombre_as += 1
            is_as = True

    ##### Doubler la mise

    if is_as:
        s1 = 0
        s2 = 0
        for carte in main_joueur:
            if carte[0][:2] == 'as':
                s1 += 1
                s2 += 10
            else:
                s1 += carte[1]
                s2 += carte[1]
        if s1 != 21 and s2 != 21:
            if "Partager_pair_as" not in historique_coups:
                liste_coups_possible.append("Doubler")
    else:
        s = 0
        for carte in main_joueur:
            s += carte[1]
        if s != 21:
            if "Partager_pair_as" not in historique_coups:
                liste_coups_possible.append("Doubler")

    ##### Partager

    if is_as:
        if nombre_as == 2:
            if "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
                liste_coups_possible.append("Partager_pair_as")
        else:
            s = 0
            for carte in main_joueur:
                if carte[0][:2] == 'as':
                    s += 1
                else:
                    s += carte[1]
            if s != 21 and "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
                liste_coups_possible.append("Partager")
    else:
        if main_joueur[0][1] == main_joueur[1][1]:
            if "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
                liste_coups_possible.append("Partager")

    ##### Assurer

    croupier_a_as = False
    for carte in main_croupier:
        if carte[0][:2] == 'as':
            croupier_a_as = True

    if croupier_a_as:
        liste_coups_possible.append("Assurer")

    ##### Tirer

    if "Partage_pair_as" not in historique_coups:
        if "Arreter" not in historique_coups:
            liste_coups_possible.append("Tirer_plusieurs_cartes")
    else:
        if "Arreter" not in historique_coups:
            liste_coups_possible.append("Tirer_une_carte")

    return liste_coups_possible






cartes = []
jeuDeCarte1 = JeuDeCarte(cartes)
jeuDeCarte1.create_cartes_set()

main_joueur = [['as de pique', [1,10]], ['10 de carreau', 10]]
historique_coup = []
main_croupier = [['roi de pique', 10], ['6 de carreau', 6]]

print(coups_possible(main_joueur, historique_coup, main_croupier, 1))

