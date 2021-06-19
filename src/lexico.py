def removeComments(source):
  # aux = False
  # while True:
  #   if source
  print('a')
def lexicalAnalyzer(source, symbols):
    removeComments(source)
    source = source.replace('\n', ' ')
    values = source.split(' ')
    
    aux = False
    source = '' #zera source p montar novamente
    for v in values:
    

      #parte comentada caso volte a chamar o lexico em loop, p verificar se o simbolo já foi verificado
      # for sym in symbols: 
      #   if sym[1] == v:
      #     aux = True
      #     break
      # if aux:
      #   aux=False
      #   continue
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
    #// e /* */, se for /* desconsidera td
      # for i in source:
    #         print(i)
    #         if i == '\n':
    #             print("AAAAAAAAAAAA")
    # 
    # checklist
    # 1. verificar atomos
    # 2. Verificar atomos contidos em outros ex: <= não é < e =
    # 3. verificar os atomos da tablea C ex: constant-string, integer-number, etc...
    # 4. verificar comentarios
    #
    #