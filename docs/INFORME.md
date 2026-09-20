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

- Traza de un ejemplo real del dataset:Tomando como entrada el dato de `versiones.txt`: `13,12,live` (la canción 13 es una versión en vivo de la 12) y asumiendo que la canción 13 tiene a su vez un remix con ID 14 (`14,13,remix`).


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
