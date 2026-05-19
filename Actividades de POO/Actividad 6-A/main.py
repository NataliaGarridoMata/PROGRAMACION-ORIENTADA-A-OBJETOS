# Importamos cada clase desde su respectivo archivo
from Mob import Mob
from Vaca import Vaca
from Creeper import Creeper
from Enderman import Enderman
from Zombie import Zombie

def ejecutar_laboratorio():
    print("---BIENVENIDO AL SIMULADOR DE MOBS ---")
    
    # 1. TAREA 2: Intento de instanciar la clase abstracta
    try:
        print("\nIntentando crear un Mob genérico...")
        test_mob = Mob("Test", 10)
    except TypeError as e:
        print(f" ERROR ESPERADO: {e}")
        print("> Observación: No se puede instanciar Mob porque es una clase abstracta.")

    # 2. TAREA 1: Crear la lista de Mobs reales
    mobs = [ 
        Vaca("clara", 10),
        Creeper("Explosi", 20),
        Enderman("Enderman", 40),
        Zombie("Eddy", 50)
    ]

    print("\n--- REPORTE DE MOBS EN EL OVERWORLD ---")
    for mob in mobs:
        mob.presentarse()

if __name__ == "__main__":
    ejecutar_laboratorio()
