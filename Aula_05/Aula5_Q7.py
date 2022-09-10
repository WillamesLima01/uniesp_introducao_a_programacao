conta = input("Informe o número da conta: ")
saldo = (float(input("Informe o saldo da conta: ")))
debito = (float(input("Informe o débito da conta: ")))
credito = (float(input("Informe o crédito da conta: ")))
saldoatual = (float((saldo - debito)+ credito))

if saldoatual >= 0:
    print(f'cliente com número de conta, {conta}, Parabéns! Você está com saldo positivo.')
else:
    print(f'Cliente com número de conta, {conta}, ATENÇÃO! Você está com saldo negativo.')