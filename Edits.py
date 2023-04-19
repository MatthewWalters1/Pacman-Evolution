import random
import time
import os
import numpy as np

# Starting maze array that keeps track of where pacman and the ghosts can move
originalMaze = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
    ['X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X'], 
    ['X', '0', 'X', 'X', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', 'X', 'X', '0', 'X'], 
    ['X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X'], 
    ['X', '0', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', '0', 'X'], 
    ['X', '0', '0', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', '0', '0', 'X'], 
    ['X', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X'], 
    ['X', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X'], 
    ['|', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X', 'X', 'X', 'X', 'X', 'X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '|'], 
    ['X', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X'], 
    ['X', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X'], 
    ['X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X'], 
    ['X', '0', 'X', 'X', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', 'X', 'X', '0', 'X'], 
    ['X', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', 'X'], 
    ['X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X'], 
    ['X', '0', '0', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', 'X', 'X', '0', '0', '0', '0', '0', '0', 'X'], 
    ['X', '0', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '0', 'X', 'X', '0', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '0', 'X'], 
    ['X', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'X'], 
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

# You could hard code this (there are 244 possible spaces for pacman to touch), 
#  however, if you wanted to later change the board, this is more general
numSpaces = 0
for i in originalMaze:
    for j in i:
        if j != 'X':
            numSpaces += 1

mazeCopy = originalMaze.copy()


### (Note from Matthew) I think it makes more sense to favor the lowest scores than to have an arbitrarily high fitness score
    ### By this I mean, make the tournament selection (or whatever mechanic we have for evolution) select the next generation
    ### via the lowest score. With a minimal score (0), it's easier to recognize how good the score is, 
    ### since the maximum scores given our criteria will be some weird number like 829 or 1273

# For pacman fitness function:
# - Get better score for staying as far away from ghosts as possible
### - I don't think he should be penalized for getting near ghosts if he can actually avoid them, but this would mirror the fitness score of the ghosts
# - Really bad score if he gets caught by a ghost
### - I think this should hurt pacman's score by the number of timesteps remaining when he gets hit by a ghost
# - Get better score for maximum coverage of the area aka not revisiting spots
### - I implemented this to be numSpaces subtracted by the number of unique spaces touched

# For ghost fitness function:
# - Higher score for either catching pacman or being the closest one to pacman
### - Yes, this should be the inverse of pacman's fitness (best score is 0, add the number of time steps before they catch him)
# - Goal is to minimize the number of steps it takes for them to catch pacman
### - also add to the score the minimum distance they achieved from pacman (the best path is the one closest to him)

# Class to manage the position and the movement of the ghost
class Ghost:
    xPos = 0
    yPos = 0
    
    # A movespeed of 1 enables that ghost to move one position every step
    moveSpeed = 1
    
# Class to manage the position and movement of pacman
class Pacman:
    xPos = 0
    yPos = 0
    
    moveSpeed = 1
    fitness = 0
    path = []
    
# Movement function that manages the movement of pacman and the ghosts
def move(movement, character):

    # Reset the maze to erase where the character was
    mazeCopy[character.yPos][character.xPos] = '0'
    
    # Character is moving up
    if movement == 0:
        # You can't move into a wall or a ghost or pacman we will check that collision later
        symbol = mazeCopy[character.yPos - character.moveSpeed][character.xPos]
        if symbol != 'X' and symbol != 'G' and symbol != 'P':
            character.yPos -= 1
    
    # Character is moving left
    elif movement == 1:
        # You can't move into a wall or a ghost or pacman we will check that collision later
        symbol = mazeCopy[character.yPos][character.xPos - character.moveSpeed]
        if symbol == '|':
            character.xPos += 25
        elif symbol != 'X' and symbol != 'G' and symbol != 'P':
            character.xPos -= 1
    
    # Character is moving down
    elif movement == 2:
        # You can't move into a wall or a ghost or pacman we will check that collision later
        symbol = mazeCopy[character.yPos + character.moveSpeed][character.xPos]
        if symbol != 'X' and symbol != 'G' and symbol != 'P':
            character.yPos += 1
    
    #Character is moving right
    elif movement == 3:
        # You can't move into a wall or a ghost or pacman we will check that collision later
        symbol = mazeCopy[character.yPos][character.xPos + character.moveSpeed]
        if symbol == '|':
            character.xPos -= 25
        elif symbol != 'X' and symbol != 'G' and symbol != 'P':
            character.xPos += 1
    
    # Error in characrer movement
    else:
        print("Incorrect movement integer was provided!")

def drawScene(pacman, ghosts):
    # Reset the screen
    os.system('cls')

    # Set the position pacman is located as a P
    mazeCopy[pacman.yPos][pacman.xPos] = 'P'

    # Set the positions of the ghosts as a G

    # Draw the maze
    for i in range(len(mazeCopy)):
        for j in range(len(mazeCopy[0])):
            if mazeCopy[i][j] == '0':
                print(' ', end='')
            else:
                print(mazeCopy[i][j], end='')

        print("")

def tournament_selection(fitnesses, ts):
    # Return index of selected individual
    tourn = np.random.choice(range(len(fitnesses)), ts, replace=False)
    tourn_fit = [fitnesses[i] for i in tourn]
    # select lowest fitness in the tournament
    return tourn[np.argmin(tourn_fit)]

def uniform_crossover(probCrossover, parent1, parent2):
    # Return children
    if (np.random.random() < probCrossover):
        path = len(parent1)
        child1 = np.zeros(path)
        child2 = np.zeros(path)
        for i in range(path):
            if (np.random.random() < 0.5):
                child1[i] = parent1[i]
                child2[i] = parent2[i]
            else:
                child1[i] = parent2[i]
                child2[i] = parent1[i]
    else:
        child1 = parent1.copy()
        child2 = parent2.copy()
    return child1, child2

def mutation(probMutate, parent):
    # Return child
    path = len(parent)
    child = parent.copy()
    for i in range(path):
        if (np.random.random() < probMutate):
            if (child[i] == 0):
                child[i] = 2
            elif (child[i] == 1):
                child[i] = 3
            elif (child[i] == 2):
                child[i] = 0
            else:
                child[i] = 1
    return child

def evolvePac(population, verbose, bestFit, currEpoch, bestEpoch):
    fitnesses = []
    for pacman in population:
        pacmanMove = pacman.path
        ghosts = []

        # Print out the screen how ever many steps we are taking this time
        pacPath = []
        timeStep = 0
        alive = 0
        # since part of the fitness is how many steps were left when pacman dies, set deathStep to numTimeSteps while he's alive,
        # and if he dies, set the deathStep to that step 
        # (I think it's best for the ghosts' evolution to always run every step even after pacman dies, but only set the deathStep the first time)
        deathStep = numTimeSteps
        for movement in pacmanMove:
            #drawScene(pacman, ghosts)
            move(movement, pacman)
            pacPath.append(str(pacman.xPos) + '-' + str(pacman.yPos))
            for g in ghosts:
                if pacman.xPos == g.xPos and pacman.yPos == g.yPos and alive == 0:
                    deathStep = timeStep
                    alive = 1
            #print("Move: " + str(movement))
            #time.sleep(0.2)
            timeStep += 1
        #drawScene(pacman, ghosts)

        ### (Note from Matthew) The coverage score will look high, but we want to minimize this, 
            ### hence "numSpaces - coverage" (subtracting number of unique spaces from total possible spaces)
            ### again, because I think it would work better to minimize scores, not maximize.
        pacSet = set(pacPath)
        coverage = len(pacSet)
        pacman.fitness = 0
        pacman.fitness += numSpaces - coverage
        pacman.fitness += numTimeSteps - deathStep
        fitnesses.append(pacman.fitness)
        # Either print or save to file final stats
        # print("Steps Taken: " + str(len(pacmanMove)))
        # print("Pacman Final Location: X -> " + str(pacman.xPos) + " Y -> " + str(pacman.yPos))
        # print("Pacman Coverage Score: " + str(coverage))
        # print("Pacman Fitness Score: " + str(pacman.fitness))
    if (verbose):
        print("Best Coverage (Epoch " + str(bestEpoch) + "): " + str(bestFit))
        print("Best Coverage this Epoch: " + str(min(fitnesses)))
        print("Worst Coverage this Epoch: " + str(max(fitnesses)))
    if min(fitnesses) < bestFit:
        bestFit = min(fitnesses)
        bestEpoch = currEpoch
    return fitnesses, bestFit, bestEpoch

def newPop(population):
    parents = [tournament_selection(fitnesses, 3) for i in range(popSize)]
    # Create children in pairs
    children = np.zeros((popSize, numTimeSteps))
    for i in range(0, popSize, 2):
        child1, child2 = uniform_crossover(probCrossover, population[parents[i]].path, population[parents[i+1]].path)
        child1 = mutation(probMutate, child1)
        child2 = mutation(probMutate, child2)
        children[i,:] = child1[:]
        children[i+1,:] = child2[:]
    # Replace population with children
    population = []
    for i in children:
        pacman = Pacman()
        pacman.xPos = 6
        pacman.yPos = 13
        pacman.path = i
        population.append(pacman)
    return population

if __name__ == "__main__":

    numTimeSteps = 1000
    popSize = 10
    probCrossover = 0.1
    probMutate = 0.1
    numEpochs = 5000

    population = []
    for i in range(popSize):
        pacman = Pacman()
        pacman.xPos = 6
        pacman.yPos = 13
        pacman.path = []
        for j in range(numTimeSteps):
            integer = random.randint(0,3)
            pacman.path.append(integer)
        population.append(pacman)

    bestFit = 244
    bestEpoch = -1
    fitnesses, bestFit, bestEpoch = evolvePac(population, 1, bestFit, -1, bestEpoch)
    for i in range(numEpochs):
        population = newPop(population)
        if i == numEpochs - 1:
            fitnesses, bestFit, bestEpoch = evolvePac(population, 1, bestFit, i, bestEpoch)
        else:
            fitnesses, bestFit, bestEpoch = evolvePac(population, 0, bestFit, i, bestEpoch)
