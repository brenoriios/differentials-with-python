from sympy import *
from Exceptions.Exceptions import *
from Models.Differential import *
import re

class DifferentialCalculator:
    first_order_differentials: list = []
    second_order_differentials: list = []

    def get_variables(self, expr):
        symbols = list(sympify(expr).free_symbols)
        return sorted(symbols, key=lambda s: s.name)

    def get_terms(self, expr = ""):
        return re.split(r"[\+\-]", expr)

    def get_expr_string(self):
        func_parameters = self.get_func_paramns(self.variables)

        return f"f({func_parameters}) = {self.expr}"
    
    def get_func_paramns(self, variables):
        func_parameters = []
        for variable in variables:
            func_parameters.append(str(variable))

        func_parameters.sort()
        func_parameters = ",".join(func_parameters)

        return func_parameters

    def calc_diff(self, expr):
        self.expr = expr
        self.variables = self.get_variables(expr)

        if len(self.variables) > 3:
            raise MaxVariablesException()

        self.first_order_differentials = []
        for variable in self.variables:
            result = diff(expr, variable)
            self.first_order_differentials.append(FirstOrderDifferential(result, variable))

        self.calc_second_order_diff()

    def calc_second_order_diff(self):
        self.second_order_differentials = []
        for differential in self.first_order_differentials:
            for second_variable in self.variables:
                result = diff(differential.expr, second_variable)
                self.second_order_differentials.append(SecondOrderDifferential(result, differential.variable, second_variable))
