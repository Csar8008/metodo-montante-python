DIGITOS = "0123456789"
SUBDIGITOS = "₀₁₂₃₄₅₆₇₈₉"
MAPA_SUB = str.maketrans(DIGITOS, SUBDIGITOS)


def a_subindice(num: int):
    return str(num).translate(MAPA_SUB)


def mostrar_sistema(matriz: list[list[float]], ingresadas: list[bool]):
    n = len(matriz)
    print("\n--- Sistema de Ecuaciones ---")

    for i in range(n):
        print(f"{i + 1}. ", end="")

        if not ingresadas[i]:
            print("__ " * (n + 1))
            continue

        terminos = []
        for j in range(n):
            coeficiente = matriz[i][j]
            var = f"x{a_subindice(j + 1)}"

            if j == 0:
                terminos.append(f"{coeficiente:g}{var}")
            else:
                signo = "+" if coeficiente >= 0 else "-"
                terminos.append(f"{signo} {abs(coeficiente):g}{var}")

        ecuacion_str = " ".join(terminos)
        print(f"{ecuacion_str} = {matriz[i][n]:g}")
    print()