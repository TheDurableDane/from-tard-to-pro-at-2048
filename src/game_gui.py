#!/usr/bin/env python
# encoding: utf-8
from game import *
import tkinter as tk


WIDTH = 400
HEIGHT = 400


class GameGUI:

    def __init__(self, master):
        self.master = master

    def build_gui(self):
        for i in range(4):
            # _columns = []
            for j in range(4):
                tk.Label(master, text="lol").grid(row=i, column=j)
            #     cell = Frame(background, bg="#%deee%df" % (i, j), 
            #                  width=WIDTH/4, height=HEIGHT/4)
            #     cell.grid(row=i, column=j)
            #     _columns.append(Frame(background, bg="#ffffff", width=WIDTH/4, 
            #                                       height=HEIGHT/4))
            # cells.append(_columns)
        self.cells = cells

if __name__ == "__main__":
    root = tk.Tk()
    gg = GameGUI(root)
    root.mainloop()