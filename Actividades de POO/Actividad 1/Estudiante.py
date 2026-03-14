# Esta es la clase
class Estudiante:
    #aquí va el constructor
    def __init__(self,nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    #  calificaciones
    def setCalificaciones(self, calificacion):
        self.calificaciones.append(calificacion)

    def getNombre(self):
        return self.nombre

    #  calcular el promedio de calif.
    def mostrarPromedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    # mostrar información del usuario
    def mostrarInformacionUsuario(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}"
    




# Crear los objetos (instancias) de la clase
estudiante1 = Estudiante("Pako",30,"Ing. en sistemas")
estudiante2 = Estudiante("Carmen",25,"Ing. en Industrial")
estudiante3 = Estudiante("Ramón",20,"Ing. en Electrónica")

print(estudiante1.mostrarInformacionUsuario())

estudiante1.setCalificaciones(100)
estudiante1.setCalificaciones(50)
estudiante1.setCalificaciones(40)

print(f"La calificación del {estudiante1.getNombre()} es: {estudiante1.mostrarPromedio()}")
print(f"La calificación es: {estudiante2.getNombre()} es: {estudiante2.mostrarPromedio()}")