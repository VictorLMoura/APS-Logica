from Node import Node

class If(Node):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def Evaluate(self, SymbolTable):
        if(self.children[0].Evaluate(SymbolTable)[0]):
            self.children[1].Evaluate(SymbolTable)
        elif(len(self.children) == 3):
            self.children[2].Evaluate(SymbolTable)
