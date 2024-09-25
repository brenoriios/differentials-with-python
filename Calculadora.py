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
            expression = self.gui.expr_input.get()

            self.engine.calc_diff(expression)

            self.gui.set_first_order_diffs(self.engine.first_order_differentials)
            self.gui.set_second_order_diffs(self.engine.second_order_differentials)

            self.gui.show_results(self.engine.get_expr_string())
        except:
            self.gui.result_frame.pack_forget()
            self.gui.expr_input.text = "Erro!"

if __name__ == "__main__":
    app = Main(DifferentialCalculator(), GUI())
    app.run()
