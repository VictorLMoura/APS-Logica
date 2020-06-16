
from Tokenizer import Tokenizer
from PrePro import PrePro
from Node import Node
from BinOp import BinOp
from UnOp import UnOp
from NoOp import NoOp
from IntVal import IntVal
from Commands import Commands
from Identifier import Identifier
from Echo import Echo
from Assignment import Assignment
from SymbolTable import SymbolTable
from Readline import Readline
from If import If
from While import While
from BoolVal import BoolVal
from StringVal import StringVal
from FloatVal import FloatVal
from FuncDec import FuncDec
from FuncCall import FuncCall
from Return import Return

class Parser():
    tokens = None

    @staticmethod
    def parseBlock():
        node = Commands()
        if(Parser.tokens.actual.token_type == "ACH"):
            Parser.tokens.selectNext()
            while(True):
                if(Parser.tokens.actual.token_type == "FCH"):
                    Parser.tokens.selectNext()
                    return node
                else:
                    node.children.append(Parser.parseCommand())
        if(Parser.tokens.actual.token_type == "INTERR"):
            Parser.tokens.selectNext()
            while(True):
                if(Parser.tokens.actual.token_type == "END"):
                    Parser.tokens.selectNext()
                    return node
                else:
                    node.children.append(Parser.parseCommand())
        if(Parser.tokens.actual.token_type == "DOISP"):
            Parser.tokens.selectNext()
            while(True):
                if(Parser.tokens.actual.token_type == "END"):
                    Parser.tokens.selectNext()
                    return node
                else:
                    node.children.append(Parser.parseCommand())
        else:
            raise ValueError('Erro de chaves')

    @staticmethod
    def parseCommand():
        if(Parser.tokens.actual.token_type == "PTVIRGULA"):
            node = NoOp()
            Parser.tokens.selectNext()
            return node
        elif(Parser.tokens.actual.token_type == "DATA_TYPE"):
            identifier = Identifier()
            identifier.tipo = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == "NOME"):
                identifier.value = Parser.tokens.actual.value
                Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == "EQUAL"):
                node = Assignment(Parser.tokens.actual.value)
                Parser.tokens.selectNext()
                node.children.append(identifier)
                node.children.append(Parser.parseRelexpr())
                if(Parser.tokens.actual.token_type == "PTVIRGULA"):
                    Parser.tokens.selectNext()
                    return node
                else:
                    raise ValueError('Esperado um ponto e virgula')

            else:
                raise ValueError('Esperado um assignment')

        elif(Parser.tokens.actual.token_type == "LOG"):
            node = Echo(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == "APAR"):
                Parser.tokens.selectNext()
                node.children.append(Parser.parseRelexpr())
                if(Parser.tokens.actual.token_type == "FPAR"):
                    Parser.tokens.selectNext()
                    if(Parser.tokens.actual.token_type == "PTVIRGULA"):
                        Parser.tokens.selectNext()
                        return node
                    else:
                        raise ValueError('Esperado um ponto e virgula')
                else:
                    raise ValueError('Esperado um parentesis')
            else:
                raise ValueError('Esperado um parentesis')  

        elif(Parser.tokens.actual.token_type == "IF"):
            node =  If(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            node.children.append(Parser.parseRelexpr())
            # if(Parser.tokens.actual.token_type == "INTERR"):
            # Parser.tokens.selectNext()
            node.children.append(Parser.parseCommand())
            # if(Parser.tokens.actual.token_type == "DOISP"):
                # Parser.tokens.selectNext()
            node.children.append(Parser.parseCommand())
            return node
            # else:
            #     return node
            # else:
            #     raise ValueError('Esperado um parenteses')

        elif(Parser.tokens.actual.token_type == "WHILE"):
            node =  While(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            node.children.append(Parser.parseRelexpr())
            node.children.append(Parser.parseCommand())
            return node

        elif(Parser.tokens.actual.token_type == "FUNCTION"):
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == "NOME"):
                node = FuncDec(Parser.tokens.actual.value)
                Parser.tokens.selectNext()
                if(Parser.tokens.actual.token_type == "EQUAL"):
                    Parser.tokens.selectNext()
                    if(Parser.tokens.actual.token_type == "DATA_TYPE"):
                        node.return_type = Parser.tokens.actual.value
                        Parser.tokens.selectNext()
                        if(Parser.tokens.actual.token_type == "APAR"):
                            Parser.tokens.selectNext()
                            while(True):
                                if(Parser.tokens.actual.token_type == "DATA_TYPE"):
                                    identifier = Identifier()
                                    identifier.tipo = Parser.tokens.actual.value
                                    Parser.tokens.selectNext()
                                    if(Parser.tokens.actual.token_type == "NOME"):
                                        identifier.value = Parser.tokens.actual.value
                                        Parser.tokens.selectNext()
                                        node.children.append(identifier)
                                        if(Parser.tokens.actual.token_type == "VIRGULA"):
                                            Parser.tokens.selectNext()
                                        elif(Parser.tokens.actual.token_type == "FPAR"):
                                            Parser.tokens.selectNext()
                                            node.children.append(Parser.parseBlock())
                                            return node
                                        else:
                                            raise ValueError("Esperado uma virgula ou parentesis")
                                elif(Parser.tokens.actual.token_type == "FPAR"):
                                    Parser.tokens.selectNext()
                                    node.children.append(Parser.parseBlock())
                                    return node
                                else:
                                    raise ValueError("Esperado um identifier")
                        else: 
                            raise ValueError("Esperado um parentesis")
                    else:
                        raise ValueError("Esperado o tipo do retorno da funcao")
            else:
                raise ValueError("Esperado o nome da funcao")

        elif(Parser.tokens.actual.token_type == "RETURN"):
            node = Return(Parser.tokens.actual.token_type)
            Parser.tokens.selectNext()
            node.children.append(Parser.parseRelexpr())
            if(Parser.tokens.actual.token_type == "PTVIRGULA"):
                Parser.tokens.selectNext()
                return node
            else:
                raise ValueError('Esperado um ponto e virgula')

        elif(Parser.tokens.actual.token_type == "NOME"):
            node = FuncCall(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == "APAR"):
                Parser.tokens.selectNext()
                while(True):
                    if(Parser.tokens.actual.token_type == "FPAR"):
                        Parser.tokens.selectNext()
                        return node
                    else:
                        node.children.append(Parser.parseRelexpr())
                        if(Parser.tokens.actual.token_type == "VIRGULA"):
                            Parser.tokens.selectNext()
                        elif(Parser.tokens.actual.token_type == "FPAR"):
                            Parser.tokens.selectNext()
                            return node
                        else:
                            raise ValueError("Esperado uma virgula ou parentesis")
            else: 
                raise ValueError("Esperado um parentesis")

        else:
            return Parser.parseBlock()

    @staticmethod
    def parseRelexpr():
        node_prev = Parser.parseExpression()
        if((Parser.tokens.actual.token_type == "COMPEQUAL") or (Parser.tokens.actual.token_type == "COMPMAIOR") or (Parser.tokens.actual.token_type == "COMPMENOR")):
            while((Parser.tokens.actual.token_type == "COMPEQUAL") or (Parser.tokens.actual.token_type == "COMPMAIOR") or (Parser.tokens.actual.token_type == "COMPMENOR")):
                node = BinOp()
                if(Parser.tokens.actual.token_type == "COMPEQUAL"):
                    node.value = Parser.tokens.actual.value
                    node.children.append(node_prev)
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parseExpression())
                    node_prev = node
                elif(Parser.tokens.actual.token_type == "COMPMAIOR"):
                    node.value = Parser.tokens.actual.value
                    node.children.append(node_prev)
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parseExpression())
                    node_prev = node
                elif(Parser.tokens.actual.token_type == "COMPMENOR"):
                    node.value = Parser.tokens.actual.value
                    node.children.append(node_prev)
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parseExpression())
                    node_prev = node
                else:
                    raise ValueError('Depois de um numero deveria vir uma operacao')     
            return node                   
        else:
            return node_prev

    @staticmethod
    def parseExpression():
        node_prev = Parser.parseTerm()
        if((Parser.tokens.actual.token_type == "PLUS") or (Parser.tokens.actual.token_type == "MINUS") or (Parser.tokens.actual.token_type == "OR") or (Parser.tokens.actual.token_type == "CONCAT")):
            while((Parser.tokens.actual.token_type == "PLUS") or (Parser.tokens.actual.token_type == "MINUS") or (Parser.tokens.actual.token_type == "OR") or (Parser.tokens.actual.token_type == "CONCAT")):
                node = BinOp()
                if(Parser.tokens.actual.token_type == "PLUS"):
                    node.value = Parser.tokens.actual.value
                    node.children.append(node_prev)
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parseTerm())
                    node_prev = node
                elif(Parser.tokens.actual.token_type == "MINUS"):
                    node.value = Parser.tokens.actual.value
                    Parser.tokens.selectNext()
                    node.children.append(node_prev)
                    node.children.append(Parser.parseTerm())
                    node_prev = node
                elif(Parser.tokens.actual.token_type == "OR"):
                    node.value = Parser.tokens.actual.value
                    Parser.tokens.selectNext()
                    node.children.append(node_prev)
                    node.children.append(Parser.parseTerm())
                    node_prev = node
                elif(Parser.tokens.actual.token_type == "CONCAT"):
                    node.value = Parser.tokens.actual.value
                    Parser.tokens.selectNext()
                    node.children.append(node_prev)
                    node.children.append(Parser.parseTerm())
                    node_prev = node
                else:
                    raise ValueError('Depois de um numero deveria vir uma operacao')
            return node                        
        else:
            return node_prev
                

    @staticmethod
    def parseTerm():
        node_prev = Parser.parseFactor()
        if((Parser.tokens.actual.token_type == "MULT") or (Parser.tokens.actual.token_type == "DIV") or (Parser.tokens.actual.token_type == "AND")):
            while((Parser.tokens.actual.token_type == "MULT") or (Parser.tokens.actual.token_type == "DIV")or (Parser.tokens.actual.token_type == "AND")):
                node = BinOp()
                if(Parser.tokens.actual.token_type == "MULT"):
                    node.value = Parser.tokens.actual.value
                    node.children.append(node_prev)
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parseFactor())
                    node_prev = node
                elif(Parser.tokens.actual.token_type == "DIV"):
                    node.value = Parser.tokens.actual.value
                    node.children.append(node_prev)
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parseFactor())
                    node_prev = node
                elif(Parser.tokens.actual.token_type == "AND"):
                    node.value = Parser.tokens.actual.value
                    node.children.append(node_prev)
                    Parser.tokens.selectNext()
                    node.children.append(Parser.parseFactor())
                    node_prev = node
                else:
                    raise ValueError('Depois de um numero deveria vir uma operacao')     
            return node                   
        else:
            return node_prev
    
    @staticmethod
    def parseFactor():
        if(Parser.tokens.actual.token_type == "INT"):
            node = IntVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            return node

        if(Parser.tokens.actual.token_type == "FLOAT"):
            node = FloatVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            return node

        elif(Parser.tokens.actual.token_type == "BOOL"):
            node = BoolVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            return node

        elif(Parser.tokens.actual.token_type == "STRING"):
            node = StringVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            return node

        elif(Parser.tokens.actual.token_type == "IDENTIFIER"):
            identifier = Identifier()
            identifier.value = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            return identifier

        elif((Parser.tokens.actual.token_type == "PLUS") or (Parser.tokens.actual.token_type == "MINUS")):
            if(Parser.tokens.actual.token_type == "PLUS"):
                node = UnOp(Parser.tokens.actual.value)

                Parser.tokens.selectNext()
                res_factor = Parser.parseFactor()

                node.children.append(res_factor)

            elif(Parser.tokens.actual.token_type == "MINUS"):
                node = UnOp(Parser.tokens.actual.value)

                Parser.tokens.selectNext()
                res_factor = Parser.parseFactor()

                node.children.append(res_factor)

        elif(Parser.tokens.actual.token_type == "NOT"):
            node = UnOp(Parser.tokens.actual.value)

            Parser.tokens.selectNext()
            res_factor = Parser.parseFactor()

            node.children.append(res_factor)

        elif(Parser.tokens.actual.token_type == "APAR"):
            Parser.tokens.selectNext()
            res = Parser.parseRelexpr()
            if(Parser.tokens.actual.token_type == "FPAR"):
                Parser.tokens.selectNext()
                return res
            else:
                raise ValueError('Parenteses nao foi fechado')

        elif(Parser.tokens.actual.token_type == "READLINE"):
            node = Readline(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == "APAR"):
                Parser.tokens.selectNext()
                if(Parser.tokens.actual.token_type == "FPAR"):
                    Parser.tokens.selectNext()
                    return node
                else:
                    raise ValueError('Parenteses nao foi fechado')

            else:
                raise ValueError('Parenteses nao foi aberto')

        elif(Parser.tokens.actual.token_type == "NOME"):
            value = Parser.tokens.actual.value
            Parser.tokens.selectNext()
            if(Parser.tokens.actual.token_type == "APAR"):
                node = FuncCall(value)
                Parser.tokens.selectNext()
                while(True):
                    node.children.append(Parser.parseRelexpr())
                    if(Parser.tokens.actual.token_type == "VIRGULA"):
                        Parser.tokens.selectNext()
                    elif(Parser.tokens.actual.token_type == "FPAR"):
                        Parser.tokens.selectNext()
                        return node
                    else:
                        raise ValueError("Esperado uma virgula ou parentesis")
            else: 
                identifier = Identifier()
                identifier.value = value 
                return identifier

        else:
            raise ValueError('Erro')
        return node

    @staticmethod
    def run(code):
        #recebe o codigo, inicializa o Tokenizer e retorna o resultado da chamada do metodo
        code = PrePro.filter(code)
        Parser.tokens = Tokenizer(code)
        Parser.tokens.selectNext()
        #parseExpression
        res = Parser.parseCommand()
        if(Parser.tokens.actual.token_type == "EOF"):
            STable = SymbolTable()
            return res.Evaluate(STable)
        else:
            raise ValueError('Deveria terminar no EOF')
        