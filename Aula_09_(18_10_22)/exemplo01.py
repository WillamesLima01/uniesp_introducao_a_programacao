from re import X


matriz=[
    [1,2,3,6,9],
    [5,7,9,3,0],
    [3,5,2,7,4],
    [2,9,5,0,1],
    [3,7,0,1,6]
]
for l in range(len(matriz)):
    for y in range(len(matriz[l])):
        if l==y:
            print(matriz[l][y])