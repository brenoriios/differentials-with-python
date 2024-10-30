from Engine.DifferentialCalculator import *
from Views.GUI import *

class Calculadora:
    def __init__(self, engine, gui):
        self.engine = engine
        self.gui = gui

        self.bind_button_actions()
    
    def run(self):
        self.gui.run()
    
    def bind_button_actions(self):
        self.gui.calculate_button.bind(
            "<Button-1>",
            lambda event, button=self.gui.calculate_button: self.calculate()
        )

    def calculate(self):
        try:
            self.gui.tip_label_error.pack_forget()
            self.gui.clear_results()
            expression = self.gui.expr_input.get()

            self.engine.calc_diff(expression)

            self.gui.show_results(
                self.engine.expr,
                self.engine.first_order_differentials,
                self.engine.second_order_differentials,
                self.engine.get_func_paramns(self.engine.variables)
            )
        except MaxVariablesException as e:
            print(str(e))
            self.gui.result_frame.pack_forget()
            self.gui.tip_label_error.config(text = str(e))
            self.gui.tip_label_error.pack()
        except Exception as e:
            print(str(e))
            self.gui.result_frame.pack_forget()
            self.gui.tip_label_error.config(text = "Erro ao calcular as derivadas da função!")
            self.gui.tip_label_error.pack()

if __name__ == "__main__":
    app = Calculadora(DifferentialCalculator(), GUI())
    app.run()
