from Node import Node

class Return(Node):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def Evaluate(self, SymbolTable):
        retTuple = (self.children[0].Evaluate(SymbolTable)[0], self.children[0].Evaluate(SymbolTable)[1])
        SymbolTable.setter("return", retTuple, retTuple[1])
        return retTuple

