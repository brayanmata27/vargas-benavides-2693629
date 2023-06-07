from Persona import *

obj1=Persona('Juan', 54321  )
print(type(obj1))
print(obj1.getnombre())
obj1.setnombre('Mario')
print(obj1.getnombre())

#print(type(obj1))
print(obj1.getdocumento())
obj1.setdocumento(12345)
print(obj1.getdocumento())

print(obj1.getcursos())
obj1.setcursos()
print(obj1.getcursos())