import numpy as np
import sys
sys.path.insert(0, '../src/')
from game import spawn_piece


def test_spawn_piece():
    board = np.zeros((4, 4), dtype=int)

    for i in range(4):
        spawn_piece(board)

    assert(np.sum(board == 0) == 12)
