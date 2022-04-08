
class Participant :

    def __init__(self):
        #Main courante du participant
        self.mains = [[]]
        #Historique des mains du participant
        self.historique = []
        self.point = [0, 0] #deux valeurs pour les valeurs de l'as
        #Les actions courantes du participant
        self.actions=[]
        #L'action courante choisie par le participant
        self.action=""
        #Int indiquant si le participant a gagné(1) ou perdu(2)
        self.gamestate=0
        #Booléen indiquant que le joueur souhaite arrêté
        self.stop=False        

    def tirer(self, jeu_de_carte):
        self.mains.append(jeu_de_carte.tirer_carte())
        self.ajouter_point()

    def ajouter_point(self):
        for main in self.mains:
            if len(main[-1][1]) == 0:
                self.point[0] += main[-1][1]
                self.point[1] += main[-1][1]
            else:  # cas de l'as
                self.point[0] += main[-1][1][0]
                self.point[1] += main[-1][1][1]

    def rester(self):
        print("le joueur reste")
        return "le joueur reste"


    def abandonner(self):
        #quitter la game
        print("le joueur abandonne")
        return "le joueur abandonne"