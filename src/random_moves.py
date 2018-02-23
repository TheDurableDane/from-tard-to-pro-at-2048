import initialization as init
import pyautogui as pag
import random
import time


# Start the game
init.initialize_game()

# Play da damn game
moves = ['left', 'right', 'up', 'down']
n_games = 2     # number of games to play
for game in range(n_games):
    for i in range(100):
        move = moves[random.randint(0, 3)]
        pag.press(move)
        time.sleep(0.1)

    init.restart_game()
