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

# You could hard code this (there are 242 possible spaces for pacman to touch), 
#  however, if you wanted to later change the board, this is more general
numSpaces = 0
for i in originalMaze:
    for j in i:
        if (j != 'X' and j != '|'):
            numSpaces += 1

mazeCopy = originalMaze.copy()


### (Note from Matthew) I think it makes more sense to favor the lowest scores than to have an arbitrarily high fitness score
    ### By this I mean, make the tournament selection (or whatever mechanic we have for evolution) select the next generation
    ### via the lowest score. With a minimal score (0), it's easier to recognize how good the score is, 
    ### since the maximum scores given our criteria will be some weird number like 829 or 1273

# For pacman fitness function:
# - Get better score for staying as far away from ghosts as possible
# - Really bad score if he gets caught by a ghost
# - Get better score for maximum coverage of the area aka not revisiting spots

# For ghost fitness function:
# - Higher score for either catching pacman or being the closest one to pacman
# - Goal is to minimize the number of steps it takes for them to catch pacman

# Class to manage the position and the movement of the ghost
class Ghost:
    xPos = 0
    yPos = 0
    team = 'G'
    
    # A movespeed of 1 enables that ghost to move one position every step
    moveSpeed = 1
    minDist = 0
    path = []
    
# Class to manage the position and movement of pacman
class Pacman:
    xPos = 0
    yPos = 0
    team = 'P'
    
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
        if symbol != 'X' and symbol != 'G':
            character.yPos -= 1
    
    # Character is moving left
    elif movement == 1:
        # You can't move into a wall or a ghost or pacman we will check that collision later
        symbol = mazeCopy[character.yPos][character.xPos - character.moveSpeed]
        if symbol == '|':
            character.xPos += 25
        elif symbol != 'X' and symbol != 'G':
            character.xPos -= 1
    
    # Character is moving down
    elif movement == 2:
        # You can't move into a wall or a ghost or pacman we will check that collision later
        symbol = mazeCopy[character.yPos + character.moveSpeed][character.xPos]
        if symbol != 'X' and symbol != 'G':
            character.yPos += 1
    
    #Character is moving right
    elif movement == 3:
        # You can't move into a wall or a ghost or pacman we will check that collision later
        symbol = mazeCopy[character.yPos][character.xPos + character.moveSpeed]
        if symbol == '|':
            character.xPos -= 25
        elif symbol != 'X' and symbol != 'G':
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
    for g in ghosts:
        mazeCopy[g.yPos][g.xPos] = 'G'

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
                child[i] = 1
            elif (child[i] == 1):
                child[i] = 2
            elif (child[i] == 2):
                child[i] = 3
            else:
                child[i] = 0
    return child

def evolvePac(population, ghosts, numTimeSteps, numSpaces, showGame):
    fitnesses = []
    for pacman in population:
        pacmanMove = pacman.path
        pacman.xPos = 6
        pacman.yPos = 13
        for g in ghosts:
            g.xPos = 13
            g.yPos = 9
        # Print out the screen how ever many steps we are taking this time
        pacPath = []
        timeStep = 0
        alive = 0
        # since part of the fitness is how many steps were left when pacman dies, set deathStep to numTimeSteps while he's alive,
        # and if he dies, set the deathStep to that step 
        deathStep = numTimeSteps
        for movement in range(len(pacmanMove)):
            # if (showGame):
            #     drawScene(pacman, ghosts)
            move(pacmanMove[movement], pacman)
            pacPath.append(str(pacman.xPos) + '-' + str(pacman.yPos))
            for g in ghosts:
                move(g.path[movement], g)
                if (pacman.xPos == g.xPos and pacman.yPos == g.yPos):
                    deathStep = timeStep
                    alive = 1
                    break
            if (alive == 1):
                break
            #print("Move: " + str(pacmanMove[movement]))
            # if (showGame):
            #     time.sleep(0.5)
            timeStep += 1
        # if (showGame):
        #     drawScene(pacman, ghosts)

        pacSet = set(pacPath)
        coverage = len(pacSet)
        
        pacman.fitness = 0
        pacman.fitness += (numSpaces - coverage)
        pacman.fitness += (numTimeSteps - deathStep)
        fitnesses.append(pacman.fitness)
        
    return fitnesses

def evolveGhosts(population, pacman, numTimeSteps, numSpaces, showGame):
    fitnesses = []
    for ghosts in population:
        pacmanMove = pacman.path
        pacman.xPos = 6
        pacman.yPos = 13
        for g in ghosts:
            g.xPos = 13
            g.yPos = 9
        # Print out the screen how ever many steps we are taking this time
        timeStep = 0
        alive = 0
        # since part of the fitness is how many steps were left when pacman dies, set deathStep to numTimeSteps while he's alive,
        # and if he dies, set the deathStep to that step
        deathStep = numTimeSteps
        for movement in range(len(pacmanMove)):
            # if (showGame):
            #     drawScene(pacman, ghosts)
            move(pacmanMove[movement], pacman)
            for g in ghosts:
                move(g.path[movement], g)
                minDist = abs(g.xPos - pacman.xPos) + abs(g.yPos - pacman.yPos)
                if minDist < g.minDist:
                    g.minDist = minDist
                if (pacman.xPos == g.xPos and pacman.yPos == g.yPos):
                    deathStep = timeStep
                    alive = 1
            #print("Move: " + str(pacmanMove[movement]))
            # if (showGame):
            #     time.sleep(0.5)
            timeStep += 1
        # if (showGame):
        #     drawScene(pacman, ghosts)

        minDist = 0
        for g in ghosts:
            minDist += g.minDist

        fitness = 0
        fitness += minDist
        fitness += deathStep
        fitnesses.append(fitness)
    
    return fitnesses

def newPop(population, fitnesses):
    parents = [tournament_selection(fitnesses, 6) for i in range(popSize)]
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

def newGhostPop(population, fitnesses):
    parents = [tournament_selection(fitnesses, 6) for i in range(popSize)]
    # Create children in pairs
    children = []
    for i in range(0, popSize, 2):
        childset = []
        for g in range(4):
            child1 = population[parents[i]][g].path
            child2 = population[parents[i+1]][g].path
            child1, child2 = uniform_crossover(probCrossover, child1, child2)
            child1 = mutation(probMutate, child1)
            child2 = mutation(probMutate, child2)
            childset.append(child1)
            childset.append(child2)
        children.append(childset)
    population = []
    for i in children:
        populationset = []
        for j in i:
            g = Ghost()
            g.xPos = 13
            g.yPos = 9
            g.path = j
            populationset.append(g)
        population.append(populationset)
    return population

if __name__ == "__main__":
    
    numTimeSteps = 500
    popSize = 500
    probCrossover = 0.01
    probMutate = 0.01
    numGens = 50
    numEpochs = 50

    filename = "hundredEpochs.csv"
    outfile = open(filename, "w")
    outfile.write("Team,Generation,Best_Fitness,Avg_Fitness,Epoch,Test\n")
    for test in range(5):
        print(test)
        # First Pacman Population
        population = []
        for i in range(popSize):
            pacman = Pacman()
            pacman.xPos = 6
            pacman.yPos = 13
            pacman.team = 'P'
            pacman.path = []
            for j in range(numTimeSteps):
                integer = random.randint(0,3)
                pacman.path.append(integer)
            population.append(pacman)

        # Original Ghosts' Paths
        ghosts = []
        for i in range(4):
            g = Ghost()
            g.xPos = 13
            g.yPos = 9
            g.team = 'G'
            g.path = []
            g.distPac = 1000
            for j in range(numTimeSteps):
                integer = random.randint(0,3)
                g.path.append(integer)
            ghosts.append(g)

        # print("Evolving Pacman")
        for i in range(numGens):
            # if you want to see the gameplay, change the zero here to a one, you probably would only want a popSize of 1
            fitnesses = evolvePac(population, ghosts, numTimeSteps, numSpaces, 0)
            outfile.write("0, " + str(i) + ", " + str(min(fitnesses)) + ", " + str(np.mean(fitnesses)) + ", " + str(0) + ", " + str(test) + "\n")
            population = newPop(population, fitnesses)
        fitnesses = evolvePac(population, ghosts, numTimeSteps, numSpaces, 0)
        currentBestPacman = population[fitnesses.index(min(fitnesses))]
        
        # print("Evolving Ghosts")
        ghostPop = []
        ghostPop.append(ghosts)
        for i in range(popSize - 1):
            ghosts = []
            for i in range(4):
                g = Ghost()
                g.xPos = 13
                g.yPos = 9
                g.team = 'G'
                g.path = []
                g.minDist = abs(13 - 6) + abs(9 - 13)
                for j in range(numTimeSteps):
                    integer = random.randint(0,3)
                    g.path.append(integer)
                ghosts.append(g)
            ghostPop.append(ghosts)
        
        for i in range(numGens):
            fitnesses = evolveGhosts(ghostPop, currentBestPacman, numTimeSteps, numSpaces, 0)
            outfile.write("1, " + str(i) + ", " + str(min(fitnesses)) + ", " + str(np.mean(fitnesses)) + ", " + str(0) + ", " + str(test) + "\n")
            ghostPop = newGhostPop(ghostPop, fitnesses)
        fitnesses = evolveGhosts(ghostPop, currentBestPacman, numTimeSteps, numSpaces, 0)
        currentBestGhosts = ghostPop[fitnesses.index(min(fitnesses))]

        # for epoch in numEpochs: all of the below code
        for epoch in range(1, numEpochs):
            print("test:", test)
            print("epoch:", epoch)
            # print("Evolving Pacman Again")
            for i in range(numGens):
                fitnesses = evolvePac(population, currentBestGhosts, numTimeSteps, numSpaces, 0)
                outfile.write("0, " + str(i) + ", " + str(min(fitnesses)) + ", " + str(np.mean(fitnesses)) + ", " + str(epoch) + ", " + str(test) + "\n")
                population = newPop(population, fitnesses)
            fitnesses = evolvePac(population, currentBestGhosts, numTimeSteps, numSpaces, 0)
            currentBestPacman = population[fitnesses.index(min(fitnesses))]

            # print("Evolving Ghosts Again")
            for i in range(numGens):
                fitnesses = evolveGhosts(ghostPop, currentBestPacman, numTimeSteps, numSpaces, 0)
                outfile.write("1, " + str(i) + ", " + str(min(fitnesses)) + ", " + str(np.mean(fitnesses)) + ", " + str(epoch) + ", " + str(test) + "\n")
                ghostPop = newGhostPop(ghostPop, fitnesses)
            fitnesses = evolveGhosts(ghostPop, currentBestPacman, numTimeSteps, numSpaces, 0)
            currentBestGhosts = ghostPop[fitnesses.index(min(fitnesses))]

    outfile.close()