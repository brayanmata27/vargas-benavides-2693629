from Aprendiz import *
from Curso import *

objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629) 
#print(objeto.__dict__)
objcurso=Curso("Programacion Software","tecnico")#aca se agrega la informacion del primer curso que se nos va a mostrar
objeto.agregarCurso(objcurso)
#print(objeto.__dict__)
objeto.componerCurso() 
objeto.componerCurso()  
#print(objeto.verCursos())
for cursito in objeto.verCursos():
    print(cursito.getNombre())