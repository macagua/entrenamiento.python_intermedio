.. -*- coding: utf-8 -*-


.. _python_leccion9:

Métodos mágicos
===============

Los métodos mágicos son métodos especiales que empiezan y terminan con dos guiones bajos (__).
También se les llama métodos *dunder*, por la abreviatura de "double underscore". Los métodos
mágicos no se deben invocar directamente por el usuario, sino que se ejecutan internamente por
la clase en ciertas situaciones. Por ejemplo, cuando se suma dos números usando el :ref:`operador + <python_opers_arit_suma>`,
internamente se llama al método ``__add__()``.

Las clases integradas en Python definen muchos métodos mágicos. Puedes usar la función ``dir()``
para ver el número de métodos mágicos heredados por una clase.

Por ejemplo, el siguiente código muestra todos los atributos y métodos definidos en la clase
``int``:

.. code-block:: pycon

    >>> print(dir(int))
    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__',
    '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__',
    '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__',
    '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__',
    '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
    '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__',
    '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__',
    '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__',
    '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
    'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag',
    'numerator', 'real', 'to_bytes']
    >>>


Como puedes ver, la clase int incluye varios métodos mágicos rodeados por dos guiones bajos.
Por ejemplo, el método ``__add__``:


.. _python_metodo_add:


Método __add__
--------------

Es un método mágico que se usa cuando se suman dos números usando el :ref:`operador + <python_opers_arit_suma>`.
Considera el siguiente ejemplo:

.. code-block:: pycon

    >>> num = 10
    >>> res = num.__add__(5)
    >>> print(res)
    15
    >>>


Como puedes ver, cuando haces ``num + 10``, el :ref:`operador + <python_opers_arit_suma>` llama al método
``__add__(10)``. También puedes llamar a ``num.__add__(5)`` directamente, lo que dará el mismo resultado.
Sin embargo, como se mencionó antes, los métodos mágicos no se deben llamar directamente, sino internamente,
a través de otros métodos o acciones.

Los métodos mágicos se usan con más frecuencia para definir comportamientos sobrecargados de los
operadores predefinidos en Python. Por ejemplo, los operadores aritméticos por defecto operan
sobre operandos numéricos.

Esto significa que los objetos numéricos deben usarse junto con operadores como :ref:`+ <python_opers_arit_suma>`,
:ref:`- <python_opers_arit_resta>`, :ref:`* <python_opers_arit_multi>`, :ref:`/ <python_opers_arit_div>`, etc.
El :ref:`operador + <python_opers_arit_suma>` también está definido como un operador de concatenación en las clases
:ref:`cadenas de caracteres <python_str>`, :ref:`listas <python_list>` y :ref:`tuplas <python_tuple>`. Podemos decir que
el :ref:`operador + <python_opers_arit_suma>` está sobrecargado.

Para hacer que el comportamiento sobrecargado esté disponible en tu propia clase personalizada, el método mágico
correspondiente debe ser redefinido. Por ejemplo, para usar el :ref:`operador + <python_opers_arit_suma>` con objetos de
una clase definida por el usuario, debe incluir el método ``__add__()``. Veamos cómo implementar y usar algunos de
los métodos mágicos más importantes.


.. _python_metodo_new:

Método __new__
--------------

Es un método mágico que se usa para crear una nueva instancia de una clase. Se llama antes
que el método ``__init__()``, que es el constructor de la clase. El método ``__new__()`` recibe la clase como
primer argumento y devuelve una instancia de esa clase. Por ejemplo, el siguiente código crea una clase
``Singleton`` que solo permite una instancia de sí misma.

.. code-block:: pycon

    >>> class Singleton:
    ...     """Clase Singleton"""
    ...     # Variable de clase que almacena la instancia única
    ...     _instance = None
    ...     def __new__(cls, *args, **kwargs):
    ...         """Método mágico para crear una nueva instancia"""
    ...         # Si no hay una instancia previa, se crea una nueva
    ...         if cls._instance is None:
    ...             cls._instance = super().__new__(cls, *args, **kwargs)
    ...         # Se devuelve la instancia única
    ...         return cls._instance
    ...     def show_id(self):
    ...         """Método para mostrar el id de la instancia"""
    ...         print(f"El id de esta instancia es {id(self)}")
    ...
    >>>

Crear dos objetos de la clase ``Singleton``:

.. code-block:: pycon

    >>> obj1 = Singleton()
    >>> obj2 = Singleton()
    >>>


Mostrar el id de cada objeto:

.. code-block:: pycon

    >>> obj1.show_id()
    El id de esta instancia es 140376583855472
    >>> obj2.show_id()
    El id de esta instancia es 140376583855472
    >>>


Como puedes ver, los dos objetos tienen el mismo id, lo que significa que son la misma instancia.


.. _python_metodo_init:

Método __init__
---------------

Es el método mágico que se usa para inicializar una nueva instancia de una clase. Se
llama después del método ``__new__()``, y recibe la instancia como primer argumento, seguido de los
argumentos que se pasan al constructor de la clase. El método ``__init__()`` no devuelve ningún valor,
sino que asigna los atributos a la instancia. Por ejemplo, el siguiente código crea una clase ``Persona``
que tiene un nombre y una edad como atributos.

.. code-block:: pycon

    >>> class Persona:
    ...     def __init__(self, nombre, edad):
    ...         """Método mágico para inicializar una nueva instancia"""
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     def mostrar(self):
    ...         """Método para mostrar los datos de la persona"""
    ...         print(f"Esta persona se llama {self.nombre} y tiene {self.edad} años")
    ...
    >>>


Crear una persona con el nombre "Ana" y la edad 25:

.. code-block:: pycon

    >>> p = Persona("Ana", 25)


Mostrar los datos de la persona:

.. code-block:: pycon

    >>> p.mostrar()
    Esta persona se llama Ana y tiene 25 años


Como puedes ver, el método ``__init__()`` asigna los valores de nombre y edad a la instancia ``p``, que luego
se pueden usar en el método ``mostrar()``.


.. _python_metodo_str:

Método __str__
--------------

Es un método mágico que se usa para devolver una representación en forma de cadena de una instancia de una
clase. Se llama cuando se usa la función ``str()`` o cuando se imprime la instancia. El método ``__str__()`` debe
devolver una cadena que describa el objeto de forma amigable para el usuario. Por ejemplo, el siguiente
código modifica la clase ``Persona`` para incluir el método ``__str__()``.


.. code-block:: pycon

    >>> class Persona:
    ...     def __init__(self, nombre, edad):
    ...         """Método mágico para inicializar una nueva instancia"""
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     def __str__(self):
    ...         """Método mágico para devolver una representación en forma de cadena"""
    ...         return f"Persona(nombre={self.nombre}, edad={self.edad})"
    ...
    >>>


Crear una persona con el nombre "Ana" y la edad 25:

.. code-block:: pycon

    >>> p = Persona("Ana", 25)
    >>>

Imprimir la persona usando el método ``__str__()``:

.. code-block:: pycon

    >>> print(p)
    Persona(nombre=Ana, edad=25)
    >>>

Como puedes ver, el método ``__str__()`` devuelve una cadena que muestra los atributos de la persona.


.. _python_metodo_repr:


Método __repr__
---------------

Es un método mágico que se usa para devolver una representación en forma de cadena de una instancia de
una clase. Se llama cuando se usa la función ``repr()`` o cuando se muestra la instancia en el intérprete
interactivo. El método ``__repr__()`` debe devolver una cadena que sea una expresión válida de Python que
pueda recrear el objeto. Por ejemplo, el siguiente código modifica la clase Persona para incluir el
método ``__repr__()``.

.. code-block:: pycon

    >>> class Persona:
    ...     def __init__(self, nombre, edad):
    ...         """Método mágico para inicializar una nueva instancia"""
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     def __repr__(self):
    ...         """Método mágico para devolver una representación en forma de cadena"""
    ...         return f"Persona('{self.nombre}', {self.edad})"
    ...
    >>>

Crear una persona con el nombre "Ana" y la edad 25

.. code-block:: pycon

    >>> p = Persona("Ana", 25)
    >>>

Mostrar la persona usando el método ``__repr__()``

.. code-block:: pycon

    >>> print(repr(p))
    Persona('Ana', 25)
    >>>

Como puedes ver, el método ``__repr__()`` devuelve una cadena que es una expresión de Python que puede crear
una nueva instancia de la persona con los mismos atributos.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.

.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html
