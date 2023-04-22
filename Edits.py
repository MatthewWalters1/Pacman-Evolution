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
                child[i] = 2
            elif (child[i] == 1):
                child[i] = 3
            elif (child[i] == 2):
                child[i] = 0
            else:
                child[i] = 1
    return child

def evolvePac(population, verbose, bestFit, currGen, bestGen, ghosts, numTimeSteps, numSpaces):
    fitnesses = []
    bestDeathStep = 0
    bestCoverage = 0
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
            #drawScene(pacman, ghosts)
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
            #time.sleep(0.5)
            timeStep += 1
        #drawScene(pacman, ghosts)

        ### (Note from Matthew) The coverage score will look high, but we want to minimize this, 
            ### hence "numSpaces - coverage" (subtracting number of unique spaces from total possible spaces)
            ### again, because I think it would work better to minimize scores, not maximize.
        pacSet = set(pacPath)
        coverage = len(pacSet)
        cov = coverage
        if cov > bestCoverage:
            bestCoverage = cov
        if deathStep > bestDeathStep:
            bestDeathStep = deathStep
        pacman.fitness = 0
        pacman.fitness += (numSpaces - coverage)
        pacman.fitness += (numTimeSteps - deathStep)
        fitnesses.append(pacman.fitness)
        # Either print or save to file final stats
        # print("Steps Taken: " + str(len(pacmanMove)))
        # print("Pacman Final Location: X -> " + str(pacman.xPos) + " Y -> " + str(pacman.yPos))
        # print("Pacman Coverage Score: " + str(coverage))
        # print("Pacman Fitness Score: " + str(pacman.fitness))
    if (verbose):
        print("Best Fitness Ever (Gen " + str(bestGen) + "): " + str(bestFit))
        print("Best Fitness this Gen: " + str(min(fitnesses)) + " (Number of Spaces Touched out of " + str(numSpaces) + ": " + str(bestCoverage) + " and Number of Time Steps Survived: " + str(bestDeathStep) + ")")
        print("Worst Fitness this Gen: " + str(max(fitnesses)))
    if min(fitnesses) < bestFit:
        bestFit = min(fitnesses)
        bestGen = currGen
    return fitnesses, bestFit, bestGen

def evolveGhosts(population, verbose, bestFit, currGen, bestGen, pacman, numTimeSteps, numSpaces):
    fitnesses = []
    bestMinDist = 1000
    bestDeathStep = numTimeSteps
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
            #drawScene(pacman, ghosts)
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
            #time.sleep(0.5)
            timeStep += 1
        #drawScene(pacman, ghosts)

        minDist = 0
        for g in ghosts:
            minDist += g.minDist
        if minDist < bestMinDist:
            bestMinDist = minDist
        if deathStep < bestDeathStep:
            bestDeathStep = deathStep

        fitness = 0
        fitness += minDist
        fitness += deathStep
        fitnesses.append(fitness)
        
        # Either print or save to file final stats
        # print("Steps Taken: " + str(len(pacmanMove)))
        # print("Pacman Final Location: X -> " + str(pacman.xPos) + " Y -> " + str(pacman.yPos))
        # print("Pacman Coverage Score: " + str(coverage))
        # print("Pacman Fitness Score: " + str(pacman.fitness))
    if (verbose):
        print("Best Fitness Ever (Gen " + str(bestGen) + "): " + str(bestFit))
        print("Best Fitness this Gen: " + str(min(fitnesses)) + " (Minimum Distance from Pacman: " + str(bestMinDist) + " and Time Steps to Catch Pacman: " + str(bestDeathStep) + ")")
        print("Worst Fitness this Gen: " + str(max(fitnesses)))
    if min(fitnesses) < bestFit:
        bestFit = min(fitnesses)
        bestGen = currGen
    return fitnesses, bestFit, bestGen
        

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

    # From here, we need to write these stats from every member of every population to a csv, 
    # so we can graph it, and then play around more with hyperparameters (heatmap style). At that point, I think we're kind of done, 
    # other than making it go back and forth between pacman and the ghosts like, 50 times instead of 2 each

    numTimeSteps = 500
    popSize = 200
    probCrossover = 0.1
    probMutate = 0.01
    numGens = 50

    filename = "nts" + str(numTimeSteps) + "ps" + str(popSize) + "pc" + str(probCrossover) + "pm" + str(probMutate) + "ng" + str(numGens) + ".csv"

    outfile = open(filename, "w")
    outfile.write("Stage,Generation,Best_Fitness,Avg_Fitness,test\n")

    for test in range(50):
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

        bestFit = numTimeSteps + numSpaces
        bestGen = -1
        print("Evolving Pacman")
        for i in range(numGens):
            if i == numGens - 1 or i == 0:
                fitnesses, bestFit, bestGen = evolvePac(population, 1, bestFit, i, bestGen, ghosts, numTimeSteps, numSpaces)
            else:
                fitnesses, bestFit, bestGen = evolvePac(population, 0, bestFit, i, bestGen, ghosts, numTimeSteps, numSpaces)
            outfile.write("1, " + str(i) + ", " + str(min(fitnesses)) + ", " + str(np.mean(fitnesses)) + ", " + str(test) + "\n")
            population = newPop(population, fitnesses)

        currentBestPacman = population[fitnesses.index(min(fitnesses))]
        
        print("Evolving Ghosts")
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
        
        bestFit = 4*(abs(13 - 6) + abs(9 - 13)) + numTimeSteps
        bestGen = -1
        for i in range(numGens):
            if i == numGens - 1 or i == 0:
                fitnesses, bestFit, bestGen = evolveGhosts(ghostPop, 1, bestFit, i, bestGen, currentBestPacman, numTimeSteps, numSpaces)
            else:
                fitnesses, bestFit, bestGen = evolveGhosts(ghostPop, 0, bestFit, i, bestGen, currentBestPacman, numTimeSteps, numSpaces)
            outfile.write("2, " + str(i) + ", " + str(min(fitnesses)) + ", " + str(np.mean(fitnesses)) + ", " + str(test) + "\n")
            ghostPop = newGhostPop(ghostPop, fitnesses)
        
        currentBestGhosts = ghostPop[fitnesses.index(min(fitnesses))]

        # for epoch in numEpochs: all of the below code
        print("Evolving Pacman Again")
        bestFit = numTimeSteps + numSpaces
        bestGen = -1
        for i in range(numGens):
            if i == numGens - 1 or i == 0:
                fitnesses, bestFit, bestGen = evolvePac(population, 1, bestFit, i, bestGen, currentBestGhosts, numTimeSteps, numSpaces)
            else:
                fitnesses, bestFit, bestGen = evolvePac(population, 0, bestFit, i, bestGen, currentBestGhosts, numTimeSteps, numSpaces)
            outfile.write("3, " + str(i) + ", " + str(min(fitnesses)) + ", " + str(np.mean(fitnesses)) + ", " + str(test) + "\n")
            population = newPop(population, fitnesses)
        
        currentBestPacman = population[fitnesses.index(min(fitnesses))]

        print("Evolving Ghosts Again")
        bestFit = 4*(abs(13 - 6) + abs(9 - 13)) + numTimeSteps
        bestGen = -1
        for i in range(numGens):
            if i == numGens - 1 or i == 0:
                fitnesses, bestFit, bestGen = evolveGhosts(ghostPop, 1, bestFit, i, bestGen, currentBestPacman, numTimeSteps, numSpaces)
            else:
                fitnesses, bestFit, bestGen = evolveGhosts(ghostPop, 0, bestFit, i, bestGen, currentBestPacman, numTimeSteps, numSpaces)
            outfile.write("4, " + str(i) + ", " + str(min(fitnesses)) + ", " + str(np.mean(fitnesses)) + ", " + str(test) + "\n")
            ghostPop = newGhostPop(ghostPop, fitnesses)
        
        currentBestGhosts = ghostPop[fitnesses.index(min(fitnesses))]

    outfile.close()