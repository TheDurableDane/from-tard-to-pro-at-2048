#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from game import game_control
from random import randint
import numpy as np
import datetime
import pandas as pd


def write_results(scores, max_tiles):
    timestamp = str(datetime.datetime.now()).replace('-', '').replace(':', '').replace(' ', '').replace('.', '')
    filename = f'../data/random_moves_results_{timestamp}.csv'
    data = dict(score=scores, max_tile=max_tiles)
    df = pd.DataFrame(data=data)
    df.to_csv(filename, index=False)


def main():
    scores = []
    max_tiles = []
    moves = ['l', 'r', 'u', 'd']
    number_of_games = 100000
    write_results_to_file = True

    for game_number in range(number_of_games):
        game = game_control.Game()
        while not game_control.is_game_over(game):
            move = moves[randint(0, len(moves)-1)]
            game_control.execute_move(game, move)
        scores.append(game.score)
        max_tiles.append(np.max(game.board))
        percentage = round(game_number/number_of_games*100)
        print("{0}% of {1} games completed.".format(percentage, number_of_games), end='\r', flush=True)

    if write_results_to_file:
        write_results(scores, max_tiles)


if __name__ == '__main__':
    main()
