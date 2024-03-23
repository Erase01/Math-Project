import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk
from functionFrameBase import FunctionFrameBase

class Exponential(FunctionFrameBase):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def clear_canvas(self):
        # Clear the canvas
        self.ax.clear()
        self.canvas.draw()

    def create_widgets(self):
        self.initial_label = ttk.Label(self, text="Initial Value:")
        self.initial_entry = ttk.Entry(self)
        self.base_label = ttk.Label(self, text="Base Value:")       # Have to be greater than 0
        self.base_entry = ttk.Entry(self)
        self.start_label = ttk.Label(self, text="Start Value for x:")
        self.start_entry = ttk.Entry(self)
        self.end_label = ttk.Label(self, text="End Value for x:")
        self.end_entry = ttk.Entry(self)
        self.xvalue_lable = ttk.Label(self, text="x-label")
        self.xvalue_entry = ttk.Entry(self)
        self.yvalue_lable = ttk.Label(self, text="y-label")
        self.yvalue_entry = ttk.Entry(self)

        self.plot_button = ttk.Button(self, text="Plot", command=self.plot_exponential)
        self.clear = ttk.Button(self, text="Clear", command=self.clear_canvas)

        # Create the canvas
        self.fig = plt.figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        self.grid_widgets()

    def grid_widgets(self):
        self.initial_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.initial_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.base_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.base_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.start_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.start_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.end_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.end_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.xvalue_lable.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.xvalue_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.yvalue_lable.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.yvalue_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        self.plot_button.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky="w")
        self.clear.grid(row=0, column=1, columnspan=1, padx=5, pady=5, sticky="w")

        self.canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

    def plot_exponential(self):
        a = float(self.initial_entry.get())
        b = float(self.base_entry.get())
        start = float(self.start_entry.get())
        end = float(self.end_entry.get())
        x_values = np.arange(start, end, 0.1)
        y_values = a * (b ** x_values)

        legend_label = fr"$y = {a} \cdot {b}^x$"
        self.ax.plot(x_values, y_values, label=legend_label)
        self.ax.set_xlabel(self.xvalue_entry.get())
        self.ax.set_ylabel(self.yvalue_entry.get())
        self.ax.grid(True)
        self.ax.legend(loc='upper right')
        self.ax.set_title('Exponential Function')
        self.canvas.draw()