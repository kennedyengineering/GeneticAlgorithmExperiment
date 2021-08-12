import random
from creature import Creature

def generateRandomChromosome(length: int):
    zeroCount = random.randint(0, length)
    oneCount = length - zeroCount

    chromosome = [0]*zeroCount + [1]*oneCount
    random.shuffle(chromosome)
    return chromosome

parent1 = Creature([1]*5)
parent0 = Creature([0]*5)

[child0, child1] = parent0.mate(parent1, 0.1)
