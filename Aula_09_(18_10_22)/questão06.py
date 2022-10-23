#Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um
#  número qualquer e verificar se esse número existe no vetor ou não. Se existir, o 
# algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverão números
# repetidos no vetor).

from random import randint

controle=True


while controle: 

    V1=[]   
    indece=0
    numero=0
    sorteado=False

    numero=int(input("Informe um número de 0 a 100 para verificar se está na relação ou 200 para sair: "))
    
    if numero==200:
        controle=False
    else:
        for i in range(20):
            V1.append(randint(0, 100))
            if i<19:
                print(f'{V1[i]}, ', end="")
            else:
                print(f'{V1[i]}', end="")
        
        for x in range(len(V1)):
            if numero==V1[x]:
                indece=x
                sorteado=True    

        if sorteado==True:

            del V1[indece]
            print("")
            for n in range(20):
                print("-----", end="")
            print("")

        if sorteado==True:
            for j in range(len(V1)):
                if j < 18:
                    print(f'{V1[j]}, ', end="")
                else:
                    print(f'{V1[j]}', end="")
            print("")
        else:
            print(f'  -----> O número {numero} não foi sorteado!')