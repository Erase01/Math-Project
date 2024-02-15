import tkinter as tk
from tkinter import ttk
from mainWindowBase import WindowBase

# Class to create the main window
class MainWindow(WindowBase):
    def __init__(self):
        super().__init__()

        self.createWidgets()

    # Method to create widgets
    def createWidgets(self):
        self.createMenu()

    # Method to create the menu
    def createMenu(self):
        self.menuBar = tk.Menu(self)
        self.config(menu=self.menuBar)
        self.option_add('*tearOff', 'FALSE')

        self.programMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Program", menu=self.programMenu)
        self.programMenu.add_command(label="Exit", command=self.quit)

        self.funktionsMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Funktions", menu=self.funktionsMenu)
        self.funktionsMenu.add_command(label="Linear, Quadratic, ...")

        self.extrasMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Extras", menu=self.extrasMenu)
        self.extrasMenu.add_command(label="Export")

        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
        self.helpMenu.add_command(label="About")

    # Idea: tabs?!

if __name__ == "__main__":
    mainWindow = MainWindow()
    mainWindow.mainloop()