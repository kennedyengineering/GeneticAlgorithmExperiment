from creature_util import generateRandomPopulation
from creature_util import generateChildGeneration

def fitness(creature):
    answer = [1,1,1,1,0,0,0]
    wrong = 0
    for i in range(len(answer)):
        if answer[i] != creature.chromosome[i]:
            wrong += 1
    return len(answer) - wrong

generationNumber = 0
generation = generateRandomPopulation(10, 7)

# evolution variables
generation.sort(key=fitness, reverse=True)
fitnessVal = fitness(generation[0])

goal = 7
topPercentageBreeding = 0.4
mutationRate = 0.2

while fitnessVal < goal:
    generation = generateChildGeneration(fitness, generation, topPercentageBreeding, mutationRate)
    generationNumber += 1

    generation.sort(key=fitness, reverse=True)
    fitnessVal = fitness(generation[0])

    print("Generation: ", generationNumber, " with fitness: ", fitnessVal, " and chromosome: ", generation[0].chromosome)

print("Done! Found Chromosome: ", generation[0].chromosome)