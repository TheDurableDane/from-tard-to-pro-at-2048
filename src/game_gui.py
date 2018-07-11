#!/usr/bin/env python
# encoding: utf-8
from game import *
import tkinter as tk


my_game = Game()


root = tk.Tk()
root.geometry("400x400")



gametext = tk.Label(root,   text=repr(my_game),
                            font=("Consolas", 20))
gametext.pack(fill="both", expand=True)





root.mainloop()
