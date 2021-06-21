def getState(states,id):
    for st in states:
        
        if st.estado==id:
            return st
        
    return None

def countFinal(states,id): #conta quantas transições tem para esse estado (se retornar 0, ele não é acessivel)
    count = 0 
    for st in states:
        for tr in st.transicoes:
            for fn in tr.finais:
                if fn == id:
                    count+=1
    return count

    
def removeComments(source):
  text=''
  i = 0 
  open_aspas = False
  while i < len(source):
    #print(i)
    if source[i] == '"':
      open_aspas = not open_aspas
    if source[i]=='/' and not open_aspas:
      if source[i+1]== '*':
        i+=2
        while i < len(source):
          if source[i] == '*' and source[i+1]=='/':
            i+=2
            break
          else:
            i+=1
          
      elif source[i+1] =='/':
        i+=2
        while i < len(source):
          source[i]
          if source[i] == '\n':
            break
          else:
            i+=1
    else:
      text += source[i]
    i+=1
  return text
  

def isAlphabeticalChar(ch):
    if (ord(ch) >= ord('a') and ord(ch)<= ord('z')) or (ord(ch) >= ord('A') and ord(ch)<= ord('Z')):
        return True
    else:
        return False

def isReservedDigit(ch):
    if ch=="[" or ch=="]" or ch==";" or ch=="," or ch=="(" or ch==")" or ch=="{" or ch=="}" or ch=="|" or ch=="!" or ch=="&" or ch=="=" or ch=="#" or ch=="+" or ch=="-" or ch=="*" or ch=="/" or ch==">" or ch=="<":
        return True 