.. _python_fun_predicado:

Funciones de predicado
----------------------

Las funciones de predicado no es más que una función la cual dice si algo es :ref:`True <python_bool>`
o :ref:`False <python_bool>`, es decir, es una función que devuelve un tipo de datos
:ref:`booleano <python_bool>`.

Una **función de predicado** (o simplemente *predicado*) es una función que evalúa una condición sobre
uno o más argumentos y **devuelve un valor booleano** (:ref:`True <python_bool>` o :ref:`False <python_bool>`).

En programación funcional y en el ecosistema de Python, los predicados son fundamentales para filtrar
datos, validar entradas, tomar decisiones condicionales y controlar flujos complejos de manera
declarativa.

----

¿Qué es un Predicado?
~~~~~~~~~~~~~~~~~~~~~~

Matemáticamente, un predicado es una proposición lógica que depende de variables. En Python, se traduce
en una función con la firma tipada de la siguiente manera:

.. code:: python

    from typing import Callable

    # Un predicado que recibe un valor de tipo T y devuelve un booleano
    PredicadoT = Callable[[T], bool]


De esta forma, un predicado puede ser cualquier función que tome uno o más argumentos y devuelva un valor
booleano.

Características principales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Dominio y Codominio:** Aceptan cualquier tipo de entrada (números, cadenas, objetos complejos) y su
   salida es estrictamente :ref:`bool <python_bool>`.

2. **Pureza:** Idealmente, las funciones de predicado deben ser **funciones puras** (sin efectos secundarios),
   lo que significa que dado el mismo argumento, siempre devuelven el mismo resultado sin modificar estados externos.

3. **Composición:** Son altamente reutilizables y se pueden combinar mediante operadores lógicos (:ref:`and <python_opers_logi_and>`, :ref:`or <python_opers_logi_or>`, :ref:`not <python_opers_logi_not>`).

----

Casos prácticos básicos
~~~~~~~~~~~~~~~~~~~~~~~~

Definición y uso con filtros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La función integrada :ref:`filter() <python_fun_filter>` y las comprensiones de listas
son los escenarios más comunes donde se emplean predicados.

.. literalinclude:: ../../recursos/leccion2/funciones_predicado_filter.py
    :language: python
    :linenos:
    :lines: 1-21


De esta manera, usted puede crear predicados simples y aplicarlos en escenarios prácticos
de filtrado de datos.

Funciones de validación con `all()` y `any()`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python ofrece funciones de orden superior como :ref:`all() <python_fun_all>` y :ref:`any() <python_fun_any>`
que aceptan iterable de booleanos generados por predicados.

.. literalinclude:: ../../recursos/leccion2/funciones_predicado_all_any.py
    :language: python
    :linenos:
    :lines: 1-22


De esta manera, usted puede crear predicados simples y aplicarlos en escenarios prácticos
de filtrado y validación de datos.

----

Casos prácticos avanzados
~~~~~~~~~~~~~~~~~~~~~~~~~~

Predicate factories
^^^^^^^^^^^^^^^^^^^^

Tambien conocidas *Fábricas de Predicados*, utilizando closures (como vimos en guías anteriores),
puedes crear funciones que devuelven predicados parametrizados a medida.


.. literalinclude:: ../../recursos/leccion2/funciones_predicado_closures.py
    :language: python
    :linenos:
    :lines: 1-21


De esta manera, usted puede crear predicados más complejos y reutilizables sin
necesidad de definir funciones auxiliares largas.


----


Combinación dinámica de predicados
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Puedes escribir funciones utilitarias que combinen lógicamente múltiples predicados
utilizando operadores de cortocircuito (:ref:`all() <python_fun_all>` o
:ref:`any() <python_fun_any>` aplicados a funciones).


.. literalinclude:: ../../recursos/leccion2/funciones_predicado_all_any_utility_functions.py
    :language: python
    :linenos:
    :lines: 1-25


De esta manera, usted puede crear predicados más complejos combinando varios predicados
simples, sin necesidad de definir funciones auxiliares largas.


----


Predicados nativos optimizados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python incluye el módulo estándar :mod:`operator`, el cual provee funciones equivalentes a los
operadores de sintaxis de Python implementados en C, altamente optimizados y listos para
actuar como predicados o funciones de orden superior.


.. literalinclude:: ../../recursos/leccion2/funciones_predicado_operator.py
    :language: python
    :linenos:
    :lines: 1-14


De esta manera, usted puede crear funciones de predicado utilizando el módulo :mod:`operator`
para operaciones comunes, sin necesidad de definir funciones auxiliares largas.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces: :download:`funciones_predicado.py <../../recursos/leccion2/funciones_predicado.py>`,
    :download:`funciones_predicado_filter.py <../../recursos/leccion2/funciones_predicado_filter.py>`,
    :download:`funciones_predicado_all_any.py <../../recursos/leccion2/funciones_predicado_all_any.py>`,
    :download:`funciones_predicado_closures.py <../../recursos/leccion2/funciones_predicado_closures.py>`,
    :download:`funciones_predicado_all_any_utility_functions.py <../../recursos/leccion2/funciones_predicado_all_any_utility_functions.py>`, y
    :download:`funciones_predicado_closures.py <../../recursos/leccion2/funciones_predicado_closures.py>`.


.. tip::
    Para ejecutar el código :file:`funciones_predicado.py`, :file:`funciones_predicado_filter.py`,
     :file:`funciones_predicado_all_any.py`, :file:`funciones_predicado_closures.py`,
     :file:`funciones_predicado_all_any_utility_functions.py`, y
     :file:`funciones_predicado_closures.py`, abra una
    consola de comando, acceda al directorio donde se encuentra los programas:

    ::

        leccion2/
        ├── funciones_predicado.py
        ├── funciones_predicado_filter.py
        ├── funciones_predicado_all_any.py
        ├── funciones_predicado_closures.py
        ├── funciones_predicado_all_any_utility_functions.py
        └── funciones_predicado_closures.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 funciones_predicado.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 funciones_predicado_filter.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 funciones_predicado_all_any.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 funciones_predicado_closures.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 funciones_predicado_all_any_utility_functions.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 funciones_predicado_closures.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
