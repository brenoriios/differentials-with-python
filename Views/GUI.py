import tkinter as tk
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Models.Differential import *

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de Derivadas Parciais")
        self.root.minsize(450, 350)

        self.init_gui()
        self.pack_gui()

    def init_gui(self):
        self.main_frame = tk.Frame(
            master = self.root,
            padx=10,
            pady=10
        )

        self.tip_label = tk.Label(
            master = self.main_frame,
            text = "Digite a expressão de uma função de duas ou mais variáveis:",
            font=("TkDefaultFont", 13)
        )

        self.controls_frame = tk.Frame(
            master = self.main_frame,
        )

        self.expr_input = tk.Entry(
            master = self.controls_frame,
            font=("TkDefaultFont", 13)
        )

        self.calculate_button = tk.Button(
            master = self.controls_frame,
            text = "Calcular",
        )

        self.result_frame = tk.Frame(
            master = self.main_frame,
            padx=10,
            pady=10
        )

        self.current_function = tk.Frame(
            master = self.result_frame
        )

        self.current_function_label = tk.Label(
            master = self.current_function,
            text = "Função Considerada:",
            justify="left",
            font=("TkDefaultFont", 13)
        )

        self.first_order_diff_result = tk.Frame(
            master = self.result_frame
        )

        self.first_order_diff_label = tk.Label(
            master = self.first_order_diff_result,
            text = "Derivadas parciais de primeira ordem:",
            justify="left",
            font=("TkDefaultFont", 13)
        )

        self.second_order_diff_result = tk.Frame(
            master = self.result_frame
        )

        self.second_order_diff_label = tk.Label(
            master = self.result_frame,
            text = "Derivadas parciais de segunda ordem:",
            justify="left",
            font=("TkDefaultFont", 13)
        )

        self.tip_label = tk.Label(
            master = self.main_frame,
            text = "",
            font=("TkDefaultFont", 13)
        )

    
    def pack_gui(self):
        self.expr_input.pack(side="left", fill="x", expand=True)
        self.calculate_button.pack(side="right")

        self.controls_frame.pack(fill="x")

        self.current_function.pack(fill="x")
        self.current_function_label.pack(fill="x")

        self.first_order_diff_label.pack(fill="x")
        self.first_order_diff_result.pack(fill="x")

        self.second_order_diff_label.pack(fill="x")
        self.second_order_diff_result.pack(fill="x")

        self.tip_label.pack()
        self.main_frame.pack(fill="both", expand=True)

    def set_first_order_diffs(self, results, params = ""):
        formatted_result_list = []

        for result in results:
            formatted_result_list.append(f"∂f({params})/∂{result.variable} = {result.expr.replace('**', '^')}")

        self.first_order_diff_result.config(text = "\n".join(formatted_result_list))

    def set_second_order_diffs(self, results, params = ""):
        formatted_result_list = []

        for result in results:
            formatted_result_list.append(f"∂²f({params})/∂{result.variable}∂{result.second_variable} = {result.expr.replace('**', '^')}")

        self.second_order_diff_result.config(text = "\n".join(formatted_result_list))

    def show_results(self, funcExpr, firstOrderDiffs, secondOrderDiffs, variables):
        self.print_function(self.current_function, funcExpr, variables)

        for diff in firstOrderDiffs:
            self.print_function(self.first_order_diff_result,diff.expr, variables, diff.variable)
        
        for diff in secondOrderDiffs:
            self.print_function(self.second_order_diff_result, diff.expr, variables, diff.variable, diff.second_variable)

        self.result_frame.pack(fill="x", expand=True)

    def print_function(self, element, expr, variables, first_var = "", second_var = ""):
        vars = ""

        if first_var != "":
            vars = "_{" + first_var + "}"

        if second_var != "":
            vars = "_{" + first_var + second_var + "}"

        function_expr = sp.sympify(expr)
        function_latex = f"$f{vars}({variables}) = {sp.latex(function_expr)}$"
        
        fig, ax = plt.subplots(figsize=(5, 0.4))
        ax.axis('off')
        ax.text(0.5, 0.5, function_latex, fontsize=13, ha='center', va='center')
        canvas = FigureCanvasTkAgg(fig, master = element)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=0, pady=0)
        plt.close(fig)

    def clear_results(self):
        for widget in self.current_function.winfo_children():
            if not isinstance(widget, tk.Label):
                widget.destroy()

        for widget in self.first_order_diff_result.winfo_children():
            if not isinstance(widget, tk.Label):
                widget.destroy()

        for widget in self.second_order_diff_result.winfo_children():
            if not isinstance(widget, tk.Label):
                widget.destroy()

    def run(self):
        self.root.mainloop()
