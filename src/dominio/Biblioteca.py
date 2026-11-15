
from pathlib import Path
from src.dominio.cancion import Cancion
from src.excepciones import ArchivoInvalidoError, ColeccionLlenaError
from src.persistencia.binario import (
    actualizar_registro,
    cargar_binario,
    guardar_binario,
    posicion_del_id,
)
from src.persistencia.texto import cargar_csv, guardar_csv
from src.tads.lista_enlazada import ListaEnlazada

# Rutas ancladas a la raíz del proyecto (evita FileNotFoundError)
RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"
RUTA_TXT = DATA / "Lista_Canciones.txt"  # Unificamos un solo archivo de texto
RUTA_BIN = DATA / "canciones.bin"
ENCABEZADOS = ["id", "titulo", "artista", "album", "anio"]


class Biblioteca:

    def __init__(self):
        self.capacidad_maxima = 100
        self.canciones = ListaEnlazada()
        self.coleccion_principal = ListaEnlazada()
        self.versiones_directas = {1: [2], 2: [3]}

        # Al arrancar carga desde el archivo de texto
        self.cargar_desde_csv(RUTA_TXT)

    def cargar_desde_csv(self, ruta=RUTA_TXT):
        filas = cargar_csv(ruta)
        self.canciones = ListaEnlazada()  # Limpia antes de cargar
        for fila in filas:
            cancion = Cancion(
                fila["id"],
                fila["titulo"],
                fila["artista"],
                fila["album"],
                fila["anio"],
            )
            self.canciones.insertar_al_final(cancion)

    # ... (mantené igual obtener_filas, obtener_canciones, buscar_cancion_por_id, etc.) ...

    def agregar_cancion(self, cancion):
        if self.canciones.tamanio() >= self.capacidad_maxima:
            raise ColeccionLlenaError(
                "La colección principal alcanzó su capacidad máxima."
            )
        self.canciones.insertar_al_final(cancion)
        self.guardar_todo()

    def eliminar_cancion(self, id_cancion):
        cancion = self.buscar_cancion_por_id(id_cancion)
        if cancion is None:
            return False
        self.canciones.eliminar(cancion)
        self.guardar_todo()
        return True

    def modificar_titulo(self, id_cancion, nuevo_titulo):
        cancion = self.buscar_cancion_por_id(id_cancion)
        if cancion is None:
            return False

        cancion.titulo = nuevo_titulo
        # Si existe el .bin, actualiza SOLO ese registro con seek (acceso directo)
        if RUTA_BIN.exists():
            posicion = posicion_del_id(self.canciones, int(id_cancion))
            actualizar_registro(RUTA_BIN, posicion, cancion)
        # Actualiza el texto secuencial
        guardar_csv(RUTA_TXT, self.obtener_filas(), ENCABEZADOS)
        return True

    def guardar_todo(self):
        guardar_csv(RUTA_TXT, self.obtener_filas(), ENCABEZADOS)
        guardar_binario(RUTA_BIN, self.canciones)
