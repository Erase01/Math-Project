from functionFrameBase import FunctionFrameBase
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class Integral(FunctionFrameBase):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()
    
    def clear_canvas(self):
        # Clear the canvas
        self.ax.clear()
        self.canvas.draw()

    def create_widgets(self):
        self.func_lable = ttk.Label(self, text="Function:")
        self.func_entry = ttk.Entry(self)
        self.lb_label = ttk.Label(self, text="Lower Bound:")
        self.lb_entry = ttk.Entry(self)
        self.ub_label = ttk.Label(self, text="Upper Bound:")
        self.ub_entry = ttk.Entry(self)
        self.n_label = ttk.Label(self, text="Number of intervals:")
        self.n_entry = ttk.Entry(self)
        self.xvalue_lable = ttk.Label(self, text="x-label")
        self.xvalue_entry = ttk.Entry(self)
        self.yvalue_lable = ttk.Label(self, text="y-label")
        self.yvalue_entry = ttk.Entry(self)
        self.result_label = ttk.Label(self, text="")

        self.plot_button = ttk.Button(self, text="Plot", command=self.plot_integral)
        self.clear = ttk.Button(self, text="Clear", command=self.clear_canvas)

        # Create the canvas
        self.fig = plt.figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        self.grid_widgets()

    def grid_widgets(self):
        self.func_lable.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.func_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.lb_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.lb_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.ub_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.ub_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.n_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.n_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.xvalue_lable.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.xvalue_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.yvalue_lable.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.yvalue_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        self.plot_button.grid(row=0, column=2, columnspan=1, padx=5, pady=5, sticky="w")
        self.clear.grid(row=1, column=2, columnspan=1, padx=5, pady=5, sticky="w")

        self.canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

    def plot_integral(self):
        try:
            # Read limits and number of intervals from the input fields
            lb = float(self.lb_entry.get())
            ub = float(self.ub_entry.get())
            n = int(self.n_entry.get())

            func_str = self.func_entry.get()
            func = lambda x: eval(func_str)

            # Calculate integral and display result
            integral_result = self.trapezoidal_rule(func, lb, ub, n)
            self.result_label.config(text=f"The integral of the function is approximately: {integral_result}")

            # Generate function values for plotting
            x_values = np.linspace(lb, ub, 100)
            y_values = func(x_values)

            # Generate trapezoidal control area for plotting
            trapezoid_x = np.linspace(lb, ub, n + 1)
            trapezoid_y = func(trapezoid_x)

            # Plotting
            self.ax.clear()
            self.ax.plot(x_values, y_values, label="Function")
            self.ax.plot(trapezoid_x, trapezoid_y, 'r', label="Trapezoidal Rule")
            self.ax.fill_between(trapezoid_x, 0, trapezoid_y, alpha=0.2)
            self.ax.legend()
            self.ax.set_xlabel(self.xvalue_entry.get())
            self.ax.set_ylabel(self.yvalue_entry.get())
            self.canvas.draw()
        except Exception as e:
            self.result_label.config(text=f"Error during calculation. Make sure that your input is correct: {e}")

    def trapezoidal_rule(self, func, lb, ub, n):

        """Approximate the definite integral of a function using the trapezoidal rule.

        Parameters:
            func (callable): The function to be integrated.
            a (float): The lower limit of integration.
            b (float): The upper limit of integration.
            n (int): The number of subintervals for approximating the integral.

        Returns:
            float: The approximate value of the definite integral.
        """

        # Calculate the width of each interval
        h = (ub - lb) / n

        # Calculate the sum of the function values at the interpolation points
        sum_of_val = 0.5 * (func(lb) + func(ub))
        for i in range(1, n):
            sum_of_val += func(lb + i * h)

        # Calculate the result of the trapezoidal rule
        result = h * sum_of_val
        return result