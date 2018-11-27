#!/usr/bin/env python
# encoding: utf-8

import game
import pygame as pg
import sys


this_game = game.Game()
print(this_game)

# Initialization
pg.init()
game_w = 600
game_h = 800
game_screen = pg.display.set_mode((game_w, game_h))

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

        print(this_game)

    pg.display.update()

pg.quit()
sys.exit()

