import random
from creature import Creature

def generateRandomChromosome(length: int):
    zeroCount = random.randint(0, length)
    oneCount = length - zeroCount

    chromosome = [0]*zeroCount + [1]*oneCount
    random.shuffle(chromosome)
    return chromosome

def generateRandomPopulation(size: int, chromosomeLength: int):
    population = []
    for i in range(size):
        population.append(Creature(generateRandomChromosome(chromosomeLength)))

    return population

def generateChildGeneration(fitnessFunction, population, topPopulationPercentage: float, mutationPercentage: float):
    population.sort(key=fitnessFunction, reverse=True)

    topPopulationSize = int(len(population) * topPopulationPercentage)
    breedingPopulation = population[0:topPopulationSize]

    childPopulation = []
    for i in range(int(len(population)/2)):
        parents = random.sample(breedingPopulation, 2)
        childPopulation.extend(parents[0].mate(parents[1], mutationPercentage))

    return childPopulation