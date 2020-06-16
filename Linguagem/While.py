from Node import Node

class While(Node):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def Evaluate(self, SymbolTable):
        while(self.children[0].Evaluate(SymbolTable)[0]):
            self.children[1].Evaluate(SymbolTable)