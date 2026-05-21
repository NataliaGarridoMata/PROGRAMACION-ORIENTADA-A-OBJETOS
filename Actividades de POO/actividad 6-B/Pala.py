from Herramientas import Herramientas

class Pala(Herramientas):
    """Excava tierra, arena y grava rápidamente."""
    # TODO: propiedad 'nombre' y método 'usar'
    pass

    @property
    def nombre(self) -> str:
        return "Pala"

    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"¡Excava {objetivo} con la pala de {self._material}! (Daño: {daño})"