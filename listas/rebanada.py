import random
tam=random.randint(5,20)
lista=[random.randrange(100) for i in range(tam) ]
print(lista)
rebanada=lista[len(lista)//2]
print(rebanada)
#Llenar una lista con numeros aleatorios(reales con un decimal) que representen calificaciones de un curso. 
#Se evalua de 0 a 5. 
#El curso puede tener ENTRE 20 Y 30 aprendices 
#HALLAR
#Genere listas nuevas para los aprobados y los reprobados(se aprueba con 3)
#Genere listas nuevas por cada unidad. Es decir, los que sacan de 0 a 1 son un rupo, los de 1 a 2 otro y asi sucesivamente
#Diga cual es el promedio de los quer aprueban y de los que reprueban por separado.
