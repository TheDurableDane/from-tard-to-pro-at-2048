# encoding: utf-8
import random
import numpy as np
import argparse


def move_right(board):
#    return board
    pass


def move_left(board):
#    return board
    pass


def move_up(board):
#    return board
    pass


def move_down(board):
#    return board
    pass


def empty_fields(board):
    return np.where(board == 0)


def print_board(board):
    print(board)


def spawn_piece(board):
    piece = 2 if random.random() < 0.9 else 4
    rows, cols = empty_fields(board)
    i, j = [np.random.choice(elem, 1)[0] for elem in (rows, cols)]
    board[i,j] = piece
    return board



def execute_move(board, move):
#    if move == 'right:
#        board = move_right(board)
#    elif:
#        pass
#    .
#    .
#    .
#    board = spawn_piece(board)
#    
#    return board
    pass


def new_board():
    board = np.zeros((4,4))
    for i in range(2):
        spawn_piece(board)
    return board


def test_spawn_piece():
    board = np.zeros((4,4), dtype=int)
    print_board(board)
    for i in range(4):
        spawn_piece(board)
    print_board(board)


if __name__ == '__main__':
#    execute_move()
    test_spawn_piece()
    pass
    parser = argparse.ArgumentParser(description='Mad execution of 2048 move.')
    parser.add_argument('-b','--board',
                        type=int,
                        help='4x4 Numpy array containing the board',
                        required=True)
    parser.add_argument('-m','--move',
                        type=str,
                        help='The move you want to make: left, right, up, or down',
                        required=True)
    args = parser.parse_args()

    execute_move(args.board, args.move)
