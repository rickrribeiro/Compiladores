from src.helpers import getState, countFinal

def elimina_iguais(states):
    
    for st in states[:]:
        
        for st2 in states[:]:
            # if st2.estado == 230 and st.estado == 227:
            #     print("230 aq")
            if st2.isFinal != st.isFinal:
                continue
            
            if st2.estado < st.estado:
                continue
            if st.estado == st2.estado: #verifica se é ele mesmo
                continue
            eq2 = True
            temTrans=False
            if len(st.transicoes) == len(st2.transicoes):
                for trans in st.transicoes:
                    temTrans=True
                    eq1 = False
                    for trans2 in st2.transicoes:
                        if trans.atomo == trans2.atomo:
                            if trans.finais == trans2.finais:
                                eq1=True
                    if(eq1 == False):
                        eq2 = False
                if eq2 == True and temTrans == True:
                    
                    for st3 in states:
                        for trans3 in st3.transicoes:
                            for n in trans3.finais:
                                if n == st2.estado:
                                    n = st.estado
                    
                    #print(str(st.estado)+ ' '+ str(st2.estado))
                   
                    states.remove(st2)
    return states

def eliminaEquivalentes( states):
    states = elimina_iguais(states)
    # for st in states:
    #     aux = countFinal(states, st.estado)
    #     if aux == 0:
    #         print(st.estado)    
    
    return states

