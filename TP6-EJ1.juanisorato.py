def evaluar_alumnos(apellidos, nota1, nota2, nota3, resultados):
    print("\nListado de alumnos y su condición:")
    for i in range(len(apellidos)):
        promedio = (nota1[i] + nota2[i] + nota3[i]) / 3
        if promedio >= 60:
            estado = "Aprobado"
        else:
            estado = "Desaprobado"
        resultados.append(estado)
        print(f"{apellidos[i]} - {estado}")

# --- Carga de datos ---
apellidos = []
notas_parcial1 = []
notas_parcial2 = []
notas_parcial3 = []
resultados_finales = []

N = int(input("¿Cuántos alumnos vas a ingresar? "))
contador = 0

while contador < N:
    apellido = input(f"Ingrese el apellido del alumno #{contador + 1}: ")
    apellidos.append(apellido)

    # Ingresar notas y validar que estén entre 0 y 100
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i} del alumno {apellido} (0-100): "))
                if 0 <= nota <= 100:
                    break
                else:
                    print("❌ Error: La nota debe estar entre 0 y 100.")
            except ValueError:
                print("❌ Error: Debes ingresar un número válido.")

        if i == 1:
            notas_parcial1.append(nota)
        elif i == 2:
            notas_parcial2.append(nota)
        else:
            notas_parcial3.append(nota)

    contador += 1

# --- Procesar los datos y mostrar resultados ---
evaluar_alumnos(apellidos, notas_parcial1, notas_parcial2, notas_parcial3, resultados_finales)

# --- (Opcional) Mostrar arreglo final de resultados ---
print("\nResultados guardados:", resultados_finales)
