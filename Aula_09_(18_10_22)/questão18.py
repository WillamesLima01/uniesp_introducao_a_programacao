from random import randint

v1=[]
v2=[]

for n in range(50):
    v1.append(randint(0, 10))
    v2.append(randint(0, 10))

print(v1)
print(v2)

for n in range(len(v1)):
    if v1[n]==v2[n]:
        print(v1[n])