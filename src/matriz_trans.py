import csv
from src.trans_vazio import eliminaVazio
from src.trans_nao_det import eliminaNaoDeterministica
from src.trans_acess import eliminaNaoAcessivel
from src.trans_equivalentes import eliminaEquivalentes
from src.model import Estado, Transicao
#o estado tem uma lista de transicoes atreladas a ele


def genMatrizes(name,array, finais):
    atoms = set(e[1] for e in array)
    states = genEstados(array, finais)
    genMatrix(name,states, atoms)
    states = eliminaVazio(states)
    genMatrix('vazio_'+name, states,atoms)
    states = eliminaNaoDeterministica(states)
    genMatrix('Nao_Deterministica_'+name, states,atoms)
    states = eliminaNaoAcessivel(states)
    genMatrix('Nao_Acessivel_'+name, states,atoms)
    # states2 = eliminaEquivalentes(states)
    # genMatrix('Nao_Equivalentes_'+name, states,atoms)
    return states
    
def genEstados(array, finais): 
    estados = []
    transicao= ''
    init = set(e[0] for e in array)
    aux = set(e[2] for e in array) 
    init = set.union(init,aux)# para adicionar os estados sem transições partindo deles
    estado=''
    
    for i in init:
        isFinal = False
        for fn in finais:
            if i == fn:
                isFinal = True
        estado = Estado(i, isFinal)
        for trans in array:
            if(trans[0]==i):
                
                tem=False
                for tr in estado.transicoes:
                    if tr.atomo == trans[1]:
                    
                        tem=True
                        
                       
                        tr.finais.append(trans[2])

                if tem == False:
                    transicao = Transicao(trans[1])
                    transicao.finais.append(trans[2])
                    
                    estado.transicoes.append(transicao)    
        
                  
        estados.append(estado)
    return estados


def genMatrix(name, states, atoms):
    filename='txts/matriz_'+name+'.csv'
    row_list = []
    row = []
    
    atoms = list(atoms)
    atoms.sort()
    atoms.remove('e')
    atoms.insert(0,'e')

    row_list.append(atoms)
    aux = ''

    for i in states:        
        row = []
        if i.isFinal==True:
            row.append('('+str(i.estado)+')')
            
            
        else:    
            row.append(i.estado)
        for at in atoms:
            tem = False
            for tr in i.transicoes:
                if(tr.atomo==at):
                    tem=True 
                    aux=tr.finais
            if tem == True:

                row.append(aux)
                tem = False   
            else:
                row.append('-')     
        row_list.append(row)
        


    with open(filename, 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

   
    