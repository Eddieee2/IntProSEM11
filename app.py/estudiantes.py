#!/usr/bin/env python3
"""
Programa para almacenar datos de un estudiante ingresados por el usuario.
Campos: Nombres, Apellidos, Carrera, Año, Promedio
"""

def input_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Este campo no puede estar vacío. Intente de nuevo.")

def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Por favor ingrese un número entre {min_val} y {max_val}.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

def input_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt).strip())
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Por favor ingrese un número entre {min_val} y {max_val}.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número decimal.")

def main():
    print("\nIngrese los datos del estudiante:\n" + "-"*30)
    nombres = input_string("Nombres: ")
    apellidos = input_string("Apellidos: ")
    carrera = input_string("Carrera: ")
    ano = input_int("Año (1 - 10): ", 1, 10)
    promedio = input_float("Promedio (0.0 - 20.0): ", 0.0, 20.0)

    estudiante = {
        "Nombres": nombres,
        "Apellidos": apellidos,
        "Carrera": carrera,
        "Año": ano,
        "Promedio": promedio
    }

    print("\nDatos del estudiante almacenados:\n" + "-"*30)
    for clave, valor in estudiante.items():
        print(f"{clave:10}: {valor}")

if __name__ == "__main__":
    main()

