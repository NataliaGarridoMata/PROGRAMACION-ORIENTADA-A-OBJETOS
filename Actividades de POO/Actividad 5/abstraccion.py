from abc import ABC, abstractmethod

#clase abstracta (plantilla) 
class Animal (ABC):
    
    @abstractmethod
    def hablar (self):
        pass   #no se implementa el metodo 
    

#clase en especifico 
class Perro(Animal):
    
    def hablar(self):
        return("guau")
 
#clase en especifico   
class Gato(Animal):
    
    def hablar(self):
        return("miau")  
    
#usar las clases
perro1 = Perro()
gato1 = Gato()
print(Perro().hablar())
print(Gato().hablar())