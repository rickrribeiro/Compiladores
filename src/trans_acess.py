from os import stat
from src.helpers import getState

#lembrar:
# verificar em todas os estados se não tem nenhuma transicao para aquele estado antes de remover algum estado final
def eliminaNaoAcessivel( states):
    
    
    for st in states:
        tem = False
        if st.estado == 0:
            continue
        for st2 in states:
            for trans in st2.transicoes:
                for fn in trans.finais:
                    if fn == st.estado:
                        tem=True
        if tem == False:
            # print(st.estado)
            states.remove(st)
   
    return states