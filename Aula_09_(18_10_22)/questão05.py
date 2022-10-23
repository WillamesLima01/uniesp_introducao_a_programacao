#Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B.
#  Exemplo: A[0] + B[0] deverá ser salva em N[0].

from random import randint

N=[]
A=[]
B=[]

for i in range(10):
    A.append(randint(0, 20))
    B.append(randint(20, 40))
    N.append(A[i]+B[i])

for x in range(len(N)):
    print(N[x])