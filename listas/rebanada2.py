#Llenar una lista con numeros aleatorios(reales con un decimal) que representen calificaciones de un curso. 
#Se evalua de 0 a 5. 
#El curso puede tener ENTRE 20 Y 30 aprendices 
#HALLAR
#Genere listas nuevas para los aprobados y los reprobados(se aprueba con 3)
#Genere listas nuevas por cada unidad. Es decir, los que sacan de 0 a 1 son un rupo, los de 1 a 2 otro y asi sucesivamente
#Diga cual es el promedio de los quer aprueban y de los que reprueban por separado.
import random
curso=random.randint(20,30)
aprendices=[float(random.randrange(1,5)) for i in range(curso)]
print(aprendices)
aprobados=0
reprobados=0
aprobados=aprendices[len(aprendices):]
reprobados=aprendices[len(aprendices):]
print(curso)
print(aprendices)
if aprobados>=3:
    print(aprobados)
if reprobados<=2:
    print(reprobados)

#print(curso)
#print(aprendices)
#print(aprobados)
#print(reprobados)
