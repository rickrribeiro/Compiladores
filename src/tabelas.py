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

    tabela.append(('program', 'D01'))
    tabela.append(('factor', 'D02'))
    tabela.append(('statement', 'D03'))
   

    return tabela


simbolos = ['a']
def tabelaSimbolos(simb): #tem as strings, variáveis, numeros inteiros, numeros float
    simbolos.append(simb)
    return simbolos