
from JeuDeCarte import JeuDeCarte
from Joueur import Joueur
from Croupier import Croupier

class BlackJack:

    def __init__(self,nbjoueurs, memoire, compotement_aleatoire):

        #Instanciation des joueurs
        self.listeParticipants = []
        # 1- Initialisation jeu de carte
        self.memoire = memoire
        self.comportement_aleatoire = compotement_aleatoire
        self.jeuDeCarte = JeuDeCarte()
        self.initialisation_Partie(nbjoueurs)

    def PartieNormale(self):
        self.deroulement_Partie()
        self.ResultatPartie()
        return self.memoire

    def PartiePopInitiale(self):
        for participant in self.listeParticipants[:-1]:
            for i, main in enumerate(participant.mains):
                # Définition des actions possibles
                main.actions = BlackJack.coups_possible(main.main, [], self.listeParticipants[-1].mains[0].main, 0)
                participant.comportement_aleatoire(i)
                self.memoire.placerComportement(main.main, self.listeParticipants[-1].mains[0].main, main.action)
        return self.memoire




    @staticmethod
    def is_pair(carte1, carte2):
        id1 = ''
        id2 = ''
        for i in range(len(carte1[0])):
            id1 += carte1[0][i]
            if i > 1:
                ch = carte1[0][i - 1] + carte1[0][i]
                if ch == "de":
                    break
        for i in range(len(carte2[0])):
            id2 += carte2[0][i]
            if i > 1:
                ch = carte2[0][i - 1] + carte2[0][i]
                if ch == "de":
                    break
        if id1 == id2:
            return True
        return False




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

        if len(main_joueur) == 2:
            if BlackJack.is_pair(main_joueur[0], main_joueur[1]):
                liste_coups_possible.append("Partager")



        # if is_as:
        #      if nombre_as == 2:
        #          if "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
        #              liste_coups_possible.append("Partager_pair_as")
        #      else:
        #         s = 0
        #         for carte in main_joueur:
        #             if carte[0][:2] == 'as':
        #                 s += 1
        #             else:
        #                 s += carte[1][0]
        #         if s != 21 and "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
        #             liste_coups_possible.append("Partager")
        # else:
        #     if len(main_joueur) > 1:
        #         if main_joueur[0][1] == main_joueur[1][1]:
        #             if "Partage_pair_as" not in historique_coups and nombre_main_joueur < 4:
        #                 liste_coups_possible.append("Partager")


        ##### Tirer

        if "Arreter" not in historique_coups:
            liste_coups_possible.append("Tirer")
        # if "Partage_pair_as" not in historique_coups:
        #     if "Arreter" not in historique_coups:
        #         liste_coups_possible.append("Tirer_plusieurs_cartes")
        # else:
        #     if "Arreter" not in historique_coups:
        #         liste_coups_possible.append("Tirer_une_carte")

        return liste_coups_possible

    #Appliquer l'action choisit par le participant en fonction des règles du blackjack
    def appliquer_Action(self, joueur, numMain):

        if joueur.mains[numMain].action == "Doubler":
            joueur.doublerMise(self.jeuDeCarte, numMain)
        elif joueur.mains[numMain].action == "Arreter":
            joueur.mains[numMain].stop = True
        elif joueur.mains[numMain].action == "Tirer":
            joueur.mains[numMain].tirer(self.jeuDeCarte)
        elif joueur.mains[numMain].action == "Partager":
            joueur.partager(self.jeuDeCarte, numMain)
        # elif joueur.mains[numMain].action == "Partager_pair_as":
        #     joueur.mains.partager(numMain)
        # elif joueur.mains[numMain].action == "Partager_pair_as":
        #     joueur.mains.partager(numMain)


    def checkCardsValue(self,main):
        if main.point[1] > 21:
            if main.point[0] > 21:
                #Le participant a bust
                main.gameState = 2
                main.stop = True

    def initialisation_Partie(self, nb_Joueur):

        if nb_Joueur <= 0 or nb_Joueur > 7:
            print("Veuillez entrer un nombre de joueur valide (entre 1 et 7 joueur(s)")
            return None

        for _ in range(nb_Joueur):
            self.listeParticipants.append(Joueur())

            # Instanciation du croupier qui jouera en dernier
        self.listeParticipants.append(Croupier())


        #2- Distribution de deux cartes face visible à chaque joueur
        for participant in self.listeParticipants[:-1]:
            participant.mains[0].tirer(self.jeuDeCarte)
            participant.mains[0].tirer(self.jeuDeCarte)
        
        #3- Distribution d'une carte visible au croupier
        self.listeParticipants[-1].mains[0].tirer(self.jeuDeCarte)


    def deroulement_Partie(self):
        result = []
        #Tant qu'il reste des participants qui jouent
        while(self.listeParticipants[:-1]):
            #Pour chaque joueur de la table
            #A tour de rôle, les joueurs effectuent des actions
            for participant in self.listeParticipants[:-1]:
                for i, main in enumerate(participant.mains):
                    if not participant.mains[i].stop:
                        #Définition des actions possibles

                        main.actions = BlackJack.coups_possible(main.main, [], self.listeParticipants[-1].mains[0].main, 0)
                        participant.comportement_deter(i, self.memoire, self.listeParticipants[-1].mains[0].main)
                        #Ajout de l'action dans l'historique du joueur

                        main.historique.append(main.action)

                        #L'action est joué

                        self.appliquer_Action(participant, i)

                        #On check la valeur des cartes pour savoir si le joueur n'a pas dépassé 21

                        self.checkCardsValue(main)
                participant.checkAllStop() #Vérifie si toutes les mains du joueur peuvent jouer

            #On enlève de la liste les joueurs ayant dépassé 21 OU ayant souhaité se coucher

            temp = self.listeParticipants[:-1].copy()
            for participant in self.listeParticipants[:-1]:
                if participant.stop:
                    result.append(participant)
                    temp.remove(participant)
            self.listeParticipants[:-1] = temp

        self.listeParticipants[:-1] = result

        #On fait ensuite jouer le croupier
        while(not self.listeParticipants[-1].stop):
            self.listeParticipants[-1].comportement()

            if not self.listeParticipants[-1].stop:
                self.appliquer_Action(self.listeParticipants[-1], 0)
                self.listeParticipants[-1].mains[0].historique.append(self.listeParticipants[-1].mains[0].action)
                self.checkCardsValue(self.listeParticipants[-1].mains[0])
            self.listeParticipants[-1].checkAllStop()
        #On gère la distribution des récompenses à chaque joueur
        self.distributionJeton()


    def distributionJeton(self):
        for joueur in self.listeParticipants[:-1]:
            for i, main in enumerate(joueur.mains):
                #Si le croupier a perdu
                if self.listeParticipants[-1].mains[0].gameState == 2:
                    if min(main.point[0], main.point[1]) <= 21:
                        main.gameState = 1
                        #Récompense de 5 pour avoir gagné
                        joueur.solde += joueur.mises[i] * 2
                    else:
                        main.gameState = 2

                #Si le joueur a perdu
                elif main.gameState == 2:
                    pass

                elif((min(main.point[0], main.point[1]) > min(self.listeParticipants[-1].mains[0].point[0], self.listeParticipants[-1].mains[0].point[1])) or
                     (max(main.point[0], main.point[1]) > max(self.listeParticipants[-1].mains[0].point[0], self.listeParticipants[-1].mains[0].point[1]))):
                    main.gameState = 1
                    #Récompense de 5 pour avoir gagné
                    joueur.solde += joueur.mises[i] * 2

                else:
                    main.gameState = 2


    def afficherPartie(self):
        for i, joueur in enumerate(self.listeParticipants):
            if i < len(self.listeParticipants)-1:
                print("Joueur : ", i, " Solde : ", joueur.solde)
            else:
                print("Croupier")
            for j, main in enumerate(joueur.mains):
                print("Main : ", j)
                print(main.main)
                print("score : ", main.point)


    def calculerScores(self):
        for i in range(len(self.listeParticipants[:-1])):
            for j in range(len(self.listeParticipants[i].mains)):
                score = self.calculerScore(i, j)
                #print(score)
                self.memoire.placerScore(self.listeParticipants[i].mains[j].main,
                                         self.listeParticipants[-1].mains[0].main,
                                         self.listeParticipants[i].mains[j].historique, score)

    def calculerScore(self, indicejoueur, indicemain):
        """ Quand on va ajouter dans le tableau on va moyenner à fois
        Si Gagner :
            Si blackJack:
                - BlackJack = 5
            Sinon :
                - Différence au blackjack = (21 - points) / 5
        Si Perdre :
            Si BlackJack Croupier :
                - BlackJack Croupier = -5
            Sinon :
                - Différence au blackjack = - (points - 21) / 5

        :return:
        """
        main = self.listeParticipants[indicejoueur].mains[indicemain]
        croupier = self.listeParticipants[-1]
        score = 0

        #Le joueur a gagné
        if croupier.mains[0].gameState == 2 and main.gameState == 1:
            if main.point[0] == 21 or main.point[1] == 21:
                score += 5
            else:
                if main.point[1] > 21:
                    score += (main.point[0]) / 5
                else:
                    score += (main.point[1]) / 5
        # Le joueur a perdu
        elif main.gameState == 2:
            if croupier.mains[0].point[0] == 21 or croupier.mains[0].point[1] == 21:
                score -= 5
            else:
                if main.point[0] >= 21:
                    score -= (main.point[0] - 21) / 5
                else:
                    score -= (croupier.mains[0].point[1] - main.point[0]) / 5

        return score


    def ResultatPartie(self):
        for joueur in self.listeParticipants[:-1]:
            for main in joueur.mains:
                self.memoire.total_main_joue += 1
                if main.gameState == 1:
                    self.memoire.total_win += 1

