# Configuración electrónica automática a partir del número atómico Z

# Lista de subniveles en orden de llenado (regla de Aufbau)
subniveles = [
    "1s", "2s", "2p", "3s", "3p",
    "4s", "3d", "4p", "5s", "4d",
    "5p", "6s", "4f", "5d", "6p",
    "7s", "5f", "6d", "7p"
]

# Capacidad máxima por tipo de subnivel
capacidad_subnivel = {
    "s": 2,
    "p": 6,
    "d": 10,
    "f": 14
}

def configuracion_electronica(Z):
    """
    Devuelve la configuración electrónica para un número atómico Z.
    """
    e_restantes = Z
    configuracion = []

    for sub in subniveles:
        # Tipo de subnivel: s, p, d o f (último carácter de la cadena)
        tipo = sub[-1]
        capacidad = capacidad_subnivel[tipo]

        if e_restantes <= 0:
            break

        ocupados = min(capacidad, e_restantes)
        configuracion.append(f"{sub}{ocupados}")
        e_restantes -= ocupados

    return " ".join(configuracion)

# Ejemplo: Níquel, Z = 28
if __name__ == "__main__":
    Z = 28
    print(f"Z = {Z} →", configuracion_electronica(Z))
