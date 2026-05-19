from Guerrero import Guerrero
from Mago import Mago
from Arquero import Arquero
from Elfo import Elfo

guerrero = Guerrero("Thorin", 8, "Hacha")
mago = Mago("Gandalf", 20, "Bola de fuego")
arquero = Arquero("Legolas", 15, 30)
elfo = Elfo("merlin",10,"disminucion de vida")

guerrero.presentarse()
guerrero.usar_habilidad()

print("---")

mago.presentarse()
mago.usar_habilidad()

print("---")

arquero.presentarse()
arquero.usar_habilidad()

print("---")

elfo.presentarse()
elfo.usar_habilidad()