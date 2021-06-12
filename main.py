from src.lexico import lexicalAnalyzer
from src.bota_ponto import bpontos
import sys

if len(sys.argv)!= 2:
    print('Informe o arquivo de entrada e o arquivo de saida! ex: python ./compiler.py entrada.txt saida.txt')
if(len(sys.argv[1].split('.txt'))!= 2):
    print('O arquivo de entrada deve ser um txt')

states = []
final = []
name = 'teste'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
testStates= bpontos(name, text)
f = open('txts\\estado_final_'+name+'.txt', 'r')
testeFinal = f.read()
f.close()

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


f = open(sys.argv[1], 'r')
text = f.read()
f.close()

lexicalAnalyzer(text,states,final)