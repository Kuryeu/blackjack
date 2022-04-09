import random

class JeuDeCarte:

    def __init__(self):
        self.create_cartes_set()
        self.melanger_cartes()


    def create_cartes_set(self):
        self.cartes = [['2 de coeur', [2]], ['2 de pique', [2]], ['2 de carreau', [2]], ['2 de trefle', [2]],
                  ['3 de coeur', [3]], ['3 de pique', [3]], ['3 de carreau', [3]], ['3 de trefle', [3]],
                  ['4 de coeur', [4]], ['4 de pique', [4]], ['4 de carreau', [4]], ['4 de trefle', [4]],
                  ['5 de coeur', [5]], ['5 de pique', [5]], ['5 de carreau', [5]], ['5 de trefle', [5]],
                  ['6 de coeur', [6]], ['6 de pique', [6]], ['6 de carreau', [6]], ['6 de trefle', [6]],
                  ['7 de coeur', [7]], ['7 de pique', [7]], ['7 de carreau', [7]], ['7 de trefle', [7]],
                  ['8 de coeur', [8]], ['8 de pique', [8]], ['8 de carreau', [8]], ['8 de trefle', [8]],
                  ['9 de coeur', [9]], ['9 de pique', [9]], ['9 de carreau', [9]], ['9 de trefle', [9]],
                  ['10 de coeur', [10]], ['10 de pique', [10]], ['10 de carreau', [10]], ['10 de trefle', [10]],
                  ['valet de coeur', [10]], ['valet de pique', [10]], ['valet de carreau', [10]], ['valet de trefle', [10]],
                  ['dame de coeur', [10]], ['dame de pique', [10]], ['dame de carreau', [10]], ['dame de trefle', [10]],
                  ['roi de coeur', [10]], ['roi de pique', [10]], ['roi de carreau', [10]], ['roi de trefle', [10]],
                  ['as de coeur', [1,11]], ['as de pique', [1,11]], ['as de carreau', [1,11]], ['as de trefle', [1,11]]]



    def tirer_carte(self):
        return self.cartes.pop()

    def melanger_cartes(self):
        random.shuffle(self.cartes)
        #print("le jeu a été mélangé")

    def bruler_carte(self):
        self.cartes.remove(self.cartes[-1])
        #print("Une carte a été brûlée")
