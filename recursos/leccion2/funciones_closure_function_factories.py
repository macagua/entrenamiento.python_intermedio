"""Fábrica de funciones para crear funciones multiplicadoras."""


def creador_multiplicador(factor: int):
    """Crea una función que multiplica por un factor dado.

    Args:
        factor (int): El factor por el cual multiplicar.

    Returns:
        function: Una función que toma un número y lo multiplica por el factor.
    """

    # 'factor' queda atrapado en el closure
    def multiplicar(numero: int) -> int:
        return numero * factor

    return multiplicar


por_dos = creador_multiplicador(2)
por_diez = creador_multiplicador(10)

print(por_dos(5))  # Salida: 10
print(por_diez(5))  # Salida: 50
