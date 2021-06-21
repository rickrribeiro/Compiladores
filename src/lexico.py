
from src.helpers import isAlphabeticalChar, isReservedDigit
from src.tabelas import tabelaLexico,tabelaSimbolos



def lexicalAnalyzer(source, symbols):
    
    source = source.replace('\n', '\n ')
    values = source.split(' ')
    
    aux = False
    source = '' #zera source p montar novamente botando os codigos
    line =1
    for v in values:
      if '\n' in v:
        line+=1
      for sym in symbols:
        if sym[0].lower() == v.lower(): #pertence a tabela de simbolos e palavras
          v= sym[1]
          tabelaLexico(sym[0], line)
          break
      
      source+=v+' '
  
     
    
    
    return source
    
    
    
    
    
    
    #lembrar:
    #pegar o caracter i e adicionar em aux todos os simbolos e palavras reservadas que começam com ele, então ir p ir p/ i+1
    #em i+1 já descartar os que não são e passar pra i+2...i+n
    #verificar espaço apos os que começam com A pois são palavras reservadas, nos simbolos não precisa
 
    # 
    # checklist
    # 1. (check) verificar atomos 
    # 2. (check) Verificar atomos contidos em outros ex: <= não é < e = -> olha o reserved digit e ve se ele+1 é =
    # 3. verificar os atomos da tablea C ex: constant-string, integer-number, etc...
    # 4. (check) verificar comentarios 
    # 5. (check) verificar se as barras de comentarios, atomos ex: float e atomos simbolos ex: ( nao estao no meio de uma string 
    # 6. verificar atomos juntos, ex (True)

    #LEMBRAR DE DESCOMENTAR SINTATICO E AUTOMATOS