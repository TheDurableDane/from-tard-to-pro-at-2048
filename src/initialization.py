#!/usr/bin/env python3
import webbrowser
import pyautogui as pag
import time
import argparse


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
    pag.moveTo(width, int(height/2))
    pag.dragRel(0, 120)


def restart_game():
    """
    Move the cursor to the "New Game" button and click it.
    """
    button_location = pag.locateOnScreen('data/new_game_button.png')
    x_button, y_button = pag.center(button_location)
    pag.click(x_button, y_button)


def initialize_game(url='https://gabrielecirulli.github.io/2048/'):
    """
    This is the main function of this file.
    """
    start_webbrowser(url)
    time.sleep(2)
    center_game_on_screen()
    restart_game()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Initialize a game of 2048.')
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        default='https://gabrielecirulli.github.io/2048/',
                        help='The url of the 2048 game.')
    args = parser.parse_args()

    initialize_game(args.url)
