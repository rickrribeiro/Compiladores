text = '."a" ."b" .(."c".|.A.(."a" .| ."b".).).|.[."a".|."b".].{."b"."c".|.A.|.B.}.'
text = text.replace(" ","")

j = 0
open = 0
open_key=0
a = ""
b = ""
for i in range(9999):
#while(True):
    if '.' not in text:
        break
    for idx, item in enumerate(text):
        
        if item == '.':
            if open == 0:
                if text[idx-1] == '}':
                    j-=1
                text = text[:idx] + str(j) + text[idx + 1:]
                j = j+1
                break
        else:
            if (item== '(' or item =='[') and (text[idx + 1]=='.'):
                open +=1
                if open== 1:
                    val=0
                    for i in range(30):
                        if text[idx-i-1].isdigit():
                            val*=10   
                            val+= ord(text[idx-i-1]) - ord('0')
                            #print(val)                        
                        else:
                            break
                    text = text[:idx+1] + str(val)[::-1] + text[idx + 2:]
                    
                    break
            elif (item == ')' or item == ']' ) and (text[idx + 1]=='.'):
                open -=1      
            elif item =='{' and (text[idx + 1]=='.') and open==0:   
                text = text[:idx+1] + str(j) + text[idx + 2:]
                for idx2, item2 in enumerate(text[idx+1:]):
                    print(idx2)   
                    if item2 == '{':
                        open_key+=1
                    elif item2 =='}':
                        open_key-=1
                        if open_key == -1:
                            text = text[:idx+idx2+2] + str(j) + text[idx+idx2 + 3:]
                            j+=1
                        break
                break
print(text)

#."a" ."b" .(."c".|.A.(."a" .| ."b".).).|.[."a".|."b".].{."b"."c".|.A.|.B.}.

#2:01 -- completo
#1:46 -- regras