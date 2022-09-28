lista_seq = []
pvl=1

vl= int(input('Informe um número inteiro: '))
fat=vl
while vl>=1:
    pvl=(pvl * vl)    
    lista_seq.append(vl)
    
    vl=vl-1
print(f'{fat}!=',end="")
for num in lista_seq:
    if num!=1:
        print(f' {num} x', end="")
    else:
        print(f' {num}= {pvl}', end="") 