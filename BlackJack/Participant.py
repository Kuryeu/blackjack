from MainJoueur import MainJoueur

class Participant:

    def __init__(self):
        #Main courante du participant
        self.mains = [MainJoueur()]
        self.stop = False

    def checkAllStop(self):
        for main in self.mains:
            if not main.stop:
                self.stop = False
                return
        self.stop = True
