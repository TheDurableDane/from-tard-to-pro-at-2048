#!/usr/bin/env python
# encoding: utf-8
from game import *
import tkinter as tk

_translator = {"Left":"l", "Right":"r", "Up":"u", "Down":"d"}


def bind_move_to_gui(key, my_game, tklabel):
    execute_move(my_game, key)
    tklabel.config(text = repr(my_game))

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
            bind_move_to_gui(_translator[key], my_game, gametext)

root.bind("<Key>", on_key_down)


# class GameGUI:
#     def __init__(self):
#         game = Game()
#         root = tk.Tk()
#         root.geometry("400x400")
#         label = tk.Label(root,  text=repr(game), 
#                                 font=("Consolas", 20))
#         self.game = game
#         self.root = root
#         self.label = label

#     def 

while True:
    root.update()
    # execute_move(my_game, "u")
