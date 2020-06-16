from Node import Node

class UnOp(Node):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def Evaluate(self, SymbolTable):
        if(self.value == "+"):
            return (self.children[0].Evaluate(SymbolTable)[0], self.children[0].Evaluate(SymbolTable)[1])
        elif(self.value == "-"):
            return (-self.children[0].Evaluate(SymbolTable)[0], self.children[0].Evaluate(SymbolTable)[1])
        elif(self.value == "!"):
            return (not self.children[0].Evaluate(SymbolTable)[0], self.children[0].Evaluate(SymbolTable)[1])