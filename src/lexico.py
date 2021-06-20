from src.helpers import isAlphabeticalChar, isReservedDigit
def lexicalAnalyzer(source, symbols):
    
    source = source.replace('\n', ' ')
    values = source.split(' ')
    
    aux = False
    source = '' #zera source p montar novamente botando os codigos
    for v in values:
      for sym in symbols:
        if sym[0].lower() == v.lower():
          v= sym[1]
          break
      source+=v+' '
  
     
    
    
    return source
    
    
    
    
    
    
    #lembrar:
    #pegar o caracter i e adicionar em aux todos os simbolos e palavras reservadas que começam com ele, então ir p ir p/ i+1
    #em i+1 já descartar os que não são e passar pra i+2...i+n
    #verificar espaço apos os que começam com A pois são palavras reservadas, nos simbolos não precisa
 
    # 
    # checklist
    # 1. verificar atomos (check)
    # 2. Verificar atomos contidos em outros ex: <= não é < e = -> olha o reserved digit e ve se ele+1 é =
    # 3. verificar os atomos da tablea C ex: constant-string, integer-number, etc...
    # 4. verificar comentarios (check)
    # 5. verificar se as barras de comentarios, atomos ex: float e atomos simbolos ex: ( nao estao no meio de uma string
    # 6. verificar atomos juntos, ex (True)