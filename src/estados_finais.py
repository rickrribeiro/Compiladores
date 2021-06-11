

def estadosFin(name, text):
    text = text.replace(" ","")
    fin = []
    state =0 
    i=0 
    opend = 0   
    while i < len(text):
        if (text[i] == '{' or text[i]=='[' or text[i]=='(') and text[i+1] !='"':
            opend+=1
        if (text[i] == '}' or text[i]==']' or text[i]==')') and text[i+1] !='"':
            opend-=1
        if text[i]=='|' and text[i+1] !='"' and opend==0:
            aux=i
            while(ord(text[aux-1]) >= ord('0') and ord(text[aux-1])<= ord('9')):
                aux-=1
            while(ord(text[aux]) >= ord('0') and ord(text[aux])<= ord('9')):
                state*=10
                state+=ord(text[aux]) - ord('0')
                aux+=1    
            fin.append(state)
            state=0    
        i+=1

    aux=len(text)-1
    count = 0
    while(ord(text[aux-1]) >= ord('0') and ord(text[aux-1])<= ord('9')):
        aux-=1
        count+=1
    aux=len(text)-count-1
    while(aux!=len(text)):
        state*=10
        state+=ord(text[aux]) - ord('0')
        aux+=1    
    fin.append(state)

    f = open("txts\\estado_final_"+name+".txt", "w+")
    f.write('Inicial: 0\n\n')
    f.write('Finais: ')
    f.write(str(fin))
    f.close()

    return fin