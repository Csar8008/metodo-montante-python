import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pedir_entero(mensaje: str, min_val: int | None = None, max_val: int | None = None):
    while True:
        try:
            val = int(input(mensaje))
            if min_val is not None and val < min_val:
                print(f" Error: El numero debe ser mayor o igual a {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f" Error: El numero debe ser menor o igual a {max_val}.")
                continue
            return val
        except ValueError:
            print(" Error: Ingrese un numero entero valido.")


def pedir_flotante(mensaje: str):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" Error: Ingrese un número numerico valido.")