import webbrowser
import pyautogui as pag
import time
import numpy as np
import matplotlib.pylab as pl


# test upload
webbrowser.open('https://gabrielecirulli.github.io/2048/', new=1)
time.sleep(3)

width, height = pag.size()

# center game area in browser by scrolling down 50 px
pag.moveTo(width, int(height/2))
pag.dragRel(0, 50)

img = pag.screenshot()
img = np.array(img)[round(height/4):, round(width/4):round(width/4*3)]

pl.imshow(img)
