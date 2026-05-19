import os
ruta ="test.txt"
#regresa el tamaño en Bites
Size = os.path.getSize(ruta)
KB = Size/1024
MB =Size/(1024**2)

print(f"tamaño:{KB:.2f}")
print(f"Tamaño:{MG:.4F}")