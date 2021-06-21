from src.helpers import getState
from src.model import Estado, Transicao
#lembrar:
# verificar em todas os estados se não tem nenhuma transicao para aquele estado antes de remover algum estado final


def eliminaNaoDeterministica(name, states):
    
    for estado in states:     
           
        if len(estado.transicoes) > 1:
            newEstado = Estado
            newEstado.transicoes = estado.transicoes
            newEstado.isFinal = estado.isFinal
            newEstado.estado = states[-1].estado + 1
            states.append(newEstado)
            for aux in states:
               
                for transaux in aux.transicoes:
                    for fin in transaux.finais:
                        auxEstado = getState(states, fin)
                        
                        if auxEstado == estado.estado:
                            auxEstado.transicoes
                            for tempTrans in auxEstado.transicoes:
                                for finTemp in tempTrans.finais:
                                    if finTemp == estado.estado:
                                        finTemp = newEstado.estado
                                        
            states.remove(estado)
    
    return states
