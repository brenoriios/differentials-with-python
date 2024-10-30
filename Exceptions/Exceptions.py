class MaxVariablesException(Exception):
    def __init__(self):
        super().__init__("A função deve ter no maximo 3 variáveis!")
