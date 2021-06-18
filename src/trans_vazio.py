from src.helpers import getState
from src.trans_nao_det import eliminaNaoDeterministica
#lembrar:
# verificar em todas os estados se não tem nenhuma transicao para aquele estado antes de remover algum estado final. transforma a anterior em final
def eliminaVazio(name, states, finais):
    state = getState(states,1)
    print('stateee')
    if state != None:
        print(state)
        
    return eliminaNaoDeterministica(name,states,finais) #retornar finais