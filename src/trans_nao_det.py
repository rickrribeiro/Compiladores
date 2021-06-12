from src.helpers import getState
from src.trans_acess import eliminaNaoAcessivel
#lembrar:
# verificar em todas os estados se não tem nenhuma transicao para aquele estado antes de remover algum estado final
def eliminaNaoDeterministica(name, states, finais):
    
    return eliminaNaoAcessivel(name,states,finais)