n = int(input("Please enter a number for the board size -> "))

board = [0 for x in range(n*n)]
board[(n-1)*n] = 1

def displayBoard():
    for row in range(0,n):
        print(*board[row*n:(row+1)*n])
def getPosition():
    return board.index(1)

def movementInput():
    anInput = int(input("Please enter a movement key. (8:UP, 2:DOWN,4:LEFT,6:RIGHT"))
    while anInput not in [2,4,6,8]:
        anInput = int(input("Please enter a correct movement key. (8:UP, 2:DOWN,4:LEFT,6:RIGHT"))
    if anInput == 6 and getPosition()+1 not in [((x+1)*n) for x in range(n)]:

        temp = getPosition()
        board[getPosition()] =  0
        board[temp+1] = 1
    elif anInput == 8 and getPosition() - 5 >-1:

        temp = getPosition()
        board[getPosition()] = 0
        board[temp -5] = 1
    elif anInput == 2 and getPosition() + 5 < n*n:

        temp = getPosition()
        board[getPosition()] = 0
        board[temp +5] = 1
    elif anInput == 4 and getPosition()-1 not in [((x)*n)-1 for x in range(n)]:

        temp = getPosition()
        board[getPosition()] =  0
        board[temp-1] = 1
    else:
        print("Invalid Move")

while True:
    displayBoard()
    movementInput()
