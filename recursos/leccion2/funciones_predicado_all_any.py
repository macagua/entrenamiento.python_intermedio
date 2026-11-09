"""Ejemplo de uso de predicados con all() y any()."""

usuarios = [
    {"nombre": "Ana", "activo": True, "edad": 38},
    {"nombre": "Leonardo", "activo": True, "edad": 46},
    {"nombre": "Irma", "activo": False, "edad": 56},
]


# Predicado de validación individual
def esta_activo(usuario: dict) -> bool:
    return usuario["activo"]


def es_mayor_de_edad(usuario: dict) -> bool:
    return usuario["edad"] >= 18


# all(): Comprueba si TODOS los elementos cumplen el predicado
todos_activos = all(esta_activo(u) for u in usuarios)
print(f"¿Están todos activos? {todos_activos}")  # Salida: False

# any(): Comprueba si AL MENOS UN elemento cumple el predicado
algun_mayor = any(es_mayor_de_edad(u) for u in usuarios)
print(f"¿Hay algún mayor de edad? {algun_mayor}")  # Salida: True
