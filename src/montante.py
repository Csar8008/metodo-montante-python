from copy import deepcopy
from os import system
from os import name

digitos = "0123456789"
subdigitos = "₀₁₂₃₄₅₆₇₈₉"
mapa_sub = str.maketrans(digitos, subdigitos)


def montante(matriz: list[list[float]], size: int):
    matriz_anterior = deepcopy(matriz)
    matriz_actual = deepcopy(matriz)

    resultados: list[float] = []

    pivote_anterior = 1
    pivote_actual = 1

    for iteracion in range(size):
        pivote_actual = matriz_anterior[iteracion][iteracion]
        for i in range(size):
            if i == iteracion:
                continue
            for j in range(size + 1):
                if j <= iteracion:
                    if j == i:
                        matriz_actual[i][j] = pivote_actual
                    else:
                        matriz_actual[i][j] = 0
                else:
                    matriz_actual[i][j] = (
                        (matriz_anterior[iteracion][iteracion] * matriz_anterior[i][j])
                        - (
                            matriz_anterior[iteracion][j]
                            * matriz_anterior[i][iteracion]
                        )
                    ) / pivote_anterior

        matriz_anterior = deepcopy(matriz_actual)
        pivote_anterior = pivote_actual

    for i in range(size):
        resultados.append((float)(matriz_actual[i][size] / pivote_actual))

    return resultados


system("cls" if name == "nt" else "clear")

while True:
    try:
        print("--- METODO MONTANTE ---")
        size = int(input("\nIngrese el tamaño del sistema por solucionar: "))
        if size <= 1:
            raise ValueError
        break
    except ValueError:
        _ = input(
            "Error validando el dato, favor de ingresar un tamaño entero valido (Mayor a 1).\nPresione enter para continuar."
        )
        system("cls" if name == "nt" else "clear")

ecuacion_indice: int = size
ecuacion_ingresada: list[bool] = [False] * size

matriz: list[list[float]] = [[0.0 for _ in range(size + 1)] for _ in range(size)]

while ecuacion_indice != 0 or False in ecuacion_ingresada:
    system("cls" if name == "nt" else "clear")
    print("Sistema de ecuaciones:\n")

    for i in range(size):
        print(f"{i + 1}. ", end="")
        for j in range(size + 1):
            if ecuacion_ingresada[i] == False:
                print("__ ", end="")
            elif j == 0:
                print(f"{matriz[i][j]:g}x{(str(j+1)).translate(mapa_sub)} ", end="")
            elif j < size:
                print(
                    f"{abs(matriz[i][j]):g}x{(str(j+1)).translate(mapa_sub)} ", end=""
                )
            else:
                print(f"{matriz[i][j]:g}", end="")

            if j < size:
                if j == size - 1:
                    print("= ", end="")
                elif matriz[i][j] < 0.0:
                    print("- ", end="")
                else:
                    print("+ ", end="")
        print("")

    while True:
        try:
            ecuacion_indice = int(
                input(
                    "\nIngrese el numero de ecuacion por modificar, ingrese 0 para resolver el sistema: "
                )
            )
            if ecuacion_indice < 0 or ecuacion_indice > size:
                raise ValueError
            if ecuacion_indice == 0 and False in ecuacion_ingresada:
                raise IndexError
            break
        except ValueError:
            print("Error validando el indice, favor de ingresar uno valido o 0")
        except IndexError:
            print(
                "El sistema aun no esta completo, llene primero todo el sistema para poder solucionarlo"
            )

    print("")

    if ecuacion_indice == 0 and False not in ecuacion_ingresada:
        resultados = montante(matriz, size)
        print(resultados)
        break

    for i in range(size + 1):
        while True:
            try:
                if i != size:
                    print(
                        f"Ingrese el termino de la variable x{(str(i+1)).translate(mapa_sub)}: ",
                        end="",
                    )
                else:
                    print("Ingrese el resultado de la ecuacion: ", end="")
                matriz[ecuacion_indice - 1][i] = float(input())
                break
            except ValueError:
                print("Error validando el dato, favor de ingresar un numero valido")

    ecuacion_ingresada[ecuacion_indice - 1] = True
