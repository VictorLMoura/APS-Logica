from Node import Node
from SymbolTable import SymbolTable

class FuncCall:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def Evaluate(self, STFunc):
        Func = STFunc.getter_func(self.value)
        if(len(Func.children)-1 != len(self.children)):
            raise ValueError("Numero de argumentos da funcao esta errado")

        STable2 = SymbolTable()
        cmds = Func.children[-1]
        for i in range(len(Func.children)-1):
            STable2.setter(Func.children[i].value, self.children[i].Evaluate(STFunc), Func.children[i].tipo)
        
        # print(cmds.Evaluate(STable2))
        res = cmds.Evaluate(STable2)
        if(res):
            if(res[1] == Func.return_type.upper()):
                return res
            else:
                raise ValueError("Tipo {} do retorno da funcao nao corresponde ao declarado {}".format(res[1], Func.return_type))
    