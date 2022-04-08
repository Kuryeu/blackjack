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


    def doublerMise(self, jeu_de_carte, num_main):
        self.mise = self.mise*2
        self.tirer(jeu_de_carte, num_main)
        print("le joueur double sa mise")
        return "le joueur double sa mise"

    def partager(self, num_main):
        if len(self.mains[num_main]) == 2:
            new_main = self.main[num_main][1]
            self.mains[num_main].pop()
            self.mains.append(new_main)
            print("le joueur partage sa main")
            return "le joueur partage sa main"
        else:
            print("partage impossible")
            return "partage impossible"

    def assurer(self, num_main):
        self.mains[num_main].append("assurer")
        print("le joueur assure sa main")
        return "le joueur assure sa main"
