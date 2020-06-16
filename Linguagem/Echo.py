from Node import Node

class Echo(Node):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def Evaluate(self, SymbolTable):
        print(self.children[0].Evaluate(SymbolTable)[0])