class empleado:

    objetos=0
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
        empleado.objetos+=1

    def getnombre(self):
        return self.nombre
    
    def setnombre(self,nombre):
        self.nombre=nombre

    def getcargo(self):
        return self.cargo
    
    def setcargo(self,cargo):
        self.cargo=cargo

    def getsalario(self):
        return self.salario
    
    def setsalario(self,salario):
        self.salario=salario

    def calcularHora(self):
        horastrabajo=8
        diassemana=5
        diasmes=20
        salariohora=self.salario /(horastrabajo * diassemana * diasmes)
        return self.__salariohora

    
