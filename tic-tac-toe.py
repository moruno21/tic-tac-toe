def printWelcome():
    print("Welcome to the tic-tac-toe game.  I wish you enjoy it, let's get started!")
    print("Those are all the positions:\n")
    print("[ 1 ][ 2 ][ 3 ]")
    print("[ 4 ][ 5 ][ 6 ]")
    print("[ 7 ][ 8 ][ 9 ]\n")


def printBoard():
    print('[' + board["1"] + '][' + board["2"] + '][' + board["3"] + ']')
    print('[' + board["4"] + '][' + board["5"] + '][' + board["6"] + ']')
    print('[' + board["7"] + '][' + board["8"] + '][' + board["9"] + ']\n')


def checkIfTicTacToe():
    if(board["1"] == board["2"] and board["2"] == board["3"] and board["3"] != ' '):
        return True
    if(board["4"] == board["5"] and board["5"] == board["6"] and board["6"] != ' '):
        return True
    if(board["7"] == board["8"] and board["8"] == board["9"] and board["9"] != ' '):
        return True
    if(board["1"] == board["4"] and board["4"] == board["7"] and board["7"] != ' '):
        return True
    if(board["2"] == board["5"] and board["5"] == board["8"] and board["8"] != ' '):
        return True
    if(board["3"] == board["6"] and board["6"] == board["9"] and board["9"] != ' '):
        return True
    if(board["1"] == board["5"] and board["5"] == board["9"] and board["9"] != ' '):
        return True
    if(board["3"] == board["5"] and board["5"] == board["7"] and board["7"] != ' '):
        return True


printWelcome()

board = {"1": ' ', "2": ' ', "3": ' ', "4": ' ',
         "5": ' ', "6": ' ', "7": ' ', "8": ' ', "9": ' '}

x = True  # Stablish whether it's X's or O's turn

while(True):
    if(x == True):
        position = input("X's turn, choose a position: ")
        board[position] = 'X'
        x = False  # O's turn
        printBoard()
    else:
        position = input("O's turn, choose a position: ")
        board[position] = 'O'
        x = True  # X's turn
        printBoard()
    if checkIfTicTacToe():
        break

if x == True:
    print("O wins!")
else:
    print("X wins!")
