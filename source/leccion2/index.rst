.. _python_fun_avanzadas:

Uso avanzado de funciones
=========================

En Python hay varias funciones avanzadas que se describen a continuación:


.. _python_fun_predicado:

Funciones de predicado
----------------------

Las funciones de predicado no es más que una función la cual dice si algo es :ref:`True <python_bool>`
o :ref:`False <python_bool>`, es decir, es una función que devuelve un tipo de datos
:ref:`booleano <python_bool>`.

.. comments:

    .. todo::
        TODO terminar de escribir la sección Funciones de predicado.


.. _python_fun_objetos_fincion:

Objetos de función
------------------

En Python, las funciones son ciudadanos de primera clase (first-class citizens).
Esto significa que las funciones son objetos en toda regla, exactamente igual
que los enteros, las cadenas o las listas. Pueden asignarse a variables,
almacenarse en estructuras de datos, pasarse como argumentos a otras funciones y
devolverse como resultados.

**Las Funciones como Objetos**

Al definir una función con :ref:`def <python_sent_def>`, Python crea un objeto
en memoria de tipo function. Este objeto contiene el código ejecutable, su ámbito
(``scope``) y metadatos asociados.

**Características clave**

- **Asignación a variables:** Puedes guardar una función en una variable sin invocarla
  (es decir, sin los paréntesis ``()``).

- **Estructuras de datos:** Puedes meter funciones dentro de listas, tuplas o diccionarios.

- **Paso como argumentos:** Funciones que reciben otras funciones se conocen como funciones
  de orden superior (higher-order functions).

A continuación, se muestra un ejemplo básico:

.. code:: python

    def saludar(nombre: str) -> str:
        return f"¡Hola, {nombre}!"


    # 1. Asignar la función a otra variable (sin paréntesis)
    operacion_saludo = saludar

    # 2. Invocar la función a través de la nueva variable
    print(operacion_saludo("Ana"))  # Salida: ¡Hola, Ana!

    # 3. Comprobar su tipo y identidad
    print(type(saludar))  # Salida: <class 'function'>


De esta manera, puedes ver que las funciones en Python son objetos de primera
clase, lo que permite una gran flexibilidad en la programación funcional y
orientada a objetos.

A continuación, se muestra algunos casos prácticos:

Diccionarios de despacho
""""""""""""""""""""""""

Tambien conocidos como "Dispatch Dictionaries", son una técnica útil para evitar largas
estructuras de :ref:`if <python_sent_if>`, :ref:`elif <python_sent_elif>`,
y :ref:`else <python_sent_else>`, puedes almacenar funciones en un diccionario para
seleccionar y ejecutar la lógica dinámicamente según una clave.

A continuación, se muestra un ejemplo básico:

.. code:: python

    def sumar(a: int, b: int) -> int:
        return a + b


    def restar(a: int, b: int) -> int:
        return a - b


    def multiplicar(a: int, b: int) -> int:
        return a * b


    # Diccionario que mapea strings a objetos de función
    operaciones = {"sumar": sumar, "restar": restar, "multiplicar": multiplicar}

    accion = "multiplicar"
    resultado = operaciones[accion](10, 5)
    print(resultado)  # Salida: 50


De esta manera, puedes cambiar la operación a realizar simplemente modificando la clave
en el diccionario, sin necesidad de reescribir la lógica de control de flujo.


----


Objetos de funciones de Orden Superior
""""""""""""""""""""""""""""""""""""""

Puedes diseñar :ref:`funciones de orden superior <python_fun_orden_superior>`
(:ref:`map() <python_fun_map>`, :ref:`filter() <python_fun_filter>`, y funciones personalizadas)
que acepten otras :ref:`funciones <python_funciones>` para delegar comportamiento específico.

A continuación, se muestra un ejemplo básico:

.. code:: python

    from typing import Callable, List


    def transformar_numeros(
        numeros: List[int], funcion_regla: Callable[[int], int]
    ) -> List[int]:
        """Aplica una regla (función) a cada elemento de una lista."""
        return [funcion_regla(n) for n in numeros]


    # Definimos funciones simples o usamos lambdas
    def al_cuadrado(x: int) -> int:
        return x**2


    numeros = [1, 2, 3, 4]
    resultados = transformar_numeros(numeros, al_cuadrado)
    print(resultados)  # Salida: [1, 4, 9, 16]


De esta manera, puedes crear funciones genéricas que acepten otras funciones como parámetros,
permitiendo una gran flexibilidad y reutilización de código.


----


Objetos llamables
"""""""""""""""""

El Método Especial ``__call__``.

En Python, cualquier objeto que pueda ser invocado usando paréntesis ``()`` se denomina
objeto llamable (``callable``). No solo las funciones tradicionales son llamables; también
lo son las instancias de clases que implementan el :ref:`método mágico <python_leccion9>`
llamado :meth:`__call__`.

Esto permite crear objetos que actúan como funciones, pero que además mantienen un estado
interno entre llamadas (algo que las funciones puras tradicionales no pueden hacer fácilmente
sin variables globales o cierres).

A continuación, se muestra un ejemplo básico de una clase llamable:

.. code:: python

    class Multiplicador:
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


De esta manera, las clases llamables permiten encapsular tanto la lógica como el estado,
proporcionando una forma poderosa y flexible de crear funciones con memoria interna.


----


Funciones Anónimas y Aplicación Parcial
"""""""""""""""""""""""""""""""""""""""

Las :ref:`expresiones lambda <python_expresion_lambda>`: Son funciones anónimas de una sola línea,
muy útiles cuando necesitas pasar un objeto de función rápido y sencillo como argumento (por
ejemplo, en ordenamientos con :ref:`sorted(..., key=...) <python_fun_sorted>`).

``functools.partial``: Permite "congelar" algunos argumentos de una función existente para generar
un nuevo objeto de función con menos parámetros requeridos.

A continuación, se muestra un ejemplo básico:

.. code:: python

    from functools import partial


    def potencia(base: int, exponente: int) -> int:
        return base**exponente


    # Creamos una nueva función especializada donde el exponente ya está fijo en 2 (al cuadrado)
    cuadrado = partial(potencia, exponente=2)

    print(cuadrado(5))  # Salida: 25 (equivalente a potencia(5, 2))


De esta manera, puedes crear funciones especializadas a partir de funciones más generales,
lo que facilita la reutilización y la claridad del código.


----


Objeto de función Closure
"""""""""""""""""""""""""

Un ``closure`` (o cierre) es un :ref:`objeto de función <python_fun_objetos_fincion>` que recuerda
y tiene acceso a las variables de su ámbito léxico superior (envolvente), incluso después de que
esa función externa haya terminado de ejecutarse y ya no esté activa en la pila de llamadas.

Para que se forme un ``closure`` en Python, deben cumplirse tres condiciones:

#. Debe existir una función anidada (una función definida dentro de otra).

#. La función anidada debe hacer referencia a una variable definida en la función externa (envolvente).

#. La función externa debe devolver la función anidada.

**¿Cómo funciona internamente?**

Cuando una función anidada accede a una variable local de su función madre, Python empaqueta esa
variable junto con el objeto de función en un atributo especial llamado ``__closure__``. Esto
permite que el estado persista de forma privada y segura.

**Ejemplo Práctico: Un Generador de Contadores**

Imagina que quieres crear contadores independientes. Con un ``closure``, puedes mantener un
estado interno (el valor actual del contador) sin necesidad de recurrir a variables globales
ni a clases complejas.

A continuación, se muestra un ejemplo básico:

.. code:: python

    from typing import Callable


    def crear_contador(inicio: int = 0) -> Callable[[], int]:
        """Crea una función contador que recuerda su propio estado."""
        # Variable en el ámbito envolvente (enclosing scope)
        contador = inicio

        def incrementar() -> int:
            nonlocal contador  # Permite modificar la variable del ámbito superior
            contador += 1
            return contador

        # Devolvemos el objeto de función (aún sin ejecutar)
        return incrementar


    # Creamos dos contadores independientes
    contador_a = crear_contador(10)
    contador_b = crear_contador(0)

    # Cada closure mantiene su propio estado aislado
    print(contador_a())  # Salida: 11
    print(contador_a())  # Salida: 12

    print(contador_b())  # Salida: 1: (empieza desde 0)
    print(contador_a())  # Salida: 13 (contador_a no se ve afectado por b)


**Nota sobre nonlocal:** Por defecto, si intentas reasignar una variable de un ámbito superior
(``contador += 1``), Python asumirá que es una variable local y lanzará un error si no ha sido
inicializada localmente. La palabra clave nonlocal le indica a Python que busque y modifique
la variable en el ámbito envolvente más cercano.

**Inspeccionando el Closure**

Puedes verificar que el objeto de función realmente está almacenando estas variables examinando
su atributo ``__closure__``:

A continuación, se muestra un ejemplo básico:

.. code:: python

    print(contador_a.__closure__)
    # Salida muestra objetos de celda (cell objects) que contienen los valores capturados:
    # (<cell at 0x...: int object at 0x...>,)

    # Puedes ver el valor exacto almacenado en la primera celda del closure:
    print(contador_a.__closure__[0].cell_contents)  # Salida: 13


**Casos de Uso Avanzados**

Los ``closures`` son la base de patrones de diseño muy potentes en Python:

**A. Fábricas de Funciones (Function Factories)**

Permiten crear funciones personalizadas "al vuelo" configurando parámetros iniciales.

A continuación, se muestra un ejemplo básico:

.. code:: python

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


**B. Decoradores en Python**

Los :ref:`decoradores <python_decoradores>` (como ``@staticmethod``, ``@property`` o decoradores
personalizados) dependen directamente de los ``closures`` y de tratar a las funciones como objetos
de primera clase para envolver código y añadir funcionalidad (como registros, control de accesos
o caché) de forma transparente.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces: :download:`diccionarios_despacho.py <../../recursos/leccion2/diccionarios_despacho.py>`,
    :download:`objetos_funcion.py <../../recursos/leccion2/objetos_funcion.py>`, y :download:`objetos_llamables.py <../../recursos/leccion2/objetos_llamables.py>`.


.. tip::
    Para ejecutar el código :file:`diccionarios_despacho.py`, :file:`objetos_funcion.py` y :file:`objetos_llamables.py`, abra una
    consola de comando, acceda al directorio donde se encuentra los programas:

    ::

        leccion2/
        ├── diccionarios_despacho.py
        ├── objetos_funcion.py
        └── objetos_llamables.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 listas_comprension_archivo.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 objetos_funcion.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 objetos_llamables.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
