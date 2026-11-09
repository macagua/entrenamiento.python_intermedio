"""Ejemplo de combinación de predicados usando funciones de utilidad."""

from typing import Any
from collections.abc import Callable


def combinar_y(*predicados: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """Combina múltiples predicados con un operador lógico AND."""

    def predicado_combinado(valor) -> bool:
        return all(p(valor) for p in predicados)

    return predicado_combinado


# Define predicados individuales
es_positivo = lambda x: x > 0  # noqa: E731
es_menor_que_cien = lambda x: x < 100  # noqa: E731
es_par = lambda x: x % 2 == 0  # noqa: E731

# Cree un super-predicado combinando los anteriores
es_numero_valido = combinar_y(es_positivo, es_menor_que_cien, es_par)

print(es_numero_valido(50))  # Salida: True (es positivo, < 100 y par)
print(es_numero_valido(105))  # Salida: False (falla la condición < 100)
print(es_numero_valido(-4))  # Salida: False (falla la condición positivo)
