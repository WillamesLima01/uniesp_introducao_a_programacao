qtde = (int(input("Informe a quantidade de maçã desejada: ")))

if qtde < 12:
    total = qtde * 1.30
    print(f'O valor da compra é {total} reais')
else:
    total = qtde * 1
    print(f'O valor da compra é {total} reais')