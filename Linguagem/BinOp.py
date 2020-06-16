from Node import Node

class BinOp(Node):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def getType(self, a, b):
        if(a == b ):
            return a
        else: 
            return "FLOAT"

    def Evaluate(self, SymbolTable):
        ch0 = self.children[0].Evaluate(SymbolTable)[0]
        ch0_type = self.children[0].Evaluate(SymbolTable)[1]
        ch1 = self.children[1].Evaluate(SymbolTable)[0]
        ch1_type = self.children[1].Evaluate(SymbolTable)[1]
        return_type = self.getType(ch0_type, ch1_type)

        if(self.value == "+"):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")
            return (ch0 + ch1, return_type)
        elif(self.value == "-"):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")
            return (ch0 - ch1, return_type)
        elif(self.value == "*"):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")
            return (ch0 * ch1, return_type)
        elif(self.value == "/"):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")
            return (ch0 // ch1, return_type)
        elif(self.value.upper() == "AND"):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")
            return (ch0 and ch1, "BOOL")
        elif(self.value.upper() == "OR"):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")
            return (ch0 or ch1, "BOOL")
        elif(self.value == "::::"):
            return (ch0 == ch1, "BOOL")
        elif(self.value == ">"):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")
            return (ch0 > ch1, "BOOL")
        elif(self.value == "<"):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")
            return (ch0 < ch1, "BOOL")
        elif(self.value == "."):
            if(ch0_type == "STRING" or ch1_type == "STRING"):
                return (str(ch0) + str(ch1), "STRING")
            else:
                raise ValueError("Operacao nao suportada entre esses tipos de variaveis")