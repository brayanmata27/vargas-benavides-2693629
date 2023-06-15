def lista_lenguajes():
    lenguajes = set()
    while True:
        try:
            lenguaje = input("Ingrese un lenguaje de programación (0 para terminar): ")
            if lenguaje == '0':
                break
            lenguajes.add(lenguaje.upper())
        except:
            print("Error: Ingrese un valor válido.")
    return lenguajes

def lista_regionales():
    regionales = set()
    while True:
        try:
            regional = input("Ingrese una regional del SENA (0 para terminar): ")
            if regional == '0':
                break
            regionales.add(regional.upper())
        except:
            print("Error: Ingrese un valor válido.")
    return regionales

def lista_pares():
    pares = set()
    while True:
        try:
            numero = int(input("Ingrese un número par (0 para terminar): "))
            if numero == 0:
                break
            if numero % 2 == 0:
                pares.add(numero)
            else:
                print("Error: El número ingresado no es par.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    return pares

def lista_multiplos4():
    multiplos4 = set()
    while True:
        try:
            numero = int(input("Ingrese un número múltiplo de 4 (0 para terminar): "))
            if numero == 0:
                break
            if numero % 4 == 0:
                multiplos4.add(numero)
            else:
                print("Error: El número ingresado no es múltiplo de 4.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    return multiplos4

def lista_curso():
    nombres = set()
    while True:
        try:
            nombre = input("Ingrese el nombre de un aprendiz del grupo 2693630 (0 para terminar): ")
            if nombre == '0':
                break
            nombres.add(nombre.upper())
        except:
            print("Error: Ingrese un valor válido.")
    return nombres

def lista_solo_letras():
    letras = set()
    while True:
        try:
            letra = input("Ingrese una letra (0 para terminar): ")
            if letra == '0':
                break
            if letra.isalpha():
                letras.add(letra.upper())
            else:
                print("Error: Ingrese solo letras.")
        except:
            print("Error: Ingrese un valor válido.")
    return letras

def imprimir_listas():
    print("Contenido de las listas:")
    print("1. Lista de Lenguajes de Programación:", lista_lenguajes())
    print("2. Lista de Regionales SENA:", lista_regionales())
    print("3. Lista de Números Pares:", lista_pares())
    print("4. Lista de Múltiplos de 4:", lista_multiplos4())
    print("5. Lista de Aprendices del grupo 2693630:", lista_curso())
    print("6. Lista de Letras:", lista_solo_letras())

def menu():
    while True:
        print("=== Menú ===")
        print("1. Cargar lista de Lenguajes de Programación")
        print("2. Cargar lista de Regionales SENA")
        print("3. Cargar lista de Números Pares")
        print("4. Cargar lista de Múltiplos de 4")
        print("5.")
