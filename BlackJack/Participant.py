
class Participant :

    def __init__(self):
        self.main = [[]]
        self.historique = []
        self.point = [0, 0] #deux valeurs pour les valeurs de l'as
        self.mise = 30

    def tirer(self, jeu_de_carte, num_main):
        self.main[num_main].append(jeu_de_carte.tirer_carte())
        self.ajouter_point()

    def ajouter_point(self):
        for hand in self.main:
            if len(hand[-1][1]) == 0:
                self.point[0] += hand[-1][1]
                self.point[1] += hand[-1][1]
            else: #cas de l'as
                self.point[0] += hand[-1][1][0]
                self.point[1] += hand[-1][1][1]

    def rester(self):
        print("le joueur reste")
        return "le joueur reste"

    def doublerMise(self, jeu_de_carte, num_main):
        self.mise = self.mise*2
        self.tirer(jeu_de_carte, num_main)
        print("le joueur double sa mise")
        return "le joueur double sa mise"

    def partager(self, num_main):
        if len(self.main[num_main]) == 2:
            new_main = self.main[num_main][1]
            self.main[num_main].pop()
            self.main.append(new_main)
            print("le joueur partage sa main")
            return "le joueur partage sa main"
        else:
            print("partage impossible")
            return "partage impossible"

    def assurer(self, num_main):
        self.main[num_main].append("assurer")
        print("le joueur assure sa main")
        return "le joueur assure sa main"

    def abandonner(self):
        #quitter la game
        print("le joueur abandonne")
        return "le joueur abandonne"


