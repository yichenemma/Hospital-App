from tkinter import *
import tkinter as tk

class cal:
    def __init__(self, window):
        self.window = window

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)

        sun1 = Button(self, text="Sun 9 a.m.")
        sun1.grid(row=1, column=0)
        mon1 = Button(self, text="Mon 9 a.m.")
        mon1.grid(row=1, column=1)