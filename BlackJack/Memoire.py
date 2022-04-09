from operator import itemgetter
from MainJoueur import MainJoueur
from BlackJack import BlackJack
import numpy as np
import random

class Memoire:

    def __init__(self):
        self.matrice = np.zeros((32, 10, 4), dtype=float)

    @staticmethod
    def whereToPlace(main_Joueur, main_croupier, historique):
        i = 0
        j = 0
        k = 0
        ### Partie Joueur ###

        cartes_Joueur = main_Joueur[:2]
        cartes_Croupier = main_croupier[:1]

        if BlackJack.is_pair(cartes_Joueur[0], cartes_Joueur[1]):
            if cartes_Joueur[0][1][0] == 1:
                i = 9
            elif cartes_Joueur[0][1][0] == 2:
                i = 0
            elif cartes_Joueur[0][1][0] == 3:
                i = 1
            elif cartes_Joueur[0][1][0] == 4:
                i = 2
            elif cartes_Joueur[0][1][0] == 5:
                i = 3
            elif cartes_Joueur[0][1][0] == 6:
                i = 4
            elif cartes_Joueur[0][1][0] == 7:
                i = 5
            elif cartes_Joueur[0][1][0] == 8:
                i = 6
            elif cartes_Joueur[0][1][0] == 9:
                i = 7
            elif cartes_Joueur[0][1][0] == 10:
                i = 8
        else:
            if cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 2 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 2:
                i = 10
            elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 3 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 3:
                i = 11
            elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 4 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 4:
                i = 12
            elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 5 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 5:
                i = 13
            elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 6 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 6:
                i = 14
            elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 7 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 7:
                i = 15
            elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 8 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 8:
                i = 16
            elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 9 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 9:
                i = 17
            elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 10 or cartes_Joueur[1][1][0] == 1 and \
                    cartes_Joueur[0][1][0] == 10:
                i = 18
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 5:
                i = 19
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 6:
                i = 20
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 7:
                i = 21
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 8:
                i = 22
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 9:
                i = 23
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 10:
                i = 24
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 11:
                i = 25
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 12:
                i = 26
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 13:
                i = 27
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 14:
                i = 28
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 15:
                i = 29
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 16:
                i = 30
            elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] >= 17:
                i = 31

        ### Partie Croupier ###

        if cartes_Croupier[0][1][0] == 1:
            j = 9
        elif cartes_Croupier[0][1][0] == 2:
            j = 0
        elif cartes_Croupier[0][1][0] == 3:
            j = 1
        elif cartes_Croupier[0][1][0] == 4:
            j = 2
        elif cartes_Croupier[0][1][0] == 5:
            j = 3
        elif cartes_Croupier[0][1][0] == 6:
            j = 4
        elif cartes_Croupier[0][1][0] == 7:
            j = 5
        elif cartes_Croupier[0][1][0] == 8:
            j = 6
        elif cartes_Croupier[0][1][0] == 9:
            j = 7
        elif cartes_Croupier[0][1][0] == 10:
            j = 8

        ### Partie Coups ###

        if historique[0] == "Tirer":
            k = 0
        elif historique[0] == "Partager":
            k = 1
        elif historique[0] == "Doubler":
            k = 2
        elif historique[0] == "Rester":
            k = 3

        return i, j, k

    def placerScore(self, main_Joueur, main_croupier, historique, score):
        i, j, k = Memoire.whereToPlace(main_Joueur, main_croupier, historique)
        print("IJK", i, j, k)
        self.matrice[i,j,k] = (self.matrice[i,j,k] + score)/2


    def findBestActionSto(self, main_Joueur, main_croupier):
        coupsPossibles = self.findBestCoupsPossibles(main_Joueur, main_croupier)

        coupsPossibles = np.copy(coupsPossibles)
        if min(coupsPossibles) < 0:
            coupsPossibles += min(coupsPossibles) + 1

        coupsPossibles /= sum(coupsPossibles)
        r = random.random()
        if r < coupsPossibles[0]:
            return "Tirer"
        elif r < coupsPossibles[0] + coupsPossibles[1]:
            return "Partager"
        elif r < coupsPossibles[0] + coupsPossibles[1] + coupsPossibles[2]:
            return "Doubler"
        else:
            return "Rester"


    def findBestActionDeter(self, main_Joueur, main_croupier):
        coupsPossibles = self.findBestCoupsPossibles(main_Joueur, main_croupier)
        valMax = max(coupsPossibles)
        k = coupsPossibles.index(valMax)

        if k == 0:
            return "Tirer"
        elif k == 1:
            return "Partager"
        elif k == 2:
            return "Doubler"
        elif k == 3:
            return "Rester"

    def findBestCoupsPossibles(self, main_Joueur, main_croupier):
        i = 0
        j = 0
        ### Partie Joueur ###
        cartes_Croupier = main_croupier[:1]
        cartes_Joueur = main_Joueur

        if len(cartes_Joueur) == 2:
            if BlackJack.is_pair(cartes_Joueur[0], cartes_Joueur[1]):
                if cartes_Joueur[0][1][0] == 1:
                    i = 9
                elif cartes_Joueur[0][1][0] == 2:
                    i = 0
                elif cartes_Joueur[0][1][0] == 3:
                    i = 1
                elif cartes_Joueur[0][1][0] == 4:
                    i = 2
                elif cartes_Joueur[0][1][0] == 5:
                    i = 3
                elif cartes_Joueur[0][1][0] == 6:
                    i = 4
                elif cartes_Joueur[0][1][0] == 7:
                    i = 5
                elif cartes_Joueur[0][1][0] == 8:
                    i = 6
                elif cartes_Joueur[0][1][0] == 9:
                    i = 7
                elif cartes_Joueur[0][1][0] == 10:
                    i = 8
            else:
                if cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 2 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 2:
                    i = 10
                elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 3 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 3:
                    i = 11
                elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 4 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 4:
                    i = 12
                elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 5 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 5:
                    i = 13
                elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 6 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 6:
                    i = 14
                elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 7 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 7:
                    i = 15
                elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 8 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 8:
                    i = 16
                elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 9 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 9:
                    i = 17
                elif cartes_Joueur[0][1][0] == 1 and cartes_Joueur[1][1][0] == 10 or cartes_Joueur[1][1][0] == 1 and \
                        cartes_Joueur[0][1][0] == 10:
                    i = 18
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 5:
                    i = 19
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 6:
                    i = 20
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 7:
                    i = 21
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 8:
                    i = 22
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 9:
                    i = 23
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 10:
                    i = 24
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 11:
                    i = 25
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 12:
                    i = 26
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 13:
                    i = 27
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 14:
                    i = 28
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 15:
                    i = 29
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] == 16:
                    i = 30
                elif cartes_Joueur[0][1][0] + cartes_Joueur[1][1][0] >= 17:
                    i = 31
        else:
            s1 = 0
            s2 = 0
            for i in range(len(cartes_Joueur)):
                s1 += cartes_Joueur[i][1][0]
                s2 += cartes_Joueur[i][1][1]

            if s2 > 21:
                if s1 == 5:
                    i = 19
                elif s1 == 6:
                    i = 20
                elif s1 == 7:
                    i = 21
                elif s1 == 8:
                    i = 22
                elif s1 == 9:
                    i = 23
                elif s1 == 10:
                    i = 24
                elif s1 == 11:
                    i = 25
                elif s1 == 12:
                    i = 26
                elif s1 == 13:
                    i = 27
                elif s1 == 14:
                    i = 28
                elif s1 == 15:
                    i = 29
                elif s1 == 16:
                    i = 30
                elif s1 >= 17:
                    i = 31
            else :
                if s2 == 5:
                    i = 19
                elif s2 == 6:
                    i = 20
                elif s2 == 7:
                    i = 21
                elif s2 == 8:
                    i = 22
                elif s2 == 9:
                    i = 23
                elif s2 == 10:
                    i = 24
                elif s2 == 11:
                    i = 25
                elif s2 == 12:
                    i = 26
                elif s2 == 13:
                    i = 27
                elif s2 == 14:
                    i = 28
                elif s2 == 15:
                    i = 29
                elif s2 == 16:
                    i = 30
                elif s2 >= 17:
                    i = 31
        ### Partie Croupier ###
        if cartes_Croupier[0][1][0] == 1:
            j = 9
        elif cartes_Croupier[0][1][0] == 2:
            j = 0
        elif cartes_Croupier[0][1][0] == 3:
            j = 1
        elif cartes_Croupier[0][1][0] == 4:
            j = 2
        elif cartes_Croupier[0][1][0] == 5:
            j = 3
        elif cartes_Croupier[0][1][0] == 6:
            j = 4
        elif cartes_Croupier[0][1][0] == 7:
            j = 5
        elif cartes_Croupier[0][1][0] == 8:
            j = 6
        elif cartes_Croupier[0][1][0] == 9:
            j = 7
        elif cartes_Croupier[0][1][0] == 10:
            j = 8

        return self.matrice[i,j]

