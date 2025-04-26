referencia = "ATGCTAGCTAAT"

# Función para detectar mutaciones
def detectar_mutaciones(ref, muestra):
    mutaciones = []
    for i, (r, m) in enumerate(zip(ref, muestra)):
        if r != m:
            mutaciones.append(i)
    return mutaciones

# Leer las secuencias desde el archivo
ruta_archivo = "datos_sensor.txt"  

with open(ruta_archivo, "r") as archivo:
    secuencias_sensor = archivo.read().splitlines()

# Comparar cada secuencia con la referencia
for idx, secuencia in enumerate(secuencias_sensor):
    mutaciones = detectar_mutaciones(referencia, secuencia)
    print(f"Secuencia {idx + 1}: {secuencia}")
    if mutaciones:
        print(f"  → Mutaciones detectadas en posiciones: {mutaciones}")
    else:
        print("  → No se detectaron mutaciones.")