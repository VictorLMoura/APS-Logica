from Token import Token
import re

class Tokenizer:
    def __init__(self, origin):
        self.origin = origin #Codigo fonte que sera tokenizado
        self.position = 0
        self.actual = None
    
    def selectNext(self):
        res = 0
        contador = 1

        if(self.position >= len(self.origin)):
            tipo = "EOF"
            value = ""

        else:
            while(self.origin[self.position] == " "):
                self.position+=1

            #Le o proximo token e atualiza o atributo actual
            if(self.origin[self.position].isdigit()):
                if(self.position < len(self.origin)-1):
                    i = self.position+1
                    while(self.origin[i].isdigit()):
                        i+=1
                        contador+=1
                        if(i >= len(self.origin)):
                            break
                    res = int(self.origin[self.position:i])
                    if(self.origin[i] != "."):
                        tipo = "INT"
                    else:
                        i+=1
                        contador+=1
                        while(self.origin[i].isdigit()):
                            i+=1
                            contador+=1
                            if(i >= len(self.origin)):
                                break
                            res = float(self.origin[self.position:i])
                            tipo = "FLOAT"

                else:
                    res = int(self.origin[self.position])
                    tipo = "INT"

            elif(self.origin[self.position] == "."):
                res = self.origin[self.position]
                tipo = "CONCAT"
            
            elif(self.origin[self.position] == "+"):
                res = self.origin[self.position]
                tipo = "PLUS"
            
            elif(self.origin[self.position] == "-"):
                res = self.origin[self.position]
                tipo = "MINUS"

            elif(self.origin[self.position] == "*"):
                res = self.origin[self.position]
                tipo = "MULT"
            
            elif(self.origin[self.position] == "/"):
                i = self.position+1
                if(self.origin[i] == "/"):
                    i += 1
                    if(self.origin[i] == "/"):
                        res = self.origin[self.position:i+1]
                        contador+=2
                        tipo = "IF"
                    else:
                        raise ValueError("Caracter nao suportado")
                else:
                    res = self.origin[self.position]
                    tipo = "DIV"

            elif(self.origin[self.position] == "("):
                res = self.origin[self.position]
                tipo = "APAR"

            elif(self.origin[self.position] == ")"):
                res = self.origin[self.position]
                tipo = "FPAR"

            elif(self.origin[self.position] == "{"):
                res = self.origin[self.position]
                tipo = "ACH"

            elif(self.origin[self.position] == "}"):
                res = self.origin[self.position]
                tipo = "FCH"

            elif(self.origin[self.position] == ":"):
                temp = self.origin[self.position:self.position+4]
                temp2 = self.origin[self.position:self.position+2]
                if(temp == "::::"):
                    contador += 3
                    res = temp
                    tipo = "COMPEQUAL"
                elif(temp2 == "::"):
                    contador += 1
                    res = temp
                    tipo = "EQUAL"
                else: 
                    res = self.origin[self.position]
                    tipo = "DOISP"

            elif(self.origin[self.position] == "?"):
                res = self.origin[self.position]
                tipo = "INTERR"

            elif(self.origin[self.position] == ">"):
                temp = self.origin[self.position:self.position+3]
                if(temp == ">>>"):
                    contador += 2
                    res = temp
                    tipo = "WHILE"
                else:
                    res = self.origin[self.position]
                    tipo = "COMPMAIOR"

            elif(self.origin[self.position] == "<"):
                res = self.origin[self.position]
                tipo = "COMPMENOR"

            elif(self.origin[self.position] == "!"):
                res = self.origin[self.position]
                tipo = "NOT"

            elif(self.origin[self.position] == ";"):
                res = self.origin[self.position]
                tipo = "PTVIRGULA"

            elif(self.origin[self.position] == ","):
                res = self.origin[self.position]
                tipo = "VIRGULA"

            elif(self.origin[self.position] == "$"):
                i = self.position+1
                identifier_temp = self.origin[i]
                if(re.match("^[a-zA-Z_$]", identifier_temp)):
                    i += 1
                    contador += 1
                    while(re.match("^[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*$", identifier_temp) and i < len(self.origin)-1):
                        identifier = identifier_temp
                        identifier_temp += self.origin[i]    
                        i += 1
                        contador += 1

                if(re.match("^[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*$", identifier)):
                    contador -= 1
                    res = identifier
                    tipo = "IDENTIFIER"
                
                else:
                    raise ValueError("Identificador invalido")

            elif(self.origin[self.position] == "\""):
                i = self.position+1
                string = ""
                while(self.origin[i] != "\""):
                    string += self.origin[i]
                    i += 1
                    contador += 1
                res = string
                tipo = "STRING"
                contador += 1

            elif(re.match("^[a-zA-Z_$]", self.origin[self.position])):
                i = self.position
                reserved_temp = self.origin[i]
                i += 1
                contador += 1
                while(re.match("^[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*$", reserved_temp) and i < len(self.origin)-1):
                    reserved = reserved_temp
                    reserved_temp += self.origin[i]
                    i += 1
                    contador += 1
                
                if(reserved.upper() == "LOG"):
                    contador -= 2
                    res = reserved
                    tipo = "LOG"
                
                elif(reserved.upper() == "AND"):
                    contador -= 1
                    res = reserved
                    tipo = "AND"

                elif(reserved.upper() == "OR"):
                    contador -= 1
                    res = reserved
                    tipo = "OR"

                elif(reserved.upper() == "READLINE"):
                    contador -= 2
                    res = reserved
                    tipo = "READLINE"

                elif(reserved.upper() == "TRUE" or reserved.upper() == "FALSE"):
                    contador -= 2
                    res = reserved
                    tipo = "BOOL"
                
                elif(reserved.upper() == "FUNCTION"):
                    contador -= 2
                    res = reserved
                    tipo = "FUNCTION"

                elif(reserved.upper() == "RETURN"):
                    contador -= 2
                    res = reserved
                    tipo = "RETURN"

                elif(reserved.upper() == "INT"):
                    contador -= 2
                    res = reserved
                    tipo = "DATA_TYPE"

                elif(reserved.upper() == "FLOAT"):
                    contador -= 2
                    res = reserved
                    tipo = "DATA_TYPE"

                elif(reserved.upper() == "STR"):
                    contador -= 2
                    res = "STRING"
                    tipo = "DATA_TYPE"

                elif(reserved.upper() == "END"):
                    contador -= 2
                    res = "end"
                    tipo = "END"

                else:
                    contador -= 2
                    res = reserved
                    tipo = "NOME"

            else:
                raise ValueError(self.origin[self.position], "Caracter nao suportado")
        print(tipo, res)
        self.actual = Token(tipo, res)
        self.position += contador