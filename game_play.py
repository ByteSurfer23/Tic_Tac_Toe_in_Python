#from tic_tac_toe import player_1(),player_2(),system(),print_board(),mode
#from check_win import check_win,game_end 
#game for single_player
import tic_tac_toe
import check_win
def single_player():
    for i in range(1,10):
        if i%2 == 0:
            tic_tac_toe.player_1()
        else:
            tic_tac_toe.system()
        check_win.check_win()
        if check_win.game_end == True:
            break

# game for multi_player
def multi_player():
    for i in range(1,10):
        if i%2 == 0:
            tic_tac_toe.player_2()
        else:
            tic_tac_toe.player_1()
        check_win.check_win()
        if check_win.game_end == True:
            break
# choosing the mode and calling the respective functions 
if tic_tac_toe.mode == "singleplayer":
    single_player()
elif tic_tac_toe.mode == "multiplayer":
    multi_player()

