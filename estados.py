text = '."a" ."b" .(."c".|.A.(."a" .| ."b".).).|.[."a".|."b".].{."b"."c".|.A.B.}.'
text = text.replace(" ","")

j = 0
open = 0
a = ""
b = ""
for i in range(9999):
#while(True):
    if '.' not in text:
        break
    for idx, item in enumerate(text):
        
        if item == '.':
            if open == 0:
                text = text[:idx] + str(j) + text[idx + 1:]
                j = j+1
                break
        else:
            if (item== '(' or item =='[' or item == '{') and (text[idx + 1]=='.'):
                open +=1
                if open== 1:
                    print(text[idx])
                    text = text[:idx+1] + str(j-1) + text[idx + 2:]
                    
                    break
            elif (item == ')' or item == ']' or item == '}') and (text[idx + 1]=='.'):
                open -=1            

print(text)

#."a" ."b" .(."c".|.A.(."a" .| ."b".).).|.[."a".|."b".].{."b"."c".|.A.B.}.