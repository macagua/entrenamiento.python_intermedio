"""Ejemplo de Objetos llamables"""

class Multiplicador:
    """Clase Multiplicador"""

    def __init__(self, factor: int):
        self.factor = factor  # Estado interno

    def __call__(self, numero: int) -> int:
        # Permite que la instancia se comporte como una función
        return numero * self.factor


# Creamos una instancia configurada
duplicador = Multiplicador(2)
triplicador = Multiplicador(3)

# Invocamos la instancia directamente como si fuera una función
print(duplicador(10))  # Salida: 20
print(triplicador(10))  # Salida: 30

# Podemos verificar si es un objeto llamable
print(callable(duplicador))  # Salida: True
