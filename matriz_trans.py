import csv

def genMatrix(filename,array):
    elements = []
    array.sort(key=lambda x:x[0])
    state = set(e[1] for e in array)
    init = set(e[0] for e in array)
    # for i in array:
    #     print(i)
    row_list =[]
    row_list.append(state)
    aux = ''
    for i in init:
        print(i)
        linha = []
        for st in state:
            tem = False
            for n in array:
                if(n[0]==i and n[1]==st):
                    tem=True 
                    aux=n[2]
            if tem == True:
                linha.append(aux)
                tem = False   
            else:
                linha.append('-')     
        row_list.append(linha)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

   
    