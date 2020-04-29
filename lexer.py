from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('EQUAL', r'\::')
        self.lexer.add('END', r'end')
        self.lexer.add('DATA_TYPE', r'int')
        self.lexer.add('PRINT', r'print')
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')
        #IF
        #ELSE
        #WHILE
        self.lexer.add('APAR', r'\(')
        self.lexer.add('FPAR', r'\)')
        self.lexer.add('ACH', r'\{')
        self.lexer.add('FCH', r'\}')
        self.lexer.add('PTVIRGULA', r'\;')
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('COMPEQUAL', r'\::::')
        self.lexer.add('COMPMAIOR', r'\>')
        self.lexer.add('COMPMENOR', r'\<')
        self.lexer.add('NOT', r'\!')  
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('IDENTIFIER', r'\w')
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
