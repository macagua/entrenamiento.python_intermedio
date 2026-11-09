"""Ejemplo de uso de funciones de predicado en Python."""

from typing import TypeVar
from collections.abc import Callable

# Define la variable de tipo genérico
T = TypeVar("T")

# Un predicado que recibe un valor de tipo T y devuelve un booleano
PredicadoT = Callable[[T], bool]


# Función que utiliza el predicado
def filtrar_elementos(elementos: list[T], predicado: PredicadoT) -> list[T]:
    return [e for e in elementos if predicado(e)]


# Definición de un predicado simple (función que devuelve True o False)
def es_par(n: int) -> bool:
    return n % 2 == 0


# Define una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Invoca la función e imprime el resultado
resultado = filtrar_elementos(numeros, es_par)
print(resultado)  # Salida esperada: [2, 4, 6, 8]

# También funciona con otros tipos de datos (gracias al TypeVar T)
palabras = ["gato", "elefante", "sol", "murciélago"]
es_larga = lambda s: len(s) > 4  # noqa: E731

resultado_palabras = filtrar_elementos(palabras, es_larga)
print(resultado_palabras)  # Salida esperada: ['elefante', 'murciélago']
