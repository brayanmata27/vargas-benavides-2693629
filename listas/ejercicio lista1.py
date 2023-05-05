#tamaño lista=15 y 20 datos dentro de la lista=o a 9 buscar un numero ingresado por teclado en la lista, decir si esta, decir si esta repetido, cuantas veces esta repetido, decir las posiciones en la que esta
import random
tam=random.randint(15,20)
lista=[random.randrange(0,9) for i in range(tam)]
print(lista)

x=int(input('ingrese numero que desea buscar'))

if x  in lista:
    print('si esta en la lista')
else: 
    print('no esta')

lista=[10 for i in range(10)]
print(lista)









#for i in range (len(lista)):
#    if n[i]<=n [i]:
#        n[i], n[i<=n]=n[i<=n],lista[n]

#print(lista)

