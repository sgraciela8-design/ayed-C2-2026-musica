from src.tads import Pila 
from src.dominio.Biblioteca import Biblioteca
mi_biblioteca = Biblioteca()
historial = Pila()



cancion_reproducida = mi_biblioteca.obtener_canciones(1) 


historial.apilar(cancion_reproducida)