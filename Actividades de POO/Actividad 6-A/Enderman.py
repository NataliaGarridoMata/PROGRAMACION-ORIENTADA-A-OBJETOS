from Mob import Mob

class Enderman(Mob):
    """Mob Pasivo, suena 'Grrr', teletransportacion."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    def hacer_sonido(self) -> str:
        return "Grrr"

    def comportamiento(self) -> str:
        return "Pasivo"

    def moverse(self) -> str:
        return "teletransportacion"