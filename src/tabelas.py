def tabelaSimbolosPalavras():
    tabela = []
    tabela.append(('bool', 'A01'))
    tabela.append(('begin', 'A02'))
    tabela.append(('while', 'A03'))
    tabela.append(('return', 'A04'))
    tabela.append(('break', 'A05'))
    tabela.append(('false', 'A06'))
    tabela.append(('void', 'A07'))
    tabela.append(('program', 'A08'))
    tabela.append(('char', 'A09'))
    tabela.append(('float', 'A10'))
    tabela.append(('true', 'A11'))
    tabela.append(('int', 'A12'))
    tabela.append(('if', 'A13'))
    tabela.append(('else', 'A14'))
    tabela.append(('string', 'A15'))
    tabela.append(('end', 'A16'))

    tabela.append(('!=', 'B01'))
    tabela.append(('!', 'B02'))
    tabela.append(('#', 'B03'))
    tabela.append(('%', 'B04'))
    tabela.append(('&', 'B05'))
    tabela.append(('/', 'B06'))
    tabela.append(('(', 'B07'))
    tabela.append(('*', 'B08'))
    tabela.append((')', 'B09'))
    tabela.append(('+', 'B10'))
    tabela.append((';', 'B11'))
    tabela.append((']', 'B12'))
    tabela.append(('[', 'B13'))
    tabela.append(('|', 'B14'))
    tabela.append(('{', 'B15'))
    tabela.append(('}', 'B16'))
    tabela.append((',', 'B17'))
    tabela.append(('<', 'B18'))
    tabela.append(('<=', 'B19'))
    tabela.append(('==', 'B20'))
    tabela.append(('>', 'B21'))
    tabela.append(('=', 'B22'))
    tabela.append(('>=', 'B23'))
    tabela.append(('-', 'B24'))


    tabela.append(('identifier', 'C01'))
    tabela.append(('constant-string', 'C02'))
    tabela.append(('integer-number', 'C03'))
    tabela.append(('function', 'C04'))
    tabela.append(('character', 'C05'))
    tabela.append(('float-number', 'C06'))

    #ver oq são essas submaquinas
    tabela.append(('program', 'D01'))
    tabela.append(('factor', 'D02'))
    tabela.append(('statement', 'D03'))

    return tabela


#No. | Lexeme | Atomo | Tamanho | Tipo | QT. Aparicoes | Linhas
simbolos = []
def tabelaSimbolos(Lexeme, Tamanho, tipo, linha): #tem as strings, variáveis, numeros inteiros, numeros float
    for it in simbolos: #verifica se ja tem na lextable
        if it[1].lower() == Lexeme.lower():
            it[5]+=1
            it[6].append(linha)
            return it[2]
   
    if len(simbolos)<1:
        num=1
        atomo = 'E01'
    else:
        num= int(simbolos[-1][0])+1
        if(num<10):
            atomo='E0'+str(num)
        else:
            atomo='E'+str(num)
    simbolos.append([num,Lexeme, atomo, Tamanho,tipo,1,[linha]])
    
    return atomo

def getTabelaSimbolos():
    return simbolos



#No. | Lexeme | Atomo | ID Tabela
lexTable = []
def tabelaLexico(Lexeme): 
    
    if len(lexTable)<1:
        num=1
    else:
        num= int(lexTable[-1][0])+1
    id_tb = 0#pra verificar se foi encontrado na tabela de simbolos e palavras, se n tiver sido encontrado ai busca na de simbolos
    for sym in tabelaSimbolosPalavras():
        if sym[0].lower() == Lexeme.lower():
          Atomo = sym[1]
          id_tb = '-'
          break
    if id_tb == 0: #busca na tabela de simbolos
        for sym in simbolos:
            if sym[1].lower() == Lexeme.lower():
                Atomo = sym[2]
                id_tb = sym[0]
                break
    lexTable.append([num,Lexeme, Atomo, id_tb]) #verificar antes se ja tem
    
    

def getTabelaLexico():
    return lexTable