from Platillo import Platillo 

class Bebida(Platillo):
    def __init__(self, nombre, precio, temperatura):
        super().__init__(nombre,precio)
        self.temperatura = temperatura 
    
    def mostrarInformacion(self):
       
        print (f"temperatura: {self.temperatura}")
        