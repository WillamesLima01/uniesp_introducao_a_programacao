#Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene 
# os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de 
# mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver 
# entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.
lista=[]
controle=True
confirmado=False

while controle:
    nome = input("Informe o time: ")
    lista.append(nome)
    qtd=(len(lista))
    if qtd==10:
        controle=False

verificado=input("Informe o nome do clube para verificar na lista de times classificados: ")

for i in range(len(lista)): 
    if verificado==lista[i]:
        confirmado=True

if confirmado==True:
    print(f'ACHEI o clube {verificado}')
else:
    print(f'NÃO ACHEI o clube {verificado} na relação de clubes classificados')