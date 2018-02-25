#!/usr/bin/env python3
import pandas as pd
import webbrowser
import pyautogui as pag
import time
import argparse
import sys
import image_processing as img_proc
import os

# os-independent (not tested on Mac, obviously) hack for linking to relative paths.
# underscore makes them private, i.e. not imported via *
_here = os.path.dirname(os.path.realpath(__file__))
def _abs_path(f):
    return os.path.join(_here, f)


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


def restart_game(x_new_game_button, y_new_game_button):
    """
    Move the cursor to the "New Game" button and click it.
    """
    pag.click(x=x_new_game_button, y=y_new_game_button)


def initialize_game(url='https://gabrielecirulli.github.io/2048/'):
    """
    This is the main function of this file.
    """
    start_webbrowser(url)
    time.sleep(2)
    # center_game_on_screen()    # Needs improvement

    # Locate screen content
    screen_content = pd.DataFrame(data=[],
                                  columns=['row', 'column', 'height', 'width', 'x_center', 'y_center'],
                                  index=['board', 'new game', 'score', 'best'])
    template_paths = ['data/game_board-2.png',
                      'data/new_game_button-2.png',
                      'data/score-2.png',
                      'data/best-2.png']
    # we should consider moving these paths into a utils file together
    # with the _abs_path function...
    template_paths = map(_abs_path, template_paths) # fix for the S Bag!
    for i, path in enumerate(template_paths):
        screen_content.iloc[i, :] = img_proc.locate_image_on_screen(path)
        pag.moveTo(screen_content.iloc[i, 4], screen_content.iloc[i, 5])

    restart_game(screen_content.loc['new game', 'x_center'],
                 screen_content.loc['new game', 'y_center'])

    return screen_content


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Initialize a game of 2048.')
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        default='https://gabrielecirulli.github.io/2048/',
                        help='The url of the 2048 game.')
    args = parser.parse_args()

    sys.exit(initialize_game(args.url))
