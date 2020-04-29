from rply import ParserGenerator
from ast import CompEqual, CompMaior, CompMenor, Add, Sub, Div, Mult, Number, Print, Assignment, Commands, Declaration, Identifier, NoOp, Or, And, Not, UnAdd, UnSub

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['EQUAL', 'END', 'PRINT', 'AND', 'OR', 'APAR', 'FPAR', 'DATA_TYPE',
             'ACH', 'FCH', 'PTVIRGULA', 'PLUS', 'MINUS', 'MULT', 'DIV', 'COMPEQUAL',
             'COMPMAIOR', 'COMPMENOR', 'NOT', 'NUMBER', 'IDENTIFIER', '$end', 'IF', 'ELSE', 'WHILE'],
            
            precedence=[ 
                ('left', ['FUNCTION',]), 
                ('left', ['EQUAL']), 
                ('left', ['IF', 'ELSE', 'END','WHILE',]), 
                ('left', ['AND', 'OR',]), 
                ('left', ['NOT',]), 
                ('left', ['COMPEQUAL','COMPMAIOR', 'COMPMENOR']), 
                ('left', ['PLUS', 'MINUS',]), 
                ('left', ['MULT', 'DIV',]),        
            ] 
        )

    def parse(self):
        @self.pg.production('commands : commands command')
        def commands(p):
            Cmds = Commands()
            Cmds.children.append(p[1])
            return Cmds

        @self.pg.production('command : IDENTIFIER EQUAL relexpr PTVIRGULA')
        @self.pg.production('command : PRINT APAR relexpr FPAR PTVIRGULA')
        # @self.pg.production('command : WHILE APAR relexpr FPAR commands')
        # @self.pg.production('command : IF APAR relexpr FPAR commands')
        # @self.pg.production('command : IF APAR relexpr FPAR commands ELSE commands')   
        @self.pg.production('command : PTVIRGULA')
        def command(p):
            if(p[0].gettokentype() == 'PRINT'):
                return Print(p[2])

            elif(p[0].gettokentype() == 'IDENTIFIER'):
                return Assignment(p[0], p[1])

            elif(p[0].gettokentype() == 'PTVIRGULA'):
                return NoOp()

        @self.pg.production('relexpr : expression COMPEQUAL expression')
        @self.pg.production('relexpr : expression COMPMAIOR expression')
        @self.pg.production('relexpr : expression COMPMENOR expression')
        @self.pg.production('relexpr : expression')
        def relexpr(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'COMPEQUAL':
                return CompEqual(left, right)
            elif operator.gettokentype() == 'COMPMAIOR':
                return CompMaior(left, right)
            elif operator.gettokentype() == 'COMPMENOR':
                return CompMenor(left, right)

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression OR expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'PLUS':
                return Add(left, right)
            elif operator.gettokentype() == 'MINUS':
                return Sub(left, right)
            elif operator.gettokentype() == 'OR':
                return Or(left, right)

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression AND expression')
        def term(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'MULT':
                return Add(left, right)
            elif operator.gettokentype() == 'DIV':
                return Sub(left, right)
            elif operator.gettokentype() == 'AND':
                return And(left, right)

        @self.pg.production('expression : PLUS expression')
        @self.pg.production('expression : MINUS expression')
        @self.pg.production('expression : NOT expression')
        @self.pg.production('expression : APAR relexpr FPAR')
        def factor(p):
            children = p[1]
            operator = p[0]
            if operator.gettokentype() == 'PLUS':
                return UnAdd(children)
            elif operator.gettokentype() == 'MINUS':
                return UnSub(children)
            elif operator.gettokentype() == 'AND':
                return Not(children)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('expression : IDENTIFIER')
        def identifier(p):
            return Identifier(p[0])

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
