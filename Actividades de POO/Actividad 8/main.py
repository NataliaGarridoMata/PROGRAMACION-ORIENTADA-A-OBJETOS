from Jugador import Jugador 
from Competidor import Competidor 
from Observador import Observador 

def main():
    jugador1 = Jugador("Juan", "12345", "Principiante", 100)
    competidor1 = Competidor("Ana", "54321", "Avanzado", 200, "Equipo A")
    observador1 = Observador("Carlos", "67890", "Intermedio", 150, 5)
    
    jugador1.mostrar_perfil()
    print("\n")
    competidor1.mostrar_perfil()
    print("\n")
    observador1.mostrar_perfil()

if __name__ == "__main__":
    main()
    
