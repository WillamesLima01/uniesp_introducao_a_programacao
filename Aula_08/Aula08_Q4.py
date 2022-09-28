peso=(float(input("Informe seu peso: ")))
altura=(float(input("Informe sua altura: ")))

resultado=(peso/altura**2)

if resultado <= 18.5:
    print("Abaixo do peso")
elif resultado > 18.5 and resultado < 26:
    print("Peso normal")
elif resultado > 25 and resultado < 31:
    print("Acima do peso")
else:
    print("Obeso")