# --- Definición de excepciones personalizadas ---

class EdadInvalidaError(Exception):
    def __init__(self, edad):
        super().__init__(f"Edad inválida: {edad}. Debe estar entre 18 y 35.")
        self.edad = edad

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente. Tienes ${saldo}, necesitas ${monto}.")
        self.saldo = saldo
        self.monto = monto

# --- Funciones que usan raise ---

def registrar_edad(edad):
    if not (18 <= edad <= 35):
        raise EdadInvalidaError(edad)
    return f"Edad {edad} registrada correctamente."

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto

# --- Programa principal ---

try:
    print(registrar_edad(200))   # esto lanzará EdadInvalidaError

except EdadInvalidaError as e:
    print(f"❌ {e}")

try:
    nuevo_saldo = retirar(500, 800)  # esto lanzará SaldoInsuficienteError
    print(f"✅ Nuevo saldo: ${nuevo_saldo}")

except SaldoInsuficienteError as e:
    print(f"❌ {e}")
    print(f"   Faltan ${e.monto - e.saldo} para completar el retiro.")