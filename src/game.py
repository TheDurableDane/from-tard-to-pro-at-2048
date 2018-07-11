#!/usr/bin/env python
# encoding: utf-8
import random
import numpy as np


class Game:
    def __init__(self):
        self.board = new_board()
        self.score = 0


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
    nums, cts = np.unique(first_board, return_counts=True)
    for num, ct in zip(nums, cts):
        N = sum(second_board == num)
        points += (N-ct)*num
    return points


def execute_move(board, move):
    initial_board = board.copy()
    if move == 'r':
        board = move_right(board)
    elif move == 'l':
        board = move_left(board)
    elif move == 'u':
        board = move_up(board)
    elif move == 'd':
        board = move_down(board)
    else:
        print('Wrong input, nigga!')

    if not np.array_equal(initial_board, board):
        board = spawn_piece(board)

    return board


def new_board():
    board = np.zeros((4, 4), dtype=int)
    for i in range(2):
        spawn_piece(board)
    return board


def input_loop():
    board = new_board()
    print_board(board)
    while True:
        key = input("u/d/l/r? ")
        board = execute_move(board, key)
        print_board(board)


if __name__ == '__main__':
    input_loop()
