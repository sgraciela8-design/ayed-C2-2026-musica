from typing import Self

from src.dominio.cancion import Cancion
from src.tads.lista_enlazada import ListaEnlazada
from src. excepciones import ColeccionLlenaError 


class Biblioteca:
     
      def __init__(self):
        self.capacidad_maxima = 6
        self.canciones = ListaEnlazada()

      #1. Lista con instancias de Cancion
      def agregar_canciones(self, cancion):
         if self.canciones.tamanio() >= self.capacidad_maxima:
            raise ColeccionLlenaError(
               "La playlist alcanzó su capacidad máxima."
            )
        
            
        
         # 2. Relaciones de versiones directas (id_original -> lista de id_derivadas)
        
         self.versiones_directas = {
         1: [],
         2: [3]
       }
         self.cargar_canciones_iniciales()  # Carga las canciones iniciales al crear la biblioteca

      def cargar_canciones_iniciales(self):
                 #carga el catálogo al inicializar
          self.agregar_cancion(Cancion(1, "Crimen", "Gustavo Cerati", "Fuerza natural", "2006"))
          self.agregar_cancion(Cancion(2, "Adios", "Gustavo Cerati", "Fuerza natural", "2006"))
          self.agregar_cancion(Cancion(3, "Here Comes the Sun", "The Beatles", "Abbey Road", "1969"))
          self.agregar_cancion(Cancion(4, "Creep", "Radiohead", "Album de estudio", "1992"))
          self.agregar_cancion(Cancion(5, "505", "Arctic Monkeys", "Favorite Worst Nightmare", "2007"))
          self.agregar_cancion(Cancion(6, "Demoliendo Hoteles", "Charly García", "Piano Bar", "1984"))


        #Lista con instancias de Canción
      def agregar_cancion(self, cancion):
        if self.canciones.tamanio() >= self.capacidad_maxima:
            raise ColeccionLlenaError("La playlist alcanzó su capacidad máxima.")
        self.canciones.insertar_al_final(cancion)
        

      def obtener_canciones(self):
        return self.canciones

      def obtener_todas_las_versiones_recursivo(self, id_cancion):
        """Método RECURSIVO para la Entrega 2."""
        id_cancion = int(id_cancion)
        ids_derivados = self.versiones_directas.get(id_cancion, [])

        #Caso base: Si no hay derivaciones para es ID
        if not ids_derivados:
            return []
         #Caso recursivo: se obtienen las canciones y se llama a si misma
        resultado = []


        for id_derivado in ids_derivados:
            #buscamos la canción directamente en el loop
            for cancion in self.canciones:
                if int(cancion.id) == int(id_derivado):
                    resultado.append(cancion)
                    break

            resultado += self.obtener_todas_las_versiones_recursivo(id_derivado)
        
        return resultado

    