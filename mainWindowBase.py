import tkinter as tk

# Class to create the base of the main window

class WindowBase(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Math Project")
        self.geometry("1200x700")
        self.resizable(width=False, height=False)