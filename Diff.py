from sympy import *
import re

class DiffCalculator:
    differentials = []
    second_order_differentials = []

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
        self.expression = expr
        self.variables = self.get_variables(expr)
        print(self.get_expr_string(expr, self.variables))
        print()

        print("Derivadas parciais primeiras da função f:")

        for variable in self.variables:
            result = diff(expr, variable)
            self.differentials.append({"expression": result, "variable": str(variable)})
            print(f"∂f/∂{variable} = {result}")
        
        print()
        self.calc_second_order_diff()

    def calc_second_order_diff(self):
        print("Derivadas parciais segundas da função f:")
        for differential in self.differentials:
            for variable in self.variables:
                result = diff(differential['expression'], variable)
                self.second_order_differentials.append({"expression": result, "variable": [str(differential['variable']), str(variable)]})
                print(f"∂²f/∂{differential['variable']}∂{variable} = {result}")
            
            print()