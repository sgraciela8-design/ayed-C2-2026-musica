from src.tads.lista_enlazada import ListaEnlazada

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""
def __init__(self):
    self._datos = ListaEnlazada()

    def encolar(self, dato):
        self._datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.datos._cabeza.dato
        self._datos._cabeza = self._datos._cabeza.siguiente
        self._daatis._tamanio -=1
        return dato

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self._datos._cabeza.dato

    def esta_vacia(self):
        return self._datos.esta_vacia()
