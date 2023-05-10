import random 
import math 
from check_win import check_win
# making a board
winner = "None"
mode = input("Enter mode: ")
board = ["-","-","-","-","-","-","-","-","-"]
system_options = [0,1,2,3,4,5,6,7,8]
def print_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

# coding for player_1
# player letter is X
def player_1():
    n = int(input("Enter your position player_1: "))-1
    board[n] ="X"
    system_options.remove(n)
    print_board()
    print(" ")

# coding for player_2
# player_2 letter is O
def player_2():
    n = int(input("Enter your positon player_2: "))-1
    board[n] = "O"
    print_board()
    print(" ")

# coding for computer
# computer letter is O 
def system():
    n = random.choice(system_options)
    board[n] = "O"
    system_options.remove(n)
    print_board()
    print(" ")

# finding winner 
"""
def check_win():
    global winner 
    possibility = [(0,1,2),(0,3,6),(1,4,7),(2,5,8),(3,4,5),(6,7,8),(0,4,8),(2,4,6)]
    for i in possibility:
        p1 = i[0]
        p2 = i[1]
        p3 = i[2]
        line = board[p1]+board[p2]+board[p3] 
        if line == "XXX":
            winner = "Player_1"
        elif line == "OOO" and mode == "single_player":
            winner = "Computer"
        elif line == "OOO" and mode == "multi_player":
            winner = "Player_2"
"""
# coding for single player mode
def single_player():
    global winner 
    for i in range(1,9):
        if i%2!=0:
            player_1()
            check_win()
            if winner!="None":
                break
        else:
            system()
            check_win()
            if winner!="None":
                break 
# printing winner
    if winner!="None":
        print("Winner is "+winner)
    else:
        print("It's a tie")
# coding for multiplayer mode
def multi_player():
    global winner
    for i in range(1,9):
        if i%2!=0:
            player_1()
            check_win()
            if winner!="None":
                break
        else:
            player_2()
            check_win()
            if winner!="None":
                break
    if winner!="None":
        print("Winner is "+winner)
    else:
        print("It's a tie")
#checking mode 
if mode == "single_player":
    single_player()
else:
    multi_player()
