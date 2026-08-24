from copy import deepcopy


class MontanteError(Exception):
    pass


def resolver_montante(matriz: list[list[float]], size: int) -> list[float]:
    matriz_anterior = deepcopy(matriz)
    matriz_actual = deepcopy(matriz)

    resultados: list[float] = []
    pivote_anterior = 1
    pivote_actual = 1

    if len(matriz) != size:
        raise MontanteError("El tamaño indicado no coincide con la matriz.")

    for i in range(size):
        if len(matriz[i]) != size + 1:
            raise MontanteError("La matriz debe tener size + 1 columnas.")

    for iteracion in range(size):
        if matriz_anterior[iteracion][iteracion] == 0:
            fila_pivote = -1

            for i in range(iteracion + 1, size):
                if matriz_anterior[i][iteracion] != 0:
                    fila_pivote = i
                    break

            if fila_pivote == -1:
                raise MontanteError("El sistema no tiene una solución unica.")

            matriz_anterior[iteracion], matriz_anterior[fila_pivote] = (
                matriz_anterior[fila_pivote],
                matriz_anterior[iteracion],
            )
        pivote_actual = matriz_anterior[iteracion][iteracion]

        for j in range(size + 1):
            matriz_actual[iteracion][j] = matriz_anterior[iteracion][j]

        for i in range(size):
            if i == iteracion:
                continue

            for j in range(size + 1):
                if j == iteracion :
                    matriz_actual[i][j] = 0
                else:
                    matriz_actual[i][j] = (
                        (matriz_anterior[iteracion][iteracion] * matriz_anterior[i][j])
                        - (matriz_anterior[iteracion][j] * matriz_anterior[i][iteracion])
                    ) / pivote_anterior

        matriz_anterior = deepcopy(matriz_actual)
        pivote_anterior = pivote_actual

    if pivote_actual == 0:
        raise MontanteError("El sistema no tiene una solucion unica.")

    for i in range(size):
        resultados.append(float(matriz_actual[i][size] / pivote_actual))

    return resultados