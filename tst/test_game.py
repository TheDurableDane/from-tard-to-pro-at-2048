import numpy as np
import sys
sys.path.insert(0, 'src/')
from game import spawn_piece, pair_pieces


def test_spawn_piece():
    np.random.seed(11)
    board = np.zeros((4, 4), dtype=int)

    for i in range(4):
        spawn_piece(board)

    assert np.sum(board == 0) == 12


def test_pair_pieces():
    lsts = [[2, 4, 2, 4],
            [2, 2, 0, 2],
            [2, 8, 8, 2],
            [2, 2, 2, 2]]
    ress = [[2, 4, 2, 4],
            [4, 2, 0, 0],
            [2, 16, 2, 0],
            [4, 4, 0, 0]]
    for lst, res in zip(lsts, ress):
        lst = pair_pieces(lst)
        assert lst == res
