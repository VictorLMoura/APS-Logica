## Definição da Linguagem
1. ### Funções   
  >  (name :: return_type , params_list) \
  >  function_body \
  >  return variable | expression | none ; \
  >  end ; 

2. ### Declarações de variáveis
  >  data_type name :: expression ;

3. ### Atribuição de valor para variáveis
  >  variable :: expression ;

4. ### If
  >  // condition / \
  >  corpo do if \
  >  end ;
5. ### Else if
  >  / condition / \
  >  corpo da outra condicao ; \
  >  end ;
6. ### Else
  >  / condition // \
  > corpo da condicao ; \
  >  end ;
7. ### While
  > (// condition /) \
  >  corpo do while ; \
  > end ;

## EBNF

  1. DECLARATION: EXPRESSION ; | DECLARATION EXPRESSION ;

  2. EXPRESSION: DATA_TYPE IDENTIFIER | EXPRESSION :: NUMBER ;

  3. EXPRESSION: DIGIT+

  4. NUMBER: INT_VALUE | FLOAT_VALUE | CHAR_VALUE | STR_VALUE

  5. WHILE: ( IF ) STATEMENT_LIST END;

  6. STATEMENT_LIST: STATEMENT+

  7. STATEMENT: DECLARATION | ASSIGNMENT | RETURN ;

  8. ASSIGNMENT: VARIABLE :: EXPRESSION ;

  9. RETURN: VARIABLE | EXPRESSION | NONE ;

  7. IF: // CONDITION / STATEMENT_LIST END;

  8. ELSE IF: / CONDITION / STATEMENET_LIST END;

  9. ELSE: / CONDITION // STATEMENT_LIST END;

  10. FUCTIONS: ( NAME :: RETURN_TYPE, PARAMS_LIST) STATEMENT_LIST END;

