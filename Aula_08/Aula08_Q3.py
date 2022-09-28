import math

vlr1=(float(input('Informe o primeiro número: ')))
vlr2=(float(input('Informe o segundo número: ')))
op= int(input('Informe a operação a ser realizada(1- soma; 2- subtração; 3- multiplicação; 4- divisão e 5- potenciação): '))

match op:
    case 1:
        print(vlr1+vlr2)
    case 2:
        print(vlr1-vlr2)
    case 3:
        print(vlr1*vlr2)
    case 4:
        print(vlr1/vlr2)
    case 5:
        print((vlr1**vlr2))
               