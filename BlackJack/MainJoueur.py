

class MainJoueur:

    def __init__(self):
        # Main courante
        self.main = []
        # Historique de la main
        self.historique = []
        # Valeur des cartes en main
        self.point = [0, 0]  # Deux valeurs pour les valeurs de l'as
        # Les actions courantes du participant
        self.actions = []
        # L'action courante choisie par le participant
        self.action = ""
        # Int indiquant si le participant a gagné(1) ou perdu(2)
        self.gameState = 0
        # Booléen indiquant que le joueur souhaite arrêter
        self.stop = False

    def tirer(self, jeu_de_carte):
        self.main.append(jeu_de_carte.tirer_carte())
        self.ajouter_point()

    def ajouter_point(self):
        if len(self.main[-1][1]) == 1:
            self.point[0] += self.main[-1][1][0]
            self.point[1] += self.main[-1][1][0]
        else:  # cas de l'as
            self.point[0] += self.main[-1][1][0]
            self.point[1] += self.main[-1][1][1]

    def rester(self):
        print("le joueur reste")
        self.stop = True
        return "le joueur reste"

    def abandonner(self):
        #quitter la game
        print("le joueur abandonne")
        self.stop = True
        return "le joueur abandonne"

