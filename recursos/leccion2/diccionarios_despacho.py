"""Ejemplo de funciones como Diccionarios de despacho."""


def sumar(a: int, b: int) -> int:
    return a + b


def restar(a: int, b: int) -> int:
    return a - b


def multiplicar(a: int, b: int) -> int:
    return a * b


# Diccionario que mapea strings a objetos de función
operaciones = {"sumar": sumar, "restar": restar, "multiplicar": multiplicar}

accion = "multiplicar"
resultado = operaciones[accion](10, 5)
print(resultado)  # Salida: 50
