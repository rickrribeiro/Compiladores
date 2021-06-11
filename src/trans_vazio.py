from src.helpers import getState

#lembrar:
# verificar em todas os estados se não tem nenhuma transicao para aquele estado antes de remover algum estado final
def eliminaVazio(name, states, finais):
    state = getState(states,1)
    print('stateee')
    if state is not None:
        print(state)
    return states