from Node import Node

class NoOp(Node):
    def __init__(self, value=None):
        self.value = value

    def Evaluate(self, SymbolTable):
        pass