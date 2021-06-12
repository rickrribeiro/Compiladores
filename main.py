from src.bota_ponto import bpontos
import sys

if len(sys.argv)!= 2:
    print('Informe o arquivo de entrada e o arquivo de saida! ex: python ./compiler.py entrada.txt saida.txt')
if(len(sys.argv[1].split('.txt'))!= 2):
    print('O arquivo de entrada deve ser um txt')


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


name = 'factor'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
factorStates = bpontos(name, text)
f = open('txts\\estado_final_'+name+'.txt', 'r')
factorFinal = f.read()
f.close()


name = 'statement'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
statementStates = bpontos(name, text)
f = open('txts\\estado_final_'+name+'.txt', 'r')
statementFinal = f.read()
f.close()
