class FirstOrderDifferential:
    def __init__(self, expr, variable):
        self.expr = str(expr)
        self.variable = str(variable)

class SecondOrderDifferential(FirstOrderDifferential):
    def __init__(self, expr, variable, second_variable):
        super().__init__(expr, variable)
        self.second_variable = str(second_variable)
