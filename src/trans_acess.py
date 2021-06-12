from src.helpers import getState
from src.trans_equivalentes import eliminaEquivalentes
#lembrar:
# verificar em todas os estados se não tem nenhuma transicao para aquele estado antes de remover algum estado final
def eliminaNaoAcessivel(name, states, finais):
    
    return eliminaEquivalentes(name,states,finais)