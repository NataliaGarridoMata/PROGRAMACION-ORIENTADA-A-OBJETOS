from Herramientas import Herramientas 

class Espada(Herramientas):
    @property
    def nombre(self) -> str:
        return "Espada"

    def usar(self, objetivo: str) -> str:
        self.desgastar()               # Resta 1 a los usos
        daño = self.calcular_daño()     # Obtiene el daño de la tabla
        return f"⚔️ Atacando a {objetivo} con la Espada de {self._material} causando {daño} de daño"