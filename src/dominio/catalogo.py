from src.dominio.cancion import Cancion

class Biblioteca:
    def __init__(self):
        # Lista que contiene INSTANCIAS de la clase Cancion
        self.canciones = [
            Cancion(1, "Crimen", "Gustavo Cerati", "Fuerza natural", "2006"),
            Cancion(2, "Adios", "Gustavo Cerati", "Fuerza natural", "2006"),
            Cancion(3, "Here Comes the Sun", "The Beatles", "Abbey Road", "1969"),
            Cancion(4, "Creep", "Radiohead", "Album de estudio", "1992"),
            Cancion(5, "505", "Arctic Monkeys", "Favorite Worst Nightmare", "2007"),
            Cancion(6, "Demoliendo Hoteles", "Charly García", "Piano Bar", "1984")
        ]

    def obtener_canciones(self):
        return self.canciones