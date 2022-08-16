#GAME
import random
import time

n = 7

board = [0 for x in range(n*n)]
board[4:7] = ["X","X","X"]
board[14:17] = ["X","X","X"]
board[19:21] = ["X","X"]
board[31:35] = ["X","X","X","X"]
board[42:45] = ["X","X","X"]
board[28] = "X"
board[0] = "AB"

turn = 0
players = ["A","B"]
points = [0,0]
def displayBoard():
    for row in range(0,n):
        print(*board[row*n:(row+1)*n])

def diceRoll():
    return random.randint(1,6)

def getPosition(turn):
    players[turn]
    if players[turn] in board:
        return board.index(players[turn])
    elif board[0] == "AB":
        return 0
    else:
        return board.index("AB")

def movementInput(turn):
    global points
    directions = [2,4,6,8]
    anInput = directions[random.randint(0,len(directions)-1)]
    roll = diceRoll()
    print()
    print(f"{players[turn]} has rolled a {roll}.")
    print(anInput)
    if "AB" not in board:

        if "A" not in board :
            board[0]="A"
        elif "B" not in board :
            board[0] = "B"


    if anInput == 6 :
        print("Trying to Move Right by",roll)
        for x in range(1,roll+1):
            #Checks movement for each number on the dice up to the value rolled
            if getPosition(turn)+x in [((y+1)*n) for y in range(n)]:
                print("Not a valid move")
                print()
                return 1


        temp = getPosition(turn)
        if board[getPosition(turn)] != "AB":
            board[getPosition(turn)] =  0
            #print("Set old Position to 0")
        else:
            board[getPosition(turn)]= players[turn - 1]
            #print("Set old position to other player")
        if  board[temp+x]  =="X" :
            if board[0] not in ["A", "B"]:
                board[temp] = 0
                board[0] = players[turn]
            else:
                board[temp] = 0
                board[0] = "AB"
        elif board[temp+(1*roll)] ==0:

            board[temp+(1*roll)] = players[turn]
            #print("Empty space ahead, moved player")
        else:
            board[0] =players[turn-1]
            board[temp + (1*roll)] = players[turn]
            #print(f"None space ahead, {players[turn-1]} goes back")
            points[turn] +=1
            print("Moved Right")
    elif anInput == 8 :
        print("Trying to Move Up by", roll)
        for x in range(1,roll+1):
            #Checks movement for each number on the dice up to the value rolled
            if getPosition(turn) - (n*x) <= -1:
                print("Not a valid move")
                print()
                return 1
        temp = getPosition(turn)
        if board[getPosition(turn)] != "AB":
            board[getPosition(turn)] = 0
            #print("Set old Position to 0")
        else:
            board[getPosition(turn)] = players[turn - 1]
            #print("Set old position to other player")

        if  board[temp - (n*x)] =="X" :
            if board[0] not in ["A", "B"]:
                board[temp] = 0
                board[0] = players[turn]
            else:
                board[temp] = 0
                board[0] = "AB"
        elif board[temp-(n*roll)] ==0:
            board[temp -(n*roll)] = players[turn]
            #print("Empty space ahead, moved player")
        else:
            board[0] =players[turn-1]
            board[temp -(n*roll)] = players[turn]
            #print(f"None space ahead, {players[turn - 1]} goes back")
        print("Moved Up")
    elif anInput == 2  :
        print("Trying to Move Down by", roll)
        for x in range(1,roll+1):
            #Checks movement for each number on the dice up to the value rolled
            if getPosition(turn) + (n*x) >= n*n :
                print("Not a valid move")
                print()
                return 1
        temp = getPosition(turn)
        if board[getPosition(turn)] != "AB":
            board[getPosition(turn)] = 0
        else:
            board[getPosition(turn)] = players[turn - 1]


        if  board[temp + (n*x)] =="X" :
            if board[0] not in ["A", "B"]:
                board[temp] = 0
                board[0] = players[turn]
            else:
                board[temp] = 0
                board[0] = "AB"
        elif board[temp+(n*roll)] ==0:
            board[temp +(n*roll)] = players[turn]

        else:
            board[0] =players[turn-1]
            board[temp +(n*roll)] = players[turn]
        print("Moved Down")
    elif anInput == 4  :
        print("Trying to Move Left by", roll)
        for x in range(1,roll+1):
            #Checks movement for each number on the dice up to the value rolled
            if getPosition(turn) - (1 * x) in [((y) * n) - 1 for y in range(n)]:
                print("Not a valid move")
                print()
                return 1

        temp = getPosition(turn)
        if board[getPosition(turn)] != "AB":
            board[getPosition(turn)] = 0
        else:
            board[getPosition(turn)] = players[turn - 1]
            print(players[turn - 1])
        if  board[temp-x] =="X" :
            if board[0] not in ["A", "B"]:
                board[temp] = 0
                board[0] = players[turn]
            else:
                board[temp] = 0
                board[0] = "AB"
        elif board[temp-(1*roll )] ==0:
            board[temp -(1*roll )] = players[turn]
        else:
            board[0] =players[turn-1]
            board[temp -1] = players[turn]
        print("Moved Left")
    else:
        print("Invalid Move")
    print()

    return 1

while True:

    print(f"A has {points[0]} points, B has {points[1]} points")
    displayBoard()
    #print(diceRoll())


    print()
    if movementInput(turn) == 0:
        break
    if turn == 0:
        turn = 1
    else:
        turn = 0
    if board[len(board)-1] != 0:
        displayBoard()
        print(f"{board[len(board)-1]} wins!")
        break
    #time.sleep(1)
