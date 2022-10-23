#Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada. Calcular e escrever a 
#quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.

from random import randint

V1=[]
V2=[]
listaresultante=[]
posicao=[]
contador=0
listavazia=True

for i in range(10):
    V1.append(randint(0, 10)) 
    if i<9:
        print(f'{V1[i]}', end=", ")
    else:
        print(f'{V1[i]}', end="\n")

print("--------------------------------------------------------------")
for i in range(10):    
    V2.append(randint(0, 10))
    if i<9:
        print(f'{V2[i]}', end=", ")
    else:
        print(f'{V2[i]}', end="\n")
print("")

for i in range(10):
    if V1[i]==V2[i]:
        contador=contador+1
        listaresultante.append(V1[i])
        posicao.append(i)
        listavazia=False

if listavazia==True:
    print("Não houve número coincidente e na mesma posição!")
else:
    print(f'Os Número(s) que se repente(em) na mesma posicão (é) são em quantidade: {contador}, na posição: {posicao} e o(s) número(s) (é) são: {listaresultante}')