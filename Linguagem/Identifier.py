from Node import Node

class Identifier(Node):
    def __init__(self, value=None):
        self.value = value
        self.tipo = None

    def Evaluate(self, SymbolTable):
        #Ja retorna a tupla
        return SymbolTable.getter(self.value)
