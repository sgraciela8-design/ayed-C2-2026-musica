
import csv

from src.dominio.cancion import Cancion
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError
from src.persistencia.texto import cargar_csv, guardar_csv
from src.persistencia.binario import (guardar_binario, cargar_binario,actualizar_registro, posicion_del_id)



class Biblioteca:
    def __init__(self):
        self.capacidad_maxima = 100
        self.canciones = ListaEnlazada()
        self.coleccion_principal = ListaEnlazada()

        self.versiones_directas = {
            1: [2],
            2: [3]
        }

        self.cargar_desde_csv("data/canciones.csv")
    def cargar_desde_csv(self, ruta):

        filas = cargar_csv(ruta)

        for fila in filas:

            cancion = Cancion(
                fila["id"],
                fila["titulo"],
                fila["artista"],
                fila["album"],
                fila["anio"]
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
                "anio": cancion.anio
            })

        return filas

    def cargar_canciones_iniciales(self):  #inserta canciones precargadas
        self.canciones.insertar_al_final(
            Cancion(1, "Crimen", "Gustavo Cerati", "Fuerza natural", "2006")
        )
        self.canciones.insertar_al_final(
            Cancion(2, "Adios", "Gustavo Cerati", "Fuerza natural", "2006")
        )
        self.canciones.insertar_al_final(
            Cancion(3, "Here Comes the Sun", "The Beatles", "Abbey Road", "1969")
        )
        self.canciones.insertar_al_final(
            Cancion(4, "Creep", "Radiohead", "Album de estudio", "1992")
        )
        self.canciones.insertar_al_final(
            Cancion(5, "505", "Arctic Monkeys", "Favorite Worst Nightmare", "2007")
        )
        self.canciones.insertar_al_final(
            Cancion(6, "Demoliendo Hoteles", "Charly García", "Piano Bar", "1984")
        )

    def obtener_canciones(self):
        return self.canciones #devuelve la lista enlazada completa

    def obtener_canciones_como_lista(self):
     #se genera una copia temporal sobre la que podemos aplicar ordenamiento por selección e insercion
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

        """Alta persistente
        alta persistente: se agrega la canción a la lista enlazada y se guarda en el archivo binario y csv
        """
    def agregar_cancion(self, cancion):
        if self.canciones.tamanio() >= self.capacidad_maxima:
            raise ColeccionLlenaError(
                "La colección principal alcanzó su capacidad máxima."
            )
        self.canciones.insertar_al_final(cancion)
        self.guardar_todo()  # Guardar en binario y CSV después de agregar la canción

    """Baja persistente
    baja persistente: se elimina la canción de la lista enlazada y se elimina del archivo binario y csv
    """
    def eliminar_cancion(self, id_cancion):
        cancion = self.buscar_cancion_por_id(id_cancion)

        if cancion is None:
           return False  # La canción no existe, no se puede eliminar
        
        self.canciones.eliminar(cancion)
        self.guardar_todo()  # Guardar en binario y CSV después de eliminar la canción
        return True

    """Modificación persistente"""
    #se modifica el título de la canción y se guarda en el archivo binario y csv
    def modificar_titulo(self, id_cancion, nuevo_titulo):
        cancion = self.buscar_cancion_por_id(id_cancion)

        if cancion is None:
            return False  # La canción no existe, no se puede modificar

        cancion.titulo = nuevo_titulo
        posicion = posicion_del_id(self.canciones, id_cancion)
        actualizar_registro("data/canciones.bin", posicion, cancion)
        self.guardar_todo()  # Guardar en binario y CSV después de modificar el título
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

            resultado += self.obtener_todas_las_versiones_recursivo(
                id_derivado
            )

        return resultado

    def guardar_todo(self): #guarda en binario y csv
        guardar_csv(
            "data/canciones.csv",
            self.obtener_filas(),
            ["id", "titulo", "artista", "album", "anio"],
        )
        guardar_binario("data/canciones.bin", self.canciones)
