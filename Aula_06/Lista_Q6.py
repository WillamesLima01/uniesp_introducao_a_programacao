indx = (int(input("Confirme a presença por código (0 = joão, 1 = Pedro, 2 = Tiago, 3 = José, 4 = Antônio, 5 = Ricardo, 6 = Ronaldo e 7 = Lucas): ")))
jantar = ["João" , "Pedro" , "Tiago", "José" , "Antônio" , "Ricardo" , "Ronaldo" , "Lucas"]

i = len(jantar) -1
print(i)
while i >= 0:
    #if indx != i:
        print(jantar[i])        
        i-= 1       