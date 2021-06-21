from src.helpers import getState


def eliminaVazio(name, states):
    for estado in states:
        aux = False
        
        while aux == False:
            aux = True
            for trans in estado.transicoes:
                if trans.atomo == "e": 
                    aux = False
                    for fn in trans.finais:
                        estado.transicoes += getState(states,fn).transicoes
                        if getState(states,fn).isFinal == True:
                            estado.isFinal=True
                    estado.transicoes.remove(trans) 
    
    return states

    # checklist

    # ve se tem transiçao em vazio
    
    # se tiver transicao em vazio pega a lista de transicoes do atomo anterior
    