import initialization as init
import pyautogui as pag
import random
import time

# fix for linking to relative paths
import os.path
here = os.path.dirname(os.path.realpath(__file__))
abs_path = lambda fname: os.path.join(here, fname)

# Start the game
init.initialize_game()

moves = ['left', 'right', 'up', 'down']

for i in range(100):
    move = moves[random.randint(0, 3)]
    pag.press(move)
    print(move)
    time.sleep(0.1)

button_location = pag.locateOnScreen(abs_path('../fkn_pro/data/new_game_button.png'))
x_button, y_button = pag.center(button_location)
pag.click(x_button, y_button)
