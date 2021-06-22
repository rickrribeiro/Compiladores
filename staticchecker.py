from os import stat
from src.lexico import lexicalAnalyzer
from src.sintatico import sintaticAnalyzer
from src.bota_ponto import bpontos
import sys
from src.tabelas import getTabelaLexico, tabelaSimbolos, tabelaSimbolosPalavras, getTabelaSimbolos
from src.helpers import removeComments
from sys import exit

# if len(sys.argv)!= 2:
#     print('Informe o codigo fonte! ex: python ./staticchecker.py entrada.201')
# try:

#     if(len(nameFile.split('.201'))!= 2):
#         f = open(nameFile+'.201', 'r')
#     else:
#         f = open(nameFile, 'r')
# except:
#     print('Código fonte não encontrado!')
#     exit()
try:
    nameFile = input('Digite o nome do arquivo:')
    if(len(nameFile.split('.201'))!= 2):
        f = open(nameFile+'.201', 'r')
    else:
        f = open(nameFile, 'r')
except:
    print('Código fonte não encontrado!')
    input()
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
for ch in source: #verificar se é uma string vazia
    if ch == '\n':
        line+=1
    if ch == '"':
       open_aspas +=1

if open_aspas%2 == 1:
    print('Aspas sem fechar na linha '+ str(line)) 
    input()
    exit()

#verifica se tem char e se char len ==1

line = 1 
i = 0
open_aspas = False
#Se quebrar por ter aspas simples dentro de aspas duplas, lembrar que no padrão da constant-string só tem alfa
for ch in source:
    if open_aspas == True:
        i+=1
    if ch == '\n':
        line+=1
    if ch == "'":
        open_aspas = not open_aspas
        if open_aspas==False:
            if(i==1):
                print('Erro de aspas simples na linha '+ str(line)+'. Atribua um valor para o caracter!')
                input()
                exit()
            i=0
    if i>= 2:
        print('Erro de aspas simples na linha '+ str(line)+'. Verifique se foram fechadas ou se você não está definindo uma string(utilizar aspas duplas)')
        input()
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
    elif (ch == 'A' or ch == 'B' or ch == 'C' or ch == 'D' or ch == 'E') and open_aspas == False:
        if source[i+1].isdigit() == True and source[i+2].isdigit() == True:
            print(source[i]+source[i+1]+source[i+2]+"na linha "+str(line)+" é um simbolo reservado para compilação. Por favor, troque para outra combinação!")
            input()
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
    input()
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
    input()
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
    input()
    exit()

#analisador lexico
source = lexicalAnalyzer(source, tabelaSimbolosPalavras())
# print(source)    

#para testes, remover dps


filename = nameFile.split('.201')

f = open(filename[0]+'.LEX', 'w+')
f.write('E-02\n')
f.write('Ricardo Ramos Ribeiro | ricardo.r@aln.senaicimatec.edu.br | 71 996820764 \n')
f.write('Hercules Mosley de Araujo Pinheiro Leonel | hercules.leonel@aln.senaicimatec.edu.br | 71 999207259 \n')
f.write('Yuri Papaterra | | \n\n\n')
f.write('No. | Lexeme | Atomo | ID Tabela\n') #botar - id tabela qnd for ta tabela e simbolos e palavras
for simb in getTabelaLexico():
    f.write('\n')
    f.write(str(str(simb[0]) + ' | '+str(simb[1])+' | '+str(simb[2])+' | '+ str(simb[3])))
f.close()


f = open(filename[0]+'.TAB', 'w+')
f.write('No. | Lexeme | Atomo | Tamanho | Tipo | QT. Aparicoes | Linhas \n')
for simb in getTabelaSimbolos():
    f.write('\n')
    f.write(str(str(simb[0]) + ' | '+str(simb[1])+' | '+str(simb[2])+' | '+ str(simb[3])+ ' | '+str(simb[4]) +'| ' +str(simb[5])+'| ' +str(simb[6])))
f.close()

# remover recursoes
#(226, 'factor', 228),
# E pq o (349, 'Integer-Number', 350) a 350 não tem nenhuma transição começando c ela, sendo que ela n é final


result = sintaticAnalyzer(source, tabelaSimbolosPalavras(), states)#passa tabela de simbolos com none quando n quer adicionar um novo   
    
input()

