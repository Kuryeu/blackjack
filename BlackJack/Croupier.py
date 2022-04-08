from Participant import Participant
class Croupier(Participant):

    def __init__(self):
        super().__init__()

    def comportement(self):

        if len(self.mains[0]) in [0, 1]:
            self.action="Tirer_une_carte"

        elif self.point[1] > 21 and self.point[0] > 21:
            #Le croupier a perdu
            self.gamestate=2

        elif max(self.point[0], self.point[1]) >= 17:
            self.stop=True
        else:
            self.action="Tirer_une_carte"






