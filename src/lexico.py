from src.tabelas import tabelaSimbolos, tabelaSimbolosPalavras

def lexicalAnalyzer(source, states, final):
    result = []
    result.append('E02 - Ricardo Ramos Ribeiro - rickribeiro99@gmail.com - 71 996820764')
    table = tabelaSimbolosPalavras()
    #lembrar:
    #pegar o caracter i e adicionar em aux todos os simbolos e palavras reservadas que começam com ele, então ir p ir p/ i+1
    #em i+1 já descartar os que não são e passar pra i+2...i+n
    #verificar espaço apos os que começam com A pois são palavras reservadas, nos simbolos não precisa
    aux = []
    
    
    return[result,tabelaSimbolos(None)]