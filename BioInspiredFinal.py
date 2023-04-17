import random
import time
import os

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

mazeCopy = originalMaze.copy()

# For pacman fitness function:
# - Get better score for staying as far away from ghosts as possible
# - Really bad score if he gets caught by a ghost
# - Get better score for maximum coverage of the area aka not revisiting spots

# For ghost fitness function:
# - Higher score for either catching pacman or being the closest one to pacman
# - Goal is to minimize the number of steps it takes for them to catch pac man

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
        if symbol != 'X' and symbol != 'G' and symbol != 'P':
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
        if symbol != 'X' and symbol != 'G' and symbol != 'P':
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

if __name__ == "__main__":
    pacman = Pacman()
    pacman.xPos = 6
    pacman.yPos = 13

    # Generate the movement list for pacman
    pacmanMove = []
    ghosts = []

    for i in range(50):
        integer = random.randint(0,3)
        pacmanMove.append(integer)

    # Print out the screen how ever many steps we are taking this time
    for movement in pacmanMove:
        drawScene(pacman, ghosts)
        move(movement, pacman)
        print("Move: " + str(movement))
        time.sleep(0.5)
    drawScene(pacman, ghosts)

    # Either print of save to file final stats
    print("Steps Taken: " + str(len(pacmanMove)))
    print("Pacman Final Location: X -> " + str(pacman.xPos) + " Y -> " + str(pacman.yPos))
    print("Pacman Coverage Score: N/A")
    print("Pacman Fitness Score: N/A")
