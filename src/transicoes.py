from src.matriz_trans import genMatrix

def defTransicoes(name,text):

    text = text.replace(" ","")

    rule1 = []
    rule2 = []
    rule3 = []
    rule4 = []
    init = -1
    end = 0
    state =''


    i=0    
    while i < len(text):
        if(text[i] == '"'):
            i+=1
            continue
        if ord(text[i]) >= ord('0') and ord(text[i])<= ord('9'):
            if init == -1:
                init = ord(text[i]) - ord('0')
            else:
                if state == '':
                    init*=10
                    init += ord(text[i]) - ord('0')
                else:
                    end*=10
                    end += ord(text[i]) - ord('0')
        elif (ord(text[i]) >= ord('a') and ord(text[i])<= ord('z')) or (ord(text[i]) >= ord('A') and ord(text[i])<= ord('Z')):
            if end != 0:
                rule1.append((init,state,end))
                state = ''
                init = -1
                end = 0

                i-=1
                while(i>=0):
                    if(ord(text[i-1]) >= ord('0') and ord(text[i-1])<= ord('9')):
                        i-=1
                    else:
                        i-=1
                        break    
            else:
                state +=text[i]
        else:
            if end != 0:
                
                rule1.append((init,state,end))
                state = ''
                init = -1
                end = 0

                i-=1
                while(i>=0):
                    if(ord(text[i-1]) >= ord('0') and ord(text[i-1])<= ord('9')):
                        i-=1
                    else:
                        i-=1
                        break
            if text[i].isdigit()== False and text[i] != '"' and ((ord(text[i]) < ord('a') or ord(text[i])> ord('z')) and (ord(text[i]) >= ord('A') or ord(text[i])<= ord('Z'))):
                init = -1            
        i+=1



    init = 0
    end = 0
    state =''
    rule1_2 = []
    i=0    
    aux =0
    while i < len(text):
        if text[i]=='"':
            if text[i+1]=="[" or text[i+1]=="]" or text[i+1]==";" or text[i+1]=="," or text[i+1]=="(" or text[i+1]==")" or text[i+1]=="{" or text[i+1]=="}" or text[i+1]=="|" or text[i+1]=="!" or text[i+1]=="&" or text[i+1]=="=" or text[i+1]=="#" or text[i+1]=="+" or text[i+1]=="-" or text[i+1]=="*" or text[i+1]=="/" or text[i+1]==">" or text[i+1]=="<":
                state+=text[i+1]
                if text[i+2]=="=":
                    state+=text[i+2]
            if state!='':
                aux = i-1
                while(True):
                    if ord(text[aux]) >= ord('0') and ord(text[aux])<= ord('9'):
                        init*=10
                        init+= ord(text[aux]) - ord('0')
                        aux-=1
                        continue
                    else:
                        break
                i+=2
                if text[i] != '"':
                    i+=1
                aux=i+1
                while(True):
                    if ord(text[aux]) >= ord('0') and ord(text[aux])<= ord('9'):
                        end*=10
                        end+= ord(text[aux]) - ord('0')
                        aux+=1
                        continue
                    else:
                        break
                rule1_2.append((init,state,end))
                                
        state=''
        init=0
        end=0
        i+=1
        aux=0

    rule1 +=rule1_2
    print(rule1)





    i=0
    init = 0
    end = 0
    old_i =0 #guarda o valor de i quando ele começou a buscar no parentesis
    opend=0
    aux=0    
    while i < len(text):
        
        if (text[i] == '(' or text[i]=='[') and text[i+1] !='"':
            i+=1
            old_i = i
            #vai buscar o estado final
            while(True):
                
                if (text[i] == '(' or  text[i]=='[' or text[i]=='{') and text[i+1] !='"':
                    opend+=1
                if (text[i] == ')' or  text[i]==']'or text[i]=='}') and text[i+1] !='"':
                    if opend == 0:
                        
                        while i<len(text)-1 and(ord(text[i+1]) >= ord('0') and ord(text[i+1])<= ord('9')):
                            
                            end*=10
                            end+= ord(text[i+1]) - ord('0')
                            i+=1
                        break
                    else:
                        opend-=1 
                i+=1               
            i=old_i

            while(opend!=-1):
                if (text[i] == '(' or  text[i]=='[' or text[i]=='{') and text[i+1] !='"':
                    opend+=1
                
                if ((text[i]== '|' or (text[i]==')' or text[i]==']' or text[i]=='}')) and opend==0 and text[i+1] !='"'):
                    aux=i
                    while(ord(text[aux-1]) >= ord('0') and ord(text[aux-1])<= ord('9')):
                        aux-=1
                    while(ord(text[aux]) >= ord('0') and ord(text[aux])<= ord('9')):
                        init*=10
                        init+=ord(text[aux]) - ord('0')
                        aux+=1    
                    rule2.append((init,'e',end))
                    init=0     
                if (text[i] == ')' or  text[i]==']' or text[i]=='}')and text[i+1] !='"':        
                    opend-=1
                i+=1
            i=old_i
            end=0   
        else:
            i+=1
            opend=0    

    print(rule2)    




    i=0
    init = 0
    end = 0
    old_i =0 #guarda o valor de i quando ele começou a buscar no parentesis
    opend=0
    aux=0    
    while i < len(text):
        
        if (text[i] == '{') and text[i+1] !='"':
            i+=1
            old_i = i
            #vai buscar o estado final
            while(True):
                
                if (text[i] == '(' or  text[i]=='[' or text[i]=='{') and text[i+1] !='"':
                    opend+=1
                if (text[i] == ')' or  text[i]==']'or text[i]=='}') and text[i+1] !='"':
                    if opend == 0:
                        
                        while i<len(text)-1 and(ord(text[i+1]) >= ord('0') and ord(text[i+1])<= ord('9')):
                            
                            end*=10
                            end+= ord(text[i+1]) - ord('0')
                            i+=1
                        break
                    else:
                        opend-=1 
                i+=1               
            i=old_i

            while(opend!=-1):
                if (text[i] == '(' or  text[i]=='[' or text[i]=='{') and text[i+1] !='"':
                    opend+=1
                
                if ((text[i]== '|' or (text[i]==')' or text[i]==']' or text[i]=='}')) and opend==0 and text[i+1] !='"'):
                    aux=i
                    while(ord(text[aux-1]) >= ord('0') and ord(text[aux-1])<= ord('9')):
                        aux-=1
                    while(ord(text[aux]) >= ord('0') and ord(text[aux])<= ord('9')):
                        init*=10
                        init+=ord(text[aux]) - ord('0')
                        aux+=1    
                    rule3.append((init,'e',end))
                    init=0     
                if (text[i] == ')' or  text[i]==']' or text[i]=='}') and text[i+1] !='"' :        
                    opend-=1
                i+=1
            i=old_i
            end=0   
        else:
            i+=1
            opend=0    

    print(rule3)    





    i=0
    init = 0
    end = 0
    old_i =0 #guarda o valor de i quando ele começou a buscar no parentesis
    opend=0
    aux=0    
    while i < len(text):
        
        if (text[i] == '{' or text[i]=='[') and text[i+1] !='"':
            aux=i
            while(ord(text[aux-1]) >= ord('0') and ord(text[aux-1])<= ord('9')):
                aux-=1
            while(ord(text[aux]) >= ord('0') and ord(text[aux])<= ord('9')):
                init*=10
                init+=ord(text[aux]) - ord('0')
                aux+=1  

            i+=1
            old_i = i
            #vai buscar o estado final
            while(True):
                
                if (text[i] == '{' or  text[i]=='[') and text[i+1] !='"':
                    opend+=1
                if (text[i] == '}' or  text[i]==']') and text[i+1] !='"':
                    if opend == 0:
                        
                        while  i<len(text)-1 and (ord(text[i+1]) >= ord('0') and ord(text[i+1])<= ord('9')):
                            
                            end*=10
                            end+= ord(text[i+1]) - ord('0')
                            i+=1
                        break
                    else:
                        opend-=1 
                i+=1               
            i=old_i
            rule4.append((init,'e',end))
            end=0
            init=0
            
        else:
            i+=1
            opend=0    

    print(rule4)    

    f = open("txts/trans_regra1_"+name+".txt", "a")
    f.write(str(rule1))
    f.close()

    f = open("txts/trans_regra2_"+name+".txt", "a")
    f.write(str(rule2))
    f.close()

    f = open("txts/trans_regra3_"+name+".txt", "a")
    f.write(str(rule3))
    f.close()

    f = open("txts/trans_regra4_"+name+".txt", "a")
    f.write(str(rule4))
    f.close()

    all = rule1+rule2+rule3+rule4
    genMatrix(name, all)

#2:08
#2:23