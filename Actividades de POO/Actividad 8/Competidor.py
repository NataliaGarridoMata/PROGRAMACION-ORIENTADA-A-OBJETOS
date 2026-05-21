from Jugador import Jugador
class Competidor(Jugador):
    def __init__(self, nombre, numero_de_control, nivel, puntos, equipo):
        super().__init__(nombre, numero_de_control, nivel, puntos)
        self.equipo = equipo
        
    def mostrar_perfil(self):
        super().mostrar_perfil()
        print(f"Equipo: {self.equipo}")