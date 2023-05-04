import random
lista= []
suma=0
mayor=100
menor=0
tam=int(random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    suma+=num

if num>mayor:
    mayor=num
if num<menor and num!=0:
    menor=num 


print(lista)
print(f'la suma es{suma}')
print(f'el mayor es{mayor}')
print(f'el menor es{menor}')

