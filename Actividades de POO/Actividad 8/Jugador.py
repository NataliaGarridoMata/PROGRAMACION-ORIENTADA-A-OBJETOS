class Jugador:
    def __init__(self, nombre, numero_de_control, nivel, puntos):
        self.nombre = nombre
        self.numero_de_control = numero_de_control
        self.nivel = nivel
        self.puntos = puntos
        
    def ganar_puntos(self, cantidad):
        self.puntos += cantidad
    
    def perder_puntos(self, cantidad):
        self.puntos -= cantidad 
    
    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}\nNúmero de Control: {self.numero_de_control}\nNivel: {self.nivel}\nPuntos: {self.puntos}")
   