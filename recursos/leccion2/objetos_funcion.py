"""Ejemplo de Objetos de función"""


def saludar(nombre: str) -> str:
    return f"¡Hola, {nombre}!"


# Asignar la función a otra variable (sin paréntesis)
operacion_saludo = saludar

# Invocar la función a través de la nueva variable
print(operacion_saludo("Ana"))  # Salida: ¡Hola, Ana!

# Comprobar su tipo y identidad
print(type(saludar))  # Salida: <class 'function'>
print(id(saludar))  # Salida: dirección de memoria de la función
print(id(operacion_saludo))  # Salida: misma dirección de memoria
