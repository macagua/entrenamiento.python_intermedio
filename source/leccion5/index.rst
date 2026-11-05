.. _python_fun_anonimas:

Funciones anónimas
==================

Una función anónima, como su nombre indica es una función sin nombre. Es decir, es
posible ejecutar una función sin referenciar un nombre, en Python puede ejecutar
una función sin definirla con :ref:`def <python_sent_def>`.

De hecho son similares pero con una diferencia fundamental, **el contenido de una
función anónima debe ser una única expresión en lugar de un bloque de acciones**.

Las funciones anónimas se implementan en Python con las funciones o expresiones
:ref:`lambda <python_expresion_lambda>`, esta es unas de las funcionalidades más
potentes de Python, pero a la vez es la más confusas para los principiantes.

Más allá del sentido de función que usted tiene hasta el momento, con su nombre y
sus acciones internas, una función en su sentido más trivial significa realizar algo
sobre algo. Por tanto se podría decir que, mientras las funciones anónimas
``lambda`` sirven para realizar funciones simples, las funciones definidas con
:ref:`def <python_sent_def>` sirven para manejar tareas más extensas.

A diferencia de las funciones tradicionales definidas con :ref:`def <python_sent_def>`,
las lambda están limitadas a **una sola expresión** y devuelven el resultado de esa
expresión automáticamente.


.. _python_expresion_lambda:

Expresión lambda
----------------

La estructura de una función lambda es la siguiente:

.. code:: python

    lambda argumentos: expresion


- ``lambda``: Palabra clave para declarar la función.

- ``argumentos``: Los valores de entrada (pueden ser varios separados por comas, o ninguno).

- ``expresion``: La operación que se realiza y cuyo resultado se devuelve automáticamente
  (no se usa la palabra :ref:`return`).

Si deconstruye una función sencilla, puede llegar a una función ``lambda``. Por ejemplo
la siguiente función es para doblar un valor de un número:

.. code-block:: pycon

    >>> def doblar(numero):
    ...     resultado = numero * 2
    ...     return resultado
    ...

    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Si el código fuente anterior se simplifica se verá, de la siguiente forma:

.. code-block:: pycon

    >>> def doblar(numero):
    ...     return numero * 2
    ...

    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Usted puede todavía simplificar más, escribirlo todo en una sola línea, de la
siguiente forma:

.. code-block:: pycon

    >>> def doblar(numero):
    ...     return numero * 2
    ...

    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>
    >>> lambda numero: numero * 2
    <function <lambda> at 0x7f1023944e60>


Esta notación simple es la que una función ``lambda`` intenta replicar, observe,
a continuación se va a convertir la función en una función anónima:

.. code-block:: pycon

    >>> lambda numero: numero * 2
    <function <lambda> at 0x7f1023944e60>

En este ejemplo tiene una función anónima con una entrada que recibe ``numero``,
y una salida que devuelve ``numero * 2``.

Lo único que necesita hacer para utilizarla es guardarla en una variable y utilizarla
tal como haría con una función normal:

.. code-block:: pycon

    >>> doblar = lambda numero: numero * 2
    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Con la flexibilidad de Python usted puede implementar infinitas funciones simples.
Usted puede encontrar más ejemplos de funciones anónimas usando ``lambda`` en la
sección :ref:`ejemplos de funciones avanzadas <python_fun_avanzadas_ejs>`.

Usted puede explotar al máximo la función lambda utilizándola en conjunto con otras
funciones como :ref:`filter() <python_fun_filter>` y :ref:`map() <python_fun_map>`.


.. _python_fun_avanzadas_ejs:

Ejemplos de funciones avanzadas
-------------------------------

A continuación, se presentan algunos ejemplos de su uso:


**Función lambda - operaciones aritméticas**

A continuación, se presenta un ejemplo para comprobar si un número es impar:

.. code-block:: pycon

    >>> impar = lambda numero: numero % 2 != 0
    >>> impar(5)
    True


De esta manera, usted puede crear funciones anónimas para realizar operaciones
aritméticas simples, como sumar, restar, multiplicar o dividir, sin necesidad
de definir una función completa con :ref:`def <python_sent_def>`.


----


**Función lambda - operaciones de cadena**

A continuación, se presenta un ejemplo para darle la vuelta a una :ref:`cadena <python_str>` rebanándola
en sentido inverso:

.. code-block:: pycon

    >>> revertir = lambda cadena: cadena[::-1]
    >>> revertir("Plone")
    'enolP'
    >>> revertir("enolP")
    'Plone'

De esta manera, usted puede crear funciones anónimas para realizar operaciones de cadena simples, como invertir,
convertir a mayúsculas o minúsculas, sin necesidad de definir una función completa con :ref:`def <python_sent_def>`.


----


**Función lambda - múltiples argumentos**

A continuación, se presenta un ejemplo para varios parámetros separándolos por comas, igual que en una
función normal, por ejemplo para sumar dos :ref:`números <python_int>`:

.. code-block:: pycon

    >>> sumar = lambda x, y: x + y
    >>> sumar(5, 2)
    7


De esta manera, usted puede crear funciones anónimas para realizar operaciones simples con múltiples
argumentos, sin necesidad de definir una función completa con :ref:`def <python_sent_def>`.


----


**Función lambda - función filter()**

La función :ref:`filter() <python_fun_filter>` filtra los elementos de una lista basándose en una condición
(si devuelve  :ref:`True <python_bool>` o  :ref:`False <python_bool>`). Es ideal
combinarla con lambda para no crear funciones auxiliares largas.

.. code:: python

    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    # Filtrar solo los números pares
    pares = list(filter(lambda x: x % 2 == 0, numeros))

    # Salida: [2, 4, 6, 8]
    print(pares)


De esta manera, usted puede crear funciones anónimas para filtrar elementos de una lista basándose en una condición
simple, sin necesidad de definir una función completa con :ref:`def <python_sent_def>`.


----


**Función lambda - función map()**

La función :ref:`map() <python_fun_map>` aplica una operación a todos los elementos de una lista o iterable.

.. code:: python

    precios = [100, 200, 300]

    # Aplicar un descuento del 10% a cada precio (multiplicar por 0.9)
    precios_con_descuento = list(map(lambda p: p * 0.9, precios))

    # Salida: [90.0, 180.0, 270.0]
    print(precios_con_descuento)


De esta manera, usted puede crear funciones anónimas para aplicar operaciones a todos los elementos de una lista
o iterable, sin necesidad de definir una función completa con :ref:`def <python_sent_def>`.


----


**Función lambda - función sorted()**

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
