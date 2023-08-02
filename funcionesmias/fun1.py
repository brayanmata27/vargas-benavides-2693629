def guardar_datos():
    nombre=input("Ingrese nombre")
    apellido=input("ingrese apellido")
    telefono=input("Ingrese numero de telefono")
    corre=input("Ingrese su correo")
    
archivo= open("datos_personales.txt","w")

archivo.write(f"nombre:{nombre}\n")