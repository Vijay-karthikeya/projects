import random
def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def ansi(col):
    if col.lower()=='red':
        return 31
    elif col.lower()=='green':
        return 32
    elif col.lower()=='yellow':
        return 33 
    else:
        return 34
def func(s,code):
    return("\33[{code}m".format(code=code)+s+"\33[0m".format(code=code))
def printColour(s,col):
    a=ansi(col)
    p=func(s,a)
    print(p)

def inputPlayerLetter():
# Lets the player type which letter they want to be.
# Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = input('Do you want to be X or O?\n')
    while(True):
        if(letter.upper()=='X' or letter.upper()=='O'):
            break
        else:
            print('Please pick either X or O')
            letter = input('Do you want to be X or O?\n')
    if letter.upper()=='X':
        return ['X','O']
    else:
        return ['O','X']

def isWinner(b,l):
    return (b[1]==b[2] and b[1]==b[3] and b[1]==l) or (b[4]==b[5] and b[4]==b[6] and b[5]==l) or (b[7]==b[8] and b[7]==b[9] and b[9]==l) or (b[7]==b[1] and b[7]==b[4] and b[1]==l) or (b[2]==b[8] and b[2]==b[5] and b[8]==l) or (b[3]==b[6] and b[3]==b[9] and b[9]==l) or (b[7]==b[5] and b[5]==b[3] and b[7]==l) or (b[1]==b[5] and b[1]==b[9] and b[9]==l)

def firstPlayer():
    if random.randint(0,1):
        return "player"
    else:
        return "computer"
    
def playAgain():
    a=input("Do you want to play again?(y/n)")
    return a.lower()=='y'

def makeMove(board,letter,move):
    board[move]=letter

def boardcopy(board):
    nb=[]
    for i in board:
        nb.append(i)
    return nb

def isSpaceFree(board,move):
    if move>9:
        return False
    else:
        return board[move]==' '

def playerMove(board):
    move=int(input('Make your move(1-9): '))
    while(True):
        if(isSpaceFree(board,move)):
            return move
        else:
            print('Space is not free or given move is out of bounds, please enter move between 1-9')
            move=int(input('Make your move(1-9): '))
            
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)            
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
    
def getComputerMove(board, computerLetter):
    
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

# First, check if we can win in the next move

    for i in range(1, 10):
        copy = boardcopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = boardcopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
# Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

    
def game():
    print('Welcome to Tic Tac Toe!\n')
    print('Defined grid:')
    print('Place your move according to the defined grid')
    print(' \n')
    grid=['0','1','2','3','4','5','6','7','8','9']
    drawBoard(grid)
    while True:
        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = firstPlayer()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                move = playerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    printColour('Hooray! You have won the game!','green')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        printColour(" The game is a draw!\n",'yellow')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    printColour('The computer has beaten you! You lose.','red')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        printColour("The game is a draw! \n",'yellow')
                        break
                    else:
                        turn = 'player'


        if not playAgain():
            break

game()
