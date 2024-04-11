from functionFrameBase import FunctionFrameBase
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import sympy as sp
import re

class FunctionAnalyzer(FunctionFrameBase):
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
        self.rangeX_label = ttk.Label(self, text="Range for x:")
        self.rangeX_entry = ttk.Entry(self)
        self.rangeY_label = ttk.Label(self, text="Range for y:")
        self.rangeY_entry = ttk.Entry(self)
        self.xvalue_lable = ttk.Label(self, text="x-label")
        self.xvalue_entry = ttk.Entry(self)
        self.yvalue_lable = ttk.Label(self, text="y-label")
        self.yvalue_entry = ttk.Entry(self)

        self.plot_button = ttk.Button(self, text="Plot", command=self.calculate_function)
        self.clear = ttk.Button(self, text="Clear", command=self.clear_canvas)

        # Create the canvas
        self.fig = plt.figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        self.grid_widgets()


    def grid_widgets(self):
        self.func_lable.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.func_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.rangeX_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.rangeX_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.rangeY_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.rangeY_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.xvalue_lable.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.xvalue_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.yvalue_lable.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.yvalue_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")


        self.plot_button.grid(row=0, column=2, columnspan=1, padx=5, pady=5, sticky="w")
        self.clear.grid(row=1, column=2, columnspan=1, padx=5, pady=5, sticky="w")

        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=3)

    '''def function_string(self):
        function_string = self.func_entry.get()
        return function_string'''

    '''def analyze_function(self, function_sting):
        if self.linear_function(function_sting):
            print("Linear Function")
            self.analyze_lfunction(function_sting)
        elif self.quadratic_function(function_sting):
            print("Quadratic Function")
            self.analyze_qfunction(function_sting)
        elif self.polynomail_function(function_sting):
            print("Polynomail Function")
            self.analyze_pfunction(function_sting)
        else:
            print("No Function")

    def linear_function(self, function_sting):
        linear_pattern = re.compile(r"^\s*f\(x\)\s*=\s*[+-]?\s*\d+\s*\*\s*x\s*[+-]?\s*\d+\s*$")
        return re.match(linear_pattern ,function_sting) is not None

    def quadratic_function(self, function_sting):
        quadratic_pattern = re.compile(r"^\s*f\(x\)\s*=\s*[+-]?\s*\d+\s*\*\s*x(\^2|²)\s*[+-]?\s*\d+\s*\*\s*x\s*[+-]?\s*\d+\s*$")  #^\s*f\(x\)\s*=\s*[+-]?\s*\d+\s*\*\s*x\*\*2\s*[+-]?\s*\d+\s*\*\s*x\s*[+-]?\s*\d+\s*$
        return re.match(quadratic_pattern, function_sting) is not None

    def polynomail_function(self, function_sting):
        polynomail_pattern = re.compile(r"^") #^\s*f\(x\)\s*=\s*[+-]?\s*\d+\s*\*\s*x\^2?\²?\s*[+-]?\s*\d+\s*\*\s*x\s*[+-]?\s*\d+\s*$
        return re.match(polynomail_pattern, function_sting) is not None
^\s*f\(x\)\s*=\s*[+-]?\s*\(\s*\d+\s*\*\s*x\^\(\d+\)\s*\)\s*[+-]?\s*\(\s*\d+\s*\*\s*x\^\(\d+\)\s*\)\s*([+-]?\s*\d+\s*)*$
    def analyze_lfunction(self, function_sting):
        pass
#q: kannst du mir ein regex schreiben, dass alle polynomailen Funktionen erkennt? #a: ^\s*f\(x\)\s*=\s*[+-]?\s*\(\s*\d+\s*\*\s*x\^\(\d+\)\s*\)\s*[+-]?\s*\(\s*\d+\s*\*\s*x\^\(\d+\)\s*\)\s*([+-]?\s*\d+\s*)*$
    def analyze_qfunction(self, function_sting):
        pass

    def analyze_pfunction(self, function_sting):
        pass

g(x)=0,5x^4-3x^3+5x^2-2x+0,5
^\s*f\(x\)\s*=\s*[+-]?\s*\(\s*\d+\s*\*\s*x\^\(\d+\)\s*\)\s*[+-]?\s*\(\s*\d+\s*\*\s*x\^\(\d+\)\s*\)\s*([+-]?\s*\d+\s*)*$
'''
    def remove_whitespace(self, string):
        output = ""

        for _, char in enumerate(string):
            if char != " ":
                output += char
        return output


    def range(self, inp):

        cln_input = self.remove_whitespace(inp)
        rangeX, rangeY = cln_input.split(',')
        return float(rangeX), float(rangeY)


    def extract_function_components(self, function_string):
        # Tokenize the function string
        tokens = re.findall(r'[-+]?\^?\s*\d*\.\d+\s*x?\s*|[-+]?\^?\s*\d*\,\d+\s*x?\s*|[-+]?\^?\s*\d+\s*x?\s*', function_string)       #[-+]?\d*\.\d+|[-+]?\d*\,\d+|[-+]?\d+

        terms = []
        exponents = []

        for token in tokens:
            # Extract the coefficient and exponent
            coefficient_match = re.search(r'[-+]?(?<!\^)\d*\.\d+|[-+]?(?<!\^)\d*\,\d+|[-+]?(?<!\^)\d+', token)    #'[-+]?(?<!\^)\d*\.\d+x?\s*|[-+]?(?<!\^)\d*\,\d+x?\s*|[-+]?(?<!\^)\d+x\s*'
            coefficient = coefficient_match.group(0) if coefficient_match else '1'
            
            exponent_match = re.search(r'\^[-+]?\d*\.?\d*', token)
            exponent = exponent_match.group(1) if exponent_match else '1'

            terms.append(coefficient)
            exponents.append(exponent)

        return terms, exponents, tokens
        

    def create_basis_exponent_pairs(self, terms, exponents):
        basis_exponent_pairs = []
        for term, exponent in zip(terms, exponents):
            try:
                '''basis = float(term)
                exponent = int(exponent)'''
                basis_exponent_pairs.append((float(term), int(exponent)))
            except ValueError:
                pass
                #basis = term  #0
            # Convert the term and exponent to a tuple and append it to the list
            #basis_exponent_pairs.append((term, exponent))

        return basis_exponent_pairs


    def create_derivative(self, function_string):

        terms, exponents = self.extract_function_components(function_string)
        # Create a symbolic variable
        x = sp.symbols('x')

        # Create the derivative for each term and combine them
        derivative_terms = []
        for term, exponent in zip(terms, exponents):
            # Create the expression for the term
            expression = term * x ** exponent

            # Calculate the derivative of the term
            derivative = sp.diff(expression, x)

            # Append the derivative to the list of derivative terms
            derivative_terms.append(derivative)

        # Combine the derivative terms to get the derivative of the function
        derivative_function = sum(derivative_terms)

        return derivative_function
    

    def determine_degree(self, exponents):
        # Extract the numerical values of the exponents
        cln_exponents = [int(exp.split('^')[-1]) for exp in exponents]

        max_degree = max(cln_exponents)

        return max_degree
    
    def reconstruct_function_string(self, basis_exponent_pairs, max_degree):
        function_parts = []

        for exponent in range(max_degree, -1, -1):
            coefficient = next((pair[0] for pair in basis_exponent_pairs if pair[1] == exponent), 0)
            if exponent == 0:
                term = f"{coefficient}"
            elif exponent == 1:
                term = f"{coefficient}x"
            else:
                term = f"{coefficient}x^{exponent}"
            function_parts.append(term)

        function = '+'.join(function_parts)
        return function
    

    def calculate_roots(self, function_string):
        
        terms, exponents, tokens = self.extract_function_components(function_string)

        max_degree = self.determine_degree(exponents)

        basis_exponent_pairs = self.create_basis_exponent_pairs(terms, exponents)

        function = self.reconstruct_function_string(basis_exponent_pairs, max_degree)

        x = sp.symbols('x')

        roots = []

        match max_degree:

            case 1:
                a, b = float(terms[1]), float(terms[0])
                if a != 0:
                    root = -b / a
                    roots.append(root)

            case 2:
                a, b, c = terms[2], terms[1], terms[0]
                if a != 0:
                    discriminant = b ** 2 - 4 * a * c
                    if discriminant > 0:
                        root1 = (-b + sp.sqrt(discriminant)) / (2 * a)
                        root2 = (-b - sp.sqrt(discriminant)) / (2 * a)
                        roots.extend([root1, root2])
                    elif discriminant == 0:
                        root = -b / (2 * a)
                        roots.append(root)

            case _:
                polynomial = sp.sympify(function)
                roots = sp.solve(polynomial, x)

        return roots
    

    def func(self, x_value):
        y_value = 0
        for basis, exponent in self.basis_exponent_pairs:
            try:
                basis = float(basis)
                exponent = int(exponent)
            except ValueError:
                continue
            y_value += basis * (x_value ** exponent)
        return y_value


    def from_func(self, x_value, func):
        y_value = 0
        for basis, exponent in self.basis_exponent_pairs:
            y_value += basis * x_value ** exponent
        return y_value


    def calculate_function(self):
   
        x_label = self.xvalue_entry.get()
        y_label = self.yvalue_entry.get()

        terms, exponents, tokens = self.extract_function_components(self.func_entry.get())
        self.basis_exponent_pairs = self.create_basis_exponent_pairs(terms, exponents)
        max_degree = self.determine_degree(exponents)

        self.fig.clear()

        x_val = np.arange(-50, 50, 0.01)
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.set_title('Function Plot')
        from_X, to_X = self.range(self.rangeX_entry.get())
        self.ax.set_xlim(from_X, to_X)
        from_Y, to_Y = self.range(self.rangeY_entry.get())
        self.ax.set_ylim(from_Y, to_Y)
        self.ax.grid(True)
        
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.spines['left'].set_position(('data', 0))

        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

        self.ax.plot(x_val, self.func(x_val), label=self.func_entry.get())

        roots_with_dub = self.calculate_roots(self.func_entry.get())

        roots_wout_dub = list(dict.fromkeys(roots_with_dub))

        roots = []

        for n in roots_wout_dub:
            if complex(self.setIn(self.func_entry.get(), n)) == 0:
                roots.append(n.real)

        self.ax.scatter(roots, [0 for _ in roots], color='blue', label='Roots')


        reconstruct_func = self.reconstruct_function_string(self.func_entry.get(), max_degree)

        self.ax.plot(x_val, self.from_func(x_val, reconstruct_func), label=reconstruct_func)

        _turning_points = self.calculate_roots(reconstruct_func)
        
        turning_points = []

        for n in _turning_points:
            if complex(self.setIn(reconstruct_func, n)) == 0:
                turning_points.append(n.real)

        if self.determine_degree(exponents) > 1:
            sec_reconstruct = self.reconstruct_function_string(reconstruct_func, max_degree - 1)

            if self.determine_degree(exponents) > 2:
                _point_of_inflection = self.calculate_roots(sec_reconstruct)

                point_of_inflection = []
                for n in _point_of_inflection:
                    if complex(self.setIn(sec_reconstruct, n)) == 0:
                        turning_points.append(n.real)

                self.ax.scatter(turning_points, [self.func(x) for x in turning_points], color='red', label='Turning Points')
                self.ax.scatter(point_of_inflection, [self.func(x) for x in point_of_inflection], color='green', label='Point of Inflection')
                self.ax.plot(x_val, self.from_func(x_val, sec_reconstruct), label=sec_reconstruct)


        self.ax.legend(loc='upper right')

        self.canvas.get_tk_widget().destroy() if hasattr(self, "canvas") else None
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.figure_frame)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.figure_frame.grid(row=9, column=0, sticky="nsew")


    def setIn(self, func, val):
        terms, exponents, tokens = self.extract_function_components(self.func_entry.get())
        basis_exponent_pairs = self.create_basis_exponent_pairs(terms, exponents)
        end_val = 0
        val = float(val)
        for basis, exponent in basis_exponent_pairs:
            exponent = int(exponent)
            basis = float(basis)
            match exponent:
                case 0:
                    end_val += basis
                case 1:
                    end_val += basis * val
                case _:
                    end_val += basis * val ** exponent
        return end_val
    
