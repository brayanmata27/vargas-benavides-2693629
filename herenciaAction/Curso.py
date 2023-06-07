class Curso:
    def __init__(self,nombre,tipo): #constructor de la clase curso
        self.__nombre=nombre
        self.__tipo=tipo

    def getNombre(self):#de esta manera se retorna el nombre del curso dque se agregue 
        return self.__nombre