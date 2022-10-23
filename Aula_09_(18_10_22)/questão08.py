#Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer,
# calcular e escrever quantas vezes esse número aparece no vetor.

from random import randint

V1=[]
numero=0
contador=0
posicao=[]
aparece=False

numero=int(input("Informe um número de 0 a 100: "))

for i in range(30):
    V1.append(randint(0, 100))
    if i<29:
        print(f'{V1[i]}', end=", ")
    else:
        print(f'{V1[i]}', end="\n")
print("---------------------------------------------------------------------------------------------------------------------")

for i in range(30):
    if V1[i]==numero:
        contador=contador+1
        posicao.append(i)
        aparece=True

if aparece==True:
    print(f'O número {numero} aparece {contador} vez(es) na lista na posição {posicao}.')
else:
    print(f'O número {numero} não aparece na lista!')