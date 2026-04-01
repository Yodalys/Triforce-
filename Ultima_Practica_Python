# Función para calcular promedio (uso de def + operaciones + len)
def calcular_promedio(notas):
    return sum(notas) / len(notas)
# Tupla (no cambia)
grados_validos = ("10A", "10B", "11A", "11B")
# Lista de estudiantes
estudiantes = []
# Contador
i = 0
# WHILE → pedir datos de 5 estudiantes
while i < 5:
    print(f"\n--- Estudiante {i + 1} ---")
    # Entrada de usuario
    nombre = input("Ingrese el nombre: ")
    # Lista de notas
    notas = []
    # FOR + range → pedir 3 notas
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1}: "))
        notas.append(nota)  # append
    # Calcular promedio (función)
    promedio = calcular_promedio(notas)
    # Conversión de tipo
    grado = input("Ingrese el grado (10A, 10B, 11A, 11B): ")
    # Condicional
    if grado not in grados_validos:
        print("Grado no válido, se asignará 10A")
        grado = "10A"
    # Diccionario
    estudiante = {
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio,
        "grado": grado
    }
    # Agregar a la lista
    estudiantes.append(estudiante)
    i += 1  # aumento
# Ordenar estudiantes por promedio (sort)
estudiantes.sort(key=lambda x: x["promedio"], reverse=True)
print("\n===== RESULTADOS =====")
# FOR → recorrer estudiantes
for est in estudiantes:
    # Condicionales
    if est["promedio"] >= 4.0:
        estado = "Aprueba"
    elif est["promedio"] >= 3.0:
        estado = "Recuperación"
    else:
        estado = "Reprueba (se queda de año)"
    # Mostrar usando f-strings + items()
    print("\n--- Información del estudiante ---")
    for clave, valor in est.items():
        print(f"{clave}: {valor}")
    print(f"Estado final: {estado}")
