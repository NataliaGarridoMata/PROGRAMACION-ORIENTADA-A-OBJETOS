#Clase
from Comida import Comida
from Bebida import Bebida
from Postre import Postre 

platillo = Comida ("pozole",100.00,"Plato Fuerte")
platillo.mostrarInformacion()

Soda = Bebida ("Coca-cola",40.00,"Fria")
Soda.mostrarInformacion()

postre = Postre ("Flan Napolitano",80.00,"False")
postre.mostrarInformacion()
postre.tipo()