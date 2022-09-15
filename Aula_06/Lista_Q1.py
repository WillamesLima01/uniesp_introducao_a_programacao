'''Desenvolva um programa que verifique e mostre os números entre
1000 e 2000 que, quando dividido por 11, produzam o resto igual a 5.'''

# '%' modulo (quer dizer resto da divisão)
for num in range(1000, 2001):
    if (num % 11) == 5:
        print(num)
