from os import truncate
from tkinter import *
from tkinter.ttk import *
import random


class moveAnt:
    def __init__(self):
        self.x = round((random.random() - 0.5) * 2, 3)
        self.y = round((random.random() - 0.5) * 2, 3)


