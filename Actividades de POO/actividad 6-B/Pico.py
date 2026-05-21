from Herramientas import Herramientas 

class Pico (Herramientas):
    """Mina bloques de piedra, carbón, hierro, etc."""
    # TODO: propiedad 'nombre' y método 'usar'
    # En usar(): llama a calcular_daño() y a desgastar()
    @property
    def nombre(self) -> str:
        return "Pico"

    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"¡Mina {objetivo} con el pico de {self._material}! (Daño: {daño})" 