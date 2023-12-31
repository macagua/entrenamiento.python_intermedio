.. -*- coding: utf-8 -*-


.. _python_leccion4:

Funciones de orden superior
===========================

Las funciones de Python pueden tomar funciones como parámetros y devolver funciones
como resultado. Una función que hace ambas cosas o alguna de ellas se llama función
de orden superior.


.. _python_fun_filter:

filter()
........

La función ``filter()`` es una función la cual toma un :ref:`predicado <python_fun_predicado>`
y una :ref:`lista <python_list>` y devuelve una :ref:`lista <python_list>` con los elementos que satisfacen el predicado. Tal como
su nombre indica ``filter()`` significa filtrar, ya que a partir de una lista o iterador
y una función condicional, es capaz de devolver una nueva colección con los elementos
filtrados que cumplan la condición.

Todo esto podría haberse logrado también usando :ref:`listas por comprensión <python_listas_comprension>`
que usaran *predicados*. No hay ninguna regla que diga cuando usar la función
:ref:`map() <python_fun_map>` o la función ``filter()`` en lugar de las
:ref:`listas por comprensión <python_listas_comprension>`, simplemente debe decidir
que es más legible dependiendo del contexto.

Por ejemplo, suponga que tiene una :ref:`lista <python_list>` varios números y requiere filtrarla,
quedando únicamente con los :ref:`números <python_int>` múltiples de 5, eso seria así:

.. code-block:: pycon

    >>> # Primero declaramos una función condicional
    >>> def multiple(numero):
    ...     # Comprobamos si un numero es múltiple de cinco
    ...     if numero % 5 == 0:
    ...         # Sólo devolvemos True si lo es
    ...         return True
    ...

    >>> numeros = [2, 5, 10, 23, 50, 33]
    >>> for numero in filter(multiple, numeros):
    ...     print(numero)
    ...
    5
    10
    50
    >>>

Si ejecuta el filtro obtiene una :ref:`lista <python_list>` los :ref:`números <python_int>` múltiples de 5. Por tanto cuando
utiliza la función ``filter()`` tiene que enviar una función condicional, para esto,
puede utilizar una función anónima ``lambda``, como se muestra a continuación:

.. code-block:: pycon

    >>> numeros = [2, 5, 10, 23, 50, 33]
    >>> for i in filter(lambda numero: numero % 5 == 0, numeros):
    ...     print(i)
    ...
    5
    10
    50
    >>>

Así, en una sola línea ha definido y ejecutado el filtro utilizando una función
condicional anónima y devolviendo una :ref:`lista <python_list>` de :ref:`números <python_int>`.


Filtrando objetos
~~~~~~~~~~~~~~~~~

Sin embargo, más allá de filtrar listas con valores simples, el verdadero potencial
de la función ``filter()`` sale a relucir cuando usted necesita filtrar varios objetos
de una :ref:`lista <python_list>`.

Por ejemplo, dada una :ref:`lista <python_list>` con varias personas, a usted le gustaría filtrar únicamente
las cuales son menores de edad:

.. code-block:: pycon

    >>> class Persona:
    ...     def __init__(self, nombre, edad):
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     def __str__(self):
    ...         return "{} de {} años".format(self.nombre, self.edad)
    ...
    >>> personas = [
    ...     Persona("Leonardo", 38),
    ...     Persona("Ana", 33),
    ...     Persona("Sabrina", 12),
    ...     Persona("Enrique", 3),
    ... ]
    >>> menores = filter(lambda persona: persona.edad < 18, personas)
    >>> for menor in menores:
    ...     print(menor)
    ...
    Sabrina de 12 años
    Enrique de 3 años
    >>>

Este es un ejemplo sencillo, con el cual usted puede realizar filtrados con objetos, de
forma amigable.


.. _python_fun_map:

map()
.....

La función ``map()`` toma una función y una :ref:`lista <python_list>` y aplica esa función a cada elemento
de esa :ref:`lista <python_list>`, produciendo una nueva :ref:`lista <python_list>`. Va a ver su definición de tipo y como se
define.

Esta función trabaja de una forma muy similar a :ref:`filter() <python_fun_filter>`,
con la diferencia que en lugar de aplicar una condición a un elemento de una :ref:`lista <python_list>` o
secuencia, aplica una función sobre todos los elementos y como resultado se devuelve un
:ref:`lista <python_list>` de :ref:`números <python_int>` doblado su valor:

.. code-block:: pycon

    >>> def doblar(numero):
    ...     return numero * 2
    ...
    >>> numeros = [2, 5, 10, 23, 50, 33]
    >>> map(doblar, numeros)
    [4, 10, 20, 46, 100, 66]

Usted puede simplificar el código anterior usando una función ``lambda`` para substituir
la llamada de una función definida, como se muestra a continuación:

.. code-block:: pycon

    >>> map(lambda x: x * 2, numeros)
    [4, 10, 20, 46, 100, 66]

La función ``map()`` se utiliza mucho junto a expresiones ``lambda`` ya que permite
evitar escribir :ref:`bucles for <python_bucle_for>`.

Además se puede utilizar sobre más de un objeto iterable con la condición que tengan
la misma longitud. Por ejemplo, si requiere multiplicar los :ref:`números <python_int>` de dos :ref:`listas <python_list>`:

.. code-block:: pycon

    >>> a = [1, 2, 3, 4, 5]
    >>> b = [6, 7, 8, 9, 10]
    >>> map(lambda x, y: x * y, a, b)
    [6, 14, 24, 36, 50]

E incluso usted puede extender la funcionalidad a tres listas o más:

.. code-block:: pycon

    >>> a = [1, 2, 3, 4, 5]
    >>> b = [6, 7, 8, 9, 10]
    >>> c = [11, 12, 13, 14, 15]
    >>> map(lambda x, y, z: x * y * z, a, b, c)
    [66, 168, 312, 504, 750]


Mapeando objetos
~~~~~~~~~~~~~~~~

Evidentemente, siempre que la función ``map()`` la utilice correctamente podrá mapear
una serie de objetos sin ningún problema:

.. code-block:: pycon

    >>> class Persona:
    ...     def __init__(self, nombre, edad):
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     def __str__(self):
    ...         return "{} de {} años".format(self.nombre, self.edad)
    ...
    >>> personas = [
    ...     Persona("Leonardo", 38),
    ...     Persona("Ana", 33),
    ...     Persona("Sabrina", 12),
    ...     Persona("Enrique", 3),
    ... ]
    >>> def incrementar(p):
    ...     p.edad += 1
    ...     return p
    ...
    >>> personas = map(incrementar, personas)
    >>> for persona in personas:
    ...     print(persona)
    ...
    Leonardo de 39 años
    Ana de 34 años
    Sabrina de 13 años
    Enrique de 4 años

Claro que en este caso tiene que utilizar una función definida porque no necesitamos
actuar sobre la instancia, a no ser que usted se tome la molestia de rehacer todo el
objeto:

.. code-block:: pycon

    >>> class Persona:
    ...     def __init__(self, nombre, edad):
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     def __str__(self):
    ...         return "{} de {} años".format(self.nombre, self.edad)
    ...
    >>> personas = [
    ...     Persona("Leonardo", 38),
    ...     Persona("Ana", 33),
    ...     Persona("Sabrina", 12),
    ...     Persona("Enrique", 3),
    ... ]
    >>> def incrementar(p):
    ...     p.edad += 1
    ...     return p
    ...
    >>> personas = map(lambda p: Persona(p.nombre, p.edad + 1), personas)
    >>> for persona in personas:
    ...     print(persona)
    ...
    Leonardo de 39 años
    Ana de 34 años
    Sabrina de 13 años
    Enrique de 4 años


.. _python_fun_lambda:

lambda
......

La expresión ``lambda``, es una función anónima que suelen ser usadas cuando necesita
una función una sola vez. Normalmente usted crea funciones ``lambda`` con el único
propósito de pasarlas a funciones de orden superior.

En muchos lenguajes, el uso de ``lambdas`` sobre funciones definidas causa problemas
de rendimiento. No es el caso en Python.

.. code-block:: pycon

    >>> import os
    >>> archivos = os.listdir(os.__file__.replace("{}os.py".format(os.sep), os.sep))
    >>> print(list(filter(lambda x: x.startswith("os."), archivos)))
    ['os.py']

En el ejemplo anterior se usa el método ``os.__file__`` para obtener la ruta donde
esta instalada el módulo ``os`` en su sistema, ejecutando la siguiente sentencia:

.. code-block:: pycon

    >>> os.__file__
    '/usr/lib/python3.11/os.pyc'

Si con el método ``os.__file__`` obtiene la ruta del módulo ``os`` con el método
``replace("{}os.py".format(os.sep), os.sep)`` busca la cadena de carácter ``/os.py`` para Linux
y para Windows ``\\os.py`` y la remplaza por la cadena de carácter ``/`` para Linux
y para Windows ``\\``

.. code-block:: pycon

    >>> os.__file__.replace("{}os.py".format(os.sep), os.sep)
    '/usr/lib/python3.11/'

Luego se define la variable ``archivos`` generando una lista de archivos usando la
función ``os.listdir()``, pasando el parámetro obtenido de la ruta donde se instalo
el módulo ``os`` ejecutando en el comando previo, con la siguiente sentencia:

.. code-block:: pycon

    >>> archivos = os.listdir("/usr/lib/python3.11/")

De esta forma se define en la variable ``archivos`` un :ref:`tipo lista <python_list>`
con un tamaño de *433*, como se puede comprobar a continuación:

.. code-block:: pycon

    >>> type(archivos)
    <type 'list'>
    >>> len(archivos)
    443

Opcionalmente puede comprobar si la cadena de caracteres **os.py** se encuentras
una de las posiciones de la lista ``archivos``, ejecutando la siguiente sentencia:

.. code-block:: pycon

    >>> "os.py" in archivos
    True

Ya al comprobar que existe la cadena de caracteres "**os.py**" se usa una función
``lambda`` como parámetro de la función :ref:`filter() <python_fun_filter>` para
filtrar todos los archivos del directorio "*/usr/lib/python3.11/*" por medio del función
``os.listdir()`` que inicien con la cadena de caracteres "**os.**" usando la función
:ref:`startswith() <python_fun_startswith>`.

.. code-block:: pycon

    >>> print(filter(lambda x: x.startswith("os."), os.listdir("/usr/lib/python3.11/")))
    ['os.py']

Así de esta forma se comprueba que existe el archivo compilado "**os.py**" de Python
junto con el mismo módulo Python "**os.py**".


.. tip::
    Más detalle consulte la referencia de las expresiones :ref:`lambda <python_expresion_lambda>`.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.

.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
