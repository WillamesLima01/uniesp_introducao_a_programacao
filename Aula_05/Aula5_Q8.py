qtd_atual = (int(input("Informe a quantidade atual em estoque: ")))
qtd_max = (int(input("Informe a quantidade máxima de estoque: ")))
qtd_min = (int(input("Informe a quantidade mínima de estoque: ")))

media = (float((qtd_max + qtd_min)/2))

if qtd_atual >= media:
    print("Não efetuar compra!")
else:
    print("Atenção! efetuar compra!")