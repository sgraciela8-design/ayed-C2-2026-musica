class Pila:
    """TAD pila implementado sobre ListaEnlazada."""
from src.tads.lista_enlazada import ListaEnlazada
def __init__(self):
    self._datos = ListaEnlazada()
    

    def apilar(self, dato):
        self._datos.insertar_al_inicio(dato)

    def desapilar(self): #quita el nodo de la cabeza y devuelve su dato
        if self.esta_vacia():#evita errores si no hay elementos
            return None
        dato = self._datos._cabeza.dato #guarda el dato
        self._datos._cabeza = self._datos._cabeza.siguiente #mueve la cabeza 
        return dato

    def ver_tope(self): #el último elemento agregado siempre queda primero
        if self.esta_vacia():
            return None
        return self._datos._cabeza.dato
    
    def esta_vacia(self):
        return self._datos.esta_vacia()
