import math
controle=True

while controle:
    sair= (input('Digite E para sair ou C para continuar:')).upper()

    if sair=="E":
        controle= False
    else:
        a = (float(input('Informe o valor de a: ')))
        b = (float(input('Infome o valor de b: ')))
        c = (float(input('Infome o valor de c: ')))
    
        delta = (b**2) - (4*a*c)

        if delta==0:
            print('Por favor altere os valores, pois o discriminante é 0')        
        else:

            x = (-b+(math.sqrt(delta)))/(2*a)

            y = (-b-(math.sqrt(delta)))/(2*a)

            px1= (-b+(math.sqrt(delta)))
            px2= (2*a)

            py1= (-b-(math.sqrt(delta)))
            py2= (2*a)

            if (px1 % px2)== 0:
                print(x)
            else:
                print(f'{px1:.0f} / {px2:.0f}')

            if (py1 % py2)== 0:
                print(y)
            else:
                print(f'{py1:.0f} / {py2:.0f}')