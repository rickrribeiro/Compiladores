
from src.helpers import isAlphabeticalChar, isReservedDigit
from src.tabelas import tabelaLexico,tabelaSimbolos



def lexicalAnalyzer(source, symbols):
    
    source = source.replace('\n', '\n ')
    values = source.split(' ')
    

    aux = False
    source = '' #zera source p montar novamente botando os codigos
    line =1
    for v in values:
      alt= False
      #conta a linha
      if '\n' in v: 
        # v.replace('\n', '')
        line+=1
      if len(v)==0:
        continue
      #verifica se faz parte da tabela de palavras e simbolos reservados  
      for sym in symbols:
        cp = v
        if sym[0].lower() == cp.replace('\n','').lower(): #pertence a tabela de simbolos e palavras
          if '\n' in v:
            v= sym[1]+'\n'
          else:
            v=sym[1]
          tabelaLexico(sym[0], line)
          alt=True
          source+=v+' '
          break
      
      if alt:#verifica se foi alterado anteriormente
        continue
      
      #verifica se é char
      if v[0]=="'":
        symb = tabelaSimbolos(v[1],1,'C05')
        tabelaLexico(v[1],line)
        source+=symb+' '
        if '\n' in v:
          source+='\n'
        continue
      #verifica se é string
      if v[0]=='"':
        aux = v.split('"')
        symb = tabelaSimbolos(aux[1],len(aux[1]),'C02')
        tabelaLexico(aux[1],line)
        source+=symb+' '
        if '\n' in v:
          source+='\n'
        continue
      #verifica se é integer number ou float
      if v[0].isnumeric():
        for ch in v:
          if ch.isnumeric() == False and ch != '.' and ch !='\n':
            print("simbolo "+v+" na linha "+str(line)+" não é reconhecido na linguagem!")
            exit()
        aux = v.split('.')
        if len(aux)==1:
          symb = tabelaSimbolos(v.replace('\n',''),len(str(v)),'C03')
        else:
          symb = tabelaSimbolos(v.replace('\n',''),len(str(v)),'C06')
        tabelaLexico(v.replace('\n',''),line)
        source+=symb+' '
        if '\n' in v:
          source+='\n'
        continue
     

      #verifica se é identifier ou function e se é membro da linguagem
      for ch in v:
        if ((ord(ch)<ord('a') or ord(ch)>ord('z')) and (ord(ch)<ord('A') or ord(ch)>ord('Z'))) and ch != '_' and ch !='\n' and ch.isnumeric()==False:
          print("simbolo "+v+" na linha "+str(line)+" não é reconhecido na linguagem!")
          exit()
      if v == '\n':
        source+='\n'
        continue
      symb = tabelaSimbolos(v.replace('\n',''),len(str(v)),'C01')
      tabelaLexico(v.replace('\n',''),line)
      source+=symb+' '
      if '\n' in v:
          source+='\n'
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