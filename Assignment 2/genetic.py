# CECS 451 Assignment 3: Genetic algorithm
# Jacob Delgado
import random
import datetime
import numpy as np
from board import Board


# Use genetic processes to find the solution
def geneSolution():
    # Create a list to hold the 8 states
    genePool = []

    # Fill the list with 8 random states
    for _ in range(8):
        genePool.append(Board(5))
        # genePool[a].show_map()

    # Create values to hold the two fittest boards
    # Initiate selection
    parent1, parent2 = selection(genePool)

    # Loop until solution is found
    while True:
        # Cross the fittest boards at a random point
        # List will be returned to make it easier to mutate
        parent1Cross, parent2Cross = crossover(parent1, parent2)

        # Mutate the lists at a random point
        # Get back board objects for fitness comparison
        childM1, childM2 = mutation(parent1Cross, parent2Cross)

        # Compare mutated fitness values
        if (childM1.get_fitness() < childM2.get_fitness() ):
            # Replace 2nd fittest parent with fittest child
            parent2 = childM1
        else:
            # Replace 2nd fittest parent with fittest child
            parent2 = childM2
        # Check if the solution was found
        if(parent1.get_fitness() == 0):
            return parent1
        elif(parent2.get_fitness() == 0):
            return parent2

# Find the fittest boards
def selection(genePool):
    # Create values that hold fitness levels
    firstFit = genePool[0].get_fitness()
    secondFit = genePool[0].get_fitness()

    # Create parent values
    parent1 = Board(5)
    parent2 = Board(5)

    # View all population fitness pool
    # for z in range(8):
    #     print(genePool[z].get_fitness())

    # Find the fittest of the population
    for a in range(1, 8):
        tempFit = genePool[a].get_fitness()
        if tempFit < firstFit:
            firstFit = tempFit
            # Update parent value to fittest board
            parent1 = genePool[a]
    # print(f'firstFit is {firstFit}')
    # parent1.show_map()

    # Find the second fittest of the population
    for a in range(1, 8):
        tempFit = genePool[a].get_fitness()
        # Find the second fittest board
        if (tempFit < secondFit) and (tempFit != firstFit):
            secondFit = tempFit
            # Update parent value to second fittest board
            parent2 = genePool[a]
    # print(f'secondFit is {secondFit}')
    # parent2.show_map()

    # Return fittest parent values
    return parent1, parent2


# Cross the fittest boards at a random point
def crossover(parent1, parent2):
    # Create lists for crossing values
    c1 = []
    c2 = []

    # Fill list with values of parents
    for x in range(5):
        for y in range(5):
            c1.append(parent1.map[x][y])
            c2.append(parent2.map[x][y])
    # print(f'c1 is {c1}')
    # print(f'c2 is {c2}')

    # Generate a random integer to split the genes
    split = random.randint(0, len(c1))

    for s in range(split):
        # Create a swap value holder for the first parent
        swap = c1[s]
        # Swap values from parent2 into parent1
        c1[s] = c2[s]
        # Swap values from parent1 into parent2
        c2[s] = swap
    return c1, c2


# Choosing a random position to mutate
def mutation(parent1, parent2):
    # Get random flip point
    rand = random.randint(0, len(parent1))

    # print(f'p1 is {parent1}')
    # print(f'p2 is {parent2}')

    # Create boards to return
    board1 = Board(5)
    board2 = Board(5)
    try:
        # Flip parent1 at random point
        if (parent1[rand] == 0):
            parent1[rand] = 1
        else:
            parent1[rand] = 0

        # Flip parent2 at random point
        if (parent2[rand] == 0):
            parent2[rand] = 1
        else:
            parent2[rand] = 0

        # Check queens
        sum1 = 0
        sum2 = 0

        # Make sure the boards did not remove any queens
        for check in range(len(parent1)):
            if parent1[check] == 1:
                sum1 += 1
        for check in range(len(parent2)):
            if parent2[check] == 1:
                sum2 += 1
        # Turn the mutated lists back into board objects
        if sum1 < 5 and sum2 >= 5:
            b1 = np.array(parent1).reshape((5, 5))
            for splice in range(5):
                board1.map[splice] = b1[splice]
        if sum2 < 5 and sum1 >= 5:
            b2 = np.array(parent2).reshape((5, 5))
            for splice2 in range(5):
                board2.map[splice2] = b2[splice2]
        # print('board1')
        # board1.show_map()
        #
        # print('board 2')
        # board2.show_map()
        #
        # print('------------------------')
        # Return the mutated parents
        return board1, board2
    except:
        # Check queens
        sum1 = 0
        sum2 = 0

        # Turn the mutated lists back into board objects
        if sum1 < 5 and sum2 >= 5:
            b1 = np.array(parent1).reshape((5, 5))
            for splice in range(5):
                board1.map[splice] = b1[splice]
        if sum2 < 5 and sum1 >= 5:
            b2 = np.array(parent2).reshape((5, 5))
            for splice2 in range(5):
                board2.map[splice2] = b2[splice2]

        # print('board1')
        # board1.show_map()
        #
        # print('board 2')
        # board2.show_map()
        #
        # print('------------------------')
        # Return the mutated parents
        return board1, board2

# Start timer
start_time = datetime.datetime.now()
# Begin gene algo
finalBoard = geneSolution()
# print('found solution')
end_time = datetime.datetime.now()
# Get Runtime
runTime = (end_time - start_time).total_seconds() * 1000
print(f'Running time: {int(runTime)}ms')
# finalBoard.show_map()

# Convert 0 to -
for x in range(5):
    for y in range(5):
        if finalBoard.map[x][y] == 0:
            finalBoard.map[x][y] = "-"

# Print Solution found
for z in finalBoard.map:
    print(' '.join(map(str, z)))



