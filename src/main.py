from interfaz import a_subindice, mostrar_resultados, mostrar_sistema
from montante import MontanteError, resolver_montante
from validaciones import limpiar_pantalla, pedir_entero, pedir_flotante


def ejecutar():
    while True:

        limpiar_pantalla()

        print("==========================================")
        print("      SOLUCIÓN POR MÉTODO DE MONTANTE     ")
        print("==========================================")

        n = pedir_entero(
            "\nIngrese el tamaño del sistema de N x N: ",
            min_val=2
        )

        matriz = [[0.0] * (n + 1) for _ in range(n)]
        ingresadas = [False] * n

        while True:
            limpiar_pantalla()
            mostrar_sistema(matriz, ingresadas)

            todas_completas = True

            for i in range(n):
                if not ingresadas[i]:
                    todas_completas = False
                    break

            print("Opciones:")
            print(f"-presione de 1 a {n} para Modificar una ecuacion")

            if todas_completas:
                print("-presiona 0 Resolver el sistema")

            opcion = pedir_entero(
                "\nSeleccione una opcion: ",
                min_val=0,
                max_val=n
            )

            if opcion == 0:

                if not todas_completas:
                    print(
                        "\nDebe ingresar todas las ecuaciones antes de resolver."
                    )
                    input("Presione Enter para continuar...")
                    continue

                confirmar = input(
                    "\n¿Desea resolver el sistema? (s/n): "
                ).lower()

                if confirmar == "s":
                    break

                continue

            idx = opcion - 1

            limpiar_pantalla()

            print("------------------------------------------")
            print(f"      MODIFICANDO ECUACIÓN {opcion}")
            print("------------------------------------------")

            for j in range(n):
                var_sub = a_subindice(j + 1)

                matriz[idx][j] = pedir_flotante(
                    f" Coeficiente para x{var_sub}: "
                )

            matriz[idx][n] = pedir_flotante(
                " Término independiente (=): "
            )

            ingresadas[idx] = True

            print("\nEcuacion guardada correctamente.")
            input("Presione Enter para continuar...")

        limpiar_pantalla()

        print("==========================================")
        print("           SISTEMA INGRESADO              ")
        print("==========================================")

        mostrar_sistema(matriz, ingresadas)

        try:

            resultados = resolver_montante(matriz, n)
            mostrar_resultados(resultados, n)

        except MontanteError as err:

            print("\n==========================================")
            print("                  ERROR                   ")
            print("==========================================")
            print(f"\n{err}")

        while True:

            otra = input(
                "\n¿Desea resolver otro sistema? (s/n): "
            ).lower()

            if otra == "s":
                break

            if otra == "n":
                print("\nsaliendo....")
                return

            print("Opcion no válida. Escriba 's' o 'n'.")


if __name__ == "__main__":
    ejecutar()
