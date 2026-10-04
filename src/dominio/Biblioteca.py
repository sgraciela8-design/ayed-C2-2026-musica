
from src.dominio.cancion import Cancion
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError


class Biblioteca:
    def __init__(self):
        self.capacidad_maxima = 6
        self.canciones = ListaEnlazada()
        self.coleccion_principal = ListaEnlazada()

        self.versiones_directas = {
            1: [2],
            2: [3]
        }

        self.cargar_canciones_iniciales()

    def cargar_canciones_iniciales(self):
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
        return self.canciones

    def buscar_cancion_por_id(self, id_cancion):
        for cancion in self.canciones:
            if cancion.id == int(id_cancion):
                return cancion
        return None

    def agregar_cancion(self, cancion):
        if self.coleccion_principal.tamanio() >= self.capacidad_maxima:
            raise ColeccionLlenaError(
                "La colección principal alcanzó su capacidad máxima."
            )
        self.coleccion_principal.insertar_al_final(cancion)

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
