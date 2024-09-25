import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de Derivadas")

        self.init_gui()

    def init_gui(self):
        self.tip_label = tk.Label(
            master=self.root,
            text="Digite uma expressão"
        )
        self.expr_input = tk.Entry(
            master=self.root
        )
        self.calculate_button = tk.Button(
            master=self.root,
            text="Calcular"
        )

        self.result_box = tk.Label(
            master=self.root
        )
    
    def pack_gui(self):
        self.tip_label.pack()
        self.expr_input.pack()
        self.calculate_button.pack()
        self.result_box.pack()

    def show_results(self, results_first_order, results_second_order):
        for result in results_first_order:
            self.result_box.config(text = self.result_box.cget('text') + f"\n∂f/∂{result['variable']} = {result['expression']}")

        for result in results_second_order:
            self.result_box.config(text = self.result_box.cget('text') + f"\n∂²f/∂{'∂'.join(result['variable'])} = {result['expression']}")

    def run(self):
        self.root.mainloop()