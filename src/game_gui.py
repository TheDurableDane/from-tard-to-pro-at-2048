#!/usr/bin/env python
# encoding: utf-8
from game import *
import tkinter as tk

_translator = {"Left":"l", "Right":"r", "Up":"u", "Down":"d"}


#def run_game():
my_game = Game()

root = tk.Tk()
root.geometry("400x400")

gametext = tk.Label(root,   text=repr(my_game),
                        font=("Consolas", 20))
gametext.pack(fill="both", expand=True)


def on_key_down(event):
    key = event.keysym

    if key in _translator.keys():
        if is_game_over(my_game):
            print("Game over!... you noob!")
        else:
            execute_move(my_game, _translator[key])
            gametext.config(text = repr(my_game))

root.bind("<Key>", on_key_down)


while True:
    root.update()
    execute_move(my_game, "u")


# root.mainloop()
#    return my_game

# run_game()