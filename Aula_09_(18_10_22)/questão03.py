#Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
# o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

from random import randint

vlr1=float(input("Informe o primeiro número da sequência: "))
vlr2=float(input("Informe o último número da sequência: "))

Q=[]
maiorN=0
posicao=0

if vlr1>vlr2:
    print("ATENÇÂO!!! O valor do segundo número da sequência tem que ser maior que o primeiro número e ambos positivos!")   
    exit()
elif vlr1==vlr2:
    print("ATENÇÃO!!! Os Número tem que ser diferentes e ambos positivos!")
    exit()
for n in range(20):
    Q.append(randint(vlr1, vlr2))
    # print(Q[n])
for i in range(len(Q)):        
    if Q[i] > maiorN:
        maiorN=Q[i]
        posicao=i

print("")
print(f' O maior número da sequência é {maiorN} e sua posição numerica de da sequência é {posicao}.')