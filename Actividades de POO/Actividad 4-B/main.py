from Guerrero import Guerrero
from Mago import Mago
from Arquero import Arquero

guerrero = Guerrero("Thorin", 8, "Hacha")
mago = Mago("Gandalf", 20, "Bola de fuego")
arquero = Arquero("Legolas", 15, 30)

guerrero.presentarse()
guerrero.usar_habilidad()

print("---")

mago.presentarse()
mago.usar_habilidad()

print("---")

arquero.presentarse()
arquero.usar_habilidad()