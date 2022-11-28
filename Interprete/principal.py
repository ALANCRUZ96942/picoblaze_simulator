import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *
import sys


variables = []
registros = []



def main(arg1,arg2):
    # do whatever the script does

    def procesar_asignacion(instr, ts) :
        simbolo = TS.Simbolo(instr.id, instr.type, instr.num)
        ts.agregar(simbolo)
        print('id es '+simbolo.id+' es del tipo '+simbolo.tipo+' y vale: '+str(simbolo.valor))


    def procesar_encapsular_guardar(instr,tsf) :
        simbolo = TS.Simbolo(instr.id, 'f', 'f')
        tsf.agregar(simbolo)
        print('id es '+simbolo.id+'sus instrucciones son:'+str(instr.value))
        #procesar_instrucciones(instr.instrucciones, ts_global,ts_funciones)

    def procesar_llamado(instr,tsf) :
        
        simbolo = tsf.obtener(instr.id)
        print('id es '+simbolo.id)
        #procesar_instrucciones(instr.instrucciones, ts_global,ts_funciones)


    """def procesar_mientras(instr, ts) :
        while resolver_expreision_logica(instr.expLogica, ts) :
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            procesar_instrucciones(instr.instrucciones, ts_local)

    def procesar_if(instr, ts) :
        val = resolver_expreision_logica(instr.expLogica, ts)
        if val :
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            procesar_instrucciones(instr.instrucciones, ts_local)

    def procesar_if_else(instr, ts) :
        val = resolver_expreision_logica(instr.expLogica, ts)
        if val :
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            procesar_instrucciones(instr.instrIfVerdadero, ts_local)
        else :
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            procesar_instrucciones(instr.instrIfFalso, ts_local)"""

    """def resolver_cadena(expCad, ts) :
        if isinstance(expCad, ExpresionConcatenar) :
            exp1 = resolver_cadena(expCad.exp1, ts)
            exp2 = resolver_cadena(expCad.exp2, ts)
            return exp1 + exp2
        elif isinstance(expCad, ExpresionDobleComilla) :
            return expCad.val
        elif isinstance(expCad, ExpresionCadenaNumerico) :
            return str(resolver_expresion_aritmetica(expCad.exp, ts))
        else :
            print('Error: Expresión cadena no válida')


    def resolver_expreision_logica(expLog, ts) :
        exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
        if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
        if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
        if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
        if expLog.operador == OPERACION_LOGICA.DIFERENTE : return exp1 != exp2

    def resolver_expresion_aritmetica(expNum, ts) :
        if isinstance(expNum, ExpresionBinaria) :
            exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
            exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
            if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
            if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
            if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
            if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
        elif isinstance(expNum, ExpresionNegativo) :
            exp = resolver_expresion_aritmetica(expNum.exp, ts)
            return exp * -1
        elif isinstance(expNum, ExpresionNumero) :
            return expNum.val
        elif isinstance(expNum, ExpresionIdentificador) :
            return ts.obtener(expNum.id).valor
    """

    def procesar_instrucciones(instrucciones, ts,tsf) :
        ## lista de instrucciones recolectadas
        for instr in instrucciones :
            if isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
            elif isinstance(instr, Encapsular) : procesar_encapsular_guardar(instr,tsf)
            #elif isinstance(instr, Llamar) : procesar_llamado(instr,tsf)
            #else : print(instr)
            variables.append(instr)



    #Para archivos estáticos
    if(int(arg1) == 0):
        f = open("./programs/"+str(arg2)+".psm", "r")
        input = f.read()
    else:
        input = arg2


    instrucciones = g.parse(input)
    ts_global = TS.TablaDeSimbolos()
    ts_funciones = TS.TablaDeSimbolos()

    procesar_instrucciones(instrucciones, ts_global,ts_funciones)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
