#!/usr/bin/env python
# encoding: utf-8
import random
import time
import numpy as np


class Game:
    def __init__(self):
        self.board = self.get_empty_board()
        self.spawn_piece()
        self.spawn_piece()
        self.score = 0
        self.num_moves = 0


    def __repr__(self):
        if self.board is None:
            return 'Board is none.'
        board_str = ''
        N_max = len(str(np.max(self.board)))
        rows, cols = 4, 4
        for r in range(rows):
            for c in range(cols):
                board_str += '{message: >{fill}} '.format(message=self.board[r, c], fill=N_max)
            board_str += '\n'
        point_str = str(self.score)
        game_str = f"{board_str}Points: {point_str}\n"
        return game_str


    def get_empty_board(self):
        board = np.zeros((4, 4), dtype=int)

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


def play_game():
    game = Game()
    while not game.is_game_over():
        print(game)
        action = input('u/d/l/r? ')
        game.execute_move(action)
    print(game)
    print('Game over!')
    return game


def play_random_game():
    game = Game()
    while not game.is_game_over():
        print(game)
        action = random.choice(['r', 'u', 'l', 'd'])
        print(action)
        game.execute_move(action)
        time.sleep(1)
    print(game)
    print('Game over!')
    return game


if __name__ == '__main__':
    play_game()
