import random
from board import Board

myboard = Board(5)
showboard = myboard.show_map()
print(showboard)
print()

# Begin hill climb

# Set a random start point
def RandStart(nBoard):
    r = random.seed()
    for i in nBoard:
        for j in nBoard[0]:
            print(f'i is {i}')
            print(f'j is {j}')

print(myboard.get_fitness())

# Using get_fitness to tell if a state is more optimal than the other


'''
def hillClimbing(problem):
    loop
    neighbor = highest-value successor of current
    if (neighbor.VALUE <= current.VALUE):
        return current.STATE
    current = neighbor
'''