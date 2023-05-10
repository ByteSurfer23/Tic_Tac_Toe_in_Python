import tic_tac_toe 
from tic_tac_toe import board
winner = None 
game_end = False
def check_win():
    global winner,game_end
    possibility = [(0,1,2),(0,3,6),(1,4,7),(2,5,8),(3,4,5),(6,7,8),(0,4,8),(2,4,6)]
    for i in possibility:
        p1 = i[0]
        p2 = i[1]
        p3 = i[2]
        line = board[p1]+board[p2]+board[p3] 
        if line == "XXX":
            winner = "Player_1"
            game_end = True
        elif line == "OOO" and tic_tac_toe.mode == "singleplayer":
            winner = "Computer"
            game_end = True
        elif line == "OOO" and tic_tac_toe.mode == "multiplayer":
            winner = "Player_2"
            game_end = True
    
    if game_end == True and winner != None:
        print(f"{winner} is the winner")
    elif winner == None and game_end == True:
        print("It's a tie")