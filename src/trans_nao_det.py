from src.helpers import getState
from src.model import Estado, Transicao
#lembrar:
# verificar em todas os estados se não tem nenhuma transicao para aquele estado antes de remover algum estado final


def eliminaNaoDeterministica( states):
    
    for estado in states:     

        for trans in estado.transicoes:
            if len(trans.finais) > 1:
                newEstado = Estado(states [-1].estado + 1, estado.isFinal)
                # print(newEstado.estado)
                for fin in trans.finais:
                    newEstado.transicoes+=getState(states, fin).transicoes
                trans.finais = []
                trans.finais.append(newEstado.estado)
                states.append(newEstado)
        
    
    return states
