from Participant import Participant
class Croupier(Participant):

    def __init__(self):
        super().__init__()

    def comportement(self):

        if len(self.main) in [0, 1]:
            self.action="Tirer_une_carte"

        elif self.point[1] > 21 and self.point[0] > 21:
            #Le croupier a perdu
            self.gamestate=2

        elif max(self.point[0], self.point[1]) >= 17:
            self.stop=True
        else:
            self.action="Tirer_une_carte"

    def distributionJeton(self,listeJoueur):
        for joueur in listeJoueur:
            #Si le croupier a perdu
            if(self.gamestate==2):
                if(min(joueur.point[0], joueur.point[1])<=21):
                    joueur.gamestate==1
                    #Récompense de 5 pour avoir gagné
                    joueur.solde+=5
                else:
                    joueur.gamestate==2
                    #Malus de 5 pour avoir perdu
                    joueur.solde-=5

            #Si le joueur a perdu
            elif(joueur.gamestate==2):
                #Malus de 5 pour avoir perdu
                joueur.solde-=5

            elif((min(joueur.point[0], joueur.point[1])>min(self.point[0], self.point[1]))or(max(joueur.point[0], joueur.point[1])>max(self.point[0], self.point[1]))):
                joueur.gamestate==1
                #Récompense de 5 pour avoir gagné
                joueur.solde+=5

            else:

                joueur.gamestate==2
                #Malus de 5 pour avoir perdu
                joueur.solde-=5              




