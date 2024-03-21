'''import tkinter as tk
from tkinter import ttk
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class Trigometry:
    def __init__(self, parent):
        super().__init__()

        
        
x = sp.symbols('x')

func = sp.sin(x)
#func = x**2+7
#f.lambdafy
f1 = sp.diff(func, x) # erste ableitung
f2 = sp.diff(f1, x)
xe = sp.solve(f1, x)
ye = [ func.subs(x, s) for s in xe] # 0 for s in ny = nullstellen

xw = sp
result = sp.solve(func, x)

print(xe, ye)
print("\n", f2)


x = np.arange(0,6*np.pi,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show()'''

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from main import MainWindow
from functionFrameBase import FunctionFrameBase

class Trigonometry(FunctionFrameBase):
    def __init__(self, master):
        super().__init__(master)

        '''dir_path = os.path.dirname(os.path.realpath(__file__))
        self.tk.call('source', os.path.join(dir_path, 'azure.tcl'))
        self.tk.call("set_theme", "light")'''
        #self.parent = parent
        self.create_widget()
    '''
    # Funktionen definieren
    def sinus_funktion(x):
        return np.sin(x)

    def cosinus_funktion(x):
        return np.cos(x)

    def tangenten_funktion(x):
        return np.tan(x)

    # Werte für x generieren
    x_werte = np.linspace(-2*np.pi, 2*np.pi, 1000)

    # Funktionswerte berechnen
    sinus_werte = sinus_funktion(x_werte)
    cosinus_werte = cosinus_funktion(x_werte)
    tangenten_werte = tangenten_funktion(x_werte)

    # Plots erstellen
    plt.figure(figsize=(10, 6))

    plt.plot(x_werte, sinus_werte, label='Sinus')
    plt.plot(x_werte, cosinus_werte, label='Cosinus')
    plt.plot(x_werte, tangenten_werte, label='Tangens')

    # Achsen beschriften
    plt.xlabel('x')
    plt.ylabel('Funktionswerte')

    # Legende anzeigen
    plt.legend()

    ax = plt.gca()

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Plot anzeigen
    plt.show()'''

    def create_widget(self):
        self.amplitude_lable = ttk.Label(self, text="Amplitude")
        self.amplitude_entry = ttk.Entry(self)
        self.frequency_lable = ttk.Label(self, text="Frequency")
        self.frequency_entry = ttk.Entry(self)
        self.phase_lable = ttk.Label(self, text="Phase")
        self.phase_entry = ttk.Entry(self)
        self.xvalue_lable = ttk.Label(self, text="x-label")
        self.xvalue_entry = ttk.Entry(self)
        self.yvalue_lable = ttk.Label(self, text="y-label")
        self.yvalue_entry = ttk.Entry(self)
        self.var = tk.StringVar(value="sin")
        
        print_button = ttk.Button(self, text="Print", command=self.calculate_tfunktion)
        clear_button = ttk.Button(self, text="Clear", command=self.clear_canvas)           #ToDo: Add this method

        sin_button = ttk.Radiobutton(self, text="Sinus", variable=self.var, value="sin")
        cos_button = ttk.Radiobutton(self, text="Cosinus", variable=self.var, value="cos")
        tan_button = ttk.Radiobutton(self, text="Tangens", variable=self.var, value="tan")

        print_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        clear_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        sin_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        cos_button.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        tan_button.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        # Create the canvas
        self.fig = plt.figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        self.grid_widgets()

    def clear_canvas(self):
        # Clear the canvas
        self.ax.clear()
        self.canvas.draw()

    def grid_widgets(self):
        self.amplitude_lable.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.amplitude_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.frequency_lable.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.frequency_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.phase_lable.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.phase_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.xvalue_lable.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.xvalue_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.yvalue_lable.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.yvalue_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    def random_color(self):
        # Get random color, which is not already used in the plot
        colors = list(plt.rcParams['axes.prop_cycle'].by_key()['color'])
        lines = plt.gca().get_lines()
        used_colors = [line.get_color() for line in lines]
        available_colors = [color for color in colors if color not in used_colors]
        if available_colors:
            return np.random.choice(available_colors)
        else:
            # Fallback color
            return "black" 

    def calculate_tfunktion(self):
        # Get the values from the entries
        amplitude = float(self.amplitude_entry.get())
        frequency = float(self.frequency_entry.get())
        phase = float(self.phase_entry.get())
        x_value = self.xvalue_entry.get()
        y_value = self.yvalue_entry.get()

        x = np.linspace(-2*np.pi, 2*np.pi, 1000)

        # Get the selected function
        selected_function = self.var.get()

        # Calculate the function
        if selected_function == "sin":
            y = amplitude * np.sin(frequency * x + phase)
            title = "Sinus function"
        elif selected_function == "cos":
            y = amplitude * np.cos(frequency * x + phase)
            title = "Cosinus function"
        elif selected_function == "tan":
            y = amplitude * np.tan(frequency * x + phase)
            title = "Tangens function"

        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.spines['left'].set_position(('data', 0))

        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

        # Plot the function
        self.ax.set_xlabel(x_value, labelpad=10, loc='right')
        self.ax.set_ylabel(y_value, labelpad=10, loc='top')
        self.ax.plot(x, y, color=self.random_color(), label=selected_function)
        self.ax.legend(loc='upper right')
        self.ax.set_title(title)
        self.canvas.draw()
