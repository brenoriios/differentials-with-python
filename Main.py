from Diff import *
from GUI import *

class Main:
    def __init__(self, engine, gui):
        self.engine =  engine
        self.gui = gui

        self.bind_button_actions()
        self.gui.pack_gui()
    
    def run(self):
        self.gui.run()
    
    def bind_button_actions(self):
        self.gui.calculate_button.bind(
            "<Button-1>",
            lambda event, button=self.gui.calculate_button: self.calculate()
        )

    def calculate(self):
        self.engine.calc_diff(self.gui.expr_input.get())
        self.gui.show_results(self.engine.differentials, self.engine.second_order_differentials)

if __name__ == "__main__":
    app = Main(DiffCalculator(), GUI())
    app.run()
    # diffCalculator = DiffCalculator()
    # while True:
    #     try:
    #         expression = input("Digite uma expressão: ")

    #         if expression == "sair":
    #             break

    #         diffCalculator.calc_diff(expression)
                
    #     except:
    #         print("Não foi possível resolver a expressão.")
