 **TP integrador — AyED C2 2026**
 **Algoritmos y Estructura de Datos**
 ** Tema** :*Biblioteca Musical*

**Integrantes**

Segura Graciela Adriana 
gracielaadriana68@gmail.com
[sgraciela8-design]

Poblet Acosta Franco
pobletezequiel@gmail.com
[francojob2024-arch]

Soldano Julio
jula76@gmail.com
[JulioSoldano]

Cómo ejecutarlo requisitos:
- Python 3.10 o superior
- Biblioteca estándar de Python (no requiere dependencias externas)
Desde la raíz del repositorio ejecutar:
python -m src.main

Biblioteca Musical: aplicación de consola para gestionar un catálogo de canciones, permitiendo consultar información, realizar búsquedas y ordenamientos, administrar una colección principal y mantener persistencia de los datos.
El sistema implementa las 10 operaciones solicitadas por la cátedra:
-Listar catálogo utilizando el iterador de la colección.
-Ver detalle de una canción a partir de su ID.
-Búsquedas:
    -Búsqueda lineal por ID
    -Búsqueda lineal por título.
    -Búsqueda binaria por Id.
-Ordenamientos
    -Selection Sort por ID.
    -Insertion Sort por título.
-Operación recursiva para obtener versiones o derivados de una canción.
-ABM persistente de canciones:
    -Alta
    -Baja
    -Modificación
-Historial mediante pila (LIFO)
-Cola de reproducción mediante cola(FIFO)
-Persistencia en archivos binarios utilizando registros de longitud fija y el módulo struct

Estructuras de datos utilizadas
-Lista enlazada propia.
-Pila implementada sobre lista enlazada
-Cola implementada sobre lista enlazada
-Iterador propio para recorrer la colección.
-Algoritmos de búsqueda y ordenamiento desrrollados para la materia.

Persistencia
El sistema puede guardar y recuperr información desde:
-Archivos de texto
-Archivos binarios

Los archivos binarios utilizan:
-Cabeceera (Header) de validación
-Registros de longitud fija.
-Acceso directo mediante seek() para la actualización por posición.

Manejo de errores
La aplicación incluye excepciones propias para situaciones como:
-Archivo inválido
-Pila vacía
-Cola vacía
-Colección completa
Los errores son gestionados mediante mensajes claros para el usuario sin mostrar traceback

Limitaciones conocidas
-La búsqueda binaria se realiza únicamente sobre datos ordenados por ID
-Los campos de texto almacenados en binario poseen longitud fija y pueden truncarse si exceden el tamaño definido para el registro.
-La interfaz es completamente por consola y no posee interfaz gráfica.
-El sistema está orientado a la gestión de canciones y no contempla reproducción real de audio

Proyecto realizado para la materia Algoritmos y Estructura de Datos (AyED) año 2026

