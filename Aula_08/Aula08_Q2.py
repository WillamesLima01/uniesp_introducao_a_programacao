import math

pt1=(float(input('Informe o primeiro ponto do plano: ')))
pt2=(float(input('informe o segundo ponto do plano: ')))
pt3=(float(input('Informe o terceiro ponto do plano: ')))
pt4=(float(input('informe o quarto ponto do plano: ')))

vlr=(float(math.sqrt((pt1-pt2)**2 + (pt3-pt4)**2)))

print(f'A distância entre os ponto é {vlr:.2f}')