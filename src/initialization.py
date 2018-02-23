#!/usr/bin/env python3
import webbrowser
import pyautogui as pag
import time
import argparse
import os.path
import glob


NEW_GAME_BUTTON = None

# os-independent (not tested on Mac) hack for linking to relative paths.
# underscore makes them private, i.e. not imported via *
_here = os.path.dirname(os.path.realpath(__file__))
def _abs_path(f): return os.path.join(_here, f)


def start_webbrowser(url):
    """
    Open website in new browser window.
    """
    webbrowser.open(url, new=1)


def center_game_on_screen():
    """
    This function tries to center the game on the screen such that the entire
    board is visible. The current code is very basic and should be further
    developed to take better care of different screen resolutions once SHM is
    motivated.
    """
    # Get screen resolution
    width, height = pag.size()

    # Center game area in browser by scrolling down
    pag.moveTo(width-5, int(2*height/3))
    # pag.dragRel(0, 120)


def restart_game(ng_button=_abs_path("data/new_game_button.png")):
    """
    Move the cursor to the "New Game" button and click it.
    """
    button_location = pag.locateOnScreen(ng_button)
    x_button, y_button = pag.center(button_location)
    pag.click(x_button, y_button)


def initialize_game(url='https://gabrielecirulli.github.io/2048/'):
    """
    This is the main function of this file.
    """
    start_webbrowser(url)
    time.sleep(2)
    center_game_on_screen()

    # locate correct new game button
    success = False
    for ng_button in glob.glob(_abs_path("data/new_game_button*")):
        try:
            restart_game(ng_button)
        except TypeError:
            continue
        else:
            success = True
            NEW_GAME_BUTTON = ng_button


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Initialize a game of 2048.')
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        default='https://gabrielecirulli.github.io/2048/',
                        help='The url of the 2048 game.')
    args = parser.parse_args()

    initialize_game(args.url)
