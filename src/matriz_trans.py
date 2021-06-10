import csv
from typing import final
#o estado tem uma lista de transicoes atreladas a ele
class Estado:
    transicoes = []
    def __init__(self, init):
        self.estado = init
    
class Transicao:
    finais = []
    def __init__(self, atomo):
       self.atomo = atomo

def genMatrix(name,array):
    filename='txts/matriz_'+name+'.csv'
    estados = []
    array.sort(key=lambda x:x[0])
    state = set(e[1] for e in array)
    init = set(e[0] for e in array)
    # for i in array:
    #     print(i)
    row_list =[]
    row_list.append(state)
    aux = ''
    for i in init:
        
        linha = []
        linha.append(i)
        estado = Estado(i)
        for st in state:
            tem = False
            for n in array:
                if(n[0]==i and n[1]==st):
                    tem=True 
                    transicao = Transicao(n[1])
                    transicao.finais.append(n[2])
                    estado.transicoes.append(transicao)
                    aux=n[2]
            if tem == True:

                linha.append(aux)
                tem = False   
            else:
                linha.append('-')     
        row_list.append(linha)
        estados.append(estado)
        
    
    with open(filename, 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

   
    