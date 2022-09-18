revac = True

while revac:
    resultado = (input("Enviar convite para os convidados (S/N): (joão, Pedro, Tiago, José, Antônio, Lucas): ")).upper()
    jantar = ["João" , "Pedro" , "Tiago", "José" , "Antônio" , "Lucas"]

    if resultado == "SAIR":
        revac = False
    else:
        if resultado != "S" and resultado != "N":
            print("opção errada!") 
                          
        else:
            if resultado == "N":
                addremv = (input("Deseja adicionar convidado?(S/N): ")).upper()
                if addremv == "N":
                    revnome = (input("Informe o nome do convidado para excluir da lista: "))
                    jantar.remove(revnome)
                    for convidado in jantar:
                        print(f'Óla, {convidado}, você está convidado para um jantar em minha residência!')

                else:
                    addnome = (input("Informe o nome do convidado para inserir na lista: ")).upper()
                    jantar.append(addnome)
                    for convidado in jantar:
                        print(f'Óla, {convidado}, você está convidado para um jantar em minha residência!')
            else:
                for convidado in jantar:
                    print(f'Óla, {convidado}, você está convidado para um jantar em minha residência!')