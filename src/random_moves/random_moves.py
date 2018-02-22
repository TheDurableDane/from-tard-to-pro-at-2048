import webbrowser
import pyautogui as pag
import random
import time

# test upload
webbrowser.open('https://gabrielecirulli.github.io/2048/', new=1)
time.sleep(5)

width, height = pag.size()

# center game area in browser by scrolling down 50 px
pag.moveTo(width, int(height/2))
pag.dragRel(0, 50)

moves = ['left', 'right', 'up', 'down']

for i in range(100):
    move = moves[random.randint(0, 3)]
    pag.press(move)
    print(move)
    time.sleep(0.1)

button_location = pag.locateOnScreen('../fkn_pro/data/new_game_button.png')
x_button, y_button = pag.center(button_location)
pag.click(x_button, y_button)
