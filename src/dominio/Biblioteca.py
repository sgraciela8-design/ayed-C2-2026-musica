from src.dominio import cancion
from src.dominio.cancion import Cancion
from src.tads.lista_enlazada import ListaEnlazada
from src. excepciones import ColeccionLlenaError 

class Biblioteca:
    def __init__(self):
         self.capacidad_maxima = 6
         self.cancion = ListaEnlazada()
         self.agregar_cancion (
            Cancion (1, "Crimen", "Gustavo Cerati", "Fuerza natural", "2006")
         )
         self.agregar_cancion (         
            Cancion(2, "Adios", "Gustavo Cerati", "Fuerza natural", "2006")
         )
         self.agregar_cancion (
            Cancion(3, "Here Comes the Sun", "The Beatles", "Abbey Road", "1969")
         )
         self.agregar_cancion (
            Cancion(4, "Creep", "Radiohead", "Album de estudio", "1992")
         )
         self.agregar_cancion (
            Cancion(5, "505", "Arctic Monkeys", "Favorite Worst Nightmare", "2007")
         )
         self.agregar_cancion (
            Cancion(6, "Demoliendo Hoteles", "Charly García", "Piano Bar", "1984")
         )

        # 1. Lista con instancias de Cancion
         def agregar_cancion(self, cancion):
            if self.cancion.tamanio() >= self.capacidad_maxima:
                          raise ColeccionLlenaError(
                              "La playlist alcanzó su capacidad máxima."
            )
            
         self.cancion.insertar_al_final(cancion)      
            
        
         # 2. Relaciones de versiones directas (id_original -> lista de id_derivadas)
         self.versiones_directas = {
            1: [2],
            2: [3]
        }

    def obtener_canciones(self):
        return self.cancion 

    def obtener_todas_las_versiones_recursivo(self, id_cancion):
        """Método RECURSIVO para la Entrega 2."""
        id_cancion = int(id_cancion)
        ids_derivados = self.versiones_directas.get(id_cancion, [])

        # CASO BASE: Si no hay derivaciones para este ID
        if not ids_derivados:
            return []

        # CASO RECURSIVO: Se obtienen las canciones y se llama a sí misma
        resultado = []
        for id_derivado in ids_derivados:
            # Buscamos la canción directamente en el loop
            for cancion in self.cancion:
                if int(cancion.id) == int(id_derivado):
                    resultado.append(cancion)
                    break
            
            # Llamada recursiva
            resultado += self.obtener_todas_las_versiones_recursivo(id_derivado)

        return resultado

    def agregar_cancion(self, arg1):
        ...