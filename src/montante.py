from copy import deepcopy


class MontanteError(Exception):
    pass

def expandir_matriz(matriz: list[list[float]], size: int):
    matriz_ampliada = []
    for i in range(size):
        coeficientes = matriz[i][:size]
        identidad = [1.0 if i == j else 0.0 for j in range(size)]
        termino_indep = [matriz[i][size]]
        matriz_ampliada.append(coeficientes + identidad + termino_indep)
    return matriz_ampliada


def obtener_resultados(matriz_actual: list[list[float]], size: int, pivote_actual: float):
    adjunta = [matriz_actual[i][size : 2 * size] for i in range(size)]
    inversa = [[elem / pivote_actual for elem in fila] for fila in adjunta]
    soluciones = [float(matriz_actual[i][2 * size] / pivote_actual) for i in range(size)]

    return {
        "soluciones": soluciones,
        "determinante": pivote_actual,
        "adjunta": adjunta,
        "inversa": inversa,
    }


def resolver_montante(matriz: list[list[float]], size: int):
    if len(matriz) != size:
        raise MontanteError("El tamaño indicado no coincide con la matriz.")

    for i in range(size):
        if len(matriz[i]) != size + 1:
            raise MontanteError("La matriz debe tener size + 1 columnas.")

    matriz_expandida = expandir_matriz(matriz, size)
    columnas_totales = 2 * size + 1

    matriz_anterior = deepcopy(matriz_expandida)
    matriz_actual = deepcopy(matriz_expandida)

    pivote_anterior = 1
    pivote_actual = 1

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
            matriz_actual[iteracion], matriz_actual[fila_pivote] = (
                matriz_actual[fila_pivote],
                matriz_actual[iteracion],
            )

        pivote_actual = matriz_anterior[iteracion][iteracion]

        for j in range(columnas_totales):
            matriz_actual[iteracion][j] = matriz_anterior[iteracion][j]

        for i in range(size):
            if i == iteracion:
                continue

            for j in range(columnas_totales):
                if j == iteracion:
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

    return obtener_resultados(matriz_actual, size, pivote_actual)