#Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X.
# Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X.
#  Logo após, imprimir o vetor M.

from random import randint

A=[]
M=[]
x=0

for n in range(11):
    if n<10:
        A.append(randint(0, 20))
        #print(A[n])
    else:
        A.append(randint(0, 20))
        x=A[n]

for i in range(len(A)):
    M.append(x*A[i])
    print(M[i])