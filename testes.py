#arquivo apenas para fazer testes no python

# a = "abcde"
# print(a[:1])
# print(a[1:])
# a='\n'
# print(len(a))
# a='"abcd"'
# b = a.split('"')
# print(b)

# c= 'aaaaaaaaaassssssssssdddddddddeeeeeeeeeee'
# print(c[:30])


# from src.model import Estado, Transicao


# st1 = Estado(1,None)
# st2 = Estado(2,None)
# st3 = Estado(3,None)
# st4 = Estado(4,None)

# trans1 = Transicao('a')
# trans1.finais=[1,2]
# trans2 = Transicao('b')
# trans2.finais=[1,2]
# trans3 = Transicao('c')
# trans3.finais=[1,3]
# trans4 = Transicao('a')
# trans4.finais=[1,2]

# estados = []
# st1.transicoes.append(trans1)
# st2.transicoes.append(trans2)
# st3.transicoes.append(trans3)
# st4.transicoes.append(trans4)

# estados.append(st1)
# estados.append(st2)
# estados.append(st3)
# estados.append(st4)

# for st in estados:
#     for st22 in estados:
#         if st.estado == st22.estado:
#             continue
#         print(str(st.transicoes)+ " "+ str(st22.transicoes))
#         if st.transicoes == st22.transicoes:
#             print("IGUAL")

ar = ['ab']
ae = ['ab']
if ar == ae:
    print('true')