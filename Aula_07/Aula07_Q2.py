ano_atual = (int(input("informe o ano atual: ")))
ano_nasc = (int(input("informe o ano que você nasceu: ")))

if ano_atual - ano_nasc < 18:
    print("Você não pode votar nessa eleição!")
else:
    print("Parabéns! você pode votar nessa eleição")