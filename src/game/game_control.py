#!/usr/bin/env python
# encoding: utf-8
import random
import numpy as np


class Game:
    def __init__(self):
        self.board = new_board()
        self.score = 0
        self.num_moves = 0

    def __repr__(self):
        board_str = ''
        N_max = len(str(np.max(self.board)))
        rows, cols = 4, 4
        for r in range(rows):
            for c in range(cols):
                board_str += '{message: >{fill}} '.format(message=self.board[r, c], fill=N_max)
            board_str += '\n'
        point_str = str(self.score)
        game_str = "{0}Points: {1}\n".format(board_str, point_str)
        return game_str


def pair_pieces(lst):
    """
     pairs pieces in a list of 4 elements (row or column in board)
     returns new list with all zeros displaced to the right
     e.g. [2 0 2 4] -> [4 4 0 0]
    """
    pieces = [x for x in lst if x > 0]
    pieces = pieces + [0]  # so that last piece can always be paired
    m = len(pieces)
    new_lst = []
    i = 0
    while i < m-1:
        first, second = pieces[i], pieces[i+1]
        if first == second:
            new_lst.append(first + second)
            del pieces[i:i+2]
            m -= 2
        else:
            new_lst.append(first)
            i += 1
    new_lst = new_lst + [0]*(4-len(new_lst))
    return new_lst


def move_right(board):
    for i in range(4):
        lst = pair_pieces(board[i, :][::-1])
        board[i, :] = lst[::-1]
    return board


def move_left(board):
    for i in range(4):
        lst = pair_pieces(board[i, :])
        board[i, :] = lst
    return board


def move_up(board):
    for i in range(4):
        lst = pair_pieces(board[:, i])
        board[:, i] = lst
    return board


def move_down(board):
    for i in range(4):
        lst = pair_pieces(board[:, i][::-1])
        board[:, i] = lst[::-1]
    return board


def empty_fields(board):
    return np.where(board == 0)


def print_board(board):
    print(board)


def spawn_piece(board):
    piece = 2 if random.random() < 0.9 else 4
    rows, cols = empty_fields(board)
    idx = random.randint(0, len(rows)-1)
    i, j = rows[idx], cols[idx]
    board[i, j] = piece

    return board


def get_points(first_board, second_board):
    points = 0
    nums2, cts2 = np.unique(second_board, return_counts=True)
    for num2, ct2 in zip(nums2, cts2):
        if num2 in first_board:
            N = ct2 - np.sum(first_board == num2)
            if N > 0: points += N*num2
        else:
            points += num2
    return points


def is_game_over(game):
    moves = (move_left, move_right, move_up, move_down)
    for move in moves:
        board_copy = game.board.copy()
        board_copy = move(board_copy)
        if not np.array_equal(game.board, board_copy):
            return False
    return True


def execute_move(game, move):
    initial_board = game.board.copy()
    board = game.board
    if move == 'r':
        board = move_right(board)
        game.num_moves += 1
    elif move == 'l':
        board = move_left(board)
        game.num_moves += 1
    elif move == 'u':
        board = move_up(board)
        game.num_moves += 1
    elif move == 'd':
        board = move_down(board)
        game.num_moves += 1
    else:
        print('Wrong input, nigga!')

    # update score
    game.score += get_points(initial_board, board)

    if not np.array_equal(initial_board, board):
        board = spawn_piece(board)

    return board


def new_board():
    board = np.zeros((4, 4), dtype=int)
    for i in range(2):
        spawn_piece(board)
    return board


def input_loop():
    game = Game()
    print(game)
    while True:
        if is_game_over(game):
            print("Game over!... you noob!")
            return game
        key = input("u/d/l/r? ")
        execute_move(game, key)
        print(game)


if __name__ == '__main__':
    input_loop()
