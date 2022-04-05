from Croupier import Croupier
from JeuDeCarte import JeuDeCarte
from Joueur import Joueur
from Participant import Participant


class BlackJack:

    def __init__(self, listeJoueurs, croupier, jeuDeCarte):
        self.listeJoueurs = listeJoueurs
        self.croupier = croupier
        self.jeuDeCarte = jeuDeCarte


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
                    s1 += carte[1]
                    s2 += carte[1]
            if s1 != 21 and s2 != 21:
                if "Partager_pair_as" not in historique_coups:
                    liste_coups_possible.append("Doubler")
        else:
            s = 0
            for carte in main_joueur:
                s += carte[1]
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
                        s += carte[1]
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


    def initialisation_Partie(self, nb_Joueur):# Brice
        if nb_Joueur<=0 or nb_Joueur>7:
            print("Veuillez entrer un nombre de joueur valide (entre 1 et 7 joueur(s)")
            return
        listeJoueurs = []
        for i in range (nb_Joueur):
            joueur = Participant()
            listeJoueurs.append(joueur)
        croupier = Croupier()
        jeuDeCarte = JeuDeCarte()
        blackJack = BlackJack(listeJoueurs, croupier, jeuDeCarte)
        return blackJack

    def deroulement_Partie(self, blackJack): # Brice
        blackJack.croupier.comportement(blackJack.jeuDeCarte)
        for joueur in blackJack.listeJoueurs:
            joueur.tirer(blackJack.jeuDeCarte)
            joueur.tirer(blackJack.jeuDeCarte)
            ### Action Joueur
        blackJack.croupier.comportement(blackJack.jeuDeCarte)

    def points_count(self, joueur):
        point_mains = []
        for hand in joueur.main:
            points = 0
            for carte in hand:
                if carte[0][:2] == 'as':
                    if points + 11 > 21:
                        points += 1
                    else:
                        points += 11
                else:
                    points += carte[1]
            point_mains.append(points)
        return point_mains

    def resultat(self, points_main, points_croupier):
        for points in points_main:
            if points == 21:
                return "blackJack"
            if points > points_croupier and points<21:
                return "gagner"
            return "perdu"


    def attribution_Recompense(self): # Paul
        pass

############### MAIN ###############


jeuDeCarte1 = JeuDeCarte()
jeuDeCarte1.create_cartes_set()

main_joueur = [['as de pique', [1,10]], ['6 de carreau', 6]]



"""
-> Initialiser jeu de carte 
-> Initialiser joueurs + dealer

-> Ordre de jeu
"""




