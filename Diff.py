from sympy import *
import re

class DiffCalculator:
    def get_variables(self, expr):
        symbols = list(sympify(expr).free_symbols)
        return sorted(symbols, key=lambda s: s.name)

    def get_terms(self, expr = ""):
        return re.split(r"[\+\-]", expr)

    def get_expr_string(self, expr, variables=[]):
        func_parameters = []
        for variable in variables:
            func_parameters.append(str(variable))

        func_parameters.sort()
        func_parameters = ",".join(func_parameters)

        return f"f({func_parameters}) = {expr}"

    def calc_diff(self, expr):
        variables = self.get_variables(expr)
        print(self.get_expr_string(expr, variables))
        print()

        print("Derivadas parciais primeiras da função f:")
        differentials = []
        for variable in variables:
            result = diff(expr, variable)
            differentials.append({"expression": result, "variable": variable})
            print(f"∂f/∂{variable} = {result}")
        
        print()
        self.calc_second_order_diff(expr, differentials, variables)

    def calc_second_order_diff(self, expr, differentials, variables):
        print("Derivadas parciais segundas da função f:")
        for differential in differentials:
            for variable in variables:
                print(f"∂²f/∂{differential['variable']}∂{variable} = {diff(differential['expression'], variable)}")
            
            print()

if __name__ == "__main__":
    diffCalculator = DiffCalculator()
    while True:
        try:
            expression = input("Digite uma expressão: ")

            if expression == "sair":
                break

            diffCalculator.calc_diff(expression)
                
        except:
            print("Não foi possível resolver a expressão.")
