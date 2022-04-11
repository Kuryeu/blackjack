import random
from operator import itemgetter

class Genetique:

    def __init__(self, population, tRepro, tMuta):
        self.taille = population
        self.population = [] # Format [Matrice , score]
        self.nbEstimation = 0
        self.tR = tReproduction
        self.tM = tMutation
        self.creerPopulationInitiale()
        self.best = (None, None)

        def creerPopulationInitiale(self):
            for i in range(self.taille):
                pass

        def mutation(self, solution):
            pass

        def reproduction(self, parent1, parent2):
            enfant1 = Memoire()
            enfant2 = Memoire()

        def estimerSolution(self, solution):
            pass

        def remplacementPopulation(self, enfants):
            self.population += enfants
            self.population = sorted(self.population, key=itemgetter(1), reverse=True)
            self.population = self.population[:self.taille]

        def main(self):

            while self.nbEstimation < 10000:
                enfants = []
                for i in range(ceil(self.tR * self.taille)):
                    parent1, parent2 = random.sample(self.population, 2)
                    enfant = self.reproduction(parent1[0], parent2[0])
                if random.random() < self.tM:
                    if self.best[1] is not None and enfant[1] > self.best[1]: # Au cas ou on veille muter une solution meilleure que celle actuelle
                        self.best = enfant
                    else:
                        enfant = self.mutation(enfant[0])
                enfants.append(enfant)
                self.remplacementPopulation(enfants)
                self.population = sorted(self.population, key=itemgetter(1), reverse=True)
                if self.best[0] is None or self.best[1] < self.population[0][1]:
                    self.best = self.population[0]
                    self.best[0].show()
                    print(self.best[1])