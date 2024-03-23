import tkinter as tk
from tkinter import ttk
import os
from mainWindowBase import WindowBase
'''import functions as f
print(dir(f))'''

# Dynamic import of functions
def import_functions():
    global f
    import functions as _f
    f = _f

# Class to create the main window
class MainWindow(WindowBase):
    def __init__(self):
        super().__init__()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.tk.call('source', os.path.join(dir_path, 'azure.tcl'))
        self.tk.call("set_theme", "light")

        import_functions()

        self.createWidgets()
        self.createFrame()

        self.sel_frame = None

    # Method to create widgets
    def createWidgets(self):
        self.createMenu()

    # Method to create the frame
    def createFrame(self):
        #self.createMainFrame()
        #self.createHistoryFrame()
        pass

    # Method to create the menu
    def createMenu(self):
        self.menuBar = tk.Menu(self)
        self.config(menu=self.menuBar)
        self.option_add('*tearOff', 'FALSE')

        self.programMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Program", menu=self.programMenu)
        self.programMenu.add_command(label="Exit", command=self.quit)

        self.functionsMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Functions", menu=self.functionsMenu)
        self.functionsMenu.add_command(label="Trigonometry", command=lambda: self.select_frame(f.trigonometry.Trigonometry(self)))
        self.functionsMenu.add_command(label="Exponential", command=lambda: self.select_frame(f.exponential.Exponential(self)))

        self.extrasMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Extras", menu=self.extrasMenu)
        self.extrasMenu.add_command(label="Export")

        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
        self.helpMenu.add_command(label="About")

    '''def createMainFrame(self):
        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True)'''

    '''def createHistoryFrame(self):
        self.historyFrame = ttk.Frame(self)
        self.historyFrame.grid(row=0, column=0, sticky="w")'''
    
    def forget_frame(self):
        # removes the selected frame
        if self.sel_frame is not None:
            self.sel_frame.grid_forget()

    def select_frame(self, frame: ttk.Frame):
        # selects the frame to be displayed
        self.forget_frame()
        self.sel_frame = frame
        self.sel_frame.config(height=self.winfo_height())
        self.sel_frame.grid(row=0, column=1, sticky="nswe")

    # Idea: tabs?!

if __name__ == "__main__":
    mainWindow = MainWindow()
    mainWindow.mainloop()