# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: "Biblioteca Musical"
- Por qué lo eligieron (5–8 líneas): 
 Se eligió por unanimidad ya que se trata de un primer repositorio en GitHub,, el primer proyecto de la materia. No presenta mayor dificultad ya que se trata de una temática conocida; el catálogo de canciones contiene pocos items, canción, artista, album, año; y se sabe cómo funciona una palylist. 
 Esto nos permite concentrarnos más en el código.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1).
El ítem es un producto que forma parte del catálogo o sea una lista organizada, de ésto se trata el proyecto. El ítem en nuestro catálogo sería la canción.
La lista y el diccionario en Python son mutables significa que sus componentes se pueden modificar, cambiar , agregar o borrar elementos sin necesidad de generar un objeto nuevo.
Inmutable es todo lo contrario, no se pueden modificar sus datos una vez creado, por ejemplo las tuplas. Si se necesita modificar hay que crear un objeto nuevo.

 Cómo se relacionan catálogo, colección principal, pila y cola.
 En programación el catálogo es el registro maestro, contiene datos inmutables y fijos de cada elemento.
 La colección principal es el sub-conjunto de elementos que que elegimos para formar nuestra lista de canciones.
 La pila es una estructura de datos donde los elementos se apilan uno arriba de otro; el último elemento que se agrega es el primero que se tiene que sacar. Sería el historial de canciones escuchadas.
 Cola es una estructura de datos ordenada donde el primer elemento que se coloca es el primero que debe salir, seria la fila de reproducción cuando se pone por ejemplo reproducir a continuación.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: `versiones_de(versionable, id_cancion)`Esta función busca de manera recursiva todas las canciones derivadas ( remixes, versiones en vivo) de una canción dada, incluyendo las derivadas de sus derivadas (árbol de versiones).

- Caso base:`if not directas:` Ocurre cuando una canción no tiene ninguna versión directa (covers, remixes o lives) registrada. En este punto, la recursión se detiene y devuelve una lista vacía `[]`.

- Caso recursivo:`for v in directas: resultado += versiones_de(versionable, v)`Ocurre cuando la canción sí tiene versiones directas. La función se vuelve a llamar a sí misma para cada una de esas versiones derivadas (`v`), bajando un nivel más en el árbol para encontrar versiones de las versiones, y acumula todos los hallazgos en la lista `resultado`

-- **Traza de un ejemplo real del dataset:**
  Tomando como entrada el dato de `versiones.txt`: `3,1,live` (la canción 3 es una versión en vivo de la 1) y asumiendo que la canción 3 tiene a su vez un remix con ID 2 (`2,1,remix`).

  **Llamada inicial:** `versiones_de(versionable, 1)`
  1. `versionable.versiones_directas(1)` devuelve `[3]`.
  2. Como `directas` no está vacío, salta el caso base.
  3. `resultado = [3]`.
  4. Entra al bucle para `v = 3` y ejecuta la **Segunda Llamada**: `versiones_de(versionable, 3)`.
     
     **Segunda Llamada (id_cancion = 13):**
     1. `versionable.versiones_directas(3)` devuelve `[4]`.
     2. `resultado = [4]`.
     3. Entra al bucle para `v = 4` y ejecuta la **Tercera Llamada**: `versiones_de(versionable, 4)`.
        
        **Tercera Llamada (id_cancion = 4):**
        1. `versionable.versiones_directas(4)` devuelve `[]` (no tiene derivadas).
        2. Se activa el **Caso Base**: retorna `[]`.
     
     4. De regreso en la Segunda Llamada, se suma el resultado: `[4] + [] = [4]`.
     5. Finaliza la Segunda Llamada retornando `[4]`.

  5. De regreso en la Llamada Inicial, se suma el resultado acumulado: `[3] + [4] = [3, 4]`.
  6. Finaliza la función y devuelve el listado completo: `[3, 4]`.



## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
