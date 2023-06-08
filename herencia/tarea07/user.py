class user:
    def __init__(self,name,id):
        self.__name=name
        self.__id=id

    
    def setname(self,name):
        self.__name=name

    def getname(self):
        return self.__name
    

    def setid(self,id):
        self.__id=id

    def getid(self):
        return self.__id
    
    #def verify(self):
        