/* ANTLR4 */
/* DSL FOR LOG GENERATION */ 
/* FOR QUICK AND EFFECTIVE LOG TESTING */

grammar elogGenerator;

/* Parser */ 

s       : g_type
        ;

g_type  : GENERATE output=LOG OUTPUT FILENAME body 
        | GENERATE output=DF body
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
            | TYPE t=INT_TYPE (int_option)*
            | TYPE t=NUMBER_TYPE (dec_option)*
            | TYPE t=TIMESTAMP_TYPE 
            ;

int_option  : opt_name=MIN opt_value=INT 
            | opt_name=MAX opt_value=INT 
            ; 

dec_option  : opt_name=MIN opt_value=DECIMAL 
            | opt_name=MAX opt_value=DECIMAL 
            | opt_name=DEC_CASES opt_value=INT
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
DEC_CASES   : 'DEC_CASES' ;
DF          : 'DF' ;

fragment QUOTE          : '"';
fragment LETTER         : [A-z] ; 
fragment DIGIT          : [0-9] ; 
fragment UNDERSCORE     : '_' ;

FILENAME : [A-z0-9/.]+ '.' LETTER+ ;
ID      : UNDERSCORE DIGIT+ ;
DECIMAL : DIGIT+ '.' DIGIT+ ;
INT     : DIGIT+ ;
TEXT    : LETTER+ DIGIT* ;


IGNORE : ('\r' | '\n' | ' ' | '\t')+  -> skip;