###
## Excepciones Basicas 

# Parte 1:try / except somple 
print("="* 50)
print("PARTE 1: division con manejo de errores")
print("=" * 50)

try:
     a = int(input("Ingrso del Numerador"))
     b = int(input("Ingresa el Denominador"))
     total = a / b 
     
except ValueError:
    print("Error: solo NÚMEROS, no otros símbolos")
      
except ZeroDivisionError: 
    print("Error: No se puede dividir por cero")
     
    
else:
    print(f"El resultado de {a} / {b} es: {total}")
    
finally:
    print("¡Gracias por usar el programa de división!")
    