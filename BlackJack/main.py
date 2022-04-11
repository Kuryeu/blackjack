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

def afficher_resultat(matrice):
    index_colonne = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A']
    index_ligne = ['31 : 17+ ||', '30 : 16  ||', '29 : 15  ||', '28 : 14  ||', '27 : 13  ||', '26 : 12  ||', '25 : 11  ||', '24 : 10  ||',
                   '23 : 9   ||', '22 : 8   ||', '21 : 7   ||', '20 : 6   ||' ,'19 : 5   ||', '18 : A-10||', '17 : A-9 ||', '16 : A-8 ||',
                   '15 : A-7 ||', '14 : A-6 ||', '13 : A-5 ||', '12 : A-4 ||', '11 : A-3 ||', '10 : A-2 ||', '9 : A-A  ||', '8 : 10-10||',
                   '7 : 9-9  ||', '6 : 8-8  ||', '5 : 7-7  ||', '4 : 6-6  ||', '3 : 5-5  ||', '2 : 4-4  ||', '1 : 3-3  ||', '0 : 2-2  ||']
    print("         ||", end=" ")
    for i in range(len(index_colonne)):
        print(i, end=" |")
    print("")
    print("         ||", end=" ")
    for i in range(len(index_colonne)):
        print('--', end="|")
    print("")
    print("         ||", end=" ")
    for i in range(len(index_colonne)):
        if(index_colonne[i] == "10"):
            print(index_colonne[i], end="|")
        else:
            print(index_colonne[i], end=" |")
    print("")
    print("         ||", end=" ")
    for i in range(len(index_colonne)):
        print('__', end="|")
    print("")
    for i in range(32):
        print(index_ligne[i], end=" ")
        for j in range(10):
            print(matrice[i][j], end=" |")
        print("")
    print("")
    print("T : Tirer")
    print("P : Partager")
    print("D : Doubler")
    print("R : Rester")


#memo = LoadMatrice()
memo = Memoire()
comportement_aleatoire = True

# for _ in range(1000000):
#     memo = BlackJack(3, memo, comportement_aleatoire).memoire
# comportement_aleatoire = False
# afficher_resultat(memo.transformation_resultat())
# saveMatrice(memo.matrice)
#
# memo = LoadMatrice()
comportement_aleatoire = True
for _ in range(1000000):
    memo = BlackJack(7, memo, comportement_aleatoire).memoire

saveMatrice(memo.matrice)

afficher_resultat(memo.transformation_resultat())



