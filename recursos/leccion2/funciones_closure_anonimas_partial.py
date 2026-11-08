"""Función que calcula la potencia de un número dado un exponente."""

from functools import partial


def potencia(base: int, exponente: int) -> int:
    """Función que calcula la potencia de un número dado un exponente.

    Args:
        base (int): Número base que se va a elevar.
        exponente (int): Exponente para la operación de elevar.

    Returns:
        int: Resultado de elevar la base al exponente.
    """
    return base**exponente


# Cree una nueva función especializada donde el exponente ya está fijo en 2 (al cuadrado)
cuadrado = partial(potencia, exponente=2)

print(cuadrado(5))  # Salida: 25 (equivalente a potencia(5, 2))
