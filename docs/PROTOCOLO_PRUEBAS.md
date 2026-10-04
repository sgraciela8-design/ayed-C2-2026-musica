# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |  | Catálogo listado correctamente, con canciones y sin errores. |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |  | Mensaje Opcion invalida |
| P03 | E2 | Operación recursiva sobre un ítem con cadena |Menu 5 - ID 1| imprime la cadena completa |  | Muestra las versiones encontradas para el ID 1 (si los tiene) |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |Menu 5 - ID 3 | solo el ítem (caso base) |  | Muestra las versiones encontradas para el ID 3 (si los tiene) |
| P05 | E2 | Ver el detalle de un ítem que existe  | |muestra todos sus datos | no corrido (todavía)  |Pendiente  |
| P06 | E2 | Ver el detalle de un ítem que NO existe |  | mensaje claro, no se corta el programa|no corrido (todavía)  | Pendiente |
| P07 | E2 | Elegir una opción de menú inválida (ej. “Mono”) | Mono | vuelve a mostrar el menú |  | Mensaje Opcion invalida |
| P08 | E2 | Pasar enter vacío en el menú | ENTER | Vuelve a preguntar |  |  Mensaje Opcion invalida|
| P09 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia |  | Mensaje de elemento agregado exitosamente. Cuando pasa del 6to, mensaje de advertencia (equipo lleno) |
| P10 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue |  | No hay canciones en el historial |
| P11 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue |  |La cola está vacia  |
| P12 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones |  | Pendiente |
| P13 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P14 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P15 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P16 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P17 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P18 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P19 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
