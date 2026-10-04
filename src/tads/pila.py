from src.excepciones import PilaVaciaError
from src.tads.lista_enlazada import ListaEnlazada 

class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

def __init__(self):
    self._datos = ListaEnlazada() #_datos = atributo interno

    def apilar(self, dato): #agrega al inicio de la pila
        self._datos.insertar_al_inicio(dato)

    def desapilar(self): #quita el nodo de la cabeza y devuelve su dato
        if self.esta_vacia():#evita errores si no hay elementos
            raise PilaVaciaError ("No hay elementos en el historial")
        dato = self._datos._cabeza.dato #guarda el dato
        self._datos._cabeza = self._datos._cabeza.siguiente #mueve la cabeza al siguiente nodo
        return dato

    def ver_tope(self): #el último elemento agregado siempre queda primero
        if self.esta_vacia():
            raise PilaVaciaError ("La pila está vacia")
        return self._datos._cabeza.dato
    
def esta_vacia(self):
    return self._datos.esta_vacia()
