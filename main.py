from src.bota_ponto import bpontos

name = 'teste'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
bpontos(name, text)

name = 'program'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
bpontos(name, text)

name = 'factor'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
bpontos(name, text)

name = 'statement'
f = open('txts\\wirth_'+name+'.txt', 'r')
text = f.read()
f.close()
bpontos(name, text)