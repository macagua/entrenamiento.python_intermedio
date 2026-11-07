.. _python_fun_objetos_fincion:

Objetos de función
------------------

En Python, las funciones son ciudadanos de primera clase (first-class citizens).
Esto significa que las funciones son objetos en toda regla, exactamente igual
que los enteros, las cadenas o las listas. Pueden asignarse a variables,
almacenarse en estructuras de datos, pasarse como argumentos a otras funciones y
devolverse como resultados.

Funciones como Objetos
~~~~~~~~~~~~~~~~~~~~~~~

Al definir una función con :ref:`def <python_sent_def>`, Python crea un objeto
en memoria de tipo function. Este objeto contiene el código ejecutable, su ámbito
(``scope``) y metadatos asociados.

Características clave
~~~~~~~~~~~~~~~~~~~~~~

- **Asignación a variables:** Puedes guardar una función en una variable sin invocarla
  (es decir, sin los paréntesis ``()``).

- **Estructuras de datos:** Puedes meter funciones dentro de listas, tuplas o diccionarios.

- **Paso como argumentos:** Funciones que reciben otras funciones se conocen como funciones
  de orden superior (higher-order functions).

A continuación, se muestra un ejemplo básico:

.. literalinclude:: ../../recursos/leccion2/objetos_funcion.py
    :language: python
    :linenos:
    :lines: 1-17


De esta manera, puedes ver que las funciones en Python son objetos de primera
clase, lo que permite una gran flexibilidad en la programación funcional y
orientada a objetos.

A continuación, se muestra algunos casos prácticos:

Diccionarios de despacho
~~~~~~~~~~~~~~~~~~~~~~~~

Tambien conocidos como "Dispatch Dictionaries", son una técnica útil para evitar largas
estructuras de :ref:`if <python_sent_if>`, :ref:`elif <python_sent_elif>`,
y :ref:`else <python_sent_else>`, puedes almacenar funciones en un diccionario para
seleccionar y ejecutar la lógica dinámicamente según una clave.

A continuación, se muestra un ejemplo básico:

.. literalinclude:: ../../recursos/leccion2/diccionarios_despacho.py
    :language: python
    :linenos:
    :lines: 1-21


De esta manera, puedes cambiar la operación a realizar simplemente modificando la clave
en el diccionario, sin necesidad de reescribir la lógica de control de flujo.


----


Objetos de funciones de Orden Superior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Puedes diseñar :ref:`funciones de orden superior <python_fun_orden_superior>`
(:ref:`map() <python_fun_map>`, :ref:`filter() <python_fun_filter>`, y funciones personalizadas)
que acepten otras :ref:`funciones <python_funciones>` para delegar comportamiento específico.

A continuación, se muestra un ejemplo básico:

.. literalinclude:: ../../recursos/leccion2/objetos_funcion_orden_superior.py
    :language: python
    :linenos:
    :lines: 1-37


De esta manera, puedes crear funciones genéricas que acepten otras funciones como parámetros,
permitiendo una gran flexibilidad y reutilización de código.


----


Objetos llamables
~~~~~~~~~~~~~~~~~

El Método Especial ``__call__``.

En Python, cualquier objeto que pueda ser invocado usando paréntesis ``()`` se denomina
objeto llamable (``callable``). No solo las funciones tradicionales son llamables; también
lo son las instancias de clases que implementan el :ref:`método mágico <python_leccion9>`
llamado :meth:`__call__`.

Esto permite crear objetos que actúan como funciones, pero que además mantienen un estado
interno entre llamadas (algo que las funciones puras tradicionales no pueden hacer fácilmente
sin variables globales o cierres).

A continuación, se muestra un ejemplo básico de una clase llamable:

.. literalinclude:: ../../recursos/leccion2/objetos_llamables.py
    :language: python
    :linenos:
    :lines: 1-24


De esta manera, las clases llamables permiten encapsular tanto la lógica como el estado,
proporcionando una forma poderosa y flexible de crear funciones con memoria interna.


----


Funciones anónimas y función partial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las :ref:`expresiones lambda <python_expresion_lambda>`: Son funciones anónimas de una sola línea,
muy útiles cuando necesitas pasar un objeto de función rápido y sencillo como argumento (por
ejemplo, en ordenamientos con :ref:`sorted(..., key=...) <python_fun_sorted>`).

``functools.partial``: Permite "congelar" algunos argumentos de una función existente para generar
un nuevo objeto de función con menos parámetros requeridos.

A continuación, se muestra un ejemplo básico:

.. literalinclude:: ../../recursos/leccion2/funciones_closure_anonimas_partial.py
    :language: python
    :linenos:
    :lines: 1-22


De esta manera, puedes crear funciones especializadas a partir de funciones más generales,
lo que facilita la reutilización y la claridad del código.


----


Objeto de función Closure
~~~~~~~~~~~~~~~~~~~~~~~~~

Un ``closure`` (o cierre) es un :ref:`objeto de función <python_fun_objetos_fincion>` que recuerda
y tiene acceso a las variables de su ámbito léxico superior (envolvente), incluso después de que
esa función externa haya terminado de ejecutarse y ya no esté activa en la pila de llamadas.

Para que se forme un ``closure`` en Python, deben cumplirse tres condiciones:

#. Debe existir una función anidada (una función definida dentro de otra).

#. La función anidada debe hacer referencia a una variable definida en la función externa (envolvente).

#. La función externa debe devolver la función anidada.

¿Cómo funciona internamente?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando una función anidada accede a una variable local de su función madre, Python empaqueta esa
variable junto con el objeto de función en un atributo especial llamado ``__closure__``. Esto
permite que el estado persista de forma privada y segura.

Ejemplo práctico: Un generador de contadores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Imagina que quieres crear contadores independientes. Con un ``closure``, puedes mantener un
estado interno (el valor actual del contador) sin necesidad de recurrir a variables globales
ni a clases complejas.

A continuación, se muestra un ejemplo básico:

.. literalinclude:: ../../recursos/leccion2/funciones_closure_generador.py
    :language: python
    :linenos:
    :lines: 1-36


**Nota sobre nonlocal:** Por defecto, si intentas reasignar una variable de un ámbito superior
(``contador += 1``), Python asumirá que es una variable local y lanzará un error si no ha sido
inicializada localmente. La palabra clave nonlocal le indica a Python que busque y modifique
la variable en el ámbito envolvente más cercano.


Inspeccionando el Closure
^^^^^^^^^^^^^^^^^^^^^^^^^^

Puedes verificar que el objeto de función realmente está almacenando estas variables examinando
su atributo ``__closure__``:

A continuación, se muestra un ejemplo básico:

.. code:: python

    print(contador_a.__closure__)
    # Salida muestra objetos de celda (cell objects) que contienen los valores capturados:
    # (<cell at 0x...: int object at 0x...>,)

    # Puedes ver el valor exacto almacenado en la primera celda del closure:
    print(contador_a.__closure__[0].cell_contents)  # Salida: 13


De esta forma, puedes inspeccionar y entender cómo los ``closures`` mantienen su estado interno,
lo que es especialmente útil para depuración y comprensión del flujo de datos en funciones anidadas.


----


Casos de uso avanzados
^^^^^^^^^^^^^^^^^^^^^^

Los ``closures`` son la base de patrones de diseño muy potentes en Python:

**A. Fábricas de funciones**

También conocidas como *Function Factories*, utilizando ``closures`` puedes crear funciones
personalizadas "al vuelo" configurando parámetros iniciales. Esto es especialmente útil para
crear funciones de validación, predicados o adaptadores sin necesidad de definir múltiples funciones
por separado.

Permiten crear funciones personalizadas "al vuelo" configurando parámetros iniciales.

A continuación, se muestra un ejemplo básico:

.. literalinclude:: ../../recursos/leccion2/funciones_closure_function_factories.py
    :language: python
    :linenos:
    :lines: 1-24

De esta forma, puede generar funciones especializadas a partir de una función genérica, lo que
facilita la reutilización y la claridad del código, además de permitir la creación de funciones
con comportamiento dinámico basado en los parámetros proporcionados al momento de su creación.


----


**B. Decoradores en Python**

Los :ref:`decoradores <python_decoradores>` (como ``@staticmethod``, ``@property`` o decoradores
personalizados) dependen directamente de los ``closures`` y de tratar a las funciones como objetos
de primera clase para envolver código y añadir funcionalidad (como registros, control de accesos
o caché) de forma transparente.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces: :download:`objetos_funcion.py <../../recursos/leccion2/objetos_funcion.py>`, 
    :download:`diccionarios_despacho.py <../../recursos/leccion2/diccionarios_despacho.py>`, 
    :download:`objetos_funcion_orden_superior.py <../../recursos/leccion2/objetos_funcion_orden_superior.py>`,
    :download:`objetos_llamables.py <../../recursos/leccion2/objetos_llamables.py>`,
    :download:`funciones_closure_anonimas_partial.py <../../recursos/leccion2/funciones_closure_anonimas_partial.py>`, y
    :download:`funciones_closure_function_factories.py <../../recursos/leccion2/funciones_closure_function_factories.py>`.


.. tip::
    Para ejecutar el código :file:`objetos_funcion.py`, :file:`diccionarios_despacho.py`,
    :file:`objetos_funcion_orden_superior.py`, :file:`objetos_llamables.py`,
    :file:`funciones_closure_anonimas_partial.py`,  y :file:`funciones_closure_function_factories.py`,
    abra una consola de comando, acceda al directorio donde se encuentra los programas:

    ::

        leccion2/
        ├── diccionarios_despacho.py
        ├── objetos_funcion_orden_superior.py
        ├── objetos_funcion.py
        ├── objetos_llamables.py
        ├── funciones_closure_anonimas_partial.py
        └── funciones_closure_function_factories.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 diccionarios_despacho.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 objetos_funcion_orden_superior.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 objetos_funcion.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 objetos_llamables.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 funciones_closure_anonimas_partial.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 funciones_closure_function_factories.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
