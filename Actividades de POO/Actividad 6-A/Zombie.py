from Mob import Mob

class Zombie(Mob):
    """Mob explosivo, suena 'sss', camina lento."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    def hacer_sonido(self) -> str:
        return "Aggg"

    def comportamiento(self) -> str:
        return "Muerde"

    def moverse(self) -> str:
        return "camina lento"