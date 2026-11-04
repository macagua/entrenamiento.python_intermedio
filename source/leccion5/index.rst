.. _python_leccion5:

Funciones Lambda
================

Las **funciones lambda** (también llamadas funciones anónimas) en Python son
funciones pequeñas que se definen sin un nombre utilizando la palabra clave
:ref:`lambda`. A diferencia de las funciones tradicionales definidas con
:ref:`def <python_sent_def>`, las lambda están limitadas a **una sola expresión** y devuelven
el resultado de esa expresión automáticamente.

----

Sintaxis Básica
---------------

La estructura de una función lambda es la siguiente:

.. code:: python

    lambda argumentos: expresion


- ``lambda``: Palabra clave para declarar la función.

- ``argumentos``: Los valores de entrada (pueden ser varios separados por comas, o ninguno).

- ``expresion``: La operación que se realiza y cuyo resultado se devuelve automáticamente
  (no se usa la palabra :ref:`return`).

----

Comparación: Función Normal vs. Función Lambda
'''''''''''''''''''''''''''''''''''''''''''''''

Para entenderlo mejor, veamos cómo haríamos una función simple que multiplica un número por 2 de ambas formas:

Con :ref:`def <python_sent_def>` tradicional:

.. code:: python

    def duplicar(x):
        return x * 2


    # Salida: 10
    print(duplicar(5))

Con :ref:`lambda`:

.. code:: python

    duplicar = lambda x: x * 2

    # Salida: 10
    print(duplicar(5))

**Nota:** Aunque se puede asignar una lambda a una variable como en el ejemplo,
       su verdadero poder se exprime cuando se usan de forma anónima (sin nombre)
       dentro de otras funciones.

----

Ejemplos Prácticos y Entendibles
--------------------------------

1. Lambda con múltiples argumentos
''''''''''''''''''''''''''''''''''

Podemos recibir más de un parámetro separándolos por comas, igual que en una función normal.

.. code:: python

    # Función para sumar dos números
    sumar = lambda a, b: a + b

    # Salida: 10
    print(sumar(3, 7))

1. Usando Lambda con `filter()`
'''''''''''''''''''''''''''''''
La función :ref:`filter() <python_fun_filter>` filtra los elementos de una lista basándose en una condición
(si devuelve  :ref:`True <python_bool>` o  :ref:`False <python_bool>`). Es ideal
combinarla con lambda para no crear funciones auxiliares largas.

.. code:: python

    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    # Filtrar solo los números pares
    pares = list(filter(lambda x: x % 2 == 0, numeros))

    # Salida: [2, 4, 6, 8]
    print(pares)

1. Usando Lambda con `map()`
''''''''''''''''''''''''''''

La función :ref:`map() <python_fun_map>` aplica una operación a todos los elementos de una lista o iterable.

.. code:: python

    precios = [100, 200, 300]

    # Aplicar un descuento del 10% a cada precio (multiplicar por 0.9)
    precios_con_descuento = list(map(lambda p: p * 0.9, precios))

    # Salida: [90.0, 180.0, 270.0]
    print(precios_con_descuento)


1. Ordenar colecciones complejas con `sorted()`
'''''''''''''''''''''''''''''''''''''''''''''''

Si tienes una lista de diccionarios o tuplas y quieres ordenarla por un criterio específico,
el parámetro ``key`` de :ref:`sorted() <python_fun_sorted>` acepta una función :ref:`lambda`.

.. code:: python

    estudiantes = [
        {"nombre": "Ana", "edad": 22},
        {"nombre": "Carlos", "edad": 19},
        {"nombre": "Beatriz", "edad": 25},
    ]

    # Ordenar los estudiantes por edad de menor a mayor
    estudiantes_ordenados = sorted(estudiantes, key=lambda estudiante: estudiante["edad"])

    print(estudiantes_ordenados)
    # Salida: [{'nombre': 'Carlos', 'edad': 19}, {'nombre': 'Ana', 'edad': 22}, {'nombre': 'Beatriz', 'edad': 25}]

----

¿Cuándo SÍ y cuándo NO usarlas?
-------------------------------

**NOTE:**

- **Cuándo usarlas:** Para operaciones rápidas, sencillas y de un solo uso,
  especialmente como argumentos en funciones de orden superior
  (:ref:`map() <python_fun_map>`, :ref:`filter() <python_fun_filter>`, y
  :ref:`sorted() <python_fun_sorted>`).

- **Cuándo NO usarlas:** Si la lógica requiere varias líneas, bucles
  (:ref:`for <python_bucle_for>`), estructuras condicionales complejas
  (:ref:`if <python_sent_if>`, :ref:`elif <python_sent_elif>`, y :ref:`else <python_sent_else>`)
  o múltiples sentencias, es mucho mejor y más legible utilizar una
  función tradicional con :ref:`def <python_sent_def>`.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion5>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html
