from BlackJack import BlackJack
from Memoire import Memoire
import numpy as np
# jeuDeCarte1 = JeuDeCarte()


# main_joueur = [['as de pique', [1,10]], ['10 de carreau', 10]]
# historique_coup = []
# main_croupier = [['roi de pique', 10], ['6 de carreau', 6]]

# print(BlackJack.coups_possible(main_joueur, historique_coup, main_croupier, 1))

def saveMatrice(matrice):
    matriceReshape = np.copy(matrice)
    np.savez("matrice.npz", Tirer=matriceReshape[:, :, 0], Partager=matriceReshape[:, :, 1],
             Doubler=matriceReshape[:, :, 2], Rester=matriceReshape[:, :, 3])


def LoadMatrice():
    mat = Memoire()
    data = np.load("matrice.npz", allow_pickle=True)
    mat.matrice[:, :, 0] = data['Tirer']
    mat.matrice[:, :, 1] = data['Partager']
    mat.matrice[:, :, 2] = data['Doubler']
    mat.matrice[:, :, 3] = data['Rester']
    return mat

memo = LoadMatrice()

for _ in range(100000):
    memo = BlackJack(2, memo).memoire

saveMatrice(memo.matrice)



#Faire la génération de plein de partie pour remplir la matrice du joueur

