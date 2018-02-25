import initialization as init
import pyautogui as pag
import random
import time


# Start the game
screen_content = init.initialize_game()

# Play da damn game
moves = ['left', 'right', 'up', 'down']
n_games = 2     # number of games to play
for game in range(n_games):
    for i in range(20):
        move = moves[random.randint(0, 3)]
        pag.press(move)
        time.sleep(0.1)

    init.restart_game(screen_content.loc['new game', 'x_center'],
                      screen_content.loc['new game', 'y_center'])
