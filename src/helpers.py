def getState(states,id):
    for st in states:
        if st.estado==id:
            return st
        
    return None

def countFinal(states,id):
    count = 0 
    for st in states:
        for tr in st.transicoes:
            for fn in tr.finais:
                if fn == id:
                    count+=1
    return count