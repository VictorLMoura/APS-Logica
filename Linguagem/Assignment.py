from Node import Node

class Assignment(Node):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def Evaluate(self, SymbolTable):
        #Fazer o setter na symbol table do valor do children 1
        SymbolTable.setter(self.children[0].value, self.children[1].Evaluate(SymbolTable), self.children[0].tipo)