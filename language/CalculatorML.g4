grammar CalculatorML;

// Tokens
NUMBER: [0-9]+('.'[0-9]+)?;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
// para operadores de comparación
GT: '>';
LT: '<';
EQ: '==';
LEQ: '<=';
GEQ: '>=';
NEQ: '!=';


// Matrix operations tokens
MATRIX_OP: 'transpose' | 'inverse';

// Reglas
prog: statement+;

statement
    : expr
    | ml_statement
    | assignment
    | forStatement
    | printStatement
    | whileStatement
    ;

assignment
    : ID '=' expr
    ;

expr
    : assignment                # AssignmentExpr
    | expr ('*'|'/') expr       # MulDiv
    | expr ('+'|'-') expr       # AddSub
    | expr ('<'|'>') expr       # Comparison
    | expr ('=='|'!='|'>'|'<') expr  # Comparaciones
    | matrixOperation           # MatrixOp
    | '(' expr ')'              # Parens
    | func '(' expr ')'         # Function
    | NUMBER                    # Number
    | ID                        # Variable
    | array                     # ArrayExpr
    | matrix                    # MatrixExpr
    | printStatement            # Print
    | whileStatement            # While
    | forStatement              # For
    | ifStatement		# If
    ;


matrix: '[' row (',' row)* ']';
row: '[' expr (',' expr)* ']';
matrixOperation
    : 'transpose' '(' ID ')'
    | 'inverse' '(' ID ')'
    ;

printStatement
    : 'print' '(' expr ')'
    ;
    
forStatement
    : 'for' ID 'in' expr '..' expr '{' statement* '}'
    ;
    
whileStatement
    : 'while' expr '{' statement* '}' 
    ;

func
    : 'sin' | 'cos' | 'tan'
    ;

ifStatement
    : 'if' expr '{' statement* '}' 
    | 'if' expr '{' statement* '}' 'else' '{' statement* '}' 
    ;
    
ml_statement
    : 'train' ID '(' ml_params ')'      # TrainModel
    | 'predict' ID '(' array ')'        # PredictModel
    ;

ml_params
    : array (',' array)+
    ;

array
    : '[' expr (',' expr)* ']'
    ;

