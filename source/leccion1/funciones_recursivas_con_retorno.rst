.. _python_fun_recursiva_con_retorno:

Función recursiva con retorno
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una **función recursiva con retorno** es aquella que, además de llamarse a sí misma para descomponer
un problema, **acumula y devuelve un valor** resultante en cada nivel de la pila de llamadas. A
diferencia de las funciones recursivas puramente procedimentales (que solo realizan acciones o efectos
secundarios, como imprimir en pantalla), estas devuelven un valor tangible que se propaga desde el caso
base hasta la llamada inicial.

Esta guía teórico-práctica detalla cómo diseñar correctamente el flujo de retorno, evitar errores comunes
y aplicar patrones avanzados en Python 3.

Un ejemplo de una función recursiva con retorno, es el ejemplo del calculo del
factorial de un número corresponde al producto de todos los :ref:`números <python_int>` desde 1 hasta
el propio número. Es el ejemplo con retorno más utilizado para mostrar la utilidad
de este tipo de funciones:

.. code-block:: pycon

    >>> def factorial(numero):
    ...     print("Valor inicial ->", numero)
    ...     if numero > 1:
    ...         numero = numero * factorial(numero - 1)
    ...     print("valor final ->", numero)
    ...     return numero
    ...
    >>> print(factorial(5))
    Valor inicial -> 5
    Valor inicial -> 4
    Valor inicial -> 3
    Valor inicial -> 2
    Valor inicial -> 1
    valor final -> 1
    valor final -> 2
    valor final -> 6
    valor final -> 24
    valor final -> 120
    120


De esta forma, puede ver cómo se ejecuta la función recursiva.

----


La mecánica del retorno
^^^^^^^^^^^^^^^^^^^^^^^^

Los fundamentos teóricos para que la mecánica del retorno, es decir, que una función recursiva
devuelva un resultado de forma correcta, deben cumplirse dos reglas estrictas en su estructura:

1. **El Caso Base debe retornar un valor concreto:** No puede simplemente hacer un `return` vacío
   (o omitirlo) si la función espera calcular algo. Debe devolver el valor inicial o el elemento
   mínimo que detiene la recursividad (ej. `0`, `1`, `[]`, `""`).

2. **El Caso Recursivo debe propagar el resultado:** La sentencia `return` debe combinar el resultado
   actual con la llamada recursiva (ej. `return valor + funcion(subproblema)`). Si omites la palabra
   reservada `return` en el caso recursivo, la función devolverá :ref:`None <python_obj_none>` por
   defecto al finalizar.


El viaje de ida y vuelta en la Pila
````````````````````````````````````

A continuación, se presentan el viaje de ida y vuelta en la pila (*Call Stack*)

* **Fase de ida:** La función se llama a sí misma reduciendo los datos hasta tocar fondo (el caso base).

* **Fase de vuelta (Propagación):** El caso base devuelve su valor a la función anterior, esta opera
  con él, lo devuelve a su vez a la anterior, y así sucesivamente hasta la llamada original.


----


Casos prácticos básicos y comprobación de tipos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A continuación, se presentan algunos casos prácticos básicos:

Suma de Elementos de una Lista
```````````````````````````````

Un ejemplo sencillo y directo donde cada nivel de la pila suma su elemento actual con el resultado de
procesar el resto de la lista.

.. code:: python

    from typing import List


    def sumar_lista(numeros: List[int]) -> int:
        """Suma los elementos de una lista de forma recursiva con retorno."""
        # 1. Caso base: lista vacía suma 0
        if not numeros:
            return 0

        # 2. Caso recursivo: primer elemento + suma del resto de la lista
        return numeros[0] + sumar_lista(numeros[1:])


    # Prueba de ejecución
    datos = [1, 2, 3, 4, 5]
    resultado = sumar_lista(datos)
    print(resultado)  # Salida: 15


De esta forma, la función `sumar_lista` procesa cada elemento de la lista, sumando cada uno
con el resultado de la lista restante, hasta que llegue a la lista vacía, donde devuelve 0
y finalmente devuelve la suma total.


----


Inversión de una cadena de texto
`````````````````````````````````

La recursividad con retorno también maneja cadenas de texto de manera elegante, uniendo el último
carácter procesado con el resultado de invertir el sub-texto restante.

.. code:: python

    def invertir_cadena(texto: str) -> str:
        """Invierte una cadena de texto recursivamente."""
        # 1. Caso base: texto vacío o de un solo carácter
        if len(texto) <= 1:
            return texto

        # 2. Caso recursivo: el último/primer carácter se desplaza al extremo opuesto
        return invertir_cadena(texto[1:]) + texto[0]


    # Prueba de ejecución
    print(invertir_cadena("python"))  # Salida: "nohtyp"


De esta forma, puede invertir cualquier cadena de texto de manera sencilla y eficiente.


----


Casos prácticos avanzados
^^^^^^^^^^^^^^^^^^^^^^^^^^

A continuación, se presentan algunos casos prácticos avanzados:

Búsqueda binaria recursiva
```````````````````````````

La búsqueda binaria es un algoritmo eficiente con una complejidad temporal de ``$O(\log n)$`` que encuentra
un elemento en una lista ordenada dividiendo repetidamente el espacio de búsqueda a la mitad.

.. code:: python

    from typing import List, Optional


    def busqueda_binaria(
        lista: List[int], objetivo: int, inicio: int, fin: int
    ) -> Optional[int]:
        """Busca un elemento en una lista ordenada y devuelve su índice, o None si no está."""
        # 1. Caso base: el rango de búsqueda es inválido (elemento no encontrado)
        if inicio > fin:
            return None

        medio = (inicio + fin) // 2

        # 2. Caso base: encontrar el objetivo en la posición media
        if lista[medio] == objetivo:
            return medio

        # 3. Casos recursivos: buscar en la mitad izquierda o derecha
        if objetivo < lista[medio]:
            return busqueda_binaria(lista, objetivo, inicio, medio - 1)
        else:
            return busqueda_binaria(lista, objetivo, medio + 1, fin)


    # Prueba de ejecución
    elementos_ordenados = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    # Busca el número 23
    indice = busqueda_binaria(elementos_ordenados, 23, 0, len(elementos_ordenados) - 1)
    print(f"Elemento encontrado en el índice: {indice}")  # Salida: 5


De esta forma, puede definir funciones que busquen un elemento en una lista ordenada de manera
eficiente utilizando técnicas de programación funcional y recursiva.


----


Recorrido de diccionarios anidados
```````````````````````````````````

En desarrollo *backend* o análisis de datos, es común enfrentarse a configuraciones :ref:`JSON <python_json>`
anidadas donde necesitas extraer o transformar valores recursivamente asegurando que el retorno mantenga la
estructura o devuelva el dato acumulado.

.. code:: python

    from typing import Any, Dict


    def buscar_clave_anidada(datos: Dict[str, Any], clave_buscada: str) -> Any:
        """Busca una clave en un diccionario con diccionarios anidados de profundidad arbitraria."""
        for clave, valor in datos.items():
            if clave == clave_buscada:
                return valor  # Retorno inmediato al encontrar la coincidencia

            if isinstance(valor, dict):
                # Llamada recursiva descendente
                resultado = buscar_clave_anidada(valor, clave_buscada)
                if resultado is not None:
                    return resultado  # Propaga el valor devuelto hacia arriba

        return None  # No se encontró en esta rama


    # Estructura anidada compleja
    configuracion = {
        "app": {"nombre": "MiSistema", "version": 2},
        "base_datos": {"conexion": {"host": "localhost", "puerto": 5432}},
    }

    # Prueba de ejecución
    print(
        buscar_clave_anidada(configuracion, "puerto")
    )  # Salida: 5432 (encontrado en profundidad)


De esta forma, puedes buscar cualquier valor dentro de una estructura de datos.


----


Trampas comunes y ¿cómo evitarlas?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Olvidar el `return` en el caso recursivo:**
   Si escribes `funcion(n - 1)` en lugar de `return funcion(n - 1)`, la función devolverá :ref:`None <python_obj_none>`
   al llegar al nivel superior, rompiendo por completo el cálculo acumulado.

2. **Consumo excesivo de memoria (Stack Overflow):**
   Cada llamada recursiva con retorno almacena un marco en la pila (*stack frame*). Para estructuras de datos masivas
   o profundidades mayores a 1000 iteraciones, Python lanzará una excepción integrada `RecursionError`_. En esos
   escenarios, es preferible utilizar bucles iterativos o técnicas de **recursión de cola** (*tail recursion*, aunque
   Python no la optimiza nativamente de forma automática).


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion1>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

_`RecursionError`: https://realpython.com/ref/builtin-exceptions/recursionerror/
