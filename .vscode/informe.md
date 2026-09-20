# 3. Recursión (E2)

- **Función:**
  `versiones_de(versionable, id_cancion)`
  Esta función busca de manera recursiva todas las canciones derivadas ( remixes, versiones en vivo) de una canción dada, incluyendo las derivadas de sus derivadas (árbol de versiones).

- **Caso base:**
  `if not directas:`
  Ocurre cuando una canción no tiene ninguna versión directa (covers, remixes o lives) registrada. En este punto, la recursión se detiene y devuelve una lista vacía `[]`.

- **Caso recursivo:**
  `for v in directas: resultado += versiones_de(versionable, v)`
  Ocurre cuando la canción sí tiene versiones directas. La función se vuelve a llamar a sí misma para cada una de esas versiones derivadas (`v`), bajando un nivel más en el árbol para encontrar versiones de las versiones, y acumula todos los hallazgos en la lista `resultado`.

- **Traza de un ejemplo real del dataset:**
  Tomando como entrada el dato de `versiones.txt`: `13,12,live` (la canción 13 es una versión en vivo de la 12) y asumiendo que la canción 13 tiene a su vez un remix con ID 14 (`14,13,remix`).

  **Llamada inicial:** `versiones_de(versionable, 12)`
  1. `versionable.versiones_directas(12)` devuelve `[13]`.
  2. Como `directas` no está vacío, salta el caso base.
  3. `resultado = [13]`.
  4. Entra al bucle para `v = 13` y ejecuta la **Segunda Llamada**: `versiones_de(versionable, 13)`.
     
     **Segunda Llamada (id_cancion = 13):**
     1. `versionable.versiones_directas(13)` devuelve `[14]`.
     2. `resultado = [14]`.
     3. Entra al bucle para `v = 14` y ejecuta la **Tercera Llamada**: `versiones_de(versionable, 14)`.
        
        **Tercera Llamada (id_cancion = 14):**
        1. `versionable.versiones_directas(14)` devuelve `[]` (no tiene derivadas).
        2. Se activa el **Caso Base**: retorna `[]`.
     
     4. De regreso en la Segunda Llamada, se suma el resultado: `[14] + [] = [14]`.
     5. Finaliza la Segunda Llamada retornando `[14]`.

  5. De regreso en la Llamada Inicial, se suma el resultado acumulado: `[13] + [14] = [13, 14]`.
  6. Finaliza la función y devuelve el listado completo: `[13, 14]`.
