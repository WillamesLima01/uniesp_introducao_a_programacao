avl1 = (int(input("Informe a nota da primeira avaliação: ")))
avl2 = (int(input("Informe a nota da segunda avaliação: ")))

media = (avl1 + avl2) / 2

if media >= 6:
    print(f'Parabéns, você foi aprovado(a) com média {media}')
else:
    print(f'Infelizmente sua média ficou abaixo do resultado necessário para aprovação. Média {media}')