potenci=(int(input('digite numero')))

def potencia(base,exponente):
    resultado=1
    for i in range(exponente):
        resultado *=base
    return resultado


print(potencia)