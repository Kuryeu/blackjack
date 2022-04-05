import random
from Participant import Participant

class Joueur(Participant):


    def __init__(self):
        super().__init__()
        self.solde = 100
        #Créer la matrice


    def comportement_aleatoire(self):
        self.action=random.choice(self.actions)

        pass

    def comportement_intelligent(self):
        pass

    def remplir_matrice(self, resultat_Partie):
        pass

    def exporter_matrice(self):
        pass
