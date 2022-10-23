#Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos.
#  Calcular a média da turma e contar quantos alunos obtiveram nota acima desta 
# média calculada. Escrever a média da turma e o resultado da contagem.

from random import randint

notas=[]
totalsoma=0
qtdnotas=0
acimadamedia=0

for nota in range(20):
    notas.append(randint(0, 10))

for i in range(len(notas)):
    totalsoma=totalsoma + notas[i]

qtdnotas = (len(notas))
media=totalsoma/qtdnotas

for i in range(len(notas)):
    if notas[i] > media:
        acimadamedia=acimadamedia+1

print(f'A média da turma foi {media} e a quantidade de alunos(as) que obtiveram nota acima da média foi(foram) {acimadamedia} alunos(as).')