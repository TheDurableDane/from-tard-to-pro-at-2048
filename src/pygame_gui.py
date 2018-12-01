#!/usr/bin/env python
# encoding: utf-8

import game
import pygame as pg
import sys
import numpy as np


this_game = game.Game()
print(this_game)

# Initialization
pg.init()
game_w = 400
game_h = 400
game_screen = pg.display.set_mode((game_w, game_h))

fontsize = 50
font = pg.font.SysFont('Arial', fontsize)
white = (255, 255, 255)
black = (0, 0, 0)

# Start game loop
exit_game = False
while not exit_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                game.execute_move(this_game, 'l')
            elif event.key == pg.K_RIGHT:
                game.execute_move(this_game, 'r')
            elif event.key == pg.K_UP:
                game.execute_move(this_game, 'u')
            elif event.key == pg.K_DOWN:
                game.execute_move(this_game, 'd')

    game_screen.fill(white)
    for i in range(this_game.board.size):
        row = int(np.floor(i/4))
        col = int(i%4)
        cell_number = this_game.board[row, col]
        if cell_number == 0:
            color = (0, 0, 0, 0)
        else:
            color = (int(np.log2(cell_number)/17*255), 0, 0, 0)
        text = font.render(str(cell_number), True, color)
        game_screen.blit(text, (col*fontsize*2, row*fontsize*2))
    pg.display.update()

pg.quit()
sys.exit()

