"""Ejemplo de función de orden superior que transforma una lista de números
utilizando una función de regla proporcionada."""

from typing import Callable, List


def transformar_numeros(
    numeros: List[int], funcion_regla: Callable[[int], int]
) -> List[int]:
    """Aplica una regla (función) a cada elemento de una lista.

    Args:
        numeros (List[int]): Lista de números a transformar.
        funcion_regla (Callable[[int], int]): Función que define la regla de transformación.

    Returns:
        List[int]: Lista de números transformados.
    """    
    return [funcion_regla(n) for n in numeros]


# Defe funciones simples o use lambdas
def al_cuadrado(x: int) -> int:
    """Calcula el cuadrado de un número.

    Args:
        x (int): Número a elevar al cuadrado.

    Returns:
        int: Cuadrado del número.
    """    
    return x**2


numeros = [1, 2, 3, 4]
resultados = transformar_numeros(numeros, al_cuadrado)
print(resultados)  # Salida: [1, 4, 9, 16]
