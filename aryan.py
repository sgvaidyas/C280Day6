import random
a = ['-'] * 49
score = {'Player A': 0, 'PLayer B': 0}
playerPosition = {'Player A': 0, 'PLayer B': 0}
playerA = 'Player A'
playerB = 'PLayer B'
obstacles = [4, 5, 6, 14, 15, 16, 19, 20, 28, 31, 32, 33, 34, 42, 43, 44]
directions = ['right', 'left', 'up', 'down']
winner = ""
def printBoard():
    for i in range(len(a)):
        if i % 7 == 0:
            print()
        if i in obstacles:
            print(u"\u2588", end="\t")
        elif i==playerPosition[playerA] == playerPosition[playerB]:
            print('A,B',end="\t")
        elif i == playerPosition[playerA]:
            print('A', end="\t")
        elif i == playerPosition[playerB]:
            print('B', end="\t")
        elif i == 48:
            print('X', end="\t")
        else:
            print(a[i], end="\t")
def checkMove(roll, direction, player, other):
    if (direction == 'right'):
        if ((playerPosition[player] % 7) + roll) > 6:
            print("invalid to move {} here ".format(direction))
        elif (playerPosition[player] + roll) in obstacles:
            print("There is an obstacle blocking your path!!")
        elif (playerPosition[player] + roll) == playerPosition[other]:
            print("You have killed {} ".format(other))
            playerPosition[player] = playerPosition[player] + roll
            score[player] += 1
            playerPosition[other] = 0
        else:
            print("you have moved {} in direction {} ".format(roll, direction))
            playerPosition[player] = playerPosition[player] + roll
    elif (direction == 'left'):
        if ((playerPosition[player] % 7) - roll) < 0:
            print("invalid to move {} here ".format(direction))
        elif (playerPosition[player] - roll) in obstacles:
            print("There is an obstacle blocking your path!!")
        elif (playerPosition[player] - roll) == playerPosition[other]:
            print("You have killed {} ".format(other))
            playerPosition[player] = playerPosition[player] - roll
            score[player] += 1
            playerPosition[other] = 0
        else:
            print("you have moved {} in direction {} ".format(roll, direction))
            playerPosition[player] = playerPosition[player] - roll
    elif (direction == 'up'):
        if (playerPosition[player] - (7 * roll)) < 0:
            print("invalid to move {} here ".format(direction))
        elif (playerPosition[player] - (7 * roll)) in obstacles:
            print("There is an obstacle blocking your path!!")
        elif (playerPosition[player] - (7 * roll)) == playerPosition[other]:
            print("You have killed {} ".format(other))
            playerPosition[player] = (playerPosition[player] - (7 * roll))
            score[player] += 1
            playerPosition[other] = 0
        else:
            print("you have moved {} in direction {} ".format(roll, direction))
            playerPosition[player] = (playerPosition[player] - (7 * roll))
    elif (direction == 'down'):
        if (playerPosition[player] + (7 * roll)) > 48:
            print("invalid to move {} here ".format(direction))
        elif (playerPosition[player] + (7 * roll)) in obstacles:
            print("There is an obstacle blocking your path!!")
        elif (playerPosition[player] + (7 * roll)) == playerPosition[other]:
            print("You have killed {} ".format(other))
            playerPosition[player] = (playerPosition[player] + (7 * roll))
            score[player] += 1
            playerPosition[other] = 0
        else:
            print("you have moved {} in direction {} ".format(roll, direction))
            playerPosition[player] = (playerPosition[player] + (7 * roll))
    if playerPosition[player] == 48:
        print("Winner: {} ".format(player))
        return True
    else:
        return False
def Game():
    turn = 0
    won = False
    while not won:
        if turn % 2 == 0:
            player = playerA
            other = playerB
            print()
            print("{}'s Turn".format(player))
            input("Press Enter to Randomise Dice and Direction")
            direction = random.choice(directions)
            roll = random.randint(1, 6)
            print("Rolled: {} in {} Direction ".format(roll, direction))
            won = checkMove(roll, direction, player, other)
            printBoard()
        else:
            print()
            other = playerA
            player = playerB
            print("{}'s Turn".format(player))
            input("Press Enter to Randomise Dice and Direction")
            direction = random.choice(directions)
            roll = random.randint(1, 6)
            print("Rolled: {} in {} Direction ".format(roll, direction))
            won = checkMove(roll, direction, player, other)
            printBoard()
        turn = turn +1
Game()
