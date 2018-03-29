import initialization as init
from image_processing import game_over, take_screenshot, save_image
import pyautogui as pag
import random
import time
import datetime
import os


def make_random_move():
    moves = ['left', 'right', 'up', 'down']
    move = moves[random.randint(0, 3)]
    pag.press(move)
    time.sleep(0.1)


def save_results(screen_content):
    """
    This function currently saves an image of the end-score and the end-board.
    It is simply a temporary solution, since we wish to save the score and
    possibly the board to disk as a number, not as images.
    """
    directory = 'results'
    timestamp = str(datetime.datetime.now()).replace('-', '').replace(':', '').replace(' ', '').replace('.', '')
    filename_board = '{0}_random_board.png'.format(timestamp)
    filename_score = '{0}_random_score.png'.format(timestamp)

    screen = take_screenshot()
    save_image(os.path.join(directory, filename_board),
               screen[screen_content.loc['board', 'row']:screen_content.loc['board', 'row'] + screen_content.loc['board', 'height'],
                      screen_content.loc['board', 'column']:screen_content.loc['board', 'column'] + screen_content.loc['board', 'width']])
    save_image(os.path.join(directory, filename_score),
               screen[screen_content.loc['score_best', 'row']:screen_content.loc['score_best', 'row'] + screen_content.loc['score_best', 'height'],
                      screen_content.loc['score_best', 'column']:screen_content.loc['score_best', 'column'] + screen_content.loc['score_best', 'width']])


def play_randomly():
    """
    This is the main function.
    """
    # Start the game
    screen_content = init.initialize_game()

    # Play da damn game
    while True:
        make_random_move()

        if game_over(screen_content.loc['board', :]):
            save_results(screen_content)
            init.restart_game(screen_content.loc['new game', 'x_center'],
                              screen_content.loc['new game', 'y_center'])


if __name__ == '__main__':
    play_randomly()
