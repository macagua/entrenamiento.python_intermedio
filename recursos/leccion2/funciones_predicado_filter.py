"""Ejemplo de uso de predicados con filter() y comprensiones de listas."""

from typing import List


# Definición de un predicado simple
def es_par(numero: int) -> bool:
    """Predicado que devuelve True si el número es par."""
    return numero % 2 == 0


# Define una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Usando el predicado con filter() (devuelve un iterador)
pares = list(filter(es_par, numeros))
print(pares)  # Salida: [2, 4, 6, 8]

# Usando el predicado en una comprensión de lista (más idiomático en Python)
pares_comprension = [n for n in numeros if es_par(n)]
print(pares_comprension)  # Salida: [2, 4, 6, 8]
