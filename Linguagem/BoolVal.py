from Node import Node

class BoolVal(Node):
    def __init__(self, value=None):
        self.value = value

    def Evaluate(self, SymbolTable):
        if(self.value.upper() == "TRUE"):
            return (True, "BOOL")
        else:
            return (False, "BOOL")