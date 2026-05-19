###
## Excepciones Basicas 

# Parte 1:try / except somple 
print("="* 50)
print("PARTE 1: division con manejo de errores")
print("=" * 50)

# Creamos una lista de colores 
colores = ["rojo","verde","azul","amarillo"]
print(F"Lista de colores: {colores} (inidces 0,1,2,3)")

try:
    indice = (input(" Que color quieres acceder? (0-3):"))

except ValueError as e:
    print(f" ValueError: {e}")
    
except IndexError as e:
    print(f" IndexError: {e}")
    print(f"Solo puedes usar los números 0 la 3 para acceder a los colores")
    
finally:
    print("--Fin del Programa")