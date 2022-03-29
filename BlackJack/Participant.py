
class Participant :

    def __init__(self):
        self.main = []
        self.historique = []
        self.point = [0, 0] #deux valeurs pour les valeurs de l'as

    def tirer(self, jeu_de_carte):
        self.main.append(jeu_de_carte.tirer_carte())
        self.ajouter_point()

    def ajouter_point(self):
        if len(self.main[-1][1]) == 0:
            self.point[0] += self.main[-1][1]
            self.point[1] += self.main[-1][1]
        else: #cas de l'as
            self.point[0] += self.main[-1][1][0]
            self.point[1] += self.main[-1][1][1]