## EBNF

  1. Block = "{", { Command }, "}" \
    | ? { Command } end; \
    | : { Command } end;

  2. Command = ( λ | Assignment | Log), ";" | Block | If \
  | While | FuncDec | FuncCall | Return;

  3. If = "///", RelExpression, "?", \
    ( Command | { Command } ) | ( Command | { Command }, ELSE ( Command | { Command } ) ), 
    end;

  4. While = ">>>" RelExpression "?" \
    Command | { Command } 
    end;

  5. Assignment = Data_type, Identifier, "::", RelExpression";" ;

  6. Log = "log" ( RelExpression ) ";" ;

  7. RelExpression = Expression, { ("::::" | ">" | "<"), Expression } ;

  8. Expression = Term, { ("+" | "-" | "OR" | "."), Term } ;

  9. Term = Factor, { ("*" | "/" | "AND"), Factor } ;

  10. Factor = (("+" | "-" | "!"), Factor) | String | Int | 
  Float | Bool | FuncCall | "(", RelExpression")" | Identifier | ;

  11. Identifier = Letter, { Letter | Digit | "_" } ;

  12. Int = Digit, { Digit } ;

  13. Float = Digit | { Digit }, ".", Digit | { Digit } ;

  14. Digit = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

  15. String = ( a | ... | z | A | ... | Z ) ;

  16. FuncCall = Nome ( Identifier | { Identifier })

  17. FuncDec = Nome "::" Data_type ( Identifier | { Identifier } ) ":"\
      Command | { Command } 
      end;

## Exemplos da Linguagem

1. ### Definicao Funções
  >function _func :: int (int x): \
    return x; \
  end;

2. ### Chamada Funções
  >  _func(1);

2. ### Declarações de variáveis
  > int x :: 1; \
  > float y :: 1.0; \
  > str z :: "Hello World"; \

4. ### Print
  >  log("Hello world") ;

4. ### If
  >  /// x>y ? \
    log(x);\
    end;

6. ### Else
  >  : \
    log(y);\
    end;

7. ###IfElse
  > /// x>y ? \
    log(x);\
    end \
    : log(y);\
    end;

7. ### While
  > \>>> x>y ? \
    int x :: x + 1; \
    end;

## Características da linguagem
  <li> Tipagem forte, ou seja, não é possível atribuir valores do tipo Float para varíaveis inteiras. O mesmo acontece para as funções, uma vez declarado o tipo de retorno da função, caso ela retorne algo de outro tipo, o código não será validado.</li>

  <li> Existem diferentes sintaxes de blocos:
    <ul>1. A interrogação define o início de um if/while e o end define o fim deste bloco.</ul> 
    <ul>2. O código inteiro deve estar dentro de chaves para ser executado corretamente.</ul>
    <ul>3.É possível declarar blocos de else que não dependem de nenhuma condição anterior, ou seja, caso eu escreva algo como:</ul>
  </li>

> : log("Nao dependo de nenhuma condição para ser executado")\
  end;

<li>O objetivo desta linguagem é escrever códigos um pouco mais próximos de operadores ternários se basear um pouco mais na lógica para dar liberdade do programador criar os seus blocos de código.</li> 