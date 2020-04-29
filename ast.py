class SymbolTable():
    def __init__(self):
        self.table = {}

    def getter(self, nome):
        if nome in self.table.keys():
            return self.table[nome]
        else:
            raise ValueError("Variavel nao declarada: " + nome)

    def setter(self, nome, valor):
        self.table[nome] = valor

class Identifier():
    def __init__(self, value):
        self.value = value
    
    def eval(self, SymbolTable):
        return SymbolTable.getter(self.value)

class Commands():
    def __init__(self):
        self.children = []

    def eval(self, SymbolTable):
        for stmt in self.children:
            stmt.eval(SymbolTable)

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self, SymbolTable):
        return int(self.value)

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class UnaryOp():
    def __init__(self, children):
        self.children = children

class NoOp():
    def __init__(self, value=None):
        self.value = value
    
    def eval(self, SymbolTable):
        pass

class Assignment():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, SymbolTable):
        SymbolTable.setter(self.left.value, self.right.eval(SymbolTable))

class Declaration():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, SymbolTable):
        return

class Add(BinaryOp):
    def eval(self, SymbolTable):
        return self.left.eval(SymbolTable) + self.right.eval(SymbolTable)

class UnAdd(UnaryOp):
    def eval(self, SymbolTable):
        return self.children.eval(SymbolTable)

class Sub(BinaryOp):
    def eval(self, SymbolTable):
        return self.left.eval(SymbolTable) - self.right.eval(SymbolTable)

class UnSub(UnaryOp):
    def eval(self, SymbolTable):
        return -self.children.eval(SymbolTable)

class Mult(BinaryOp):
    def eval(self, SymbolTable):
        return self.left.eval(SymbolTable) * self.right.eval(SymbolTable)


class Div(BinaryOp):
    def eval(self, SymbolTable):
        return self.left.eval(SymbolTable) // self.right.eval(SymbolTable)

class And(BinaryOp):
    def eval(self, SymbolTable):
        return self.left.eval(SymbolTable) and self.right.eval(SymbolTable)

class Not(UnaryOp):
    def eval(self, SymbolTable):
        return not(self.children.eval)

class Or(BinaryOp):
    def eval(self, SymbolTable):
        return self.left.eval(SymbolTable) or self.right.eval(SymbolTable)

class CompEqual(BinaryOp):
    def eval(self, SymbolTable):
        return self.left.eval(SymbolTable) == self.right.eval(SymbolTable)

class CompMaior(BinaryOp):
    def eval(self, SymbolTable):
        return self.left.eval(SymbolTable) > self.right.eval(SymbolTable)

class CompMenor(BinaryOp):
    def eval(self):
        return self.left.eval(SymbolTable) < self.right.eval(SymbolTable)

#Colocar o if, while

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self, SymbolTable):
        print(self.value.eval(SymbolTable))
