.. _python_fun_recursiva_sin_retorno:

Función recursiva sin retorno
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una función recursiva sin retorno (o función recursiva puramente procedimental) es
aquella que se llama a sí misma pero no propaga ni devuelve un valor acumulado a
través de la pila de llamadas. Su firma de tipo suele terminar en `->` :ref:`None <python_obj_none>`.

A diferencia de las :ref:`funciones con retorno <python_fun_recursiva_con_retorno>`, el
objetivo de estas funciones no es calcular un resultado final para asignarlo a una variable,
sino ejecutar una acción o efecto secundario (:ref:`side effect <python_fun_recur_sin_ret_side_effect>`)
en cada nivel de la recursividad: imprimir en consola, modificar estructuras de datos in situ
(:ref:`in-place <python_fun_recur_sin_ret_in_place>`), recorrer sistemas de archivos o actualizar
interfaces gráficas.


----

.. _python_fun_recur_sin_ret_side_effect:

Efectos secundarios y sin retorno
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En una función sin retorno, la sentencia :ref:`return <python_sent_return>` (cuando está presente)
se utiliza únicamente para **interrumpir la ejecución** de la función en el caso base, devolviendo
implícitamente :ref:`None <python_obj_none>`.

Características principales
````````````````````````````

1. **Ausencia de propagación:** No se utiliza el resultado de la llamada recursiva en operaciones
   matemáticas o de unión (no hay sentencias como ``return x + func(...)``).

2. **Dependencia de estado mutable o** :ref:`E/S <python_entrada_salida>`: Su utilidad radica en
   interactuar con el exterior (modificar listas pasadas por referencia, imprimir logs, escribir
   archivos).

3. **Peligro de efectos colaterales no deseados:** Al mutar estados compartidos o globales, pueden
   introducir errores difíciles de rastrear si no se gestionan con cuidado.

----

Casos prácticos básicos
^^^^^^^^^^^^^^^^^^^^^^^^

A continuación, se presentan algunos casos prácticos básicos:

Cuenta Regresiva (Efecto Secundario de Impresión)
```````````````````````````````````````````````````

El ejemplo más clásico de recursión sin retorno es una rutina que imprime mensajes en pantalla
hasta alcanzar una condición de parada.

.. code:: python

    def cuenta_regresiva(n: int) -> None:
        """Realiza una cuenta regresiva imprimiendo en consola de forma recursiva."""
        # 1. Caso base: detiene la recursividad
        if n <= 0:
            print("¡Despegue! 🚀")
            return  # Sale de la función sin devolver datos

        # 2. Efecto secundario en el nivel actual
        print(f"Quedan {n} segundos...")

        # 3. Caso recursivo (sin capturar ni retornar el resultado)
        cuenta_regresiva(n - 1)


    # Prueba de ejecución
    cuenta_regresiva(3)
    # Salida:
    # Quedan 3 segundos...
    # Quedan 2 segundos...
    # Quedan 1 segundos...
    # ¡Despegue! 🚀


De esta forma, puede ver cómo las funciones pueden ser utilizadas para resolver problemas
complejos y repetitivos.


----


Casos prácticos avanzados
^^^^^^^^^^^^^^^^^^^^^^^^^^

A continuación, se presentan algunos casos prácticos avanzados:

.. _python_fun_recur_sin_ret_in_place:

Modificación de estructuras anidadas In-Place
``````````````````````````````````````````````

Cuando se trabaja con listas de listas o árboles de directorios, a veces es más eficiente (o necesario
por la arquitectura) acumular resultados modificando una lista externa compartida en lugar de reconstruir
la estructura entera mediante retornos.

.. code:: python

    from typing import Any, List


    def aplanar_y_acumular(estructura: List[Any], acumulador: List[Any]) -> None:
        """Recorre una estructura anidada y muta una lista externa añadiendo los elementos."""
        for elemento in estructura:
            if isinstance(elemento, list):
                # Llamada recursiva para procesar la sublista
                aplanar_y_acumular(elemento, acumulador)
            else:
                # Efecto secundario: mutar la lista externa pasando la referencia
                acumulador.append(elemento)


    # Estructura anidada de prueba
    datos_anidados = [1, [2, 3], [4, [5, 6], 7], 8]
    resultado_externo: List[int] = []

    # Ejecuta la función sin retorno
    aplanar_y_acumular(datos_anidados, resultado_externo)

    print(resultado_externo)
    # Salida: [1, 2, 3, 4, 5, 6, 7, 8]


De esta forma, puede recorrer una estructura anidada y muta una lista externa añadiendo los elementos.


----


Recorrido de un sistema de archivos
````````````````````````````````````

Otro escenario común para funciones sin retorno es la exploración de jerarquías (como directorios o árboles
de componentes) donde se realizan operaciones de escritura, registro o impresión por cada nodo encontrado.

.. code:: python

    from typing import Dict, Union

    # Define un tipo para representar un sistema de archivos anidado
    FileSystem = Dict[str, Union[str, "FileSystem"]]


    def listar_directorio(nodo: FileSystem, nivel: int = 0) -> None:
        """Imprime jerárquicamente la estructura de un árbol de directorios."""
        indentacion = "  " * nivel

        for nombre, contenido in nodo.items():
            if isinstance(contenido, dict):
                print(f"{indentacion}📁 [Carpeta] {nombre}")
                # Llamada recursiva incrementando la indentación
                listar_directorio(contenido, nivel + 1)
            else:
                print(f"{indentacion}📄 [Archivo] {nombre} ({contenido})")


    # Estructura jerárquica simulada
    arbol_archivos: FileSystem = {
        "proyecto": {
            "src": {"main.py": "código", "utils.py": "código"},
            "tests": {"test_main.py": "test"},
            "README.md": "texto",
        }
    }

    # Ejecución
    listar_directorio(arbol_archivos)


De esta forma, puede imprimir jerárquicamente la estructura de un árbol de directorios.


----


¿Cuándo usar funciones recursivas sin retorno?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Tareas de registro o logging:** Cuando necesitas recorrer estructuras para inspeccionar
  o reportar estados.

* **Operaciones de mutación masiva:** Como limpiar nodos de un árbol DOM, recorrer componentes
  gráficos o actualizar estados en estructuras profundamente anidadas donde pasar acumuladores
  o modificar referencias simplifica el código imperativo.

* **Procesamiento de efectos de** :ref:`E/S <python_entrada_salida>`: Operaciones donde el valor
  de retorno lógico es irrelevante frente al impacto físico o visual de la ejecución (ej. dibujar
  fractales en un canvas).


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion1>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
