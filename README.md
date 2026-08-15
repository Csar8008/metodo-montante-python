# Método de Montante en Python

Implementación en Python del **método de Montante** para resolver sistemas de ecuaciones lineales.

El proyecto busca implementar el algoritmo de Montante de forma programática, separando la lógica matemática de la interacción con el usuario y utilizando pruebas para verificar el funcionamiento del algoritmo.

## Descripción

El método de Montante es un procedimiento utilizado para resolver sistemas de ecuaciones lineales mediante operaciones matriciales.

El programa permite ingresar un sistema de ecuaciones y obtener sus soluciones utilizando una matriz aumentada.

Actualmente, el proyecto está enfocado en sistemas de ecuaciones lineales de tamaño `n × n`.

## Objetivos

- Implementar el método de Montante en Python.
- Resolver sistemas de ecuaciones lineales mediante operaciones matriciales.
- Separar la lógica del algoritmo de la interfaz del programa.
- Validar los datos ingresados por el usuario.
- Documentar el funcionamiento del proyecto.

## Tecnologías utilizadas

- **Python 3**
- **Git**
- **GitHub**

## Estructura del proyecto

```text
metodo-montante-python/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── main.py
│
└── docs/
    
```

## Instalación (temporal)

Clonar el repositorio:

```bash
git clone https://github.com/Csar8008/metodo-montante-python.git
```

Entrar en la carpeta del proyecto:

```bash
cd metodo-montante-python
```

## Uso

Para ejecutar el programa:

```bash
python src/main.py
```

El programa solicitará el tamaño del sistema y posteriormente los coeficientes de cada ecuación.

Por ejemplo, para el sistema:

[\
\begin{cases}\
3x\_1 + 6x\_2 - x\_3 = 25 \\\
7x\_1 - x\_2 + 2x\_3 = 9 \\\
-2x\_1 - x\_2 - x\_3 = -6\
\end{cases}\
]

se debe introducir una matriz aumentada equivalente a:

```text
[ 3   6  -1 | 25 ]
[ 7  -1   2 |  9 ]
[-2  -1  -1 | -6 ]
```

El programa procesa la matriz mediante el método de Montante y muestra las soluciones obtenidas.


## Método de Montante

El algoritmo trabaja sobre una **matriz aumentada** del sistema.

Para cada iteración se selecciona un elemento de la diagonal principal como pivote. Las operaciones se realizan utilizando el pivote actual y el pivote de la iteración anterior.

La operación general utilizada para actualizar los elementos de la matriz es:

a\_{ik}^{(k)}a\_{kj}^{(k)}\
}{\
a\_{k-1,k-1}^{(k-1)}\
}\
]

donde:

- (a\_{kk}) es el pivote actual.
- (a\_{k-1,k-1}) corresponde al pivote anterior.
- (a\_{ij}) representa el elemento que se está actualizando.

El primer pivote anterior se considera igual a `1`.


## Estado del proyecto

- [x] Implementación inicial del método de Montante.
- [x] Entrada de sistemas mediante consola.
- [x] Construcción de la matriz aumentada.
- [ ] Manejo de pivotes nulos.
- [ ] Detección de sistemas sin solución.
- [ ] Detección de sistemas con infinitas soluciones.
- [ ] Mostrar el procedimiento de Montante paso a paso.
- [ ] Implementación completa de pruebas automáticas.
- [ ] Documentación final.

## Autores

