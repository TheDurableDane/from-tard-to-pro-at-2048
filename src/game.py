#!/usr/bin/env python
# encoding: utf-8
import random
import numpy as np
import argparse


# pairs pieces in a list of 4 elements (row or column in board)
# returns new list with all zeros displaced to the right
# e.g. [2 0 2 4] -> [4 4 0 0]
def pair_pieces(lst):
    pieces = [x for x in lst if x > 0]
    pieces = pieces + [0] # so that last piece can always be paired
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
        lst = pair_pieces(board[i,:][::-1])
        board[i,:] = lst[::-1]
    return board


def move_left(board):
    for i in range(4):
        lst = pair_pieces(board[i,:])
        board[i,:] = lst
    return board


def move_up(board):
    for i in range(4):
        lst = pair_pieces(board[:,i])
        board[:,i] = lst
    return board


def move_down(board):
    for i in range(4):
        lst = pair_pieces(board[:,i][::-1])
        board[:,i] = lst[::-1]
    return board


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


if __name__ == '__main__':
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
