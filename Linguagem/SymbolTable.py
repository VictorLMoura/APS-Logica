class SymbolTable():
    funcTables = {} #nomeFunc -> nó

    def __init__(self):
        self.table = {}
        
    def getter(self, nome):
        if nome in self.table.keys():
            return self.table[nome]
        else:
            raise ValueError("Variavel nao declarada: " + nome)

    def setter(self, nome, valor, tipo):
        #Sendo o valor agora uma tupla com o valor e o tipo
        # print(valor, tipo)
        if(valor[1] == tipo.upper()):
            self.table[nome] = valor
        else:
            raise ValueError("Variavel do tipo {} nao pode receber valores do tipo {}".format(tipo.upper(), valor[1]))

    @staticmethod
    def getter_func(nome):
        if nome in SymbolTable.funcTables.keys():
            return SymbolTable.funcTables[nome]

    @staticmethod
    def setter_func(func_def, nome):
        if nome in SymbolTable.funcTables.keys():
            raise ValueError("Funcao ja declarada")
        SymbolTable.funcTables[nome] = func_def

    def destroy(self):
        self.table = {}
