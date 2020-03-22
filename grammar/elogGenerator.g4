/* ANTLR4 */
/* DSL FOR LOG GENERATION */ 
/* FOR QUICK AND EFFECTIVE LOG TESTING */

grammar elogGenerator;

/* Parser */ 

s       : g_type
        ;

g_type  : GENERATE LOG OUTPUT FILENAME body 
        ;


body     : activities traces columns count
         ;

activities  : ACTIVITIES (a_mapping)+
            ;

a_mapping   : TEXT ':' ID
            ;
        
traces      : TRACES t_list+ 
            ; 

t_list      : TEXT ('-' TEXT)* 
            ; 

count       : CASES INT 
            ;

columns     : column*  
            ; 

column      : COLUMN TEXT c_type ; 

c_type      : TYPE t=STRING_TYPE 
            | TYPE t=INT_TYPE int_options
            | TYPE t=NUMBER_TYPE
            | TYPE t=TIMESTAMP_TYPE 
            ;

int_options : MIN minv=INT 
            | MAX maxv=INT 
            | MIN minv=INT MAX maxv=INT
            | 
            ; 

/* Lexer */

GENERATE    : 'GENERATE' ;
LOG         : 'LOG' ;
OUTPUT      : 'OUTPUT' ;
ACTIVITIES  : 'ACTIVITIES' ;
TRACES      : 'TRACES' ;
CASES       : 'CASES' ;
COLUMN      : 'COLUMN' ; 
TYPE        : 'TYPE' ;
STRING_TYPE : 'String' ;
NUMBER_TYPE : 'Number' ; 
INT_TYPE    : 'Int' ;
TIMESTAMP_TYPE : 'Timestamp' ;
MAX         : 'MAX';
MIN         : 'MIN';

fragment QUOTE          : '"';
fragment LETTER         : [A-z] ; 
fragment DIGIT          : [0-9] ; 
fragment UNDERSCORE     : '_' ;

FILENAME : [A-z0-9/.]+ '.' LETTER+ ;
ID      : UNDERSCORE DIGIT+ ;
INT     : DIGIT+ ;
TEXT    : LETTER+ DIGIT* ;


IGNORE : ('\r' | '\n' | ' ' | '\t')+  -> skip;