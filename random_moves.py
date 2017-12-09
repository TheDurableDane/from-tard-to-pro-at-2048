import webbrowser
import pyautogui as pag
import random
import time

# test upload
webbrowser.open('https://gabrielecirulli.github.io/2048/', new=1)
time.sleep(5)

moves = ['left', 'right', 'up', 'down']
for i in range(100):
    move = moves[random.randint(0, 3)]
    pag.press(move)
    print(move)
    time.sleep(0.1)
