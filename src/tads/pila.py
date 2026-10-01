class Pila:
    """TAD pila implementado sobre ListaEnlazada."""
from src.tads.lista_enlazada import ListaEnlazada
def __init__(self):
    self._lista = ListaEnlazada()
    

    def apilar(self, dato):
        raise NotImplementedError

    def desapilar(self):
        raise NotImplementedError

    def ver_tope(self):
        raise NotImplementedError

    def esta_vacia(self):
        raise NotImplementedError
