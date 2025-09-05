grammar IfElseLang;

program: statement+ EOF;

statement: assignment | ifStatement;

assignment: ID ASSIGN expr SEMI;

ifStatement: IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

condition: expr operator expr;

expr: ID | NUMBER;

operator: GT | EQ | LT | GE | LE | NE;

IF: 'if';
ELSE: 'else';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
GT: '>';
EQ: '==';
LT: '<';
GE: '>=';
LE: '<=';
NE: '!=';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
