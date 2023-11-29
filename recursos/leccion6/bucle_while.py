""" Ejemplo de uso de Bucle 'while' con sentencia 'else' """

print("\nBucle 'while' con sentencia 'else'")
print("==================================\n")

print("Ejemplo: calcular el promedio de notas de N estudiante ")
print("en un grado escolar, como se muestra a continuación:\n")

promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

grado = int(input(mensaje))
while grado != -1:
    total = total + grado
    contar += 1
    grado = int(input(mensaje))
else:
    promedio = total / contar
    print("Promedio de notas del grado escolar: " + str(promedio))
