import csv
from src.trans_vazio import eliminaVazio
#o estado tem uma lista de transicoes atreladas a ele
class Estado:
    def __init__(self, init):
        self.estado = init
        self.transicoes = []
    
class Transicao:
    def __init__(self, atomo):
        self.atomo = atomo
        self.finais = []

def genMatrizes(name,array, finais):
    atoms = set(e[1] for e in array)
    states = genEstados(array)
    genMatrix(name,states, atoms)
    states = eliminaVazio(name, states,finais)
    #genMatrix("vazio_"+name,states,atoms)
    return states
    
def genEstados(array): 
    estados = []
    transicao= ''
    init = set(e[0] for e in array)
    estado=''
    
    for i in init:
        estado = Estado(i)
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
    
    
    

    row_list.append(atoms)
    aux = ''

    for i in states:        
        row = []
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

   
    