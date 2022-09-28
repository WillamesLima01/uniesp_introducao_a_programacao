vlr=1
num1=0
num2=0
num3=0
num4=0

while vlr>0:

    vlr=(float(input("Informe um número: ")))

    if vlr > 0 and vlr <= 25:
        num1= num1+1
    elif vlr> 25 and vlr <= 50:
        num2=num2+1
    elif vlr > 50 and vlr <= 75:
        num3=num3+1
    elif vlr > 75 and vlr <= 100:
        num4=num4+1
    else:
        if vlr>0:
            print("Informe um número menor que 100!")

print(f"A quantidade de números entre 0 e 25 é: {num1}")
print(f'entre 26-50 é: {num2}')
print(f'entre 51-75 é: {num3}')
print(f'e entre 76-100 é: {num4}')