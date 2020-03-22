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
            | TYPE t=INT_TYPE 
            | TYPE t=NUMBER_TYPE 
            | TYPE t=TIMESTAMP_TYPE
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

ID      : [_][0-9]+ ;
INT     : [0-9]+ ;
TEXT    : [A-z]+[0-9]* ;
STR     : '"' [A-z]+ '"' ;
FILENAME : [A-z./]+ ;

IGNORE : ('\r' | '\n' | ' ' | '\t')+  -> skip;