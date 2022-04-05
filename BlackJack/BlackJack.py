
from JeuDeCarte import JeuDeCarte
from Joueur import Joueur
from Croupier import Croupier

class BlackJack:

    def __init__(self,nbjoueurs):

        #Instanciation des joueurs
        self.listeParticipants=[]
        for i in range(nbjoueurs):
            self.listeParticipants.append(Joueur())

        #Instanciation du croupier qui jouera en dernier
        self.listeParticipants.append(Croupier())

        self.initialisation_Partie()
        self.deroulement_Partie()

        #Boucle infinie
        #   Initialisation de la partie


    @staticmethod # A modifier quand on aura la classe joueur et croupier
    def coups_possible(main_joueur, historique_coups, main_croupier, nombre_main_joueur):
        liste_coups_possible = ["Arreter"]
        is_as = False
        nombre_as = 0
        for carte in main_joueur:
            if carte[0][:2] == 'as':
                nombre_as += 1
                is_as = True

        ##### Doubler la mise
        if is_as:
            s1 = 0
            s2 = 0
            for carte in main_joueur:
                if carte[0][:2] == 'as':
                    s1 += 1
                    s2 += 10
                else:
                    s1 += carte[1][0]
                    s2 += carte[1][0]
            if s1 != 21 and s2 != 21:
                if "Partager_pair_as" not in historique_coups:
                    liste_coups_possible.append("Doubler")
        else:
            s = 0
            for carte in main_joueur:
                s += carte[1][0]
            if s!= 21:
                if "Partager_pair_as" not in historique_coups:
                    liste_coups_possible.append("Doubler")

        ##### Partager

        if is_as:
             if nombre_as == 2:
                 if "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
                     liste_coups_possible.append("Partager_pair_as")
             else:
                s = 0
                for carte in main_joueur:
                    if carte[0][:2] == 'as':
                        s += 1
                    else:
                        s += carte[1][0]
                if s != 21 and "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
                    liste_coups_possible.append("Partager")
        else:
            if main_joueur[0][1] == main_joueur[1][1]:
                if "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
                    liste_coups_possible.append("Partager")

        ##### Assurer

        croupier_a_as = False
        for carte in main_croupier:
            if carte[0][:2] == 'as':
                croupier_a_as = True

        if croupier_a_as:
            liste_coups_possible.append("Assurer")

        ##### Tirer

        if "Partage_pair_as" not in historique_coups:
            if "Arreter" not in historique_coups:
                liste_coups_possible.append("Tirer_plusieurs_cartes")
        else:
            if "Arreter" not in historique_coups:
                liste_coups_possible.append("Tirer_une_carte")

        return liste_coups_possible

    #Appliquer l'action choisit par le participant en fonction des règles du blackjack
    def appliquer_Action(self,participant):
        if (participant.action=="Doubler"):
            pass
        elif (participant.action=="Arreter"):
            participant.stop=True
        elif (participant.action=="Tirer_plusieurs_cartes" or participant.action=="Tirer_une_carte"):
            participant.tirer(self.jeuDeCarte)
        elif (participant.action=="Partager"):
            pass
        elif (participant.action=="Partager_pair_as"):
            pass
        elif (participant.action=="Partager_pair_as"):
            pass        
        
    def checkCardsValue(self,participant):
        if(participant.point[1]>21):
            if(participant.point[0]>21):
                #Le participant a bust
                participant.gamestate=2

    def initialisation_Partie(self):
        #1- Initialisation jeu de carte
        self.jeuDeCarte = JeuDeCarte()

        #2- Distribution de deux cartes face visible à chaque joueur
        for participant in self.listeParticipants[:-1]:
            participant.tirer(self.jeuDeCarte)
            participant.tirer(self.jeuDeCarte)
        
        #3- Distribution d'une carte visible au croupier
        self.listeParticipants[-1].tirer(self.jeuDeCarte)


    def deroulement_Partie(self):
        result=[]
        #Tant qu'il reste des participants qui jouent
        while(self.listeParticipants[:-1]):
            #Pour chaque joueur de la table
            #A tour de rôle, les joueurs effectuent des actions
            for participant in self.listeParticipants[:-1]:
                #Définition des actions possibles
                participant.actions=BlackJack.coups_possible(participant.main,[], self.listeParticipants[-1].main,0)
                #Choix d'une action par le joueur

                #Choix d'une action aléatoire par le joueur
                participant.comportement_aleatoire()
                #Ajout de l'action dans l'historique du joueur
                participant.historique.append(participant.action)
                #L'action est joué
                self.appliquer_Action(participant)
                #On check la valeur des cartes pour savoir si le joueur n'a pas dépassé 21
                self.checkCardsValue(participant)

            #On enlève de la liste les joueurs ayant dépassé 21 OU ayant souhaité se coucher
            temp=self.listeParticipants[:-1].copy()
            for participant in self.listeParticipants[:-1]:
                if(participant.gamestate==2 or participant.stop==True):
                    result.append(participant)
                    temp.remove(participant)
            self.listeParticipants[:-1]=temp

        self.listeParticipants[:-1]=result

        #On fait ensuite jouer le croupier
        while(self.listeParticipants[-1].gamestate!=2 and self.listeParticipants[-1].stop==False):
            self.listeParticipants[-1].comportement()

            if(self.listeParticipants[-1].gamestate!=2 and self.listeParticipants[-1].stop==False):
                self.appliquer_Action(self.listeParticipants[-1])
                self.listeParticipants[-1].historique.append(self.listeParticipants[-1].action)

        #On gère la distribution des récompenses à chaque joueur
        self.listeParticipants[-1].distributionJeton(self.listeParticipants[:-1])
        pass



