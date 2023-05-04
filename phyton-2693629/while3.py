num=1
cont=0
sum=0
mayor=0
menor=1000000
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1 #cont+=1
    sum=sum+num #sumando
    if num>mayor:
        mayor=num
    if num<menor and num!=0:
        menor=num

print(f'El usuario ingreso {cont-1} numeros')
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)} numeros')
print(f'El mayor es {mayor}') #sacando el mayor
print(f'El menor es {menor}') #sacando el menor
#print('El usuario ingreso', cont, 'numeros')



#if num>mayor:
#    mayor=num
#if num<menor and num!=0:
#    menor=num 
#print(f'el mayor es{mayor}')
#print(f'el menor es{menor}')