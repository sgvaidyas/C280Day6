
import random

PlayerA = 0
PlayerB = 0
points = [0,0]
#                1       2      3      4      5      6      7
positionList = [" \033[36mAB\033[0;0m", "   ", "   ", "   ", "\033[33m███\033[0;0m", "\033[33m███\033[0;0m", "\033[33m███\033[0;0m",
                "   ", "   ", "   ", "   ", "   ", "   ", "   ",
                "\033[33m███\033[0;0m", "\033[33m███\033[0;0m", "\033[33m███\033[0;0m", "   ", "   ", "\033[33m███\033[0;0m", "\033[33m███\033[0;0m",
                "   ", "   ", "   ", "   ", "   ", "   ", "   ",
                "\033[33m███\033[0;0m", "   ", "   ", "\033[33m███\033[0;0m", "\033[33m███\033[0;0m", "\033[33m███\033[0;0m", "\033[33m███\033[0;0m",
                "   ", "   ", "   ", "   ", "   ", "   ", "   ",
                "\033[33m███\033[0;0m", "\033[33m███\033[0;0m", "\033[33m███\033[0;0m", "   ", "   ", "   ", "\033[35m███\033[0;0m"]


def printBoard():
    for i in range(0, 7 ** 2):
        print(positionList[i], end="|")
        if (i + 1) % 7 == 0:
            print("\n----------------------------")
    print("=================================")


def game(playerA, playerB):
    printBoard()
    position = [playerA, playerB]
    players = [" A ", " B "]
    direction = ["UP", "DOWN", "LEFT", "RIGHT"]
    currentPlayer = 0
    while True:
        print("Points: " + str(points[0]) + " - " + str(points[1]))
        print("It is time for\033[33m" + players[currentPlayer] + "\033[0;0mto play")
        input("Press enter to roll the dice:")
        currentRoll = random.randint(1, 6)
        currentDirection = random.randint(1, 4)
        print("You rolled a \033[34m" + str(currentRoll) + "\033[0;0m")
        print("In the \033[34m" + direction[currentDirection-1] + "\033[0;0m" + " direction.")
        positionList[position[currentPlayer]] = "   "
        if currentDirection == 4 and (position[currentPlayer] + currentRoll) % 7 != 0 and (position[currentPlayer] - currentRoll) < 49:
            position[currentPlayer] += currentRoll
        elif currentDirection == 3 and position[currentPlayer] % 7 != 0 and (position[currentPlayer] - currentRoll) >= 0:
            position[currentPlayer] -= currentRoll
        elif currentDirection == 2 and (position[currentPlayer] + 7 * currentRoll) < 7 ** 2:
            position[currentPlayer] += 7 * currentRoll
        elif currentDirection == 1 and (position[currentPlayer] - 7 * currentRoll) >= 0:
            position[currentPlayer] -= 7 * currentRoll

        if position[currentPlayer] == position[1 - currentPlayer] and position[currentPlayer] != 0:
            print("\033[1;31mPlayer" + players[currentPlayer] + "has killed" + players[1 - currentPlayer] + "\033[0;0m")
            points[currentPlayer] += 1
            position[1 - currentPlayer] = 0
        elif positionList[position[currentPlayer]] == "\033[33m███\033[0;0m":
            print("\033[33mYou hit a barrier. Go back to the start.\033[0;0m")
            position[currentPlayer] = 0
        positionList[position[currentPlayer]] = "\033[36m" + players[currentPlayer] + "\033[0;0m"
        currentPlayer = 1 - currentPlayer
        positionList[position[currentPlayer]] = "\033[36m" + players[currentPlayer] + "\033[0;0m"
        if (position[currentPlayer] + position[1 - currentPlayer]) == 0:
            positionList[position[currentPlayer]] = " \033[36mAB\033[0;0m"
        printBoard()
        if position[1 - currentPlayer] == 48:
            print("\033[32mPlayer" + players[1 - currentPlayer] + "has won!\033[0;0m")
            break


game(PlayerA, PlayerB)
