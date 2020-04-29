# import sys
# from lexer import Lexer
# from _parser import Parser

# arguments = sys.argv
# # f = open(arguments[1], "r")
# f = open("teste.txt", "r")

# text_input = ""
# lines = f.readlines()
# for i in range(len(lines)):
#     try:
#         text_input += lines[i].strip()
#         print(text_input)
#     except Exception as e:
#         print(e)

# lexer = Lexer().get_lexer()
# tokens = lexer.lex(text_input)

# pg = Parser()
# pg.parse()
# parser = pg.get_parser()
# parser.parse(tokens).eval()



from lexer import Lexer
from _parser import Parser
from ast import SymbolTable

text_input = """
print(5+5+5);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

# for token in tokens:
#     print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
STable = SymbolTable()
parser.parse(tokens).eval(STable)