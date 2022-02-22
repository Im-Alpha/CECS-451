# CECS 451 Assignment 3: Hill climbing
# Jacob Delgado
import random
import datetime
import numpy as np
from board import Board

# Create an identity matrix to generate board moves
idBoard = Board(5)  # dummy values for creating a class object
# idBoard.show_map()
identity = []
# Loop to create a list for the identity matrix
for a in range(5):
    row = []
    identity.append(row)
    # Loop columns
    for b in range(5):
        # If a = b, fill with 1
        if a == b:
            row.append(1)
        # Else fill with 0
        else:
            row.append(0)
# Fill board with identity list
for z in range(5):
    idBoard.map[z] = identity[z]
# idBoard.show_map()

# Attempt to find a child off the generated board
def find_child(board):
    startFit = board.get_fitness()
    # restartFit = startFit
    tempBoard = board
    childNode = tempBoard
    # print(f'startFit: {startFit}')
    for row in range(5):
        for col in range(5):
            for x in range(5):
                tempBoard.map[row] = identity[x]
                childFit = tempBoard.get_fitness()
                # print(f'childFit is: {childFit}')
                if (childFit < startFit) and (tempBoard != board):
                    childNode = tempBoard
                    startFit = childFit
                    # print(f'child found: {childFit}')
                    if childFit == 0:
                        # print(childNode.show_map())
                        return childNode
    # Generate new random board because no solution was found
    # tempBoard = Board(5)
    # if (restartFit == tempFit) or (tempFit > startFit):
    #     print('no child found')
    return childNode


def hillClimbWithRestart(board):
    # Create board that will hold the board from each pass to compare
    bestBoard = board

    # Loop until solution is found
    while True:
        # Get the least heuristic child from the find child helper function
        currentNode = find_child(bestBoard)

        # If there is no solution from the current board, generate a new one
        if (currentNode.get_fitness() != 0):
            currentNode = Board(5)

        # If the returned board has no conflicts, it's a solution
        if (currentNode.get_fitness() == 0):
            break
        # Make the current child the next node
        bestBoard = currentNode
    return currentNode

# Start timer
start_time = datetime.datetime.now()
# Generate first board
startBoard = Board(5)
# Begin Hill Climb
finalBoard = hillClimbWithRestart(startBoard)
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



