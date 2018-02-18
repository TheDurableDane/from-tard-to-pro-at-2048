import pyautogui as pag
from skimage.color import rgb2gray
import numpy as np


def take_screenshot():
    """
    Take screenshot of the entire screen and return it as a grayscale image in
    a numpy array. The pixel values are in range [0; 1].
    """
    img_orig = np.array(pag.screenshot())
    img_gray = rgb2gray(img_orig)

    return img_gray


def detect_cells():
    pass


def reCOCKnize_numbers():
    pass


if __name__ == '__main__':
    pass
