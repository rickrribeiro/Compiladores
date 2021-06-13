from os import stat
from src.lexico import lexicalAnalyzer
from src.bota_ponto import bpontos
import sys

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

# name = 'program'
# f = open('txts\\wirth_'+name+'.txt', 'r')
# text = f.read()
# f.close()
# programStates = bpontos(name, text)
# f = open('txts\\estado_final_'+name+'.txt', 'r')
# programFinal = f.read()
# f.close()
# states.append(programStates)
# final.append(programFinal)

# name = 'factor'
# f = open('txts\\wirth_'+name+'.txt', 'r')
# text = f.read()
# f.close()
# factorStates = bpontos(name, text)
# f = open('txts\\estado_final_'+name+'.txt', 'r')
# factorFinal = f.read()
# f.close()
# states.append(factorStates)
# final.append(factorFinal)

# name = 'statement'
# f = open('txts\\wirth_'+name+'.txt', 'r')
# text = f.read()
# f.close()
# statementStates = bpontos(name, text)
# f = open('txts\\estado_final_'+name+'.txt', 'r')
# statementFinal = f.read()
# f.close()
# states.append(statementStates)
# final.append(statementFinal)



result = lexicalAnalyzer(source,states,final)
filename = sys.argv[1].split('.201')
# for i in source:
#         print(i)
#         if i == '\n':
#             print("AAAAAAAAAAAA")

f = open(filename[0]+'.LEX', 'w+')
f.write(str(result[0]))
f.close
f = open(filename[0]+'.TAB', 'w+')
f.write(str(result[1]))
f.close

