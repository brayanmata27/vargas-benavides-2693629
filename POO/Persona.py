class Persona:
    def __init__(self, nombre, documento,cursos):
        #print('se instancio un objeto')
        self.__nombre=nombre
        self.__documento=documento
        #self.__ telefono
        self.__cursos=[]

    def setnombre(self,nombre):
        self.__nombre=nombre

    def getnombre(self):
        return self.__nombre
    
    def setdocumento(self,documento):
        self.__documento=documento 

    def getdocumento(self):
        return self.__documento
    
    def setcursos(self):
        self.__cursos=[]

    def getcursos(self):
        return self.__cursos

