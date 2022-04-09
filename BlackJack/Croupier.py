from Participant import Participant
class Croupier(Participant):

    def __init__(self):
        super().__init__()

    def comportement(self):

        if len(self.mains[0].main) in [1, 2]:
            self.mains[0].action = "Tirer"

        elif self.mains[0].point[1] > 21 and self.mains[0].point[0] > 21:
            #Le croupier a perdu
            self.mains[0].gamestate = 2
            self.mains[0].stop = True
            self.mains[0].action = "Arreter"

        elif max(self.mains[0].point[0], self.mains[0].point[1]) >= 17:
            self.mains[0].stop = True
            self.mains[0].action = "Arreter"
        else:
            self.mains[0].action = "Tirer"








