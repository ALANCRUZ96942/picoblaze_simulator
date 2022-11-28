import ts as TS
ts_global = TS.TablaDeSimbolos()

#palabras reservadas
reservadas = {
    'NZ':'NZ',
    'Z':'Z',
    'NC':'NC',
    'C':'C',




    'LOAD' : 'LOAD',

    'AND' : 'AND',
    'OR' : 'OR',
    'XOR' : 'XOR',
    
    'ADD' : 'ADD',
    'ADDCY' : 'ADDCY',
    'SUB' : 'SUB',
    'SUBCY' : 'SUBCY',

    'TEST' : 'TEST',
    'TESTCY' : 'TESTCY',
    'COMPARE' : 'COMPARE',
    'COMPARECY' : 'COMPARECY',

    'SL0' : 'SL0',
    'SL1' : 'SL1',
    'SLX' : 'SLX',
    'SLA' : 'SLA',
    'RL' : 'RL',
    'SR0' : 'SR0',
    'SR1' : 'SR1',
    'SRX' : 'SRX',
    'SRA' : 'SRA',
    'RR' : 'RR',

    'INPUT' : 'INPUT',
    'OUTPUT' : 'OUTPUT',

    'STORE' : 'STORE',
    'FETCH' : 'FETCH',

   
    'INTERRUPT' : 'INTERRUPT',
    'RETURNI' : 'RDIS',
    'ENABLE': 'ENABLE',
    'DISABLE':'DISABLE',

    'JUMP' : 'JUMP',

    'CALL' : 'CALL',

    'RETURN': 'RETURN',



    'CONSTANT': 'CONSTANT',

    'NAMEREG': 'NAMEREG',

    'ADDRESS': 'ADDRESS'
    
}

tokens  = [
    'COMA',
    'DPUNTOS',
    'COMILLAS',
    'REG',
    'LABEL',
    'ID',
    'NUMBER',
    'HEXAD',
    'HEXA',
    'CHAR',
] + list(reservadas.values())

# Tokens
t_COMA    = r','
t_DPUNTOS   = r':'
t_COMILLAS   = r'"'


from instrucciones import *

def t_REG(t):
    r's[A-F_0-9]'   
    t.type = reservadas.get(t.value,'REG')    # Check for reserved words
    return t

def t_HEXAD(t):
    r'[0-3][A-F_0-9][0-9_A-F]'
    t.type = reservadas.get(t.value,'HEXAD')# Check for reserved words
    t.value = int(t.value,base=16)     
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'ID')    # Check for reserved words
     return t

def t_NUMBER(t):
    r'[A-F_0-9][A-F_0-9]'
    t.value = int(t.value,base=16) 
    return t

def t_CHAR(t):
    r'"[0-9A-Za-z_: ]"'   
    t.type = reservadas.get(t.value,'CHAR')    # Check for reserved words
    return t


# Caracteres ignorados

t_ignore = " \t"


def t_newline(t):
    r'\n'
    t.lexer.lineno += t.value.count("\n")

    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMENTARIO_SIMPLE(t):
    r';.*\n'
    t.lexer.lineno += 1    

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()



def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]



def p_instrucciones_lista(t) :
    '''instrucciones            :  instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion              : encapsular
                                | nombre_reg
                                |  reg_reg
                                | jumping
                                | calling
                                | interrupt
                                | address
                                | returning
                                

    
     '''
                                
    t[0] = t[1]



def p_instruccion_nombre_reg(t):

    '''
    nombre_reg      : NAMEREG REG COMA ID
                    | CONSTANT ID COMA NUMBER
    '''

    if(t[1] == 'NAMEREG'):            
        t[0] = Asignacion(t[4],t[1], t[2])
    else:
        t[0] = Asignacion(t[2],t[1], t[4])

def p_instruccion_regreg(t):
    '''
    reg_reg     : LOAD reg COMA reg
                | INPUT reg COMA reg
                | CONSTANT reg COMA reg
                | AND reg COMA reg
                | OR reg COMA reg
                | XOR reg COMA reg
                | ADD reg COMA reg
                | ADDCY reg COMA reg
                | SUB reg COMA reg
                | SUBCY reg COMA reg
                | TEST reg COMA reg
                | TESTCY reg COMA reg
                | OUTPUT reg COMA reg
                | COMPARE reg COMA reg
    '''
    
    t[0] = t[1]

def p_instruccion_jumping(t):
    '''
    jumping         : JUMP ID
                    | JUMP Z COMA ID
                    | JUMP NZ COMA ID
                    | JUMP C COMA ID
                    | JUMP NC COMA ID
    '''





    t[0] = t[1]



def p_instruccion_calling(t):
    '''
    calling         : CALL ID
                    | CALL Z COMA ID
                    | CALL NZ COMA ID
                    | CALL C COMA ID
                    | CALL NC COMA ID
    '''
    t[0] = t[1]
 
    

def p_instruccion_interrupt(t):
    '''
    interrupt       :    ENABLE INTERRUPT
                | DISABLE  INTERRUPT
                | RDIS DISABLE
                | RDIS ENABLE
    '''
    t[0] = t[1]

def p_instruccion_address(t):
    '''
    address       :    ADDRESS HEXAD
    '''
    t[0] = t[1]

def p_instruccion_returning(t):
    '''
    returning         : RETURN 
                    | RETURN Z COMA ID
                    | RETURN NZ COMA ID
                    | RETURN C COMA ID
                    | RETURN NC COMA ID
    '''
    t[0] = t[1]


def p_instruccion_encapsular(t):
    '''  encapsular      :    ID DPUNTOS  
    '''
    t[0] = Encapsular(t[1],int( t.lexer.lineno))
    
def p_term(t) :
    '''reg            : REG
                    |  CHAR
                    | ID
                    | NUMBER
                    '''
    t[0] = t[1]


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)



import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)








