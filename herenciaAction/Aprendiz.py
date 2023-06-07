from Persona import * #de esta manera se puede importar todos los metodos que tengamos en otra clase o tambien modulo 
from Curso import *

class Aprendiz(Persona):
    def __init__(self,nombre,documento,formacion,ficha): #constructor de la clase aprendiz
        Persona.__init__(self,nombre,documento)
        self.__formacion=formacion
        self.__ficha=ficha
        self.__cursos=[] #aca nos mostrara la lista de cursos vacia la cual se llenara despues 
    
    def agregarCurso(self,curso): #metodo para la agregacion de los cursos
        self.__cursos.append(curso)
    
    def componerCurso(self): #metodod para componer los cursos 
        nombreCurso=input('Ingrese nombre del curso') #aca los que podremos hacer es ingresar el nombre del curso
        tipoCurso=input('Ingrese tipo del curso') #aca podremos ingresar el tipo de curso 
        objcurso=Curso(nombreCurso,tipoCurso)
        self.__cursos.append(objcurso) 
    
    def verCursos(self):
        return self.__cursos #aca nos retornara la lista de cursos que se hallan ingresado 