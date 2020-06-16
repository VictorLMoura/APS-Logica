from Node import Node

class StringVal(Node):
    def __init__(self, value=None):
        self.value = value

    def Evaluate(self, SymbolTable):
        return (self.value, "STRING")