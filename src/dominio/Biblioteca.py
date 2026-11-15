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

# Rutas ancladas a la raíz del proyecto
RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"
RUTA_TXT = DATA / "Lista_Canciones.txt"
RUTA_BIN = DATA / "canciones.bin"
ENCABEZADOS = ["id", "titulo", "artista", "album", "anio"]


class Biblioteca:

    def __init__(self):
        self.capacidad_maxima = 100
        self.canciones = ListaEnlazada()
        self.coleccion_principal = ListaEnlazada()

        self.versiones_directas = {
            1: [2],
            2: [3],
        }

        self.cargar_desde_csv(RUTA_TXT)

    def cargar_desde_csv(self, ruta=RUTA_TXT):
        filas = cargar_csv(ruta)
        self.canciones = ListaEnlazada()
        for fila in filas:
            cancion = Cancion(
                fila["id"],
                fila["titulo"],
                fila["artista"],
                fila["album"],
                fila["anio"],
            )
            self.canciones.insertar_al_final(cancion)

    def obtener_filas(self):
        filas = []
        for cancion in self.canciones:
            filas.append({
                "id": cancion.id,
                "titulo": cancion.titulo,
                "artista": cancion.artista,
                "album": cancion.album,
                "anio": cancion.anio,
            })
        return filas

    def obtener_canciones(self):
        return self.canciones

    def obtener_canciones_como_lista(self):
        canciones_lista = []
        for cancion in self.canciones:
            canciones_lista.append(cancion)
        return canciones_lista

    def buscar_cancion_por_id(self, id_cancion):
        for cancion in self.canciones:
            if cancion.id == int(id_cancion):
                return cancion
        return None

    def buscar_por_titulo(self, titulo):
        for cancion in self.canciones:
            if cancion.titulo.lower() == titulo.lower():
                return cancion
        return None

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
        if RUTA_BIN.exists():
            posicion = posicion_del_id(self.canciones, int(id_cancion))
            actualizar_registro(RUTA_BIN, posicion, cancion)
        guardar_csv(RUTA_TXT, self.obtener_filas(), ENCABEZADOS)
        return True

    def obtener_coleccion_principal(self):
        return self.coleccion_principal

    def obtener_todas_las_versiones_recursivo(self, id_cancion):
        id_cancion = int(id_cancion)
        ids_derivados = self.versiones_directas.get(id_cancion, [])

        if not ids_derivados:
            return []

        resultado = []
        for id_derivado in ids_derivados:
            cancion = self.buscar_cancion_por_id(id_derivado)
            if cancion is not None:
                resultado.append(cancion)
            resultado += self.obtener_todas_las_versiones_recursivo(id_derivado)
        return resultado

    def guardar_todo(self):
        guardar_csv(RUTA_TXT, self.obtener_filas(), ENCABEZADOS)
        guardar_binario(RUTA_BIN, self.canciones)
        
