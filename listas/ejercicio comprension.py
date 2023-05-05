import random
tam=random.randint(10,20)
lista=[random.randrange(100) for i in range(tam) ]
print(lista)

for i in range(len(lista)-1):
    if lista[i]<lista[i+1]:
        lista[i],lista[i+1]=lista[i+1],lista[i]

print(lista)