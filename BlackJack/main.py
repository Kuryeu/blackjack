# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
from JeuDeCarte import JeuDeCarte
from BlackJack import BlackJack


jeuDeCarte1 = JeuDeCarte()


main_joueur = [['as de pique', [1,10]], ['10 de carreau', 10]]
historique_coup = []
main_croupier = [['roi de pique', 10], ['6 de carreau', 6]]

print(BlackJack.coups_possible(main_joueur, historique_coup, main_croupier, 1))

