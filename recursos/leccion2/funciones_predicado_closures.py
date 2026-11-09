"""Ejemplo de funciones predicado y closures en Python."""

from collections.abc import Callable


def crear_validador_longitud(min_chars: int) -> Callable[[str], bool]:
    """Fábrica que genera un predicado para validar longitud de cadenas."""

    def validar(texto: str) -> bool:
        return len(texto) >= min_chars

    return validar


# Cree predicados específicos
es_password_valido = crear_validador_longitud(8)
es_username_valido = crear_validador_longitud(4)

print(es_password_valido("abc"))  # Salida: False
print(es_password_valido("secreto123"))  # Salida: True
print(es_username_valido("mac"))  # Salida: False
print(es_username_valido("macagua"))  # Salida: True
