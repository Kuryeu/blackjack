from operator import itemgetter
from MainJoueur import MainJoueur
from BlackJack import BlackJack
import numpy as np
import random

class Memoire:

    def __init__(self):
        self.matrice = np.zeros((32, 10, 4), dtype=float)
        self.heatmap = np.zeros((32, 10, 4), dtype=int)
        self.total_win = 0
        self.total_main_joue = 0

    @staticmethod
    def whereToPlace(main_Joueur, main_croupier, historique):
        i = 0
        j = 0
        k = 0
        ### Partie Joueur ###

        cartes_Joueur = main_Joueur[:2]
        cartes_Croupier = main_croupier[:1]

        # if len(cartes_Joueur)==1:
        #     input()
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
        #print("IJK", i, j, k)
        self.matrice[i,j,k] = (self.matrice[i,j,k] + score)/2
        self.heatmap[i,j,k] += 1


    def findBestActionSto(self, main_Joueur, main_croupier, actions):
        coupsPossibles = self.findBestCoupsPossibles(main_Joueur, main_croupier)
        coupsPossibles = np.array(coupsPossibles)
        if min(coupsPossibles) < 0:
            coupsPossibles -= min(coupsPossibles)
        coupsPossibles += 1

        if sum(coupsPossibles) == 0:
            return random.choice(actions)
        else:
            coupsPossibles /= sum(coupsPossibles)

        action = ""
        while(action not in actions):
            r = random.random()
            if r < coupsPossibles[0]:
                action = "Tirer"
            elif r < coupsPossibles[0] + coupsPossibles[1]:
                action = "Partager"
            elif r < coupsPossibles[0] + coupsPossibles[1] + coupsPossibles[2]:
                action = "Doubler"
            else:
                action = "Rester"
        return action

    def findBestActionDeter(self, main_Joueur, main_croupier, actions):
        coupsPossibles = self.findBestCoupsPossibles(main_Joueur, main_croupier)
        coupsPossibles = [cp for cp in coupsPossibles]
        action = ""
        while(action not in actions):
            valMax = max(coupsPossibles)
            k = coupsPossibles.index(valMax)
            if k == 0:
                action = "Tirer"
            elif k == 1:
                action = "Partager"
            elif k == 2:
                action = "Doubler"
            elif k == 3:
                action = "Rester"
            coupsPossibles.pop(k)
        return action

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
                if len(cartes_Joueur[i][1]) == 2:
                    s1 += cartes_Joueur[i][1][0]
                    s2 += cartes_Joueur[i][1][1]
                else:
                    s1 += cartes_Joueur[i][1][0]
                    s2 += cartes_Joueur[i][1][0]
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

    def transformation_resultat(self):
        resultat = [[[1] for i in range(10)] for j in range(32)]
        for i in range(32):
            for j in range(10):
                maxValue = max(self.matrice[i, j])
                k = np.argmax(self.matrice[i, j]==maxValue)
                if k == 0:
                    action = "T"
                elif k == 1:
                    action = "P"
                elif k == 2:
                    action = "D"
                elif k == 3:
                    action = "R"
                resultat[i][j] = action
        return(resultat)

    def transformation_heatmap(self):
        result = np.zeros((32, 10))
        s = 0
        for i in range(32):
            for j in range(10):
                s += sum(self.heatmap[i, j])
                result[i, j] = sum(self.heatmap[i, j])
        return (result / np.amax(result))*100

    def winRate(self):
        return self.total_win / self.total_main_joue
