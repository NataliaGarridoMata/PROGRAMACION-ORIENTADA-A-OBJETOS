
class mascotaVirtual:
    def __init__(self,nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad
        
    def alimentar(self):    
        self.nivelFelicidad = max(0, min(self.nivelFelicidad + 10, 100))
    
    def jugar(self): 
        self.nivelFelicidad = max(0, min(self.nivelFelicidad + 20, 100))

    def mostrarEstado(self):
            return f"Hola, me llamo {self.nombre}, tengo {self.edad} años, y soy un adorable {self.tipo}. Mi nivel de felicidad es {self.nivelFelicidad}.¿tu mascota es feliz?"
    
    def esFeliz(self):
        if self.nivelFelicidad >= 70:
            return "Tu mascota esta feliz"
        else:
            return "Tu mascota no esta feliz"
        
            

mascota1 = mascotaVirtual("petit","perrito", 3, 10)
mascota1.alimentar()
mascota1.jugar()
print(mascota1.mostrarEstado())
print(mascota1.esFeliz())


mascota2 = mascotaVirtual("rabit","conejito", 2, 30)
mascota2.alimentar()
mascota2.alimentar()
mascota2.jugar()
mascota2.jugar()
mascota2.jugar()
print(mascota2.mostrarEstado())     
print(mascota2.esFeliz())

