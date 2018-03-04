import initialization as init
from image_processing import game_over
import pyautogui as pag
import random
import time


def make_random_move():
    moves = ['left', 'right', 'up', 'down']
    move = moves[random.randint(0, 3)]
    pag.press(move)
    time.sleep(0.1)


def save_results():
    pass


def play_randomly():
    """
    This is the main function.
    """
    # Start the game
    screen_content = init.initialize_game()

    # Play da damn game
    while True:
        make_random_move()

        if game_over():
            save_results()
            init.restart_game(screen_content.loc['new game', 'x_center'],
                              screen_content.loc['new game', 'y_center'])


if __name__ == '__main__':
    play_randomly()
