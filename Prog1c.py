n = 4

def game():
    playerPos = n - 1
    printBoard(playerPos)
    while True:
        print("Up: 8, Down: 2, Left: 4, Right: 6")
        direction = eval(input("Please enter a direction:"))
        playerPos = movePlayer(playerPos, direction)
        printBoard(playerPos)

def printBoard(playerPos):
    positions = [0] * n * n
    posIx = len(positions) - 1

    for row in range(n):
        for col in range(n):
            if posIx == (playerPos):
                print("1", end="")
            else:
                print(positions[posIx], end="")
            posIx -= 1
        print()

def movePlayer(playerPos, direction):
    boundaryID = playerPos % n

    if direction == 8 and not playerPos >= (n * n) - n:
        playerPos += n
    elif direction == 2 and not playerPos <= n - 1:
        playerPos -= n
    elif direction == 4 and boundaryID != n - 1:
        playerPos += 1
    elif direction == 6 and boundaryID != 0:
        playerPos -= 1
    else:
        print("invalid move")
    return playerPos
game()
