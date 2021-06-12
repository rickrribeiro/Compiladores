from src.estados import define_estado
#text=' (("a" "b") ("c"|A("a" |"b")))|["a"|"b"]{"b""c"|A|B}'
def bpontos(name, text):
    
    text = text.replace(" ","")

    aspas = False
    while text[-1]!='.':
    
        for idx, item in enumerate(text):
            if idx==0 and text[idx]!='.':
                text =  '.' + text[idx:]
            if idx == len(text)-1:
                text = text[:idx+1] + '.'
                break
            if text[idx]=='"':
                aspas= not aspas
            if text[idx]=='.' or text[idx+1]=='.':
                continue
            if not aspas:
                if ord(text[idx])>= ord('a') and ord(text[idx]) <= ord('z'):
                    if ord(text[idx+1])>= ord('a') and ord(text[idx+1]) <= ord('z'):
                        continue
                text = text[:idx+1] + '.' + text[idx + 1:]
                break


    # cur_path = os.path.dirname(__file__)
    # new_path = os.path.relpath("txts\\automato_bruto_"+name+".txt", cur_path)
    # with open(new_path, 'w') as f:
    #     text = f.write(text)
    f = open("txts\\automato_bruto_"+name+".txt",'w+')
    f.write(text)
    f.close()
    return define_estado(name=name,text=text)
    