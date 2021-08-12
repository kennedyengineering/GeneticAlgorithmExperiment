# part of genetic algorithm test
import random

 class Creature:
     def __init__(self, chromosome: list[bool]):
        # array
        self.chromosome = chromosome

     def mate(self, otherCreature: Creature, mutationPercentage: float) -> list[Creature]:
        # check for equal length
        if len(self.chromosome) != len(otherCreature.chromosome):
            return None

        # check if empty
        if len(self.chromosome) == 0 or len(otherCreature.chromosome) == 0:
            return None
        
        # crossover
        length = len(self.chromosome)
        splitIndex = random.randint(0, length-1)

        childChromosome0 = self.chromosome[0:splitIndex].extend(otherCreature.chromosome[splitIndex:])
        childChromosome1 = otherCreature.chromosome[0:splitIndex].extend(this.chromosome[splitIndex:])

        # mutate
        numberOfMutations = length*mutationPercentage
        mutationIndexes = random.sample(range(0, length-1), numberOfMutations)
        for index in mutationIndexes:
            childChromosome0[index] = not childChromosome0[index]
            childChromosome1[index] = not childChromosome1[index]

        return [Creature(childChromosome0), Creature(childChromosome1)]
