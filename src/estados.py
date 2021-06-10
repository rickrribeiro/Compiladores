from src.transicoes import defTransicoes

#example
#text = '.(.(.{."{"."a".";"."b"."}".}.).(."c".|.A.(."a".|."b".).).).|.[."a".|."b".].{."b"."c".|.A.|.B.}.'
#text='.(.(.{.{."{"."}"."a".}."b"."}".}.).(."c".|.A.(."a".|."b".).).).|.[."a".|."b".].{."b"."c".|.A.|.B.}.'
def define_estado(name,text):
    text = text.replace(" ","")
    j = 0
    opend = 0
    opend_key=0
    opend_or =0
    a = ""
    b = ""
    up = False
    last_state =0
    #for i in range(9999):
    while(True):
    # print(text)
        up = False
        if '.' not in text:
            break
        #verify or statement
        if opend==0 or opend==1:
            
            for idx, item in enumerate(text):
                if (item== '(' or item =='[' or item=='{') and (text[idx + 1]=='.'):
                    opend_or +=1
                    
                elif (item == ')' or item == ']' or item == '}' ) and (text[idx + 1]=='.'):
                    opend_or -=1   
                    if opend_or < 0:
                        opend_or=0
                        break
                elif item =='|':
                    if (opend_or==0) and (text[idx + 1]=='.'):
                        if opend ==0:
                            text = text[:idx+1] + str(last_state) + text[idx + 2:]
                        elif opend==1:
                            text = text[:idx+1] + str(last_state) + text[idx + 2:]
                        up = True   
                        break
            if up== True:
                continue
    
        for idx, item in enumerate(text):
            
            if item == '.':
                if opend == 0:
                    
                    text = text[:idx] + str(j) + text[idx + 1:]
                    last_state= str(j)
                    j = j+1
                    break
            else:
                if (item== '(' or item =='[') and (text[idx + 1]=='.'):
                    opend +=1
                    if opend== 1:
                        val=0
                        for i in range(30):
                            if text[idx-i-1].isdigit():
                                val*=10   
                                val+= ord(text[idx-i-1]) - ord('0')
                                #print(val)                        
                            else:
                                break
                        text = text[:idx+1] + str(val)[::-1] + text[idx + 2:]
                        last_state=str(val)[::-1]
                        
                        break
                elif (item == ')' or item == ']' ) and (text[idx + 1]=='.'):
                    opend -=1      
                elif item =='{' and (text[idx + 1]=='.') and opend==0:   
                    text = text[:idx+1] + str(j) + text[idx + 2:]
                    last_state= str(j)
                    for idx2, item2 in enumerate(text[idx+1:]):
                        
                        if item2 == '{'and (text[idx + idx2 + 2]=='.'):
                            
                            opend_key+=1
                        elif item2 =='}' and   (text[idx + idx2 + 2]=='.'):
                            opend_key-=1
                            if opend_key == -1:
                                text = text[:idx+idx2+2] + str(j) + text[idx+idx2 + 3:]
                                last_state= str(j)
                                j+=1
                                opend_key=0
                                break
                    break
    
    f = open("txts\\estados_"+name+".txt",'w')
    f.write(text)
    f.close()
    defTransicoes(name,text)
#."a" ."b" .(."c".|.A.(."a" .| ."b".).).|.[."a".|."b".].{."b"."c".|.A.|.B.}.

#2:01 -- completo
#1:46 -- regras