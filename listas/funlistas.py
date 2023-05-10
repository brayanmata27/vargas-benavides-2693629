import random
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista#se retorna la funcion para poder ser llamada despues

def sumaLista(lista):#se crea una funcion la cual nos serviria 
    #para sumar los numeros que se encuentran en la lista

    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):#se crea una funcion para que halle el promedio
    return sumaLista(lista)/len(lista)


def mayor(lista):
    mayor=max(lista)
    return mayor

def menor(lista):
    menor=min(lista)
    return menor


def ascendenteyDescendente(lista,tam):
    for i in range(tam-1):
        for j in range(i+1,tam):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]



l1=llenarLista(3,10)
print(l1)
print(sumaLista(l1))
print('el promedio es',round(promedioLista(l1),2))
print('el numero mayor es',mayor(l1))
print('el menor es',menor(l1))
print(ascendenteyDescendente,(l1))
