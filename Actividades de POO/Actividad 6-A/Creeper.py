from Mob import Mob

class Creeper(Mob):
    """Mob explosivo, suena 'sss', camina lento."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    def hacer_sonido(self) -> str:
        return "sss"

    def comportamiento(self) -> str:
        return "explosivo"

    def moverse(self) -> str:
        return "camina lento"