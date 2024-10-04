import tkinter as tk
from Models.Differential import *

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de Derivadas Parciais")
        self.root.minsize(350, 350)

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
            text = "Digite a expressão de uma função:",
        )

        self.controls_frame = tk.Frame(
            master = self.main_frame,
        )

        self.expr_input = tk.Entry(
            master = self.controls_frame
        )

        self.calculate_button = tk.Button(
            master = self.controls_frame,
            text = "Calcular"
        )

        self.result_frame = tk.Frame(
            master = self.main_frame,
            padx=10,
            pady=10
        )

        self.current_function_label = tk.Label(
            master = self.result_frame,
            justify="left",
            pady=10
        )

        self.first_order_diff_label = tk.Label(
            master = self.result_frame,
            text = "Derivadas parciais de primeira ordem:",
            justify="left"
        )

        self.first_order_diff_result = tk.Label(
            master = self.result_frame,
            justify="left",
            pady=10
        )

        self.second_order_diff_label = tk.Label(
            master = self.result_frame,
            text = "Derivadas parciais de segunda ordem:",
            justify="left"
        )

        self.second_order_diff_result = tk.Label(
            master = self.result_frame,
            justify="left",
            pady=10
        )

        self.tip_label_two = tk.Label(
            master = self.main_frame,
            text = "Dica: Não esqueça de colocar o operador * entre uma constante e uma variável. Ex.: 2*x",
        )

    
    def pack_gui(self):
        self.tip_label.pack()
        self.expr_input.pack(side="left", fill="x", expand=True)
        self.calculate_button.pack(side="right")

        self.controls_frame.pack(fill="x")

        self.current_function_label.pack(fill="x")

        self.first_order_diff_label.pack(fill="x")
        self.first_order_diff_result.pack(fill="x")

        self.second_order_diff_label.pack(fill="x")
        self.second_order_diff_result.pack(fill="x")

        self.tip_label_two.pack()
        self.main_frame.pack(fill="both", expand=True)

    def set_first_order_diffs(self, results):
        formatted_result_list = []

        for result in results:
            formatted_result_list.append(f"∂f/∂{result.variable} = {result.expr.replace('**', '^')}")

        self.first_order_diff_result.config(text = "\n".join(formatted_result_list))

    def set_second_order_diffs(self, results):
        formatted_result_list = []

        for result in results:
            formatted_result_list.append(f"∂²f/∂{result.variable}∂{result.second_variable} = {result.expr.replace('**', '^')}")

        self.second_order_diff_result.config(text = "\n".join(formatted_result_list))

    def show_results(self, expression):
        self.current_function_label.config(text = expression)
        self.result_frame.pack(fill="x", expand=True)

    def run(self):
        self.root.mainloop()
