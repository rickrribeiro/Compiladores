
from src.helpers import isAlphabeticalChar, isReservedDigit
from src.tabelas import tabelaLexico,tabelaSimbolos



def lexicalAnalyzer(source, symbols):
    
    source = source.replace('\n', '\n ')
    values = source.split(' ')
    

    aux = False
    source = '' #zera source p montar novamente botando os codigos
    line =1
    for v in values:
      if len(str(v)) > 30:
        v= v[:30]
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
          tabelaLexico(sym[0])
          alt=True
          source+=v+' '
          break
      
      if alt:#verifica se foi alterado anteriormente
        continue
      
      #verifica se é char
      if v[0]=="'":
        symb = tabelaSimbolos(v[1],1,'C05',line)
        tabelaLexico(v[1])
        source+=symb+' '
        if '\n' in v:
          source+='\n'
        continue
      #verifica se é string
      if v[0]=='"':
        aux = v.split('"')
        symb = tabelaSimbolos(aux[1],len(aux[1]),'C02',line)
        tabelaLexico(aux[1])
        source+=symb+' '
        if '\n' in v:
          source+='\n'
        continue
      #verifica se é integer number ou float
      if v[0].isnumeric():
        for ch in v:
          if ch.isnumeric() == False and ch != '.' and ch !='\n':
            print("simbolo "+v+" na linha "+str(line)+" não é reconhecido na linguagem!")
            input()
            exit()
        aux = v.split('.')
        if len(aux)==1:
          symb = tabelaSimbolos(v.replace('\n',''),len(str(v)),'C03',line)
        else:
          symb = tabelaSimbolos(v.replace('\n',''),len(str(v)),'C06',line)
        tabelaLexico(v.replace('\n',''))
        source+=symb+' '
        if '\n' in v:
          source+='\n'
        continue
     

      #verifica se é identifier ou function e se é membro da linguagem
      for ch in v:
        if ((ord(ch)<ord('a') or ord(ch)>ord('z')) and (ord(ch)<ord('A') or ord(ch)>ord('Z'))) and ch != '_' and ch !='\n' and ch.isnumeric()==False:
          print("simbolo "+v+" na linha "+str(line)+" não é reconhecido na linguagem!")
          input()
          exit()
      if v == '\n':
        source+='\n'
        continue
      
      symb = tabelaSimbolos(v.replace('\n',''),len(str(v)),'C01',line)
      tabelaLexico(v.replace('\n',''))
      source+=symb+' '
      if '\n' in v:
          source+='\n'
    return source
    
    
    
    
 
    # 
    # checklist
    # 1. (check) verificar atomos 
    # 2. (check) Verificar atomos contidos em outros ex: <= não é < e = -> olha o reserved digit e ve se ele+1 é =
    # 3. (check) verificar os atomos da tablea C ex: constant-string, integer-number, etc...
    # 4. (check) verificar comentarios 
    # 5. (check) verificar se as barras de comentarios, atomos ex: float e atomos simbolos ex: ( nao estao no meio de uma string 
    # 6. verificar atomos juntos, ex (True)

    #LEMBRAR DE DESCOMENTAR SINTATICO E AUTOMATOS