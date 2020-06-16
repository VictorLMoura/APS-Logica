from Node import Node

class Readline(Node):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def Evaluate(self, SymbolTable):
        return (int(input()), "INT")
