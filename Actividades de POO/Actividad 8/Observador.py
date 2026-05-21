from Jugador import Jugador

class Observador(Jugador):
    def __init__(self, nombre, numero_de_control, nivel,puntos,partidas_vistas):
        super().__init__(nombre, numero_de_control, nivel,puntos)
        self.partidas_vistas = partidas_vistas 
        
    def ver_partida(self):
        self.partidas_vistas += 1
        
    def mostrar_perfil(self):
        super().mostrar_perfil()
        print(f"Partidas vistas: {self.partidas_vistas}") 