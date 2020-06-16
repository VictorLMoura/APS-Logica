from Node import Node

class IntVal(Node):
    def __init__(self, value=None):
        self.value = value

    def Evaluate(self, SymbolTable):
        return (self.value, "INT")