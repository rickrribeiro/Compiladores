from src.helpers import getState


def sintaticAnalyzer(source, symbols, states):

    source = "A02 A10 C09 B12 C03 B12 A01 AB01 C02"
    
    #print(states[0][15].transicoes[0].atomo)


    
    atomo = source.split(' ')
    for i, at in enumerate(atomo):
        for j, sy in enumerate(symbols):
            if at == sy[1]:
                atomo[i] = sy[0]

        for aux in states[0]:
            
            for idx, trans in enumerate(aux.transicoes):
                
                if atomo[i-1] == trans.atomo:
  
                    for fin in trans.finais:
                        for trans2 in getState(states[0], fin).transicoes:
                            if atomo[i] == trans2.atomo:
                                print("Valido")
                            else:
                                print ("Invalido")
                        
                
    
    
    
    return source

   