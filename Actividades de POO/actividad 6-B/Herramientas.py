from abc import ABC, abstractmethod

# Tabla de daño por material (no la modifiques)
DAÑO_MATERIAL = {
    "madera"    : 2,
    "piedra"    : 3,
    "hierro"    : 4,
    "oro"       : 3,  # rápido pero frágil
    "diamante"  : 6,
    "netherita" : 8,
}


class Herramientas(ABC):
    """Clase abstracta para todas las herramientas."""

    def __init__(self, material: str, durabilidad: int):
        self._material      = material.lower()
        self._durabilidad    = durabilidad
        self._usos_restantes = durabilidad

    # Propiedad ABSTRACTA
    @property
    @abstractmethod
    def nombre(self) -> str:
        """Nombre de la herramienta (ej. 'Pico')."""
        pass

    # Método ABSTRACTO
    @abstractmethod
    def usar(self, objetivo: str) -> str:
        """Describe la acción sobre el objetivo."""
        pass

    # Métodos CONCRETOS heredados por todas las subclases
    def calcular_daño(self) -> int:
        return DAÑO_MATERIAL.get(self._material, 1)

    def desgastar(self):
        if self._usos_restantes > 0:
            self._usos_restantes -= 1

    @property
    def rota(self) -> bool:
        return self._usos_restantes == 0

    def estado(self):
        txt = "💔 ROTA" if self.rota else f"✅ {self._usos_restantes} usos"
        print(f"[{self.nombre} de {self._material}] {txt}")