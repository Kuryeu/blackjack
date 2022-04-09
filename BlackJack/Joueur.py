import random
from Participant import Participant
from MainJoueur import MainJoueur

class Joueur(Participant):


    def __init__(self):
        super().__init__()
        self.solde = 100
        self.solde -= 5
        self.mises = [5] #Ajout
        #Créer la matrice


    def comportement_aleatoire(self, num_main):
        print(self.mains[num_main].actions)
        # if "Partager" in self.mains[num_main].actions:
        #     self.mains[num_main].action = input("{}".format(self.mains[num_main].main))
        # else:
        self.mains[num_main].action = random.choice(self.mains[num_main].actions)

    def comportement_sto(self, num_main, matrice, main_Croupier):
        if not self.mains[num_main].stop:
            self.mains[num_main].action = matrice.findBestActionSto(self.mains[num_main].main,
                                                                main_Croupier, self.mains[num_main].actions)

    def comportement_deter(self, num_main, matrice, main_Croupier):
        if not self.mains[num_main].stop:
            self.mains[num_main].action = matrice.findBestActionDeter(self.mains[num_main].main,
                                                                  main_Croupier, self.mains[num_main].actions)


    def doublerMise(self, jeu_de_carte, num_main):
        self.mises[num_main] *= 2 #Ajout
        self.solde -= 5 #Ajout
        self.mains[num_main].tirer(jeu_de_carte)
        #print("le joueur double sa mise")
        self.mains[num_main].stop = True
        return "le joueur double sa mise"

    def partager(self, jeu_de_carte, num_main):
        if len(self.mains[num_main].main) == 2:
            new_main = self.mains[num_main].main[1]
            self.mains[num_main].main.pop()
            self.mains[num_main].point[0] //= 2
            self.mains[num_main].point[1] //= 2
            self.mains.append(MainJoueur())
            self.mains[-1].main.append(new_main)
            self.mains[-1].ajouter_point()
            self.mises.append(5)
            self.solde -= 5
            self.mains[num_main].tirer(jeu_de_carte)
            self.mains[num_main+1].tirer(jeu_de_carte)
            #print("le joueur partage sa main")
            return "le joueur partage sa main"
        else:
            #print("partage impossible")
            return "partage impossible"

    def assurer(self, num_main):
        self.mains[num_main].actions.append("assurer")
        #print("le joueur assure sa main")
        return "le joueur assure sa main"
