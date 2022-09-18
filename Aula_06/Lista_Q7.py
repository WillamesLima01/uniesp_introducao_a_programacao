Lista_cadastro = []
controle = True

while controle:
    resp = (str(input("Digite 'S' para continuar e 'N' para sair: "))).upper()

    if resp == "N":
        exit()
    else:
        nome = (str(input("Informe seu nome, por favor: ")))
        idade = (int(input("Informe sua idade, por favor: ")))
        email = (str(input("Informe seu e-mail, por favor: ")))

        Lista_cadastro.append(nome)
        Lista_cadastro.append(idade)
        Lista_cadastro.append(email)

        print(Lista_cadastro)