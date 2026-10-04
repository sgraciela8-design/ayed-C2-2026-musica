
from src.excepciones import ColaVaciaError
from src.tads.lista_enlazada import ListaEnlazada


class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self):
        self._datos = ListaEnlazada()

    def encolar(self, dato):
        # Agrega al final de la cola.
        self._datos.insertar_al_final(dato)

    def desencolar(self):
        # Quita y devuelve el primer elemento de la cola.
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola")

        return self._datos.eliminar_primero()

    def ver_frente(self):
        # Consulta el primer elemento sin quitarlo.
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")

        return self._datos.obtener_primero()

    def esta_vacia(self):
        return self._datos.esta_vacia()
