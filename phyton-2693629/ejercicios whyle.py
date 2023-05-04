num=1
substraction=0
mayor=0
menor=1000000
while num!=0:
    num=int(input('ingrese numero'))
    substraction=substraction-num
    if num>mayor:
        mayor=num
    if num<menor and num!=0:
        menor=num


print(f'La resta es {substraction}')

print(f'El mayor es {mayor}')
print(f'El menor es {menor}')
#print('El usuario ingreso', cont, 'numeros')

