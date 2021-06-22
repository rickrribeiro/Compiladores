from src.helpers import getState

def converteAtomo(atomo, symbols):
    for i, at in enumerate(atomo):
        for j, sy in enumerate(symbols):
            if at == sy[1]:
                atomo[i] = sy[0]
    return atomo

def checaTrans(states, atomo, state, idx):
    if idx+1 >= len(atomo):
        if state.isFinal == True:
            return 1
        
    for trans in state.transicoes:
        try:
            if trans.atomo.lower() == atomo[idx].lower():  
                for fin in trans.finais:  
                    return checaTrans(states, atomo, getState(states, fin), idx+1)
        except:
            return 0
    return 0    

                                
                       


def sintaticAnalyzer(source, symbols, states):

    
    source = source.replace('\n', '')
    atomos = source.split(' ')
    atomos = converteAtomo(atomos, symbols)
    
    passou = 0#p saber se passou em algum dos automatos
    for st in states: # lembrar de verificar cada automato, ver aonde cada um vai ser chamado, se é no \n. ai fazer um split no source no \n e fazer um foreach
       
        
        valido = checaTrans(st, atomos, getState(st,0), 0)
        if valido == 1:
            passou = 1
        
    if passou == 1:
        print('Passou na verificação sintática!')
    else:
        print('Não passou na verificação sintática!')
                    
                    
    
    return source

   