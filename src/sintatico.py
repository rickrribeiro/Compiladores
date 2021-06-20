from src.helpers import getState

def converteAtomo(atomo, symbols):
    for i, at in enumerate(atomo):
        for j, sy in enumerate(symbols):
            if at == sy[1]:
                atomo[i] = sy[0]
    return atomo

def checaTrans(atomo, states, idx):

    valido = False
        
    for aux in states[0]:
        
        for trans in aux.transicoes:
            
            if atomo[idx-1] == trans.atomo and aux.estado == 0:

                for fin in trans.finais:
                    estadoatu = getState(states[0], fin)
                    for trans2 in estadoatu.transicoes:
                        if atomo[idx] == trans2.atomo:
                            print (trans2.atomo)
                            for fin2 in trans2.finais:
                                if getState(states[0], fin2).isFinal == True:
                                    valido = True
                                    
                                    return valido
                            
                            idx+=1
                            checaTrans(atomo, states, idx)
                            print (valido)
                            return valido


                                
                       


def sintaticAnalyzer(source, symbols, states):

    source = "A02 A10 C09 B12 C03 B12 A01 AB01 C02"
    idx = 1
    #print(states[0][15].transicoes[0].atomo)


    
    atomo = source.split(' ')
    atomo = converteAtomo(atomo, symbols)
    checaTrans(atomo, states, idx)
    
               
                    
    
    return source

   