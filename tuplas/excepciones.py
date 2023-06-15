def cargar_lista(opcion):
    lista = []
    while True:
        try:
            elemento = input("Ingrese un elemento para la lista (o 'q' para salir): ")
            if elemento == 'q':
                break
            if opcion == 1 or opcion == 2 or opcion == 5:
                elemento = elemento.upper()
            elif opcion == 3 or opcion == 4:
                if not elemento.isdigit() or int(elemento) % 2 != 0:
                    raise ValueError("El número ingresado no es par.")
            elif opcion == 6:
                if not elemento.isalpha():
                    raise ValueError("El elemento ingresado no es una letra.")
                elemento = elemento.upper()
            if elemento in lista:
                raise ValueError("El elemento ya existe en la lista.")
            lista.append(elemento)
        except ValueError as error:
            print("Error:", error)
    return lista

def mostrar_lista(lista):
    print("Contenido de la lista:")
    for elemento in lista:
        print(elemento)

def elegir_posicion(lista):
    try:
        posicion = int(input("Ingrese una posición de la lista: "))
        if posicion < 0 or posicion >= len(lista):
            raise IndexError("Posición fuera de rango.")
        print("El elemento en la posición", posicion, "es:", lista[posicion])
    except ValueError:
        print("Error: Ingrese un número entero.")
    except IndexError as error:
        print("Error:", error)

# Menú principal
lista = []
opcion = 0

while True:
    print("------- MENÚ -------")
    print("1. Lenguajes de programación")
    print("2. Nombre de regionales del SENA")
    print("3. Números pares")
    print("4. Números múltiplos de 4")
    print("5. Nombres de aprendices del grupo 2693629")
    print("6. Letras")
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '7':
        break
    elif opcion.isdigit() and 1 <= int(opcion) <= 6:
        lista = cargar_lista(int(opcion))
    elif opcion == '2':
        print("La lista aún no ha sido cargada. Por favor, seleccione una opción válida antes de mostrar la lista.")
    else:
        print("Opción inválida. Intente nuevamente.")

    if opcion != '2':
        mostrar_lista(lista)

    if opcion.isdigit() and (1 <= int(opcion) <= 6 or opcion == '3' or opcion == '4'):
        elegir_posicion(lista)

print("¡Hasta luego!")
