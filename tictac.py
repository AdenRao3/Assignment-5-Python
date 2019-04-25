# Created by: Aden Rao
# Created on: April 25, 2019
# This program is a two player tic tac toe in the command prompt. It lets player one choose a number on the board and then the other player chooses until one of them looses or until they tie.

# Choice list
choices = []

# Loop for the parts of the board
for x in range (0, 9) :
    choices.append(str(x + 1)) 

playerOneTurn = True # Player one turn true since they start 
winner = False # Winner starts of false and becomes true when someone wins

def printBoard() :
    # The prints used to have the correct numbers in the correct parts and to have the tic tac toe board look normal. 
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')

# Another loop for most of the game that end only when winner becomes true
while not winner :
    printBoard() # Prints tic tac toe board

    if playerOneTurn :
        print( "Player 1:") # Tells it's player one's turn
    else :
        print( "Player 2:") # Tells it's player two's turn once player one has gone

    try:
        choice = int(input(">> ")) # Input for them to enter their choice in between 1 to 9.
    except:
        print("please enter a valid part of the board") # If they enter a number more than 9 or something else that is not on the board.
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O': # If statement to see whether or not the player has entered a number that has already been moved on
        print("You can't move their, plase try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) : # Patterns to determine if the player won 
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) : # More patterns to determine if the player won
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n") # Text to tell the players which one of them won.