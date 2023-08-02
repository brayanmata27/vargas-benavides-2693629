class Pais:
    def __init__(self,nombre,poblacion,altura,pob_cap):
        self.__nombre=nombre
        self.__poblacion=poblacion
        self.__altura=altura
        self.__pob_cap=pob_cap
    def info(self):
        return f"{self.__nombre} {self.__poblacion} {self.__altura} {self.__pob_cap}"
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__poblacion
    
    def getAltura(self):
        return self.__altura
    
    def getPob_cap(self):
        return self.__pob_cap
    