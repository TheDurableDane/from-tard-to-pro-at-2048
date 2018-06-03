# encoding: utf-8
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
    

def spawn_piece(board):
#    return board
    pass


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
