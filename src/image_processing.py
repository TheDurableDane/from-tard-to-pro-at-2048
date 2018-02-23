import pyautogui as pag
from skimage.color import rgb2gray
from skimage.io import imshow
import numpy as np
from bs4 import BeautifulSoup
import urllib


def take_screenshot():
    """
    Take screenshot of the entire screen and return it as a grayscale image in
    a numpy array. The pixel values are in range [0; 1].
    """
    img_orig = np.array(pag.screenshot())
    img_gray = rgb2gray(img_orig)

    return img_gray


def detect_cells(screen):
    """
    Input: Screenshot (grayscale) of browser window containing entire game
    board as a numpy array with values in range [0; 1].

    Output: Dictionary of 16 grayscale images/entries (numpy arrays) cropped to
    contain one cell per key.
    """
    height, width = screen.shape
    screen = screen[round(height/5):round(height*4/5), round(width/4):round(width*3/4)]
    threshold = 0.9
    img = np.empty_like(screen)
    img[screen > threshold] = 1
    img[screen <= threshold] = 0

    # Find corners of board
    board_idx = np.where(img == 0)
    board_rmin = np.amin(board_idx[0])
    board_rmax = np.amax(board_idx[0])
    board_cmin = np.amin(board_idx[1])
    board_cmax = np.amax(board_idx[1])

    # Divide board into cells
    cell_size_r = int(round((board_rmax - board_rmin)/4))
    cell_size_c = int(round((board_cmax - board_cmin)/4))

    cells = {}
    for row in range(4):
        for col in range(4):
            cell_rmin = board_rmin + row*cell_size_r
            cell_rmax = board_rmin + (row + 1)*cell_size_r
            cell_cmin = board_cmin + col*cell_size_c
            cell_cmax = board_cmax + (col + 1)*cell_size_c

            cells[row, col] = screen[cell_rmin:cell_rmax, cell_cmin:cell_cmax]

    return cells


def reCOCKnize_numbers():
    pass


if __name__ == '__main__':
    pass