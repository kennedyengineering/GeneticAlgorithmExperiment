import random
def generateRandomChromosome(length: int):
    zeroCount = random.randint(0, length)
    oneCount = length - zeroCount

    chromosome = [0]*zeroCount + [1]*oneCount
    random.shuffle(chromosome)
    return chromosome

