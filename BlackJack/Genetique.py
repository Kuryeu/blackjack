import random
from operator import itemgetter
from Memoire import Memoire
from BlackJack import BlackJack
import numpy as np
from math import ceil
class Genetique:

    def __init__(self, population, tRepro, tMuta):
        self.taille = population
        self.population = [] # Format [Matrice , score]
        self.nbEstimation = 0
        self.tR = tRepro
        self.tM = tMuta
        self.creerPopulationInitiale()
        self.best = (None, None)
        self.main()

    def creerPopulationInitiale(self):
        for i in range(self.taille):
            print(i)
            memo = Memoire()
            while not memo.isAllPlaced():
                x = BlackJack(4, memo, True)
                memo = x.PartiePopInitiale()

            memo = self.estimerSolution(memo)
            self.population.append([memo, memo.getScore()])
            print("Fin de l'initialisation")

    def reproduction(self, parent1, parent2):
        enfant1 = Memoire()
        enfant2 = Memoire()
        c = 0
        for i in range(len(parent1.matrice)):
            for j in range(len(parent1.matrice[i])):
                if c % 2 == 0:
                    enfant1.matrice[i, j] = parent1.matrice[i, j]
                    enfant2.matrice[i, j] = parent2.matrice[i, j]
                else:
                    enfant2.matrice[i, j] = parent1.matrice[i, j]
                    enfant1.matrice[i, j] = parent2.matrice[i, j]

        enfant1 = self.estimerSolution(enfant1)
        enfant1 = self.estimerSolution(enfant2)
        if enfant1.getScore() > enfant2.getScore():
            return [enfant1, enfant1.getScore()]
        else:
            return [enfant2, enfant2.getScore()]


    def estimerSolution(self, solution):
        for _ in range(10000):
            solution = BlackJack(4, solution, False).PartieNormale()
        self.nbEstimation += 1
        return solution


    def remplacementPopulation(self, enfants):
        self.population += enfants
        self.population = sorted(self.population, key=itemgetter(1), reverse=True)
        self.population = self.population[:self.taille]

    def mutation(self, solution):
        i = random.randrange(len(solution.matrice))
        j = random.randrange(len(solution.matrice[i]))
        solution.matrice[i, j] = random.randint(0, 3)
        solution = self.estimerSolution(solution)
        return [solution, solution.getScore()]

    def main(self):
        gen = 0
        while self.nbEstimation < 10000:
            gen+=1
            print("Gen :", gen, self.nbEstimation)
            enfants = []
            for i in range(ceil(self.tR * self.taille)):
                parent1, parent2 = random.sample(self.population, 2)
                enfant = self.reproduction(parent1[0], parent2[0])
                if random.random() < self.tM:
                    if self.best[1] is not None and enfant[1] > self.best[1]:
                        self.best = enfant
                    else:
                        enfant = self.mutation(enfant[0])
                enfants.append(enfant)

                enfants.append(enfant)
            self.remplacementPopulation(enfants)
            self.population = sorted(self.population, key=itemgetter(1), reverse=True)
            if self.best[0] is None or self.best[1] < self.population[0][1]:
                self.best = self.population[0]
                print(self.best[1])