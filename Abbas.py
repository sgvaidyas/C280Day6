# Importing
import random

# Board setup
board=[" "] * 49
board[4:7] = "#", "#", "#"
board[14:16] = "#", "#", "#"
board[19:21] ="#", "#"
board[31:34] = "#", "#", "#", "#"
board[42:44] = "#", "#", "#"
board[28] = "#"
def draw_board(board):
    print(board[0:7],end="\n")
    print(board[7:14],end="\n")
    print(board[14:21],end="\n")
    print(board[21:28],end="\n")
    print(board[28:35],end="\n")
    print(board[35:42],end="\n")
    print(board[42:49],end="\n")

# Player 1
def player1(name1,name2,dice, pos1, pos2, kill1, kill2, moves1):
    print(name1)
    if kill1 == True:
        pos1 = 0; board[pos1] = name1[0];moves1.append(0)
    if pos1 == 48:
        return pos1
    elif pos1+dice <=48:
        if board[pos1+dice] != "#":
            board[pos1] = " "
            if pos2== 0:
                board[0] = name2[0]
            pos1 += dice; board[pos1] = name1[0];moves1.append(pos1)
        else:
            print(f"\n{name1} skipped a turn!")
            return pos1, kill2, moves1
    if pos1 == pos2:
        kill2 = True
        print(f"\n{name2} has been killed!\n")
        board[0] = name2[0]
    draw_board(board)
    return pos1, kill2,moves1

# Player 2
def player2(name1,name2,dice,pos1,pos2,kill1,kill2,moves2):
    print(name2)
    if kill2 == True:
        pos2 = 0; board[pos2] = name2[0]; moves2.append(0)
    if pos2 == 48:
        return pos2
    elif pos2+dice <=48:
        if board[pos2+dice] != "#":
            board[pos2] = " "
            if pos1== 0:
                board[0] = name1[0]
            pos2 += dice; board[pos2]= name2[0]; moves2.append(pos2)
        else:
            print(f"\n{name2} skipped a turn!")
            return pos2, kill1, moves2
    if pos2 == pos1:
        kill1 = True
        print(f"\n{name1} has been killed!\n")
        board[0] = name1[0]
    draw_board(board)
    return pos2, kill1,moves2

# The Game
def turn():
    moves1 = [0]; moves2 = [0]; pos1=0; pos2= 0;
    kill1 = False; kill2 = False;
    name1 = input("\nPlayer 1 enter your name: ")
    name2 = input("Player 2 enter your name: ")
    print()
    board[0] = name1[0] + name2[0]
    draw_board(board)
    while board[48] == " ":
        if pos1 == 48:
            break
        if pos2 ==48:
            break
        print('\n')
        action1 = ""
        action1 = input(f"{name1}: Hit enter to SPIN\n")
        dice1 = random.randint(1, 6);
        print("YOU ROLLED A", dice1, "\n")
        if pos1 != 48 and pos2 !=48:
            pos1,kill2,moves1 = player1(name1,name2,dice1,pos1,pos2,kill1,kill2,moves1)
            kill1 = False
        else:
            break
        print('\n')
        action2 = ""
        action2 = input(f"{name2}: Hit enter to SPIN\n")
        dice2 = random.randint(1, 6)
        print("YOU ROLLED A", dice2, "\n")
        if pos1 != 48 and pos2 !=48:
            pos2, kill1, moves2 = player2(name1,name2,dice2, pos1, pos2, kill1, kill2, moves2)
            kill2 = False
        else:
            break
    print("\nThe Game"); print(moves1, name1); print(moves2, name2)
    if board[48] == name2[0]:
        return print(f"\nWinner: Player 2 {name2}!!")
    elif board[48] == name1[0]:
        return print(f"\nWinner: Player 1 {name1}!!")
if __name__=='__main__':
    turn()
