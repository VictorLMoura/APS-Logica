from Node import Node

class FuncDec:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.return_type = None
        
    def Evaluate(self, SymbolTable):
        SymbolTable.setter_func(self, self.value)