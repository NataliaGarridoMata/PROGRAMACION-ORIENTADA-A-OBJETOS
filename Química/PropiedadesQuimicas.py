  # ───────────────────────────────────────────────
# Constantes físicas
# ───────────────────────────────────────────────
C = 2.998e8          # Velocidad de la luz (m/s)
H = 6.626e-34        # Constante de Planck (J·s)
EV_PER_JOULE = 1 / 1.602e-19   # Conversión J → eV


# ───────────────────────────────────────────────
# Función principal
# ───────────────────────────────────────────────
def calcular_onda(lambda_nm):

    # Conversión a metros
    lambda_m = lambda_nm * 1e-9

    # 1. Frecuencia ν = c / λ
    frecuencia = C / lambda_m

    # 2. Energía en Joules E = h·ν
    energia_j = H * frecuencia

    # 3. Energía en eV
    energia_ev = energia_j * EV_PER_JOULE

    # 4. Región espectral
    if lambda_nm < 0.01:
        region = "Rayos Gamma"
    elif lambda_nm < 10:
        region = "Rayos X"
    elif lambda_nm < 380:
        region = "Ultravioleta"
    elif lambda_nm <= 750:
        region = "Visible"
    elif lambda_nm <= 1_000_000:
        region = "Infrarrojo"
    elif lambda_nm <= 100_000_000:
        region = "Microondas"
    else:
        region = "Radio"

    # 5. Color visible
    color = None
    if region == "Visible":
        if lambda_nm < 450:
            color = "Violeta"
        elif lambda_nm < 495:
            color = "Azul"
        elif lambda_nm < 570:
            color = "Verde"
        elif lambda_nm < 590:
            color = "Amarillo"
        elif lambda_nm < 625:
            color = "Naranja"
        else:
            color = "Rojo"

    # Imprimir resultados
    separador = "─" * 50
    print(f"\n{separador}")
    print(f"  Resultados para λ = {lambda_nm} nm")
    print(separador)
    print(f"  1. Frecuencia      ν = {frecuencia:.4e} Hz")
    print(f"  2. Energía           = {energia_j:.4e} J")
    print(f"  3. Energía           = {energia_ev:.4f} eV")
    print(f"  4. Región espectral  = {region}")
    if color:
        print(f"  5. Color visible     = {color}")
    print(separador)


# ───────────────────────────────────────────────
# Bucle principal
# ───────────────────────────────────────────────
print("=" * 50)
print("  CALCULADORA DE ONDAS ELECTROMAGNÉTICAS")
print("=" * 50)

while True:

    entrada = input("\nIngresa λ (nm)  |  '0' para salir: ").strip()

    if entrada == "0":
        print("\n  Hasta luego\n")
        break

    try:
        lambda_nm = float(entrada)
        if lambda_nm <= 0:
            print("El valor debe ser positivo. Intenta de nuevo.")
            continue

        calcular_onda(lambda_nm)

    except ValueError:
        print