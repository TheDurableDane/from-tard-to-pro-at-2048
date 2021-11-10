#!/usr/bin/env python
import numpy as np
import random

from tf_agents.environments import py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step as ts


class Game2048Env(py_environment.PyEnvironment):
    def __init__(self):
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=3, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(4, 4), dtype=np.int32, minimum=0, maximum=131072, name='observation')

        self.board = self.get_empty_board()
        self.spawn_piece()
        self.spawn_piece()
        self.score = 0
        self.num_moves = 0

        self._state = self.score


    def action_spec(self):
        return self._action_spec


    def observation_spec(self):
        return self._observation_spec


    def _reset(self):
        self.board = self.get_empty_board()
        self.spawn_piece()
        self.spawn_piece()
        self.score = 0
        self.num_moves = 0

        return ts.restart(self.board)


    def _step(self, action):
        """ action interpretation: [right, up, left, down], e.g. [0, 1, 0, 0] for up
        """
        if self.is_game_over():
            # The last action ended the episode. Ignore the current action and start a new episode.
            return self.reset()

        if action == 0:
            self.execute_move('r')
        elif action == 1:
            self.execute_move('u')
        elif action == 2:
            self.execute_move('l')
        elif action == 3:
            self.execute_move('d')
        else:
            raise ValueError(f'Invalid action: {action}')

        reward = self.score
        if self.is_game_over():
            return ts.termination(self.board, reward)
        else:
            return ts.transition(self.board, reward=reward, discount=1.0)


    def get_empty_board(self):
        board = np.zeros((4, 4), dtype=np.int32)

        return board


    def spawn_piece(self):
        piece = 2 if random.random() < 0.9 else 4
        rows, cols = self.empty_fields()
        idx = random.randint(0, len(rows)-1)
        i, j = rows[idx], cols[idx]
        self.board[i, j] = piece

        return self.board


    def empty_fields(self):
        return np.where(self.board == 0)


    def is_game_over(self):
        if (self.board == 0).any():
            return False

        current_board = self.board.copy()

        self.move_right()
        right_board = self.board.copy()
        self.board = current_board.copy()

        self.move_up()
        up_board = self.board.copy()
        self.board = current_board.copy()

        self.move_left()
        left_board = self.board.copy()
        self.board = current_board.copy()

        self.move_down()
        down_board = self.board.copy()
        self.board = current_board.copy()

        board_unchanged = (
            np.array_equal(current_board, right_board) and
            np.array_equal(current_board, up_board) and
            np.array_equal(current_board, left_board) and
            np.array_equal(current_board, down_board)
        )
        if board_unchanged:
            return True
        else:
            return False


    def pair_pieces(self, lst):
        """
        Pairs pieces in a list of 4 elements (row or column in board)
        returns new list with all zeros displaced to the right
        e.g. [2 0 2 4] -> [4 4 0 0]
        """
        pieces = [x for x in lst if x > 0]
        pieces = pieces + [0]  # so that last piece can always be paired
        new_lst = []

        while len(pieces) > 1:
            first, second = pieces[0], pieces[1]
            if first == second:
                new_lst.append(first + second)
                del pieces[0:2]
            else:
                new_lst.append(first)
                del pieces[0]

        # Append zeros until column/row is full
        new_lst = (new_lst + [0]*4)[:4]

        return new_lst


    def move_right(self):
        for i in range(4):
            lst = self.pair_pieces(self.board[i, :][::-1])
            self.board[i, :] = lst[::-1]


    def move_left(self):
        for i in range(4):
            lst = self.pair_pieces(self.board[i, :])
            self.board[i, :] = lst


    def move_up(self):
        for i in range(4):
            lst = self.pair_pieces(self.board[:, i])
            self.board[:, i] = lst


    def move_down(self):
        for i in range(4):
            lst = self.pair_pieces(self.board[:, i][::-1])
            self.board[:, i] = lst[::-1]


    def update_score(self, previous_board):
        points = 0
        nums, cnts = np.unique(self.board, return_counts=True)
        for num, cnt in zip(nums, cnts):
            N = cnt - np.sum(previous_board == num)
            if N > 0:
                points += N*num

        self.score += points


    def execute_move(self, move):
        previous_board = self.board.copy()
        if move == 'r':
            self.move_right()
            self.num_moves += 1
        elif move == 'l':
            self.move_left()
            self.num_moves += 1
        elif move == 'u':
            self.move_up()
            self.num_moves += 1
        elif move == 'd':
            self.move_down()
            self.num_moves += 1
        else:
            print('Wrong input, nigga!')

        # update score
        self.update_score(previous_board)

        if not np.array_equal(previous_board, self.board):
            self.spawn_piece()


if __name__ == '__main__':
    environment = Game2048Env()
    utils.validate_py_environment(environment, episodes=5)
