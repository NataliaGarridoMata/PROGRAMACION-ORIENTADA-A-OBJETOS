from Herramientas import Herramientas 
from Pico import Pico 
from Espada import Espada 
from Pala import Pala

if __name__ == "__main__":
    herramientas = [
        Pico("diamante", 5),
        Espada("hierro", 3),
        Pala("madera", 2),
    ]
    
print("--- INICIANDO PRUEBA DE HERRAMIENTAS CON ZIP() ---\n")

for herramienta in herramientas:
    herramienta.estado()  # Muestra el estado inicial de la herramienta 
    print(herramienta.usar("bloque de piedra"))  # Usa la herramienta en un objetivo
    herramienta.estado()  # Muestra el estado después de usarla 
    print()  # Línea en blanco para separar cada herramienta
    