from os import stat
from src.lexico import lexicalAnalyzer
from src.sintatico import sintaticAnalyzer
from src.bota_ponto import bpontos
import sys
from src.tabelas import tabelaSimbolos, tabelaSimbolosPalavras

if len(sys.argv)!= 2:
    print('Informe o codigo fonte! ex: python ./staticchecker.py entrada.201')
try:

    if(len(sys.argv[1].split('.201'))!= 2):
        f = open(sys.argv[1]+'.201', 'r')
    else:
        f = open(sys.argv[1], 'r')
except:
    print('Código fonte não encontrado!')
    exit()
source = f.read()
f.close()

states = []
final = []
# name = 'teste'
# f = open('txts\\wirth_'+name+'.txt', 'r')
# text = f.read()
# f.close()
# testStates= bpontos(name, text)
# f = open('txts\\estado_final_'+name+'.txt', 'r')
# testeFinal = f.read()
# f.close()

name = 'program'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
programStates = bpontos(name, text)
f = open('txts\\estado_final_'+name+'.txt', 'r')
programFinal = f.read()
f.close()
states.append(programStates)
final.append(programFinal)

name = 'factor'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
factorStates = bpontos(name, text)
f = open('txts\\estado_final_'+name+'.txt', 'r')
factorFinal = f.read()
f.close()
states.append(factorStates)
final.append(factorFinal)

name = 'statement'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
statementStates = bpontos(name, text)
f = open('txts\\estado_final_'+name+'.txt', 'r')
statementFinal = f.read()
f.close()
states.append(statementStates)
final.append(statementFinal)


while True:
    result = lexicalAnalyzer(source, tabelaSimbolosPalavras())
    if result == source:
        break
    else:
        source = result



#Tem que ver oq faz com esses factors
#(226, 'factor', 228),
# E pq o (349, 'Integer-Number', 350) a 350 não tem nenhuma transição começando c ela, sendo que ela n é final

#tem que verificar a estrutura na tabela de simbolos, ver oq precisa botar. Por enquanto só ta feito p adicionar o valor
#usa esses sources p testar
source = "A02 A10\nC09 B12\nC03 B12\nA01 AB01 C02" #sao quatro diferentes. não deu p fzr mt pq a maioria ta em vazio
result = sintaticAnalyzer(source, tabelaSimbolosPalavras())#passa tabela de simbolos com none quando n quer adicionar um novo   
    

filename = sys.argv[1].split('.201')
f = open(filename[0]+'.LEX', 'w+')
f.write(source)
f.close
f = open(filename[0]+'.TAB', 'w+')
f.write(str(tabelaSimbolos(None)))
f.close

