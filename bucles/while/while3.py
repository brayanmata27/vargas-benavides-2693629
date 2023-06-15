num=1 
cont=0 
sum=0 
prom=0 
menor=10000000000000 
mayor = 0 
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1 #cont+=1
    sum+=num
    if num>mayor:    
        mayor=num
    if num<menor and num!=0:
        menor=num
        

cont-=1

prom=sum/cont


print("La suma de los numeros es: " , sum)
print("La promedio de los numeros es: " , prom)
print(f'El usuario ingreso {cont} numeros ')
print("El numero mayor es: " , mayor)
print("El numero menor es: " , menor)
