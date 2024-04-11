from tkinter import ttk

class FunctionFrameBase(ttk.Frame):
    # Base class for function frames
    def __init__(self, master, width=1200, height=700):
        super().__init__(master, width=width, height=height)
        self.master = master
