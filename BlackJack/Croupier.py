from Participant import Participant
class Croupier(Participant):

        def __init__(self):
            super().__init__()

        def comportement(self, jeu_de_carte):

            if len(self.main) in [0, 1]:
                self.tirer(jeu_de_carte)
            elif max(self.point[0], self.point[1]) < 17:
                self.tirer(jeu_de_carte)

            elif self.point[1] == 17 and self.point[0] != self.point[1]:
                self.tirer(jeu_de_carte)

            elif self.point[1] > 17 and self.point[0] < 17:
                self.tirer(jeu_de_carte)

            else:
                return "Le croupier passe son tour"
            return "Le croupier a tiré une carte"
