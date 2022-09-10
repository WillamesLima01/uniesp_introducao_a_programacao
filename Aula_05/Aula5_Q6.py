vlr1 = (float(input("Digite o primeiro número, por favor: ")))
vlr2 = (float(input("Digite o segundo número, por favor: ")))

if vlr1 == vlr2:
    print("Você digitou número iguais. Digite número diferentes!")
elif vlr1 > vlr2:
    print(f'Os valores em ordem crescente é {vlr2} , {vlr1}')
else:
    print(f'Os valores em ordem crescente é {vlr1}, {vlr2}')