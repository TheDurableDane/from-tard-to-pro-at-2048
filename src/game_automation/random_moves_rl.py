#!/usr/bin/env python
from game import rl_environment
from tf_agents.environments import utils
from random import randint
import numpy as np
import datetime
import pandas as pd


def write_results(scores, max_tiles):
    timestamp = str(datetime.datetime.now()).replace('-', '').replace(':', '').replace(' ', '').replace('.', '')
    filename = f'../data/results/random_moves/{timestamp}.csv'
    data = dict(score=scores, max_tile=max_tiles)
    df = pd.DataFrame(data=data)
    df.to_csv(filename, index=False)


def main():
    scores = []
    max_tiles = []
    moves = ['l', 'r', 'u', 'd']
    number_of_games = 10000
    write_results_to_file = True

    for game_number in range(number_of_games):
        environment = rl_environment.Game2048Env()
        utils.validate_py_environment(environment, episodes=1)
        scores.append(environment.score)
        max_tiles.append(np.max(environment.board))
        percentage = round(game_number/number_of_games*100)
        print("{0}% of {1} games completed.".format(percentage, number_of_games), end='\r', flush=True)

    if write_results_to_file:
        write_results(scores, max_tiles)


if __name__ == '__main__':
    main()
