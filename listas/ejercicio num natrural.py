def numat(x):
    suma= 1
    n=1
    while suma <= maximo:
        suma=suma+n
        n=n+1
    return n-1
maximo=int(input('digite un numero maximo'))
lista=numat(-1)
print('el numero umero natural mas pequeño necesario para superar el maximo es', lista)
