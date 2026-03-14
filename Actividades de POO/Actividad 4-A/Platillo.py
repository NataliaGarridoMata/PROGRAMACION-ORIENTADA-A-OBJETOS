class Platillo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def mostrarinformacion(self):
        return(f"Platillo: {self.nombre}, Precio: ${self.precio:.2f}")
    
    def tipo (self):
        return "Platillo"
    
   