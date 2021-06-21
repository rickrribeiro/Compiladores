from os import stat
from src.lexico import lexicalAnalyzer
from src.sintatico import sintaticAnalyzer
from src.bota_ponto import bpontos
import sys
from src.tabelas import tabelaSimbolos, tabelaSimbolosPalavras
from src.helpers import removeComments


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


name = 'factor'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
factorStates = bpontos(name, text)
f = open('txts\\estado_final_'+name+'.txt', 'r')
factorFinal = f.read()
f.close()
states.append(factorStates)


name = 'statement'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
statementStates = bpontos(name, text)
f = open('txts\\estado_final_'+name+'.txt', 'r')
statementFinal = f.read()
f.close()
states.append(statementStates)

source = removeComments(source)
#verifica se tem aspas abertas
open_aspas = 0
line = 1 
for ch in source:
    if ch == '\n':
        line+=1
    if ch == '"':
       open_aspas +=1

if open_aspas%2 == 1:
    print('Aspas sem fechar na linha '+ str(line))
    exit()
#verifica se usa algum simbolo reservado da tabela
i = 0
line = 1
open_aspas = False
for ch in source: #verificar se n ta dentro de uma string
    if ch == '\n':
        line+=1
    elif ch == '"':
        open_aspas= not open_aspas
    elif (ch == 'A' or ch == 'B' or ch == 'C' or ch == 'D') and open_aspas == False:
        if source[i+1].isdigit() == True and source[i+2].isdigit() == True:
            print(source[i]+source[i+1]+source[i+2]+"na linha "+str(line)+" é um simbolo reservado para compilação. Por favor, troque para outra combinação!")
            exit()
    i+=1

#verifica se fecha parentesis
i = 0
line = 1
line_open = 0
open_aspas = False
pr = 0
for ch in source: #verificar se n ta dentro de uma string
    if ch == '\n':
        line+=1
    if pr == 0:
        line_open = line
    if ch == '"':
        open_aspas= not open_aspas
    elif (ch == '(') and open_aspas == False:
        pr+=1
    elif (ch == ')') and open_aspas == False:
        pr-=1
    
if pr !=0:
    print("parêntesis na linha "+str(line_open)+" deve ser fechado!")
    exit()

#verifica se fecha colchetes
i = 0
line = 1
line_open = 0
open_aspas = False
pr = 0
for ch in source: #verificar se n ta dentro de uma string
    if ch == '\n':
        line+=1
    if pr == 0:
        line_open = line
    if ch == '"':
        open_aspas= not open_aspas
    elif (ch == '[') and open_aspas == False:
        pr+=1
    elif (ch == ']') and open_aspas == False:
        pr-=1
    
if pr !=0:
    print("Colchetes na linha "+str(line_open)+" deve ser fechado!")
    exit()

#verifica se fecha chaves
i = 0
line = 1
line_open = 0
open_aspas = False
pr = 0
for ch in source: #verificar se n ta dentro de uma string
    if ch == '\n':
        line+=1
    if pr == 0:
        line_open = line
    if ch == '"':
        open_aspas= not open_aspas
    elif (ch == '{') and open_aspas == False:
        pr+=1
    elif (ch == '}') and open_aspas == False:
        pr-=1
    
if pr !=0:
    print("Chaves na linha "+str(line_open)+" deve ser fechado!")
    exit()

#analisador lexico
source = lexicalAnalyzer(source, tabelaSimbolosPalavras())
print(source)    


filename = sys.argv[1].split('.201')
f = open(filename[0]+'.LEX', 'w+')
f.write(source)
f.close
f = open(filename[0]+'.TAB', 'w+')
f.write(str(tabelaSimbolos(None)))
f.close

# remover recursoes
#(226, 'factor', 228),
# E pq o (349, 'Integer-Number', 350) a 350 não tem nenhuma transição começando c ela, sendo que ela n é final


result = sintaticAnalyzer(source, tabelaSimbolosPalavras(), states)#passa tabela de simbolos com none quando n quer adicionar um novo   
    


