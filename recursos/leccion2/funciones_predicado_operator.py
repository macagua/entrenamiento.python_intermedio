"""Ejemplo de uso de la librería operator para crear predicados de comparación."""

import operator
from functools import partial

# operator.lt funciona como un predicado de comparación (less than)
# Equivalente a: lambda a, b: a < b
numeros = [5, 12, 3, 9, 20]

# Filtrar números menores que 10 usando operator.lt mediante partial
menores_a_diez = list(filter(partial(operator.gt, 10), numeros))

# Equivalente a buscar x donde 10 > x (es decir, x < 10)
print(menores_a_diez)  # Salida: [5, 3, 9]
