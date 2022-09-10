vlr1 = (float(input("Informe o primeiro valor: ")))
vlr2 = (float(input("Informe o segndo valor: ")))

if vlr1 == vlr2:
    print(f'Você digitou números iguais! Valor digitado {vlr1}')
elif vlr1 > vlr2:
    print(f'Seu primeiro número digitado é maior que o segundo. Digitou o número {vlr1}')
else:
    print(f'Seu segundo número digitado é maior que o primeiro. Digitou o número {vlr2}')