from Node import Node

class Commands(Node):
    def __init__(self, value="CMDS"):
        self.value = value
        self.children = []

    def Evaluate(self, SymbolTable):
        for cmd in self.children:
            res = cmd.Evaluate(SymbolTable)
            try:
                return SymbolTable.getter("return")
            except Exception as e:
                pass
            if(cmd.value == "RETURN"):
                return res
