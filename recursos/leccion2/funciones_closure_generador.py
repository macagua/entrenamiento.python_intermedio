"""Generador de contadores independientes."""

from typing import Callable


def crear_contador(inicio: int = 0) -> Callable[[], int]:
    """Crea una función contador que recuerda su propio estado.

    Args:
        inicio (int, optional): El valor inicial del contador. Por defecto es 0.

    Returns:
        Callable[[], int]: Una función que incrementa y devuelve el valor del contador.
    """    
    # Variable en el ámbito envolvente (enclosing scope)
    contador = inicio

    def incrementar() -> int:
        nonlocal contador  # Permite modificar la variable del ámbito superior
        contador += 1
        return contador

    # Devolve el objeto de función (aún sin ejecutar)
    return incrementar


# Crea dos contadores independientes
contador_a = crear_contador(10)
contador_b = crear_contador(0)

# Cada closure mantiene su propio estado aislado
print(contador_a())  # Salida: 11
print(contador_a())  # Salida: 12

print(contador_b())  # Salida: 1: (empieza desde 0)
print(contador_a())  # Salida: 13 (contador_a no se ve afectado por b)
